# SocialMediaSymptomTracker
During the Covid19 epidemic, data is essential for any decision to be made and thus the importance of data collection. One can build a simple app for to collect data but in Lebanon and in these curcumstances you have to be a bit more creative in order to include the largest portion of people you can.

some facts about the situation:
- the elderly are the most vulnerable during this epidemic and most of them only use whatsapp and mostly send arabic voice messages
- many people in Lebanon don't have access to an internet connection, and some of them only have a special bundles for Whatsapp

Thus we decided to create a proof of conecpt of a Whatsapp Symptom Tracker.
persons who would like to share some health data about themselves can send an arabic voice or text message to a phone number. The Symptom tracker will take the received message, analyse its content and save the data in a database. Once the data is collected, one can study the evolution of symptoms in the country and more appropriate decisions.

#  Overview 
1) a person sends a text or a voice message to us (a predefined phone number)
2) a whatsapp business API provider will send us a post request containing the message
3) each 30 minutes we go and retrieve the received messages from a predefined directory
4) for each message, if it is text, we send it directly to the Information Extractor
5) if it is a voice message we go and send it to be transcribed first and then send it to the Information Extractor
6) the information extractor identifies symptoms in the message text and save them in the database
7) now the data is stored in the database and ready for some analytics

# More details

This repository is a fast prototype for a social media messaging based symptom tracker as a response for the spread of COVID-19. 
It should be useful in countries where a significant majority of data packages and internet penetration is limited to social media messaging. 

The main idea is to facilitate for users to send their symptoms through text or voice notes to the tracker. 
The prototype assumes use of WhatsApp is prevalant and a number of WhatsApp accounts are dedicated to collect the messages. 

The users send their messages to the designated WhatsApp contacts. 

The WASymTrack has a server (var/www/python) that implements the WhatsApp business API to collect the text messages and the urls of the voice notes. 
It also has a pull client that pulls the collected data into a local machine, and runds speech to text engine(s) over the collected voice notes. 
It also has a test directory to test tha APIs and the scripts. 

The Watcher is a file system based server that watches a directory for changes and processes the comma separated value files that the WASymTrack servers add to the directory. 
It sends these files to the extractor. 
The extractor aggregates the messages, applies NLP technqiues to extract the symptoms and inserts the results into a central DB for analytics. 

The prototype supports the Arabic language and makes use of third party alternative Arabic speech recognition systems (one is paid and one is kaldi based and open source).

# Notes  
The system was built after consultation with the Ministry of Public Health in Lebanon and several medical doctors at the American University of Beirut Medical center who thought the system is very beneficial and can guide the management of medical resources especially whem massive testing is not possible. 
