UsernameInput = input("Username :")
PasswordInput = input("Password :")
if UsernameInput == "admin" and PasswordInput == "1234" :
    print("Welcome")
    print("------------------------")
    print("1.Latte      25 THB")
    print("2.Moccha     25 THB")
    print("3.Thai tea   20 THB")
    Userselected = input(">>")
    if Userselected == "1" :
        unit = int(input("How many :"))
        print(25 * unit)
    elif Userselected == "2" :
        unit = int(input("How many :"))
        print(25 * unit)
    elif Userselected == "3" :
        unit = int(input("How many :"))
        print(20 * unit)
    else :
        print("Try again")
else :
    print("Try again")

