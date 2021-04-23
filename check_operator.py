def check_operator(user_input):
    if user_input == '+' or user_input == '-' or user_input == '*' or user_input == '/':
        return user_input
    else:
        print("Entered opertor was not valid")

