def percentage(option):
    if option == "cc":
        maths = int(input("Enter Maths mark: "))
        physics = int(input("Enter Physics mark: "))
        chemistry = int(input("Enter Chemistry mark: "))

        total = physics /2 + chemistry /2
        display=total + maths 
        print("calculate of marks:",display)
        
    elif option == "mp":
        subject=(input("enter subject name:"))
        
        if subject in ["maths","physics","chemistry"]:
            mark=int(input("enter a mark:"))
            value = mark / 10
        print(value)
            
    else:
        print("Invalid Option")

username = input("Enter user name: ")
Dob = input("Enter DOB: ")

print("Option -- [calculate -> cc, mark to percentage -> mp]")

option = input("Enter option: ")

percentage(option)