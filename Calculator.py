def StartCalculating():
    GetTheNumber1 = int(input("Enter Your First Number : "))
    GetTheNumber2 = int(input("Enter Your Second Number : "))
    Add = GetTheNumber1 + GetTheNumber2
    Multiplication = GetTheNumber1 * GetTheNumber2
    Negative = GetTheNumber1 - GetTheNumber2
    Division = GetTheNumber1 / GetTheNumber2
    print("Select Your Request : ")
    print("* For Multiplication")
    print("/ For Division")
    print("+")
    print("-")
    GetTheRequest = input("Enter Your Request : ")
    if GetTheRequest == "+":
        print("Your Answer Is :", Add)
        StartAgain()
    elif GetTheRequest == "-":
        print("Your Answer Is :", Negative)
        StartAgain()
    elif GetTheRequest == "*":
        print("Your Answer Is :", Multiplication)
        StartAgain()
    elif GetTheRequest == "/":
        print("Your Answer Is :", Division)
        StartAgain()
    else:
        print("Invalid Format.")
        return StartCalculating()
def StartAgain():
    Again = input("Do You Want To Calculate Again (y/n) ? ")
    if Again == "y":
        StartCalculating()
    elif Again == "n":
        quit()
    else:
        print("Please Enter Your Request Again.")
        return StartAgain()
StartCalculating()
