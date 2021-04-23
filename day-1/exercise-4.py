# Exercise 4

rps_dict = {'R':'S', 'P':'R', 'S':'P'}

inputs = [
    input(f"Player {i+1}, make a selection from {', '.join(rps_dict)}! ").upper()
    for i in range(2)
]

if set(inputs).issubset(set(rps_dict)): # validation using sets
    
    for i, choice in enumerate(inputs):

        if rps_dict[choice] == inputs[(i+1)%2]: # does player i's choice beat the opponent's choice?
            print(f"Player {i+1} wins!")
            break

    else:
        print("No one wins!")

else: 
    print("Input invalid!")
