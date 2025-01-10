print(" 1 : Addition\n")
print(" 2 : sub\n")
print(" 3 : product\n")
print(" 4 : division\n")

choice = input("enter your choice: ")
num1 = int(input("Enter frist number:"))
num2 = int(input("Enter seccond number:"))

if choice == '1':
    print(f"Addition is: {num1 + num2}")

elif choice == '2':
    print(f"Substraction is : {num1 - num2}")

elif choice == '3':
    print(f"Production is : {num1 * num2}")

elif choice == '4':
    if (num2 != 0):
        print(f"Devision is : {num1 / num2}")

else:
    print("Invalid Choice")