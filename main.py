pi = ["3.1415926535", "3.14159265358979323846", "3.141592653589793238462643383279", "3.1415926535897932384626433832795028841971", "3.1415926535897932384626433832795028841971 6939937510", "3.141592653589793238462643383279502884197169399375105820974944", "3.1415926535897932384626433832795028841971693993751058209749445923078164", "3.14159265358979323846264338327950288419716939937510582097494459230781640628620899", "3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825", "3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067"]

setting = input("Test Number >> ")

if input("Enter The Digits >> ") == pi[int(setting) - 1]:
    print("You Got It Right!")
else:
    print(f"You Got It Wrong, Its: {pi[int(setting) - 1]}")