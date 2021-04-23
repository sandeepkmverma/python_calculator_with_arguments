def inputNumber(arg_value):
  while True:
    try:
       userInput = int(arg_value)
    except ValueError:
       print("Not an integer! Try again.")
       break
    else:
       return userInput
