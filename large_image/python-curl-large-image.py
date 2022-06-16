import os
import shutil
# change these to files for large images
file_out_names =  ["rels-ext.rdf", "techmd.xml", "obj.jp2", "mods.xml" ]
datastreams = ["RELS-EXT", "TECHMD", "OBJ", "MODS"]

#change these too
pids = ["lsu-sea-p15140coll21%3A3", "lsu-sea-p15140coll21%3A4", "lsu-sea-p15140coll21%3A5"]

#add a format the string with the path to a pid folder
curl_string = "curl -o {2}/{0} https://louisianadigitallibrary.org/islandora/object/{2}/datastream/{1}/download"



for z in pids:
    if os.path.exists(z):
        shutil.rmtree(z)
    os.mkdir(z)
    for (x, y) in zip(file_out_names, datastreams):
        os.system(curl_string.format(x, y, z))
        #print(curl_string.format(x, y, z))



