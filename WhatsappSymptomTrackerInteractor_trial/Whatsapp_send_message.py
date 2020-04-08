from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager


# Authors: 
# Ayham Olleik --  abo00@mail.aub.edu
# Nourhane Abdel Samad
#

#The driver required for chrome to open is automatically downloaded here
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https:web.whatsapp.com')

name = input('Enter the name of user or group : ')
msg = input('Enter your message : ')
counter = int(input('Enter the count : '))

input('Enter anything after scanning QR code')

#Finds the span that contains the user with the name you provided
user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
#clicking to open the conversation
user.click()

#locating and holding the message box
msg_box = driver.find_element_by_class_name('_1Plpp')

#Sending the message for counter times 
for i in range(counter):
    msg_box.send_keys(msg)
    #driver.execute_script("arguments[0].innerHTML("+msg+");");
    button = driver.find_element_by_class_name('_35EW6')
    #pressing the send message
    button.click()

# it seems i have problems with spaces in username and unseen names or grps probably due to 
# paging -- thus you can't add a username with spaces
# and you can't send to an old user or group