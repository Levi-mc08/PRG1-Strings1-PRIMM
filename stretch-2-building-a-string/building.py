def initials_of(full_name):
    initials = ""
    for part in full_name.split(" "):
        if len(part) >= 2:
            initials = initials + part[0].upper() + "."
    return initials


def redact(text, secret):
    if len(secret) > 4:
        encoded_secret = (len(secret) - 4) * "*" + secret[4:]
    return encoded_secret


print(initials_of("ada byron lovelace"))
print(initials_of("Grace Hopper"))

print(redact("The code is SAVE2024 until Friday", "SAVE2024"))
