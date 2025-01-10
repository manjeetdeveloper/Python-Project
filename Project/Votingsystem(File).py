# find age of a function if any exception accure it shoud print age is not positve numbers or enterd a valed numeric value or else "You are elagible to vote " inside the except block add another try a block to handled the case whre to users try to input string instand a number.

def age():
    while True:
        try:
            age = input("Enter Your Age:")
            try:
                age = int(age)
                if age >= 0:
                    raise ValueError("Age hona chiye positive number")
                print("Wow😎 App Vote De skte Hai")
                break
            except ValueError:
                print("Oops! Plese enterd positve num  And Add please Numeric NUmber make sure ")
        except Exception:
            print("Age me number dalo Yr: 🙏")

age()
