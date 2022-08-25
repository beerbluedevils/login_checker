#authenticate

def login_checker():
    #credentials
    username = "felixblue"
    password = "B1e2e3r4+"
    #counter
    login_limit = 3
    login_counter = 0

    #counter and condition
    while login_counter != login_limit:
        if login_counter < login_limit:
          username_input = input("Enter Your Username : ")
          password_input = input("Enter Your Password : ")
          login_counter += 1
          #condition for credientials
          if (username_input == username and password_input == password):
            print("Login Successfully.")
            break
          else:
            print("Your username or password is incorrect.")
        if login_counter == login_limit:
            print("You've been blocked. Please contact admin.")

login_checker()






        



    


