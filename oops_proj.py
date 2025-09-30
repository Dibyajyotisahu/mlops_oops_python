class chatbook:

    def __init__(self):
        self.username=""
        self.password=""
        self.loggedin=False

    def menu(self):
        user_input=input("""welcome to chatbook !! how would you like to proceed ? 
                            1. press 1 to signup
                            2. press 2 to login
                            3. press 3 to write post
                            4. press 4 to message a friend
                            5. press any key to exit""")

        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            self.my_post()
        elif user_input == "4":
            self.sendmsg()
        else:
            print("thank you for using chatbook")
            exit()
    
    def signup(self):
        email=input("enter your email id")
        password=input("enter your password")
        self.username=email
        self.password=password
        print("signup successful")
        print("\n")
        self.menu()

    def signin(self):
        if self.username=="" and self.password=="":
            print("user not found please signup first")
            self.menu()
        else:
            usrname=input("enter your email id")
            password=input("enter your password")
            if self.username==usrname and self.password == password:
                print("login successful")
                self.loggedin=True
                self.menu()
            else:
                print("invalid credentials")
                print("\n")
                self.menu()
    
    def my_post(self):
        if self.loggedin == True:
            txt=input("Enter your message here -> ")
            print(f"Following content has been posted  -> {txt}")
        else:
            print("you need to signin first to post something...")
        print("\n")
        self.menu()

    def sendmsg(self):
        if self.loggedin==True:
            txt = input("enter your message here -> ")
            friend=input("enter your friend's name")
            print(f"message sent to {friend} successfully")
        else:   
            print("you need to signin first to send message")
        print("\n")
        self.menu()
user1=chatbook()
user1.menu()


    