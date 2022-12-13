import json
print("choose login or sign up")
print("1_signup")
print("2_login")
user=int(input("enter your choice:-"))
if user==1:
    username=input("enter your name:-")
    password=input("enter your password:-")
    password_c=input("confirm the password:-")
    a=0
    b=0
    c=0
    d=0
    capital="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    small="abcdefghijklmnopqrstuvwxyz"
    special="@$#&?!"
    digits="0123456789"
    if len(password)>=6:
        for i in password:
            if i in capital:
                a=a+1
            if i in small:
                b=b+1
            if i in special:
                c=c+1
            if i in digits:
                d=d+1
    if (a>=1 and b>=1 and c>=1 and d>=1 and a+b+c+d==len(password)):
        print("strong password")
    else:
        print("weak password")
    if password==password_c:
        b=open("loginsignup1.json","r")
        data=json.load(b)
        if username in data["user"]:
                print("it is already exists")
        else:
                dic1={}
                dic2={}
                dic1["username"]=username
                dic1["password"]=password
                dic2["description"]=input("enter the description here")
                dic2["date of birth"]=input("enter the date of birth")
                dic2["gender"]=input("enter the gender:")
                dic2["hobbies"]=input("enter your hobbies")
                dic1["profile"]=dic2
                b=data["user"]
                b.append(dic1)
                f=open("loginsignup1.json","w")
                json.dump(data,f,indent=4)
                f.close()
                print("signup successfully")
    else:
        print("does not match")
elif user==2:
    b=open("loginsignup1.json","r")
    f=json.load(b)
    username=input("enter your name")
    password=input("enter the password for login")
    for i in f["user"]:
        if username==i["username"]:
            if password==i["password"]:
                print("login successfullly")
                print(i)
            else:
                print("check your password")
        else:
            print("check your username")





            



















    b=open("loginsignup.json","r")
    data=json.load(b)
    d={}
    d["username"]=username
    d["password"]=password
    b=data["user"]
    b.append(d)
    f=open("loginsignup.json","w")
    json.dump(data,f,indent=4)
