import re

def validate_pin(pin):
    #return true or false
    pinRegex = re.compile(r"^(\d{4})(\d{2})?\Z$")  # \Z important to avoid matching new line
    return True if pinRegex.search(pin) else False

print(validate_pin("1234"))
print(validate_pin("12345"))
print(validate_pin("a234"))
print(validate_pin("1234\n"))
