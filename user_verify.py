import pickle
# user = {"aaa" : "aaa", "bbb" : "bbb"}
# file = open('users&pass.txt', 'wb')
# pickle.dump(user, file)
# file.close()
file = open('users&pass.txt', 'r')
user = file.readlines()
complete = False

while not complete:
    username = input("UserName: ")
    if not username in user: # check to see if user does not exists
        yesno = input("Not a registered user! Do you want to Register: (Y/n)  ")
        if yesno.lower()=='y':
            password = input("Password: ")
            if password == '':
                print("Error! Cannot have blank as password.")
            confirm_password = input("Confirm Password: ")
            if password != confirm_password:
                print("Password does not match")  # print a message if different inputs
                continue  # restarts
            else:
                user[username] = password
                print("User has been registered, Welcome", username)
                file = open('users&pass.txt', 'wb')
                pickle.dump(user, file)
                file.close()
                complete = True
        else:
            print("Input username again!")
            continue
    else:
        password = input("Password: ")
        if password == user[username]:  # check to see if password match
            print("User Recognized! Welcome", username)
            complete = True
        else:
            print("password wrong! input again!")
