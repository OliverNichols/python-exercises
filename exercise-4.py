player_1 = input("Input a selection from R, P or S! ").upper()
player_2 = input("Input another selection from R, P or S! ").upper()

if player_1 not in ['R','P','S']:
    print("Input invalid!")
    quit()

if player_2 not in ['R','P','S']:
    print("Input invalid!")
    quit()

rps_dict = {'R':'S', 'P':'R', 'S':'P'}

if player_1 == player_2:
    print("No one wins!")

elif rps_dict[player_1] == player_2:
    print("Player 1 wins!")

elif rps_dict[player_2] == player_1:
    print("Player 2 wins!")

else:
    print("RPS game broken!")

