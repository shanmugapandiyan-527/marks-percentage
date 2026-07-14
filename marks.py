username= input("Enter user name: ")
Dob = input("Enter DOB: ")

print("Option -- [calculate -> cc, mark to percentage -> mp]")

option = input("Enter option: ")

if option == "cc":
    maths = int(input("Enter Maths: "))
    physics = int(input("Enter Physics: "))
    chemistry = int(input("Enter Chemistry: "))

    total = (maths + physics + chemistry) / 2  
    print("Calculate of marks:", total)

elif option == "mp":
    subject = input("Enter Subject Name: ")

    if subject in ["maths", "physics", "chemistry"]:
        marks = int(input("Enter Mark: "))
        percentage = marks / 10

print("Percentage:", percentage)
        
        



 


