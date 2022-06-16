import os
import shutil

file_out_names =  ["rels-ext.rdf", "coll-pol.xml", "mods.xml" ]
datastreams = ["RELS-EXT", "COLLECTION_POLICY", "MODS"]
pids = ["lsu-thwcoh-betsy%3Acollection", "lsu-thwcoh-lsuhistory:collection"]

#add a format the string with the path to a pid folder
curl_string = "curl -o {2}/{0} https://louisianadigitallibrary.org/islandora/object/{2}/datastream/{1}/download"



for z in pids:
    if os.path.exists(z):
        shutil.rmtree(z)
    os.mkdir(z)
    for (x, y) in zip(file_out_names, datastreams):
        os.system(curl_string.format(x, y, z))
        #print(curl_string.format(x, y, z))



