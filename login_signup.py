def register():
    db=open("database.txt","r")
    Username=input("Create username:")
    Password=input("Create Password:")
    Password1=input("Confrom password:")
    d=[]
    f=[]
    for i in db:
        a,b=i.split(",")
        b=b.strip()
        d.append(a)
        f.append(b)
    data=dict(zip(d,f))
    
    if Password!=Password1:
        print("passwords don't match, restart:")
        register()
    else:
        if len(Password)<=6:
            print("password too short, restarts:")
            register()
        elif Username in d:
            print("username exists")
            register()
        else:
            db=open("database.txt","a")
            db.write(Username+","+Password+"\n")
            print("Success!")
            

def access():
    db=open("database.txt","r")
    Username=input("Enter your username:")
    Password=input("Enter your Password:")

    if not len(Username or Password)<1:
        d=[]
        f=[]
        for i in db:
            a,b=i.split(",")
            b=b.strip()
            d.append(a)
            f.append(b)
        data=dict(zip(d,f))

        try:
            if data[Username]:
                try:
                    if Password == data[Username]:
                        print("Login Success")
                        print("Hi,",Username)
                    else:
                        print("password or Username incorrect")
                except:
                    print("Incorrect password or username")
            else:
                print("Username or password doesn't exist")
        except:
            print("Username or password doesn't exist")
    else:
        print("Please enter a value")

def home(option=None):
    option=input("Login |Signup:")
    if option == "Login":
        access()
    elif option == "Signup":
        register()
    else:
        print("Please enter an option")
home()


