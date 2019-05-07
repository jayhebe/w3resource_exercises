import string


def absent_number(phone_number):
    absents = []
    for digit in string.digits:
        if digit not in phone_number:
            absents.append(digit)
            
    return absents


if __name__ == '__main__':
    print(absent_number("13821263780"))
