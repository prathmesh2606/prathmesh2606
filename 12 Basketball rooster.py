#Basketball Roster Program
print("\t\t\tWelcome to the Basketball Roster Program")

#Get user input and define list
player = []
player.append(input("\nWho is your Point Guard: ").title().strip())
player.append(input("Who is your Shooting Guard: ").title().strip())
player.append(input("Who is your small forward: ").title().strip())
player.append(input("Who is your Power forward: ").title().strip())
player.append(input("Who is your center: ").title().strip())

#Display rooster
print("\t\t\tYour Starting 5 for the upcoming basketball Season" + "\n\t\t\t\tPoint Guard:\t\t\t" + player [0]+ "\n\t\t\t\tShooting Guard:\t\t\t" + player [1]+ "\n\t\t\t\tSmall Forward:\t\t\t" + player [2]+ "\n\t\t\t\tPower Forward:\t\t\t" + player [3]+ "\n\t\t\t\tCenter:\t\t\t\t" + player [4])

#Remove injured player
injured_player = player.pop(2)
print("\nOh No!!! " +injured_player+" is injured.")
print("Your Rooster only has "+str(len(player))+" players.")

#adding new Player
new_player = input("Who will take " + injured_player +" 's"+" spot: ").title().strip()
player.insert(2, new_player )

#dislplaying new list
print("\t\t\tYour Starting 5 for the upcoming basketball Season" + "\n\t\t\t\tPoint Guard:\t\t\t" + player [0]+ "\n\t\t\t\tShooting Guard:\t\t\t" + player [1]+ "\n\t\t\t\tSmall Forward:\t\t\t" + player [2]+ "\n\t\t\t\tPower Forward:\t\t\t" + player [3]+ "\n\t\t\t\tCenter:\t\t\t\t" + player [4])
print("Good Luck!! " +player[2] + " you will do great job." )
print("Your Rooster now has "+str(len(player)) + " players.")
