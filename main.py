import pandas as pd
import numpy as np
from Inventory import Inventory
from Customer import Customer
from Order import Order

## username and password input for verify
verify = False
welcome_message = "WELCOME TO G8-BOOKSHOP"
while not verify:
    print("\n------------------------{welcome_msg}-------------------------\n".format(welcome_msg = welcome_message))
    username = input("UserName: ")
    #############################Create Customer Object
    customer = Customer(username)
    if customer.IsMember(): # check to see if user does not exists
        yesno = input("Not a registered user! Do you want to register (Y/n) ? ")
        if yesno.lower() =='y':
            password = input("Password: ")
            conf_password = input("Confirm Password:")
            if password != conf_password:
                print("Password did not match")  # print a message if different inputs
                continue  # restarts
            else:
                address = input("Enter address:")
                customer.addMember(username, password)
                verify = True
        else:
            break
    else:
        password = input("Password: ")
        if customer.IsRightPassword(password):
            print("\n-----------------User has been identified, Welcome! {user} \n".format(user = username.upper()))
            verify = True
        else:
            print("Wrong Password, Try Again!")

##===================Verified
if verify:
    ######################Create Inventory Object
    inventory = Inventory()
    ######################Create Order Object
    order = Order(username)
    # View all items in a category
    inventory.print()

    while(1):
        
        # the user can see cart information, Delete account, Log out.
        print("\nPlease select from options below:\n")
        cdl = input("View/Edit Cart(c)\nManage account(m)\nLog Out(l)\nView Order(v)\nView Inventory(i):")

        if cdl.lower()=='l':
            customer.Logout()
        elif cdl.lower()=='v':
            order.print()
        elif cdl.lower() == "i":
            inventory.print()
        elif cdl.lower()=='m':
            
            adcb = input()
            customer.DeleteAccount(order)
        elif cdl.lower() == 'c':
            cart = customer.GetCart()
            cart_edit = True
            while cart_edit:
                # read card information
                adcb = input("\nAdd to Cart(a)\nDelete(d) by ISBN number\nCheckout(c)\nGo Back(b)\nView Cart(v):\nView Inventory(i)")
                if adcb.lower()=='a':
                    isbn = input("\nInput ISBN number:")
                    quantity = input("Number of items:")
                    # cart list
                    if inventory.checkQuantity(isbn, quantity)==1:
                        cart.AddToCart(isbn, quantity)
                    elif inventory.checkQuantity(isbn, quantity)==0:
                        print('Inventory doesn\'t have enough quantity.')
                        continue
                    elif inventory.checkQuantity(isbn, quantity)==-1:
                        print('Invalid ISBN number.')
                        continue
                if adcb.lower()=='d':
                    isbn = input("Input ISBN number:")
                    cart.RemoveFromCart(isbn)
                if adcb.lower()=='c':
                    cart.checkout(inventory, order)
                if adcb.lower() == 'u':
                    inventory.print()
                if adcb.lower() == 'v':
                    cart.print()
                if adcb.lower()=='b':
                    cart_edit = False
                if adcb.lower() == 'i'
                    inventory.print()
                    
                

