from lxml import etree
import xml.etree.ElementTree as ET
import pandas as pd

lxml_tree = etree.parse("audio/ull-acc%3A430/mods.xml")

data = ET.parse("audio/ull-acc%3A430/mods.xml")
myTags = [item.tag for item in data.iter()]
myText = [item.text for item in data.iter()]
myAtt = [item.attrib for item in data.iter()]

print(myAtt)

######Export texts from XML file
clean_values  = []
for text in myText:
    if not "\n" in text:
        clean_values.append(text)
# print(clean_values)

unclean_list = []      ## Junk!
clean_list = []        ##  A list containing the Tags and values, in the lines we have text!
namespace = "{http://www.loc.gov/mods/v3}"
for val in clean_values:
    for item in data.iter():
            if item.text == val:
                clean_list.append([item.tag[len(namespace):], val])
            else:
                unclean_list.append(item.tag[len(namespace):])

list_of_iter_ancestor = []
for tag in lxml_tree.iter():
    for pair in clean_list:
        if pair[1] == tag.text:
            list_of_iter_ancestor.insert(0, tag.iterancestors())

ancestral_tags = []
ancestor = ""

# print(list_of_iter_ancestor)

for ancestors in list_of_iter_ancestor:
    for parent in ancestors:
        ancestor += "/" + parent.tag[len(namespace):]
        # print(ancestor)
    ancestral_tags.append(ancestor)
    ancestor = ""

newtags = []
rev_ancestor = reversed(ancestral_tags)
for elem in rev_ancestor:
    newtags.append(elem)

reversed_tags = []
for tag in newtags:
    splode = tag.split('/')
    join_list = splode[::-1]
    clean ="/".join(join_list)
    reversed_tags.append(clean)

# print(reversed_tags)
# print("============================================")
# print(clean_list)

children = []
for tag, pair in clean_list:
    children.append(tag)

final = []
entry = ''
i = 0
for tag in reversed_tags:
    final.append(tag + children[i])
    i += 1

# print(final)

big_list = []
i = 0
for pair in clean_list:
    big_list.append([final[i], pair[1]])
    i += 1
# print(big_list)

# REFACTOR! SEE IF WE CAN IMPROVE EFFICIENCY
df = pd.read_csv("audio/ull-acc%3A430/Metadata_Mapping.csv")
df.drop(['Type', 'Controlled?', 'Vocabulary', 'Cardinality', 'Notes', 'RDF mapping'], axis=1, inplace=True )
df.dropna(axis=0, how='any', inplace=True)
print(df)