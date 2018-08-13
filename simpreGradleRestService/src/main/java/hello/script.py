import requests

fileWithIds = open('path', 'r')
newFile = open('path', 'a+')

lines = fileWithIds.readLines()

for line in lines:
    userGuid = line
    params = {'userGuid':userGuid}
    requisition = requests.get('apiurl', params)
    newFile.write(requisition.json() + '\n')

fileWithIds.close()
newFile.close()
