import urllib2
from bs4 import BeautifulSoup
import re
import MySQLdb as mysql





##<div class="star-box-giga-star">
##8.9
##</div>



def get_links(number):
    url="http://www.imdb.com/title/tt"+str(number) # example URL for titles
    try:
        response=urllib2.urlopen(url)
    except:
        return None
        
    data=response.read()
    soup=BeautifulSoup(data)
    
    title=str(soup.title.contents[0])
    star=soup.select(".star-box-giga-star")
    description=""
    for i in soup.findAll('p',itemprop='description')[0].contents:
        description+=str(i)
    if  description=="":
        description="Not Available"
    if star:
        rating=('.').join(re.findall('\d',str(star[0])))
    else:
        rating="No Rating Available"
    genreTags=soup.findAll('a',itemprop='genre')
    genre=""
    for i in genreTags:
        genre+=i.contents[0]
        genre+=" "
    
    return {"Title":title,"Rating":rating,"Description":description.strip("\n"),"Genre":genre}





f=open("links.txt",'a')
def test():
#    conn=mysql.connect('localhost','root','root','ml')
    for i in range(946,100000):
        a=get_links(i)
        if a:
            print "Writing ",a["Title"],":::",a["Rating"],":::",a["Description"],":::",a["Genre"],"\n"
            f.write(str(a["Title"])+":::"+str(a["Rating"])+":::"+str(a["Description"])+":::"+str(a["Genre"])+"\n")
#            query="insert into data(title,rating,desription,genre) values('"+str(a["Title"])+"',"+str(a["Rating"])+ ",'"+str(a["Description"]).replace("'","''")+"','"+str(a["Genre"])+"')"
#            print "Executing Query",query
#            conn.query(query)
#            print "Query Success full"
#            
        else:
            print "Nothing Found"
test()

f.close()