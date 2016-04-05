state_names = {"QLD":"Queensland", "NSW":"New South Wales", "TAS":"Tasmania","VIC":"Victoria", "ACT":"Australia Capital Territory","NT":"Northern Territory", "WA":"Westeran Australia"}
state = input("Enter short state:").upper()

while state != '':
    if state in state_names:
        print(state, "is", state_names[state])
    else:
        print("Invalid State Name")
    state = input("Enter short state:").upper()
