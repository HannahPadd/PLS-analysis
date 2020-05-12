program = True
while (program == False):
    UserInput = input("""
    If you want to create a user press 1.
    If you want to lend a book press 2.
    If you want to return a book press 3.
    If you want to search for a book press 4.
    """)

    if (UserInput == 1):
        print("create user")
    if (UserInput == 2):
        print("You have lended a book")
    if (UserInput == 3):
        print("You have returned a book")
    if (UserInput == 4):
        print("you have have searche")