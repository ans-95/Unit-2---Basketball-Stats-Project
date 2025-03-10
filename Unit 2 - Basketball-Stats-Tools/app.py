import constants 

def clean_data(): 
    cleaned = []
    for user in data: 
        fixed = {}
        fixed["name"] = user["name"]
        # Split guardian string into a list and remove the "and" between names
        fixed["guardian"] = user["guardians"].split("and")
        if user["experience"] == 'YES':
            fixed["experience"] = True
        else:
            fixed["experience"] = False   
        fixed["height"] = int(user["height"])
        cleaned.append(fixed)
    return cleaned 

print(clean_data(data))

def balance_teams():
    num_players_team = len(PLAYERS) / len(TEAMS)


if __name__ == '__main__':