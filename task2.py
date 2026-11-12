import hashlib
import json
import os
import time
from datetime import datetime, timedelta

if not os.path.exists("users.json"):
   data = {
        "user01": {
            "name": "user01", 
            "password": "Test@123", 
            "account_number": "10010001",  
            "balance": 2500, 
            "Card status": "Active", 
            "wrong_inputs01": 0, 
            "blocking": "No", 
            "blocked_at": None, 
            "lockout_until": None,
            "last_login": None             
        },
        "user02": {
            "name": "user02",
            "password": "Test@456", 
            "account_number": "10010002", 
            "balance": 1500, 
            "Card status": "Active", 
            "wrong_inputs02": 0, 
            "blocking": "No", 
            "blocked_at": None, 
            "lockout_until": None,
            "last_login": None            
        },
        "user03": {
            "name": "user03",
            "password": "Test@789", 
            "account_number": "10010003",  
            "balance": 3000, 
            "Card status": "Active", 
            "wrong_inputs03": 0, 
            "blocking": "No", 
            "blocked_at": None, 
            "lockout_until": None,
            "last_login": None             
        }
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

def blocked_user(seconds=60):
    print("Too many failed login attempts.")
    for remaining_time in range(seconds, -1, -1):
        # :02d o deməkdir ki, 9 rəqəmini 09 kimi göstərsin (00:59, 00:09, 00:00)
        print(f"\rPlease wait: 00:{remaining_time:02d} ", end="")
        time.sleep(1)
    print("\nYou may try again.\n")
    return 1

user1 = 999 if loaded_data["user01"]["blocking"] == 'Yes' else (6 if loaded_data["user01"]["wrong_inputs01"] >= 3 else 3)
user2 = 999 if loaded_data["user02"]["blocking"] == 'Yes' else (6 if loaded_data["user02"]["wrong_inputs02"] >= 3 else 3)
user3 = 999 if loaded_data["user03"]["blocking"] == 'Yes' else (6 if loaded_data["user03"]["wrong_inputs03"] >= 3 else 3)
def Password_checking(wrong_inputs01, wrong_inputs02, wrong_inputs03, user1, user2, user3):
    
    while not (loaded_data["user01"]["blocking"] == 'Yes' and loaded_data["user02"]["blocking"] == 'Yes' and loaded_data["user03"]["blocking"] == 'Yes'):
        
        
        if (wrong_inputs01 == user1) or (wrong_inputs02 == user2) or (wrong_inputs03 == user3):
            break

        user_name = input('Enter user name:')
    
        user_idx = users.index(user_name) if user_name in users else -1
        
        
        if user_idx != -1 and loaded_data[user_name]["blocking"] == 'Yes':
            print('Maximum login attempts exceeded. Your card has been blocked. Please contact the bank administrator.')
            continue 
        if user_idx != -1 and loaded_data[user_name]["lockout_until"] is not None:
            lockout_end = datetime.strptime(loaded_data[user_name]["lockout_until"], "%Y-%m-%d %H:%M:%S")
            now = datetime.now()
            if now < lockout_end:
                qalan_saniye = int((lockout_end - now).total_seconds())
                blocked_user(qalan_saniye)
                loaded_data[user_name]["lockout_until"] = None
                save_data()
            else:
                loaded_data[user_name]["lockout_until"] = None
                save_data()



        user_password = input('Enter your password:')
        hash_object_user = hashlib.sha256(user_password.encode('utf-8'))
        hashed_result_user = hash_object_user.hexdigest()
        pass_idx = users_passwords.index(hashed_result_user) if hashed_result_user in users_passwords else -2
        
        if user_idx == pass_idx:
            
            loaded_data[user_name][f"wrong_inputs0{user_idx+1}"] = 0
            loaded_data[user_name]["lockout_until"] = None

            loaded_data[user_name]["last_login"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            save_data()
            print(loaded_data[f"user0{user_idx+1}"])
            return user_name
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



    
    if wrong_inputs01 == 3 or wrong_inputs01 == 6:
        if wrong_inputs01 == 3 and user1 == 3:
            lockout_time = (datetime.now() + timedelta(seconds=60)).strftime("%Y-%m-%d %H:%M:%S")
            loaded_data["user01"]["lockout_until"] = lockout_time
            save_data()
            
            k = blocked_user()

            loaded_data["user01"]["lockout_until"] = None
            save_data()

            user1 = 6
            t = Password_checking(wrong_inputs01, wrong_inputs02, wrong_inputs03, user1, user2, user3)
        elif wrong_inputs01 == 6 and loaded_data["user01"]["blocking"] == 'No':
            print('Maximum login attempts exceeded. Your card has been blocked. Please contact the bank administrator.')
            loaded_data["user01"]["blocking"] = 'Yes'
            loaded_data["user01"]["Card status"] = 'Blocked'
            loaded_data["user01"]["blocked_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            user1 = 999
            save_data() 
            return Password_checking(wrong_inputs01, wrong_inputs02, wrong_inputs03, user1, user2, user3)

    
    if wrong_inputs02 == 3 or wrong_inputs02 == 6:
        if wrong_inputs02 == 3 and user2 == 3:
            lockout_time = (datetime.now() + timedelta(seconds=60)).strftime("%Y-%m-%d %H:%M:%S")
            loaded_data["user02"]["lockout_until"] = lockout_time
            save_data()

            k = blocked_user()
            user2 = 6

            loaded_data["user02"]["lockout_until"] = None
            save_data()

            return  Password_checking(wrong_inputs01, wrong_inputs02, wrong_inputs03, user1, user2, user3)
        elif wrong_inputs02 == 6 and loaded_data["user02"]["blocking"] == 'No':
            print('Maximum login attempts exceeded. Your card has been blocked. Please contact the bank administrator.')
            loaded_data["user02"]["blocking"] = 'Yes'
            loaded_data["user02"]["Card status"] = 'Blocked'
            loaded_data["user02"]["blocked_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            user2 = 999
            save_data()
            return  Password_checking(wrong_inputs01, wrong_inputs02, wrong_inputs03, user1, user2, user3)

    
    if wrong_inputs03 == 3 or wrong_inputs03 == 6:
        if wrong_inputs03 == 3 and user3 == 3:
            lockout_time = (datetime.now() + timedelta(seconds=60)).strftime("%Y-%m-%d %H:%M:%S")
            loaded_data["user03"]["lockout_until"] = lockout_time
            save_data()

            k = blocked_user()
            user3 = 6
            loaded_data["user03"]["lockout_until"] = None
            save_data()

            t = Password_checking(wrong_inputs01, wrong_inputs02, wrong_inputs03, user1, user2, user3)
        elif wrong_inputs03 == 6 and loaded_data["user03"]["blocking"] == 'No':
            print('Maximum login attempts exceeded. Your card has been blocked. Please contact the bank administrator.')
            loaded_data["user03"]["blocking"] = 'Yes'
            loaded_data["user03"]["Card status"] = 'Blocked'
            loaded_data["user03"]["blocked_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            user3 = 999
            save_data()
            t = Password_checking(wrong_inputs01, wrong_inputs02, wrong_inputs03, user1, user2, user3)

result_p_checking = Password_checking(
    loaded_data["user01"]["wrong_inputs01"], 
    loaded_data["user02"]["wrong_inputs02"], 
    loaded_data["user03"]["wrong_inputs03"], 
    user1, user2, user3
)




def change_password(user_name):
    print("\n--- CHANGE PASSWORD ---")
    current_pass = input("Enter current password: ")
    
   
    current_pass_hash = hashlib.sha256(current_pass.encode('utf-8')).hexdigest()
    stored_pass_hash = hashlib.sha256(loaded_data[user_name]["password"].encode('utf-8')).hexdigest()
    
    if current_pass_hash != stored_pass_hash:
        print("Incorrect current password. Password change failed.")
        return False
        
    while True:
        new_pass = input("Enter new password (min 8 chars, 1 uppercase, 1 lowercase, 1 digit): ")
        
        if len(new_pass) < 8:
            print("Password must be at least 8 characters long.")
            continue
       
        if not any(c.isupper() for c in new_pass):
            print("Password must contain at least one uppercase letter.")
            continue
     
        if not any(c.islower() for c in new_pass):
            print("Password must contain at least one lowercase letter.")
            continue
      
        if not any(c.isdigit() for c in new_pass):
            print("Password must contain at least one digit.")
            continue
       
        if new_pass == loaded_data[user_name]["password"]:
            print("New password cannot be the same as the old password.")
            continue
            
        
        confirm_pass = input("Confirm new password: ")
        if new_pass != confirm_pass:
            print("Passwords do not match. Please try again.")
            continue
            
        
        loaded_data[user_name]["password"] = new_pass
        save_data()
        
        
        global passwords, users_passwords
        passwords = [loaded_data["user01"]["password"], loaded_data["user02"]["password"], loaded_data["user03"]["password"]]
        users_passwords.clear()
        s()
        
        print("Password successfully changed!")
        return True


if result_p_checking in users:
    p_changing_question=input('Do you want to change your password?(Yes or No)')
    match p_changing_question:
        case 'Yes':
            result_p_changing=change_password(result_p_checking)
        case 'No':
            print('Okay!')


