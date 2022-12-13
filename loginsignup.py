import json
print("choose login or sign up")
print("1_login")
print("2_signup")
user=int(input("enter your choice:-"))
if user==1:
    username=input("enter your name:-")
    password=input("enter your password:-")
    b=open("loginsignup.json","r")
    data=json.load(b)
    d={}
    d["username"]=username
    d["password"]=password
    b=data["user"]
    b.append(d)
    f=open("loginsignup.json","w")
    json.dump(data,f,indent=4)





















    # username=input("enter your name:-")
    # password=input("enter your password:-")
    # f=open("loginsignup.json","r")
    # account=json.load(f)
    # print(account)
    # account=account["user"]
    # d[username]=password
    # account.append(d)
    # # account=json.dumps(account)
    # f=open("loginsignup.json","w")
    # json.dumps(account,f,indent=4)
    # # f.write(account)


