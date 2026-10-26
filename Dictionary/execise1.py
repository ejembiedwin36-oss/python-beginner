# A mapping of all 36 Nigerian states and the Federal Capital Territory (FCT) 
# paired with their respective administrative capitals.

nigeria_states_and_capitals = {
    "Abia": "Umuahia",
    "Adamawa": "Yola",
    "Akwa Ibom": "Uyo",
    "Anambra": "Awka",
    "Bauchi": "Bauchi",
    "Bayelsa": "Yenagoa",
    "Benue": "Makurdi",
    "Borno": "Maiduguri",
    "Cross River": "Calabar",
    "Delta": "Asaba",
    "Ebonyi": "Abakaliki",
    "Edo": "Benin City",
    "Ekiti": "Ado Ekiti",
    "Enugu": "Enugu",
    "FCT (Abuja)": "Abuja",
    "Gombe": "Gombe",
    "Imo": "Owerri",
    "Jigawa": "Dutse",
    "Kaduna": "Kaduna",
    "Kano": "Kano",
    "Katsina": "Katsina",
    "Kebbi": "Birnin Kebbi",
    "Kogi": "Lokoja",
    "Kwara": "Ilorin",
    "Lagos": "Ikeja",
    "Nasarawa": "Lafia",
    "Niger": "Minna",
    "Ogun": "Abeokuta",
    "Ondo": "Akure",
    "Osun": "Osogbo",
    "Oyo": "Ibadan",
    "Plateau": "Jos",
    "Rivers": "Port Harcourt",
    "Sokoto": "Sokoto",
    "Taraba": "Jalingo",
    "Yobe": "Damaturu",
    "Zamfara": "Gusau"
}

# Initialize empty lists to separate keys (states) and values (capitals)
states = []
capitals = []

# Distribute dictionary keys and values into their respective lists
for state, capital in nigeria_states_and_capitals.items():
    states.append(state)
    capitals.append(capital)

# Output the list of states to the console
for state in states:
    print(f"{state} state")
print("\n")

# Output the list of capitals to the console
for capital in capitals:
    print(f"{capital} capital")
