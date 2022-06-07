import os, shutil

PATH_FOR_COPY = input('folder')

def search():
    
    for adress, dirs, files in os.walk(input('Введите путь старта\n')):
        if adress == PATH_FOR_COPY:
            continue
        for dir in dirs:
            if len(dir) is not None:
                yield os.path.join(adress, dir)
   
    
def search2(path):
    for adress, dirs, files in os.walk(path):
        for dir in dirs:
            if dir.endswith('.git') and '$Recycle.Bin' not in path:
                move(path)


def move(path):
    print('Перемещение папки')
    file_name = path.split("\\")[-1]
    count = 1 
    while True:
        if os.path.isfile(os.path.join(PATH_FOR_COPY, file_name)):
                file_name = f'(count).'.join(file_name.split('.'))
                count += 1
        else:
            break
    
    get_files = os.listdir(path)
    shutil.move(path, PATH_FOR_COPY)
    print('Папка перемещена', file_name)


for i in search():
    try:
        search2(i)
    except Exception as e:
        with open(os.path.join(PATH_FOR_COPY, 'errors.txt'), 'a') as r:
            r.write(str(e) + '\n' + i + '\n')