print("Enter Electic Bill")
current_unit = float(input("Enter Your curent Unit "))
previous_unit = float(input("ENte your Privous Unit"))

Lpu_unit = current_unit - previous_unit
print("your Toal Unit is: ", Lpu_unit) 

# condition
if (Lpu_unit > 100):
    {   
        print("You Have to pay 6.95/unit : ", Lpu_unit * 6.95)
    }
else:
    print ("You have to pay 5.95.unit", Lpu_unit * 5.95)