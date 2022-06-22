#import pandas as pd
#from lxml import etree as et
import xml.etree.ElementTree as ET
data = ET.parse("mods.xml")

myTags = [item.tag for item in data.iter()]
#print(myTags)
myText = [item.text for item in data.iter()]
#print(myText)



#something is off in our final dict. find out
#we need a more unique tag. some tags like title are getting overwritten
z = zip(myTags, myText)
for a in z:
    print(a)
myDict = dict(z)
#for key in myDict:
#print(key)
#print(myDict[key])

for key in myDict:
    if len(myDict[key]) == 0:
        print(key)
    else:
        print(key, myDict[key])




#print(data.findall("./mods/titleInfo/title"))
#print(data.findall("./[@authority='marcrelator']"))

#root.findall()

#data2 = et.parse("mods.xml")
#print(data2.xpath("//text()"))
#print(data2.xpath("/mods/titleInfo/title/text()"))
#print(data2.xpath("//mods/titleInfo/title/text()"))

#x = data.findall(".//")
#x = data.findall(".//")
#print(data[0][0].tag)
#print(data[0][0].text)
#xpath_dict = {}

# # what is this doing?
# for item in data.iter():

#     print(item.text.strip(), end = ' ')
#     print(item.tag, end = ' ')
#     print(len(item.text))



# Solution for getting data out of all nodes #
# myText = [item.text for item in data.iter()]
# print(myText)

# 
# 
#  print(data[1][0][0].text)

#instead of doin something like this (below) we need a method that gets this data for us. 
# for x in data:
#     print(len(x))
#     print(x)
#     #data[0]
#     if len(x) == 1:
#         #data[0][0]
#         print(data[0][0].text)
#         print(x[0].text)
#         print(x[0][1])
#     if len(x) == 2:
#         #data[0][0]
#         print(data[2])
#         print(x[0][0].text)
#         print(x[0][1].text)
        

#for x in data:
#    print(x.get())


# for y in x:
#     print(y)

#xPaths = pd.read_csv("Metadata_Mapping.csv")

# for xPath in xPaths["xpath for MODS"]:
#     if pd.isna(xPath):
#         continue
#     else:
#         print(xPath)
#for x in data.iter():
#    print(type(x))

# dataiter = data.iter()
# for x in dataiter:
#     print(x)

#print("========================")


#print(x)
#for i in x:
    #print(i.text)

#for x in data.findall(".//titleInfo/title"):
#    print(x)

