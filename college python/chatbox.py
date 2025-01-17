
respond={
    "hello":"hi",
    "what is your name":"hello ,my name is swastik",
    "earth":"It is a planet where living organism lives ",
    "moon":"its the natural satellire of the plane",
    "how are you":"i am fine thanQ,and how you doing ,all good?",
    "yes":"Okeee",
    "you are looking gorgeous":"oh, thanQ",
    "this place is good":"yeah I also feel same",
    "how was your childhood":"I was a good student ,at my school time, i had many friends in my childhood",
    "do you want to grab some food":"yah ! sure.",
    "what do you want to eat":"My prefer is your prefer"
    }
x=' '
while x!='0':
        x= str(input("enter the message_"))
        print(respond.get(x,'I do not understand that..'))
# thisdict = dict(name = "John", age = 36, country = "Norway")
# print(thisdict)
# print(respond)
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict["brand"])