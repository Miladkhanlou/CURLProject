# python Curl project for using with LDL (islandora) datastreams.



*** todos: ***

- create a python curl for video
- convert get.sh for oral hisitory into python (like the others)
- create a pull-all.sh to run all the different curl.py files
- allow Xpath_For_metadata.py to run within each folder's subfolder. (against each mods file for all content types).
- and/or allow Xpath_For_metadata to run only one metadata file at a time.
- Xpath_For_metadata.py finish mapping tags, map to field, write out to csv


## how to run commands

```sh oral_history/get.sh```
- this runs hardcoded curl commands and writes output to file...

```python3 Xpath_For_metadata.py audio/<foldername>/mods.xml```
- runs a transformation on the mods file (doesn't point to the path yet...)

inline
> some inline lookin text 

this is a good way to execute the code
> cd audio
> python3 python-curl-audio.py
> cd ..

now you have some datastreams from the ldl
> ls audio 

You'll see some new folders

Now you can run Xpath_For_metadata.py
> python3 loop_mods_etree_to_clean_list.py

os_walk.py is a todo for the future
to recurse through all the subdirectories, and pull ldl items for each content type
