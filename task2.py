import hashlib
import time
def s():
    for password_user in passwords:
        hash_object_user=hashlib.sha256(password_user.encode('utf-8'))
        hashed_result_user=hash_object_user.hexdigest()
        users_passwords.append(hashed_result_user)
    return 1
passwords=['Test@123','Test@456','Test@789']

users=['user01','user02','user03']
users_passwords=[]
k=s()
print(users_passwords)
sum_user01=0
sum_user02=0
sum_user03=0    
other_access=0
user1=3
user2=3
user3=3
other=3
def Password_checking(sum_user01,sum_user02,sum_user03,user1,user2,user3):
    while sum_user01!=user1 and  sum_user02!=user2 and sum_user03!=user3:
        user_name=input('Enter user name:')
        user_password=input('Enter your password:')
        hash_object_user=hashlib.sha256(user_password.encode('utf-8'))
        hashed_result_user=hash_object_user.hexdigest()
        user_idx = users.index(user_name) if user_name in users else -1
        pass_idx = users_passwords.index(hashed_result_user) if hashed_result_user in users_passwords else -2
        if user_idx==pass_idx:
            return 1
        elif user_idx==-1:
            print('Wrong username or password')
        elif user_idx==0:
            print('Wrong username or password')
            sum_user01+=1
        elif user_idx==1:
            print('Wrong username or password')
            sum_user02+=1
        elif user_idx==2:
            print('Wrong username or password')
            sum_user03+=1
    def blocked_user():
        print("User account locked out, remaining seconds until next login attempt:\n")

        for remaining_time in range(60, -1, -1):
            print(f"\rRemaining time until next possible login: {remaining_time} saniyə ", end="")
            time.sleep(1)
        print("\n\n Time is over, you can log in again:")
    
        return 1
    if sum_user01==3 or sum_user01==6:
        if sum_user01==3:
            k= blocked_user()
            user1=6
            t=Password_checking(sum_user01,sum_user02,sum_user03,user1,user2,user3)
        elif sum_user01==6:
            print('This card blocked')
    if sum_user02==3 or sum_user02==6:
            if sum_user02==3:
                k= blocked_user()
                user2=6
                t=Password_checking(sum_user01,sum_user02,sum_user03,user1,user2,user3)
            elif sum_user02==6:
                print('This card blocked')
    if sum_user03==3 or sum_user03==6:
            if sum_user01==3:
                k= blocked_user()
                user3
                t=Password_checking(sum_user01,sum_user02,sum_user03,user1,user2,user3)
            elif sum_user03==6:
                print('This card blocked')

result_passwords=Password_checking(sum_user01,sum_user02,sum_user03,user1,user2,user3,)

