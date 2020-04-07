#!/usr/bin/env pythong
# -*- coding: utf-8 -*-

from cgi import parse_qs, escape
import json
import datetime
import codecs
import re
import MySQLdb as conn
#import fcntl #for race conditions 

PYTHONIOENCODING="UTF-8"

WASTMsgStorePath="/WASymTrMsgs/last/"
time1 = 0
time2 = 30

def connectDB():
    	#db = conn.connect(user="root", passwd="rayan123", database="AnnoDB", charset="utf8")
	db = conn.connect(user="user", passwd="passwd", database="WASymTracker", charset="utf8")
	cursor = db.cursor()
	return db, cursor



def getValue_hier_keys(d, keys, default=None):
    current = d
    for k in keys:
        if k in current:
           current = current[k]
        else:
           return default
    return current


class WASTMsg:
   def __init__(self, d):
      self.sender=getValue_hier_keys(d,['from','number'])
      self.time=getValue_hier_keys(d,['timeUtc'])
      self.text=getValue_hier_keys(d,['message','text'])

      self.contentType = getValue_hier_keys(d,['message','media','contentType'])
      if self.contentType != None and 'audio' in self.contentType: 
         self.isVoice = True 
         match = re.search('audio.(.+);.*',self.contentType)
         if match : 
           self.extension = match.group(1)
      else :
         self.isVoice = False
         self.extension = None

      self.VNUrl = getValue_hier_keys(d,['message','media','mediaUri'])
      if (self.VNUrl != None) :
        self.isVoice = True

      self.isLocation = False
      self.latitude = None
      self.longitude = None
      custom = getValue_hier_keys(d,['message','custom'])
      if custom != None and 'location' in custom :
          self.isLocation = True
          self.latitude = getValue_hier_keys(d,['message','custom','location','latitude'])
          self.longitude = getValue_hier_keys(d,['message','custom','location','longitude'])

   def csvHeader(self): 
     header = "Sender,Time,Text,IsVoice,IsLocation,VoiceURL,VoiceExtension,Latitude,Longitude" 
     return header 

   def csvAll(self): 
     csvres = ""
     if self.sender != None : 
        csvres += self.sender
     csvres += ','

     if self.time != None : 
        csvres += self.time
     csvres += ','

     if self.text != None : 
        csvres += '"' + self.text + '"' 
     csvres += ','

     if self.isVoice : 
       csvres += 'T'
     else : 
       csvres += 'F'
     csvres += ','

     if self.isLocation : 
       csvres += 'T'
     else : 
       csvres += 'F'
     csvres += ','

     if self.VNUrl != None : 
        csvres += '"' + self.VNUrl + '"' 
     csvres += ','

     if self.extension != None : 
        csvres += self.extension 
     csvres += ','

     if self.latitude != None : 
        csvres += '"' + str(self.latitude) + '"' 
     csvres += ','

     if self.longitude != None : 
        csvres += '"' + str(self.longitude) + '"' 
     csvres += ','
     return csvres

   def writeToFile(self, path):
      if self.sender == None or self.time == None :
          return 
      currentDT = datetime.datetime.now()
      time1 = str(currentDT.year) + '.'+ str(currentDT.month) + '.' + str(currentDT.day) + '.'  + str(currentDT.hour)
      if (currentDT.minute < 30) :
        time2 = time1 + '.30'
        time1 += '.00'
      else :
        time1 += '.30'
        one_hour = datetime.timedelta(hours=1)
        currentDT = currentDT +one_hour
        time2 = str(currentDT.year) + '.'+ str(currentDT.month) + '.' + str(currentDT.day) + '.'  + str(currentDT.hour) + '.00'

      #make sure to use time1 and time2 here
      filename = path+"WASymTrack_"+str(time1) + "_" + str(time2) + ".csv"
      f=codecs.open(filename, encoding='utf-8', mode='a+')
      f.write(self.csvAll())
      f.write("\n")
      f.close()
      filename = path+"Logs.txt"
      if (self.contentType != None) :
        f=codecs.open(filename, encoding='utf-8', mode='a+')
        f.write(self.contentType)
        f.write(", ")
        f.write(self.extension)
        f.write(", ")
        f.write(str(self.isVoice))
        f.write("\n")
        f.close()

   def writeToDB(self, db, cursor):
      db, cursor=connectDB()
      addMessage="INSERT INTO Messages "+\
         "(SENDER, SENT, TEXT, ISVOICE, ISLOCATION, VOICEURL, VOICEEXT, LONGITUDE, LATITUDE)"+\
         "(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
      cursor.execute(addMessage, \
         (self.sender, " ".join(self.time.split('T')), self.text, self.isVoice, self.isLocation, self.VNUrl, self.extension, self.longitude, self.latitude,))
      db.commit()

      


def application(environ, start_response):
   db, cursor=connectDB()
   try:
      request_body_size = int(environ.get('CONTENT_LENGTH', 0))
   except (ValueError):
      request_body_size = 0
   request_body = environ['wsgi.input'].read(request_body_size)
   dictionary=json.loads(request_body)
   status = '200 OK'
   rec = WASTMsg(dictionary)
   #    output = "<?xml version='1.0'?> <wastrack>" + rec.csvAll() + "</wastrack>"
   output = "<?xml version='1.0'?> <wastrack> none </wastrack>"
   rec.writeToFile(WASTMsgStorePath)
   rec.writeToDB(db,cursor)
   response_headers = [('Content-type', 'text/xml'),
                     ('Content-Length', str(len(output)))]
   start_response(status, response_headers)
   return [output]


if __name__ == '__main__':
   f=open("example.json")
   jsonObj=json.loads(f.read())
   rec = WASTMsg(jsonObj)
   rec.writeToFile(WASTMsgStorePath)
   #print (rec.xmlAll())
   x = getValue_hier_keys(jsonObj,['message','media','title'])
   print(str(x)) 
   x = getValue_hier_keys(jsonObj,['message','media','banana'])
   print(str(x)) 

