import requests

BASE = "http://127.0.0.1:5000/"

decision = input('Enter your task from A = Transaction, B = Create Account, C = Delete Account, D = Read Account: ')

if decision == 'A':
    src_accnt_no = input('Enter the source account number you want to transfer from: ')
    src_accnt = requests.get(BASE+ "account/"+ src_accnt_no)
    src_accnt_parsed = src_accnt.json()
    dest_accnt_no = input('Enter the destination account number you want to trasfer to: ')
    dest_accnt = requests.get(BASE+ "account/"+ dest_accnt_no)
    dest_accnt_parsed = dest_accnt.json()
    amount = float(input('Enter the amount you want to transfer: '))

    balane_in_src = float(src_accnt_parsed['balance']) - amount
    balance_in_dest = float(dest_accnt_parsed['balance']) + amount

    update_src = requests.patch(BASE + "account/" + src_accnt_no, {"balance": balane_in_src})
    print(update_src.json())
    update_dest = requests.patch(BASE + "account/" + dest_accnt_no, {"balance": balance_in_dest})
    print(update_dest.json())

if decision == 'B':
    acnt_no = input('Enter the new account number: ')
    balance = input('Enter the amount you want to put in the new account: ')

    new_account = requests.put(BASE + "account/" + acnt_no, {"account_number": acnt_no, "balance": balance})
    print(new_account.json())
        
if decision == 'C':
    del_acnt_no = input('Enter the account number you want to delete: ')
    deleted = requests.delete(BASE + "account/" + del_acnt_no)
    print(deleted.json())

if decision == 'D':
    read_accnt_no = input('Enter the account number you want to read: ')
    reading = requests.get(BASE + "account/" + read_accnt_no)
    print(reading.json())

