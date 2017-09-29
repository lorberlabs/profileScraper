from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup
from xy import profile
url = "https://scrapebook22.appspot.com/"
csv_file = open("emails.csv", "w+")
response = urlopen(url).read()

soup = BeautifulSoup (response)

print soup.html.head.title.string

for link in soup.findAll("a"):
    if link.string == "See full profile":
       responseProfile = urlopen( url + link["href"]).read()
       soupProfile = BeautifulSoup(responseProfile)
       profileData = soupProfile.findAll("li")


       gender = profileData[0].span.string
       age = int( profileData[1].string.split(" ")[1])
       city = profileData[2].span.string
       email = profileData[3].span.string


       profil = profile("", gender, age, city,email)

       csv_file.write(profil.to_csv() + "\n")

csv_file.close()





