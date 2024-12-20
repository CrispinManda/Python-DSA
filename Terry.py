import requests 

    # Send a GET request to the GitHub API
response = requests.get('https://api.github.com/users/octocat')

print(response.json())

