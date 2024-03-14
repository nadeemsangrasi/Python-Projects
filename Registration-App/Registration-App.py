from typing import Union
import json
def data():
    try:
        with open("./dataBase.txt","r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
def store_data(data):
    with open("./dataBase.txt","w") as file:
        json.dump(data,file)

def register_account(data:list[dict[str,Union[str,int]]]):
    full_name : str = input("Enter your full name ")
    email : str = input("Enter your email ")
    ph_number=...
    try:
        ph_number : int = int(input("Enter your phone number "))
        
    except ValueError:
            print("Please enter a valid value")
    recovery_otp:int=...
    try:
        recovery_otp : int = int(input("Set otp for account recovery "))
        
    except ValueError:
            print("Please enter a valid value")
    password : str = input("Enter your password ")
    re_type_password : str = input("Enter your re-type password ")
    if password==re_type_password :
        data.append({"name":full_name,"email":email,"phone":ph_number,"password":password,"otp":recovery_otp})
        store_data(data)
    else:
        print("Please enter right password")
    
    
def log_in_account(data:list[dict[str,Union[str,int]]]):
    email:str=input("Enter your email ")
    password:str=input("Enter your password ")
    for index in range(len(data)):
        if data[index]["email"]==email and data[index]["password"]==password:
            print("User loged in User full name is:{}\nUser email is:{}\nUser phone number is:{}".format(data[index]["name"],data[index]["email"],data[index]["phone"])) 
            break
            
    

def forgot_password(data_base:list[dict[str,Union[str,int]]]):
    check_email : str =input("Enter your email ")
    check_otp=...
    try:
        check_otp : int = int(input("Enter your recovery otp "))
    except ValueError:
        print("Please enter valid value")
    for index in range(len(data_base)):
        if data_base[index]["email"] ==check_email and data_base[index]["otp"]==check_otp:
            new_password=input("Enter new password ")
            re_type_new_password : str = input("Re type new password ")
            if new_password ==re_type_new_password:
                data_base[index]["password"]=new_password
            else:
                print("Please enter correct re type password")   
            break     
        

def update_information(data_base: list[dict[str,Union[str,int]]]):
    email:str=input("Enter your email ")
    password:str=input("Enter your password ")
    for index in range(len(data_base)):
        if data_base[index]["email"]==email and data_base[index]["password"]==password:
            new_name : str = input("Enter new name ")
            new_email : str = input("Enter new email ")
            new_ph_number=...
            try:
               new_ph_number : int = int(input("Enter your phone new number "))
                
            except ValueError:
                    print("Please enter a valid value")
            for index in range(len(data_base)):
                data_base[index]["name"]=new_name
                data_base[index]["email"]=new_email
                data_base[index]["phone"]=new_ph_number
        

def delet_account(data_base:list[dict[str,Union[str,int]]]):
    email : str = input("Enter your eamil ")
    password : str = input("Enter your password ")
    reason : str = input("Enter reasons why are you deleting account ")
    for index in range(len(data_base)):
        if data_base[index]["email"]==email and data_base[index]["password"]==password:
            print("Your Account Deleted Successfully\nDeleting reason is : {}".format(reason))
            data_base.pop(index)
            break
        

def show_data_base(data_base:list[dict[str,Union[str,int]]]):
    if len(data_base)!=0:
        for data in data_base:
            print(data)
    else:
        print([])
def main():
    data_base : list[dict[str,Union[str,int]]] = data()
    flage=True
    while flage:
        print("*"*70)
        print("Choose your desired option")
        print("1 Rigister Account")
        print("2 Log in Account")
        print("3 Forgotten Password")
        print("4 Update Account Information")
        print("5 Delet Account")
        print("6 Show Data Base")
        print("7 Exit from app")
        print("*"*70)
        choice=...
        try:
            choice : int = int(input("Enter your choice "))
        except ValueError:
            print("Please enter a valid value")
        match choice:
            case 1:
                register_account(data_base)
            case 2:
                log_in_account(data_base)
            case 3:
                forgot_password(data_base)
            case 4:
                update_information(data_base)
            case 5:
                delet_account(data_base)
            case 6:
                show_data_base(data_base)
            case 7:
                print("Good by have good day")
                break

if __name__=="__main__":
    main()