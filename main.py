import os


pi = ["3.1415926535", "3.14159265358979323846", "3.141592653589793238462643383279", "3.1415926535897932384626433832795028841971", "3.1415926535897932384626433832795028841971 6939937510", "3.141592653589793238462643383279502884197169399375105820974944", "3.1415926535897932384626433832795028841971693993751058209749445923078164", "3.14159265358979323846264338327950288419716939937510582097494459230781640628620899", "3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825", "3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067"]

pi_Sets = ["3.1415926535", "8979323846", "2643383279", "5028841971", "6939937510", "5820974944", "5923078164", "0628620899", "8628034825", "342117067"]
print("(Remember there are 10 tests and 10 sets of pi and each of them being harder than the others)")
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

if input("Test or Study? >> ") == "Test":
    setting = input("Enter Test Number >> ")
    if input("Enter Digits >> ") == pi[int(setting) - 1]:
        print("You did it!")
    else:
        print("You got it wrong! Here: " + pi[int(setting) - 1])
else:
    while True:
        Piset = int(input("Which Set? >> "))
        print(pi_Sets[Piset - 1])
        if input("Test? (y/n)>> ") == "y":
            cls()
            if input("Enter Digits >> ") == pi_Sets[Piset - 1]:
                print("You Got It Right!")
            else:
                print("You got it wrong! The Digits Are: " + pi_Sets[Piset - 1])



