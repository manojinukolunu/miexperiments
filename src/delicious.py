from pydelicious import get_popular ,get_userposts,get_urlposts
import pickle

import time

def initializeUserDict(tag,count=5):
    user_dict={}
    for p1 in get_popular(tag=tag)[0:count]:
        for p2 in get_urlposts(p1['url']):
            user=p2['user']
            user_dict[user]={}
    return user_dict

def fillItems(user_dict):
    all_items={}
    for user in user_dict:
        for i in range(3):
            try:
                posts=get_userposts(user)
                break
            except:
                print "Failed user "+user+", retrying"
                
    for post in posts:
        url=post['url']
        user_dict[user][url]=1.0
        all_items[url]=1
        
    for ratings in user_dict.values():
        for item in all_items:
            if item not in ratings:
                ratings[item]=0.0
                
delusers=initializeUserDict('programming')
delusers['manoji']={}
fillItems(delusers)



output = open('data.pkl', 'wb')
pickle.dump(delusers,output)
output.close()