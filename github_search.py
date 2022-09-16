import requests
import sys


class User:
    def __init__(self, username):
        self.name = ""
        self.login = username
        self.url = ""
    
    def reqUser(self):
        user = requests.get(f'https://api.github.com/users/{self.login}')
        data = user.json()
        self.name = data["name"]
        self.url = data["html_url"]
    
    def __str__(self):
        return f'{self.name:<30} {self.login:<30} {self.url:<30}'
    

if __name__ == "__main__":
    usersListTerminal = sys.argv[1:]

    for userName in  usersListTerminal:
        index = User(userName)
        index.reqUser()
        print(index)

    
