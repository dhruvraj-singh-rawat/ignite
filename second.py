import json

#Loading the JSON File
searches = []
for line in open('searches.json', 'r'):
    searches.append(json.loads(line))

print (searches[0]['login_count'])