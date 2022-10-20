from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class AccountModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account_number = db.Column(db.String, nullable=False)
    balance = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"Account(Account number = {self.account_number}, Balance = {self.balance})"

# db.create_all()  #Run only Once

account_put_args = reqparse.RequestParser()
account_put_args.add_argument("account_number", type=str, help="Account Number is required!", required=True)
account_put_args.add_argument("balance", type=float, help="Balance in the account is required!", required=True)

account_update_args = reqparse.RequestParser()
account_update_args.add_argument("account_number", type=str, help="Account Number")
account_update_args.add_argument("balance", type=float, help="Balance in the account")


account_resource_fields = {
    'id': fields.Integer,
    'account_number': fields.String,
    'balance': fields.Float
}

class Account(Resource):
    @marshal_with(account_resource_fields)
    def get(self, account_id):
        result = AccountModel.query.filter_by(id=account_id).first()
        if not result:
            abort(404, message="There is no account by that ID!")
        return result

    @marshal_with(account_resource_fields)
    def put(self, account_id):
        args = account_put_args.parse_args()
        result = AccountModel.query.filter_by(id=account_id).first()
        if result:
            abort(409, messege="Account ID already exists!")
        
        account = AccountModel(id = account_id, account_number = args['account_number'], balance = args['balance'])
        db.session.add(account)
        db.session.commit()
        return account, 201 #Created response

    @marshal_with(account_resource_fields)
    def patch(self, account_id):
        args = account_update_args.parse_args()
        result = AccountModel.query.filter_by(id=account_id).first()
        if not result:
            abort(404, message="Account does not exists!")

        if args['balance']:
            result.balance = args['balance']

        db.session.commit()
        return result

    def delete(self, account_id):
        result = AccountModel.query.filter_by(id=account_id).first()
        if not result:
            abort(404, message="Account does not exits")
        
        db.session.delete(result)
        db.session.commit()
        return {'Output': 'Deleted!'}

api.add_resource(Account, "/account/<string:account_id>")
if __name__ == "__main__":
    app.run(debug=True)


