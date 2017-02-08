import glob, os, json

os.chdir('../uploads')

with open('../data/all-images.json', 'w') as outfile:
    
    images_json = []
    
    for file in glob.glob('*.png'):
        images_json.append(file)
    
    json.dump(images_json, outfile)
    