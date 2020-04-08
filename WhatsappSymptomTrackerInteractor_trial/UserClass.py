
# Authors: 
# Ayham Olleik --  abo00@mail.aub.edu
# Nourhane Abdel Samad


class User:
    name = "" #should not contain spaces for now
    driver = ""
    def __init__(self, name,driver):
        self.name = name
        self.driver = driver

    def SendMessage(self, messageText, numberOfTimes):
        #Finding the user span with this name
        userSpan = self.driver.find_element_by_xpath('//span[@title = "{}"]'.format(self.name))
        userSpan.click()

        #locating and holding the message box
        msg_box = self.driver.find_element_by_class_name('_1Plpp')

        #Sending the message for counter times 
        for i in range(numberOfTimes):
            msg_box.send_keys(messageText)

            #driver.execute_script("arguments[0].innerHTML("+msg+");");
            button = self.driver.find_element_by_class_name('_35EW6')
            #pressing the send message
            button.click()
        print("Message Sent to User "+self.name)

    def ClearChat(self):
        #Finding the user span with this name
        userSpan = self.driver.find_element_by_xpath('//span[@title = "{}"]'.format(self.name))
        userSpan.click()

        #Locating the 3 dots on the right of the page and pressing on them
        dots3 = self.driver.find_elements_by_xpath('//*[@title = "Menu"]')
        dots3[1].click()

        #Pressing on the Clear chat row
        clear1 = self.driver.find_elements_by_class_name("Pm0Ov._34D8D")
        clear1[4].click()
      
        #Pressing the Clear button in the confirmation popup
        clear2 = self.driver.find_element_by_class_name("_1WZqU.PNlAR")
        clear2.click()

        print("Chat Cleared For User "+self.name)

    def ClearConversation(self):
        #Probably you will looset the user
        #Finding the user span with this name
        userSpan = self.driver.find_element_by_xpath('//span[@title = "{}"]'.format(self.name))
        userSpan.click()
        #right click to remove conversation
        from selenium.webdriver import ActionChains
        actionChains = ActionChains(self.driver)
        userSpan.click()
        actionChains.context_click(userSpan).perform()

        #remove conversation
        clearChat = self.driver.find_element_by_class_name("Pm0Ov._34D8D")
        clearChat.click()

    def GetRecentMessages(self):
        #Finding the user span with this name
        userSpan = self.driver.find_element_by_xpath('//span[@title = "{}"]'.format(self.name))
        userSpan.click()

        #Getting teh Mesages available in the present UI
        msgs = self.driver.find_elements_by_class_name('Tkt2p')
        messageList = []
        for msg in msgs:
            messageList.append(msg.get_attribute('textContent')) 
        # the returned text contains the user name of sended if not u
        # the time when the message was sent 
        # the text of the message 
        return messageList