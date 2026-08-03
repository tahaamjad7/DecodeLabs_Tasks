# password_checker.py
# Checks how strong a password is based on a few basic rules:
# - length
# - has lowercase letters
# - has uppercase letters
# - has numbers
# - has special symbols
#
# Not a replacement for a real security audit, just a quick sanity check.

import string

SPECIAL_CHARS = "!@#$%^&*()_+-=[]{}|;:,.<>?/~`"


def check_password(password):
    length = len(password)
    has_lower = False
    has_upper = False
    has_digit = False
    has_symbol = False

    for ch in password:
        if ch in string.ascii_lowercase:
            has_lower = True
        elif ch in string.ascii_uppercase:
            has_upper = True
        elif ch.isdigit():
            has_digit = True
        elif ch in SPECIAL_CHARS:
            has_symbol = True

    # count how many "types" of characters are present
    variety_score = sum([has_lower, has_upper, has_digit, has_symbol])

    # --- decide strength ---
    # short password = weak no matter what
    if length < 6:
        return "Weak", has_lower, has_upper, has_digit, has_symbol

    if length >= 8 and variety_score >= 3:
        strength = "Strong"
    elif length >= 6 and variety_score >= 2:
        strength = "Medium"
    else:
        strength = "Weak"

    return strength, has_lower, has_upper, has_digit, has_symbol


def print_report(password, strength, has_lower, has_upper, has_digit, has_symbol):
    print("\nPassword entered :", password)
    print("Length            :", len(password))
    print("Lowercase letters :", "Yes" if has_lower else "No")
    print("Uppercase letters :", "Yes" if has_upper else "No")
    print("Numbers           :", "Yes" if has_digit else "No")
    print("Symbols           :", "Yes" if has_symbol else "No")
    print("Strength Result   :", strength)

    # a little feedback so the user knows what to improve
    if strength == "Weak":
        print("Tip: try making it longer and mix in numbers/symbols.")
    elif strength == "Medium":
        print("Tip: add an uppercase letter or a symbol to make it stronger.")
    else:
        print("Looks good, this is a strong password.")


def main():
    print("---- Password Strength Checker ----")
    pwd = input("Enter a password to check: ")

    if pwd.strip() == "":
        print("You didn't type anything, run the program again.")
        return

    strength, has_lower, has_upper, has_digit, has_symbol = check_password(pwd)
    print_report(pwd, strength, has_lower, has_upper, has_digit, has_symbol)


if __name__ == "__main__":
    main()
