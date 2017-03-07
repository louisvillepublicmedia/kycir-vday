#!/usr/bin/python3

import glob, os, json

os.chdir('/var//www/html/vday/uploads/')

with open('/var//www/html/vday/data/all-images.json', 'w') as outfile:
    
    images_json = []
    
    for file in glob.glob('*.png'):
        single_image = {}
        single_image['imageID'] = file.rpartition('.')[0]
        single_image['imageURL'] = file
        
        images_json.append(single_image)
    
    #print(images_json)
    json.dump(images_json, outfile)
    