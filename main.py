from storage import *


while True:
    user_choice = greeting()

    if user_choice == "off":
        break
    elif user_choice == "report":
        report()
    elif user_choice == "1" or user_choice == "2" or user_choice == "3":
        resource_check = check_resource(user_choice)
        if resource_check:
            process_payment(user_choice)
            make_coffee(user_choice)
        else:
            continue
    else:
        print("Wrong Input. Try again")
