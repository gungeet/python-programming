class InstagramAccount:
    def __init__ (self, username, password):
        self.username = username
        self.password = password
        self.followers = []
        self.photos = []

    def follow (self, another_account):
        if isinstance(another_account, InstagramAccount): #if another account is an instance of InstagramAccount, append followers or print the error message
            another_account.followers.append(self.username)
        else:
            print('Not a valid account')

    def add_photos(self, photo):
        if isinstance(photo, dict):
            all_keys = photo.keys()
            if 'photo_id' in all_keys and 'url' in all_keys and 'likes' in all_keys: #troubleshooting if photos has the keys to check if it's a valid photo
                self.photos.append(photo)

    def get_followers (self):
        return self.followers

    def __repr__(self):
        return '<username: {}, password: {}, followers: {}, photos: {}>' .format(self.username, self.password, self.followers, self.photos)

my_account = InstagramAccount('gungeet', '14u')
second_acccount = InstagramAccount('mishooo', '14u2')
third_account = InstagramAccount('sushi', 'eat111')

my_account.follow(second_acccount)
third_account.follow(second_acccount)

my_account.add_photos({'photo_id': 1, 'url': 'https://picsofdogs.com', 'likes': 0})

print(second_acccount.get_followers())

print(second_acccount)

# def print_menu():
#     print("1. Add account")
#     print("2. Follow account")

# def main(): #this is what shows up first, it's like index
#     accounts = []

#     while True:
#         print_menu()
#         choice = input('Whatcha wanna do?):')
#         if choice == '1':
#             username, password = input('Enter username and password (sepatated by commas):').split(',')
#             accounts = InstagramAccount(username, password)
#             accounts.append(account)
