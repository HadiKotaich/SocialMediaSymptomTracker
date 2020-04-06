import os 
import subprocess as sub
import csv

# initialize as appropriate
CsvDir 
VNDir 

cmd=['ls', CsvDir]
proc=sub.Popen(cmd, stdout=sub.PIPE)
o, e= proc.communicate()
out=o.decode()
fileList=out.strip().split("\n")

for i in range (0, len(fileList)):
    if len(fileList[i])<10 or fileList[i][0:10]!="WASymTrack":
        continue
    f=open(CsvDir+fileList[i], "r")
    csv_reader=csv.reader(f, delimiter=',')
    updatedCSV=[]
    for row in csv_reader:
        if row[3]=="T" and len(row)<11:
            voiceName=row[0]+"_"+row[1]
            if len(row[6])!=0:
                voiceName+="."+row[6]           
            cmd=['ls', VNDir]
            proc=sub.Popen(cmd, stdout=sub.PIPE)
            o, e= proc.communicate()
            out=o.decode()
            VNList=out.strip().split("\n")
            if not(voiceName in VNList):
                os.system("wget -v  -O "+ VNDir+voiceName + " " + row[5])
            row.append(VNDir+voiceName)
        updatedCSV.append("\""+"\",\"".join(row)+"\"")
        
    f.close()
    f1=open(CsvDir+"vns_"+fileList[i], "w")
    contents = "\n".join(updatedCSV)
    f1.write(contents)
    f1.close()
        
