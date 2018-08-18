import json

# Loading the JSON File
searches = []
for line in open('searches.json', 'r'):
    searches.append(json.loads(line))

B_SearchCount=0
B_SearchUsers=0
b_users=0
b_login=0


A_SearchCount=0
A_SearchUsers=0
a_users=0
a_login=0

# Extracting the Required Fields from the JSON Files
for i in range(len(searches)):
    if searches[i]['uid'] % 2 == 0 and searches[i]["is_instructor"]==False:
        a_users=a_users+1
        a_login=a_login+searches[i]['login_count']

        if searches[i]['search_count'] :
            A_SearchCount=A_SearchCount+searches[i]['search_count']
            A_SearchUsers=A_SearchUsers+1

        

    elif searches[i]['uid'] % 2 != 0 and searches[i]["is_instructor"]==False :
        b_users=b_users+1
        b_login=b_login+searches[i]['login_count']
        

        if searches[i]['search_count'] :
            B_SearchCount=B_SearchCount+searches[i]['search_count']
            B_SearchUsers=B_SearchUsers+1

print ('Percentage of Users using Search in Design A :',(A_SearchUsers/a_users)*100,' and Percentage of Users using Search in Design B ',(B_SearchUsers/b_users)*100 )

print ('Average No of Search in Design A (who are using Search) : ', A_SearchCount/A_SearchUsers , ' and Average No of Search in Design B (who are using Search) : ', B_SearchCount/B_SearchUsers )
