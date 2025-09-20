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
            pass
        elif user_input == "2":
            pass
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:
            print("thank you for using chatbook")
            exit()
obj=chatbook()
obj.menu()

    