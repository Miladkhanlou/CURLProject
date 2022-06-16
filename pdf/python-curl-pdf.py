import os
import shutil
# change these to files for large images
file_out_names =  ["rels-ext.rdf", "techmd.xml", "obj.pdf", "mods.xml" ]
datastreams = ["RELS-EXT", "TECHMD", "OBJ", "MODS"]

#change these too
pids = ["lsu-music-p16313coll69%3A2879", "lsu-music-p16313coll69%3A2878", "lsu-music-p16313coll69%3A2877"]

#add a format the string with the path to a pid folder
curl_string = "curl -o {2}/{0} https://louisianadigitallibrary.org/islandora/object/{2}/datastream/{1}/download"



for z in pids:
    if os.path.exists(z):
        shutil.rmtree(z)
    os.mkdir(z)
    for (x, y) in zip(file_out_names, datastreams):
        os.system(curl_string.format(x, y, z))
        #print(curl_string.format(x, y, z))



