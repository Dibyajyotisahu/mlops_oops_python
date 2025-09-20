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
            pass
        elif user_input == "4":
            pass
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
                self.menu()

obj=chatbook()
obj.menu()


    