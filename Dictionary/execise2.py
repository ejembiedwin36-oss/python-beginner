
state_populations = {
    "Kano": 15.0,
    "Lagos": 16.5,
    "Anambra": 5.5,
    "Oyo": 8.0,
    "Borneo": 6.0,
    "Rivers": 7.5,
    "Kaduna": 9.5
}

state_zones = {
    "Kano": "North West",
    "Kaduna": "North West",
    "Lagos": "South East",
    "Oyo" : "South West",
    "Anambra": "South East", 
    "Borneo": "North East", 
    "Rivers": "South South",

}


states = []
populations = []
zones = []

for state, population in state_populations.items():
    if population > 8.0:
        print(f"the population of {state} is {population} million.")
print("\n")
    


for state, zone in state_zones.items():
    population = state_populations[state]

    print(f" {state} is in the {zone} and {population} million people.")

