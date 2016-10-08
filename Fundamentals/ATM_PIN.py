'''
ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.

If the function is passed a valid PIN string, return true, else return false.

eg:

validate_pin("1234") == True
validate_pin("12345") == False
validate_pin("a234") == False
'''

def validate_pin(pin):
    if str.isdigit(pin) and (len(list(pin)) == 4 or len(list(pin)) == 6):
        return True
    else:
        return False


def validate_pin2(pin):
    return len(pin) in (4, 6) and pin.isdigit()

import re
def validate_pin3(pin):
    return bool(re.match(r'^(\d{4}|\d{6})$',pin))


