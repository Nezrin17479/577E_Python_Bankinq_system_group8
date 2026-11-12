import hashlib
import json
import os
import time
from datetime import datetime, timedelta

if not os.path.exists("users.json"):
    data = {
        "user01": {"name": "user01", 'password': 'Test@123', "balance": 2500,'Card status': 'Active','wrong_inputs01': 0,'blocking': 'No','blocked_at': None},
        "user02": {"name": "user02",'password': 'Test@456', "balance": 1500 ,'Card status': 'Active','wrong_inputs02': 0,'blocking': 'No','blocked_at': None},
        "user03": {"name": "user03",'password': 'Test@789', "balance": 3000,'Card status': 'Active', 'wrong_inputs03': 0,'blocking': 'No','blocked_at': None}
    } 
    with open("users.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

with open("users.json", "r", encoding="utf-8") as file:
    loaded_data = json.load(file)

def save_data():
    with open("users.json", "w", encoding="utf-8") as file:
        json.dump(loaded_data, file, indent=4, ensure_ascii=False)
def s():
    for password_user in passwords:
        hash_object_user=hashlib.sha256(password_user.encode('utf-8'))
        hashed_result_user=hash_object_user.hexdigest()
        users_passwords.append(hashed_result_user)
    return 1
passwords=[loaded_data["user01"]["password"],loaded_data["user02"]["password"],loaded_data["user03"]["password"]]

users=[loaded_data["user01"]["name"],loaded_data["user02"]["name"],loaded_data["user03"]["name"]]
users_passwords=[]
k=s()

user1 = 999 if loaded_data["user01"]["blocking"] == 'Yes' else (6 if loaded_data["user01"]["wrong_inputs01"] >= 3 else 3)
user2 = 999 if loaded_data["user02"]["blocking"] == 'Yes' else (6 if loaded_data["user02"]["wrong_inputs02"] >= 3 else 3)
user3 = 999 if loaded_data["user03"]["blocking"] == 'Yes' else (6 if loaded_data["user03"]["wrong_inputs03"] >= 3 else 3)
def Password_checking(wrong_inputs01, wrong_inputs02, wrong_inputs03, user1, user2, user3):
    
    while not (loaded_data["user01"]["blocking"] == 'Yes' and loaded_data["user02"]["blocking"] == 'Yes' and loaded_data["user03"]["blocking"] == 'Yes'):
        
        
        if (wrong_inputs01 == user1) or (wrong_inputs02 == user2) or (wrong_inputs03 == user3):
            break

        user_name = input('Enter user name:')
        user_password = input('Enter your password:')
        
        user_idx = users.index(user_name) if user_name in users else -1
        
        
        if user_idx != -1 and loaded_data[user_name]["blocking"] == 'Yes':
            print('Maximum login attempts exceeded. Your card has been blocked. Please contact the bank administrator.')
            continue 

        hash_object_user = hashlib.sha256(user_password.encode('utf-8'))
        hashed_result_user = hash_object_user.hexdigest()
        pass_idx = users_passwords.index(hashed_result_user) if hashed_result_user in users_passwords else -2
        
        if user_idx == pass_idx:
            
            loaded_data[user_name][f"wrong_inputs0{user_idx+1}"] = 0
            save_data()
            print(loaded_data[f"user0{user_idx+1}"])
            return 1
        elif user_idx == -1:
            print('Wrong username or password')
        elif user_idx == 0:
            print('Wrong username or password')
            wrong_inputs01 += 1
            loaded_data["user01"]["wrong_inputs01"] = wrong_inputs01
            save_data()
        elif user_idx == 1:
            print('Wrong username or password')
            wrong_inputs02 += 1
            loaded_data["user02"]["wrong_inputs02"] = wrong_inputs02 
            save_data()
        elif user_idx == 2:
            print('Wrong username or password')
            wrong_inputs03 += 1
            loaded_data["user03"]["wrong_inputs03"] = wrong_inputs03 
            save_data()

    
    if loaded_data["user01"]["blocking"] == 'Yes' and loaded_data["user02"]["blocking"] == 'Yes' and loaded_data["user03"]["blocking"] == 'Yes':
        print("All cards are blocked!")
        return 0

    def blocked_user():
        print("User account locked out, remaining seconds until next login attempt:\n")
        for remaining_time in range(60, -1, -1):
            print(f"\rRemaining time until next possible login: {remaining_time} saniyə ", end="")
            time.sleep(1)
        print("\n\nTime is over, you can log in again:")
        return 1

    
    if wrong_inputs01 == 3 or wrong_inputs01 == 6:
        if wrong_inputs01 == 3 and user1 == 3:
            k = blocked_user()
            user1 = 6
            t = Password_checking(wrong_inputs01, wrong_inputs02, wrong_inputs03, user1, user2, user3)
        elif wrong_inputs01 == 6 and loaded_data["user01"]["blocking"] == 'No':
            print('This card blocked')
            loaded_data["user01"]["blocking"] = 'Yes'
            loaded_data["user01"]["Card status"] = 'Blocked'
            user1 = 999
            save_data() 
            t = Password_checking(wrong_inputs01, wrong_inputs02, wrong_inputs03, user1, user2, user3)

    
    if wrong_inputs02 == 3 or wrong_inputs02 == 6:
        if wrong_inputs02 == 3 and user2 == 3:
            k = blocked_user()
            user2 = 6
            t = Password_checking(wrong_inputs01, wrong_inputs02, wrong_inputs03, user1, user2, user3)
        elif wrong_inputs02 == 6 and loaded_data["user02"]["blocking"] == 'No':
            print('This card blocked')
            loaded_data["user02"]["blocking"] = 'Yes'
            loaded_data["user02"]["Card status"] = 'Blocked'
            user2 = 999
            save_data()
            t = Password_checking(wrong_inputs01, wrong_inputs02, wrong_inputs03, user1, user2, user3)

    
    if wrong_inputs03 == 3 or wrong_inputs03 == 6:
        if wrong_inputs03 == 3 and user3 == 3:
            k = blocked_user()
            user3 = 6
            t = Password_checking(wrong_inputs01, wrong_inputs02, wrong_inputs03, user1, user2, user3)
        elif wrong_inputs03 == 6 and loaded_data["user03"]["blocking"] == 'No':
            print('This card blocked')
            loaded_data["user03"]["blocking"] = 'Yes'
            loaded_data["user03"]["Card status"] = 'Blocked'
            user3 = 999
            save_data()
            t = Password_checking(wrong_inputs01, wrong_inputs02, wrong_inputs03, user1, user2, user3)

result_passwords = Password_checking(
    loaded_data["user01"]["wrong_inputs01"], 
    loaded_data["user02"]["wrong_inputs02"], 
    loaded_data["user03"]["wrong_inputs03"], 
    user1, user2, user3
)