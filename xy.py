
class profile(object):
    name = ""
    gender= ""
    age = ""
    city = ""
    email= ""

    def __init__(self,name,gender,age,city,email):
        self.name = name
        self.gender = gender
        self.age = age
        self.city = city
        self.email = email

    def to_csv(self):
        return self.name + ","\
           + self.gender + ","\
           +str(self.age )+ ","\
           +self.city + ","\
           +self.email






