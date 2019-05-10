import requests

response = requests.get('https://statsapi.web.nhl.com/api/v1/teams/name')

team_list = response.json()

# print(team_list['teams']) #how pull something from dictionary. name of dic team_list followed by key ['key']


# for id in team_list:
#     if 'name' == 'Toronto Maple Leafs':
#        print ('id')


# Access the stats for Toronto Maple Leaves the 2017 season. print it out!

#Find the team in the api 
#Print the list

# team_list is the api > selectively print one name > 
# for teams in team_list print Toronto Maple Leafs

# print(team_list['Toronto Maple Leafs'])



# if team_list['name'] == 'Toronto Maple Leafs':
#     return 

# parameter = {'name': 'Toronto Maple Leafs' }
# response = requests.get('https://statsapi.web.nhl.com/api/v1/teams/', params = parameter)

# print(response)

# Access the stats for Toronto Maple Leaves the 2017 season. print it out!

#Find the team in the api 
#Print the list

# team_list is the api > selectively print one name > 
# for teams in team_list print Toronto Maple Leafs

# print(team_list['Toronto Maple Leafs'])



# if team_list['name'] == 'Toronto Maple Leafs':
#     print(team_list['name'])

print(team_list['teams'])[0] 