import os

# Указываем папку в которой производить поиск
path='C:/'

for rootdir, dirs, files in os.walk(path):
    for file in files:       
        if((file.split('.')[-1])=='mp3'):
            print (os.path.join(rootdir, file))