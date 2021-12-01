import pandas as pd
import numpy as np
from Inventory import Inventory
from Customer import Customer
from Order import Order
import Cart as cart

## username and password input for verify
verify = False
welcome_message = "WELCOME TO G8-BOOKSHOP"
account_info = "Account Information"
ordernumber = 1
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
                customer.addMember(username, password)
                verify = True
                print("\n------------------------{account_information}-------------------------\n".format(account_information = account_info))
                print("Creating Account")
                firstname = input("Please enter your First Name: ")
                lastname = input("Please enter your Last Name: ")
                customer.SetName(firstname, lastname)
                print("Welcome ", firstname, lastname)
                print("Please enter your shipping address:")
                add_number = input("Address number: ")
                Street = input("Street Name: ")
                city = input("City: ")
                state = input("State: ")
                zip = input ("Zip: ")
                customer.SetAddress(Street, add_number, city, state, zip)


        else:
            print ("Invalid input.")
            break
    else:
        password = input("Password: ")
        if customer.IsRightPassword(password):
            print("\n-----------------User has been identified, Welcome! {user} \n".format(user = username.upper()))
            verify = True
        else:
            print("Wrong Password, Try Again!")
        # print(customer.GetAddress())
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
        cdl = input("(A) Manage Account \n(I) View Inventory \n(C) Cart Options and Information \n(L) Log Out\n(E) Exit\n>>")

        #(I) View Inventory
        if cdl.lower()=='i':
            inventory.print()

        #(A) Manage Account
        elif cdl.lower()=='a':
            print("\n------------------------{account_information}-------------------------\n".format(account_information = account_info))

            account_edit = True
            while account_edit == True:
                print("ACCOUNT MENU: ")
                account_option = input("(A) View Account Details\n(S) View Shipping Information\n(V) View Billing Information\n(E) Edit account information \n(P) Edit stored payment information\n(O) View Order History\n(D) Delete Account\n(B) Go Back \n>>")
                account_edit2 = True
                while account_edit2 == True:
                    if account_option.lower() == 'a':
                        customer.printAccount()
                        print('\n')
                        account_edit2 = False
                    elif account_option.lower() == 's':
                        customer.printShipping()
                        print('\n')
                        account_edit2 = False
                    elif account_option.lower()=='v':
                        customer.printBilling()
                        print('\n')
                        account_edit2 = False
                    elif account_option.lower()=='e':
                        account_option2 = input ("(A) Edit name \n(B) Edit Shipping Address\n(E) Go Back to Account Menu\n>>")
                        if account_option2.lower()=='a':
                            firstname = input("Update First Name: ")
                            lastname = input("Update Last Name: ")
                            customer.SetName(firstname, lastname)
                            print("Account Information updated.")
                            account_edit2 = False
                        elif account_option2.lower() == 'b':
                            streetNumber = input("Update Street Number: ")
                            streetName = input("Update Street Name: ")
                            city = input("Update city: ")
                            state = input("Update state: ")
                            zip = input("Update zip: ")
                            customer.SetAddress(streetName, streetNumber, city, state, zip)
                            print("Account Information updated.")
                            account_edit2 = False
                        elif account_option2.lower() == 'e':
                            account_edit2 = False
                    elif account_option.lower() == 'p':
                        print("Updating Stored Payment Information")
                        cardName = input("Name on Card: ")
                        while True:
                            cardNum = input("Input CardNumber: ")
                            if cardNum.isnumeric() == True:
                                break
                            elif cardNum.isnumeric() == False:
                                print("Invalid Input. Card Number should contain numbers only.")
                        billingAddress = input("Billing Address -- STREET NUMBER AND STREET NAME: ")
                        billingCity = input("Billing City: ")
                        billingState = input("Billing State: ")
                        billingZip = input("Billing ZIP: ")
                        customer.EditPaymentInfo(cardName, cardNum, billingAddress, billingCity, billingState, billingZip)
                        account_edit2 = False

                    elif account_option.lower()=='o':
                        order.print()
                        account_edit2 = False
                    elif account_option.lower() == 'd':
                        customer.DeleteAccount(order)
                    elif account_option.lower()=='b':
                        account_edit2 = False
                    else:
                        print("INVALID INPUT -- returning to main menu")
                        account_edit2 = False
                if (account_option.lower()=='b'):
                    account_edit = False

        #(C) Cart Options
        elif cdl.lower() == 'c':
            cart = customer.GetCart()
            cart_edit = True
            while cart_edit:
                # read card information
                cart.print()
                adcb = input("\n(A) Add to Cart\n(I) View Inventory\n(D) Delete from cart -- by ISBN number\n(C) Checkout\n(B) Go Back\n(V) View Cart\n>>")
                if adcb.lower()=='a':
                    isbn = input("\nInput ISBN number:")
                    quantity = int(input("Number of items:"))
                    # cart list
                    if inventory.checkQuantity(isbn, quantity)==1:
                        cart.AddToCart(isbn, quantity)
                        inventory.removeInventory(isbn, quantity)
                    elif inventory.checkQuantity(isbn, quantity)==0:
                        print('Inventory doesn\'t have enough quantity.')
                        continue
                    elif inventory.checkQuantity(isbn, quantity)==-1:
                        print('Invalid ISBN number.')
                        continue
                if adcb.lower()=='d':
                    isbn = input("\nInput ISBN number for the book you want to remove: ")
                    compare = cart.InventoryCheck(isbn)
                    inventory.addback(isbn, compare)
                    cart.RemoveFromCart(isbn)
                    
                elif adcb.lower()=='c':
                    cart.checkout(inventory, order, customer)
                    cart_edit = False
                elif adcb.lower() == 'u':
                    inventory.print()
                elif adcb.lower() == 'v':
                    cart.print()
                elif adcb.lower() == 'i':
                    inventory.print()
                elif adcb.lower()=='b':
                    cart_edit = False
                else: 
                    print("Please select from the options below:")
                # (L) Log Out
        elif cdl.lower() == 'l':
        # This will add all items left in cart back to inventory if the user logouts without checking out.
            cart = customer.GetCart()
            check = cart.CartCheck()
            if check == True:
                cart.AddBackToInventory(inventory)
            customer.Logout()

        #(E) Exit
        elif cdl.lower()=='e':
            cart = customer.GetCart()
            check = cart.CartCheck()
            if check == True:
                cart.AddBackToInventory(inventory)
            customer.Logout()
