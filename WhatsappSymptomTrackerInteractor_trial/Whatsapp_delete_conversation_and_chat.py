from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Authors: 
# Ayham Olleik --  abo00@mail.aub.edu
# Nourhane Abdel Samad


#The driver required for chrome to open is automatically downloaded here
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https:web.whatsapp.com')


# pick a contact name to press on a conversation
name = input('Enter the name of user or group conversation you want to delete : ')
user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()



# clear messages
dots3 = driver.find_elements_by_xpath('//*[@title = "Menu"]')
dots3[1].click()

clear1 = driver.find_elements_by_class_name("Pm0Ov._34D8D")
clear1[4].click()

clear2 = driver.find_element_by_class_name("_1WZqU.PNlAR")
clear2.click()


#right click to remove conversation
from selenium.webdriver import ActionChains
actionChains = ActionChains(driver)
user.click()
actionChains.context_click(user).perform()

#remove conversation
clearChat = driver.find_element_by_class_name("Pm0Ov._34D8D")
clearChat.click()

print("done")

    
