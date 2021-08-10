import requests

username = ""
password = ""
token = "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"
headers = {'Authorization': 'token '+ token}

# Get repo data
url = "https://api.github.com/users/RohanDeySarkar/repos?per_page=60"
req = requests.get(url, headers=headers)
data = req.json()

# Store individual repo details
repos = []
for i in range(len(data)):
    details = {}
    details["name"] = data[i]["name"]
    details["createdAt"] = data[i]["created_at"]
    details["updatedAt"] = data[i]["updated_at"]
    repos.append(details)

# Store branch details of each repo
for i in range(len(repos)):
    branchURL = "https://api.github.com/repos/RohanDeySarkar/"+ repos[i]["name"] + "/branches"
    req = requests.get(branchURL, headers=headers)
    branchData = req.json()
    repos[i]["branches"] = branchData

# print(repos[0])

# branches
# https://api.github.com/repos/RohanDeySarkar/Portfolio/branches/gh-pages
# https://api.github.com/repos/RohanDeySarkar/Portfolio/commits --> len()  Contribution
# https://api.github.com/repos/RohanDeySarkar/Portfolio/commits/a4c3115f76be60fbaae9ded79aa21235996f4c7d?per_page=60

# Only getting contributions of main branch
totalContributions = 0
for i in range(len(repos)):
    contributionURL = 'https://api.github.com/repos/RohanDeySarkar/' + repos[i]["name"] + '/contributors'
    req = requests.get(contributionURL, headers=headers)
    contributionData = req.json()
    totalContributions += contributionData[0]["contributions"]

print(totalContributions)

