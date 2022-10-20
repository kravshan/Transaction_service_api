# Transaction_service_api
How to use:
  Step 1: Run the api.py file to get the local server running on http://120.0.0.1:5000/
  Step 2: Run the transaction.py file and follow the instructions on the terminal. Four operations are available to choose from in here and can perform the transactions through this file.
  
Description: 
  api.py file:   The api.py file contains the API, database, request parsers, resorce fields, resources and the account model. 
                 This file contains the API that can be used by other files for account transactions. 
  
  transaction.py file:   The transaction.py contains the model of the transaction and it is used to perform CRUD operation from the API.
                         To operate the API and perform the transactions, this file is used. It has four operations. 
                         Operation A: Perform a trasaction between two accounts
                         Operation B: Create a new account
                         Operation C: Delete an existing account
                         Operation D: Read an existing account
                         The operations need several user inputs. The system does not use a Graphical UI. The inputs are obtained from the terminal itself.
                         
  test.py file: The test.py file iis used for testing while developing the API. It contains some tests to check the performances of the CRUD operations.
  
  requirements.txt file: This file was used to install all the necessary dependancies for the task.
  
  database.db file: Contains the SQL-ALchemy in-memory database of the system.
