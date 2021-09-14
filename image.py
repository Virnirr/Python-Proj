from PIL import Image
import sys 
import os
 
# grab the first and second argument 
path = sys.argv[1]
directory = sys.argv[2]

# check if directory new/ exists, if not create it
if not os.path.exists(directory):
    os.makedirs(directory)

# loop through images in a directory/path
for filename in os.listdir(path):
    img = Image.open(f'{path}{filename}')
    clean_name = os.path.splitext(filename)[0]
    # convert images to png
    img.save(f'{directory}{clean_name}.png', 'png')
# save to the new folder.
    print('all done!')

