#classes lets us build our own type. but if you print the date you've added, it'll return a memmory address so you have to tell python how to display it

class HockeyTeam:
    def __init__(self, name, division, conference): #the data we need to create the team; it will be called when creating the team; this is the template to create a hockey team
       self.name = name
       self.division = division
       self.conference = conference
       self.roster = []

    def add_player(self, player):
       #add player to a team
       #ask name, position, number
       #ask which team the player should be added to
       #if team already exists append player to that list
       #if not, create new team and add to that list
       name, position, number = input('Enter player\'s name, position, and shirt number: ')
       self.hockey_team.append(player)

    def remove_player(self, player_name):
         for idx, player_name in enumerate(hockey_team): #returns postion of the team inside the roster
            if hockey_team['name'] == player_name: #if the hockey team exists/ if idx exists
                hockey_teams[idx].pop(player) #return the name of team name at the idx and append that player to the team

    def get_roster(self):
       pass

def print_menu():
   print("1. Create hockey team")
   print("2. Add player to a team roster")
   print("3. Remove player from a team roster")
   print("4. Show team roster")

def main(): #this is what shows up first, it's like index
   hockey_teams = [] 

   while True:
    print_menu()
    choice = input('Enter menu option (q to quit):')
    if choice == '1':
        name, division, conference = input('Enter name, division and conference (sepatated by commas):').split(',')
        team = HockeyTeam(name, division, conference)
        hockey_teams.append(team)
        #print (hockey_teams)
    elif choice == '2':
        name, position, number = input('Enter player\'s name, position, and shirt number(sepatated by commas):').split(',')
        player = {}
        player['player_name'] = name
        player['position'] = position
        player['shirt_number'] = number
        team_name = input('Enter the name of the team to add player to:')

        for idx, team in enumerate(hockey_teams): #returns postion of the team inside the roster
            if team['name'] == team_name: #if the hockey team exists/ if idx exists
                hockey_teams[idx].roster.append(player) #return the name of team name at the idx and append that player to the team
    elif choice == '3':
        name = input('Enter the player\'s name you\'d like to delete:')
        #would we ask user to select team from which to delete the player from?
        #or search player in all teams (lists inside a roster)
        if team.player['name'] == name: 
            hockey_teams[idx].roster.pop(player)
    elif choice == '4':
        print('{}'.format(roster(team(player))))

   #  else choice == 'q':
   #      sys.exit()
        


if __name__ == "__main__":
   main()

