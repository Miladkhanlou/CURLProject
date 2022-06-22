import os
import shutil
# change these to files for large images
file_out_names =  ["rels-ext.rdf", "techmd.xml", "obj.mpeg", "mods.xml" ]
datastreams = ["RELS-EXT", "TECHMD", "OBJ", "MODS"]

#change these too
pids = ["ull-acc%3A430", "ull-acc%3A431", "ull-acc%3A432", "ull-acc%3A433"]

#add a format the string with the path to a pid folder
curl_string = "curl -o {2}/{0} https://louisianadigitallibrary.org/islandora/object/{2}/datastream/{1}/download"



for z in pids:
    if os.path.exists(z):
        shutil.rmtree(z)
    os.mkdir(z)
    for (x, y) in zip(file_out_names, datastreams):
        os.system(curl_string.format(x, y, z))
        #print(curl_string.format(x, y, z))



