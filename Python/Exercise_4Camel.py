import re


def to_camel_case(text):
    """
    capitalizes string based on pascal case rules
    text: string separated by dash or underscore
    returns pascal cased string
    """
    textRegex = re.compile(r"^\w+((_|-)\w+)+\Z$")
    if textRegex.match(text):
        words = re.split(r"_|-", text)
        camelCased = [w.capitalize() for w in words[1:]]
        camelCased.insert(0, words[0])
        return "".join(camelCased)
    else:
        return text


print(to_camel_case(""))
print(to_camel_case("the-stealth-warrior"))
print(to_camel_case("The_Stealth_Warrior"))
