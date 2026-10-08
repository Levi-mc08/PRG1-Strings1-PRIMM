record = "Lovelace;Ada;1815;mathematician;England"

parts = record.split(";")

surname = parts[0]
forename = parts[1]
born = parts[2]
role = parts[3]
country = parts[4]

print(f"{forename} {surname} was born in {born} and worked as a {role}; she was from {country}.")
print(f"Initials: {forename[0]}.{surname[0]}.")
