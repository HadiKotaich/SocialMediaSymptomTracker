from UserClass import User
from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager


# Authors: 
# Ayham Olleik --  abo00@mail.aub.edu
# Nourhane Abdel Samad

#The driver required for chrome to open is automatically downloaded here
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https:web.whatsapp.com')

#need to scan the QR code here manually before continuing!

name = input('Press Enter If you scanned the QR code')

# -------------------------------------------------
#creating a user that is already in my whatsapp chat and trying the features 

TestUser = User("Test", driver) # name something you have in the list of your chat conversations
#TestUser.SendMessage("Hello Test User", 2)
#TestUser.ClearChat()
messages = TestUser.GetRecentMessages()
for msg in messages:
    print(msg)


del TestUser