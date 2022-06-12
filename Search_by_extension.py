import os, shutil

def create_folder():
    
    global new_folder
    new_folder = 'Repositories'
    path_random = 'C:/Users/densh/Desktop/'
    global path_to_move
    path_to_move = ('C:/Users/densh/Desktop/' + str(new_folder)) 
    if os.path.isdir(os.path.join(path_random, new_folder)):
        os.path.join(path_random, new_folder)
        print("The folder " + new_folder + "was found on the desktop, the repositories will be moved to it")
    else:
        os.mkdir(os.path.join(path_random, new_folder))
        print("The folder " + new_folder + "was create on the desktop, the repositories will be moved to it")

def search():
    
    DISK = ['C:/', 'E:/', 'D:/']
    for j in range(len(DISK)):
        for adress, dirs, files in os.walk(DISK[j]):
            for dir in dirs:
                if f'{new_folder}' and '$' and '.git' not in adress:
                    if '.git' == dir:  
                        yield adress
        j += 1
            
                    
def move(path):
    
    file_name = os.path.split(path)[-1]
    print('Перемещение папки', file_name)
    count = 2 
    while True:
        if os.path.isdir(os.path.join(path_to_move, file_name)):
            if f'({count - 1})' in file_name:
                    file_name = file_name.replace(f'({count - 1})', '')     
            file_name = file_name + f'({count})'
            count += 1
        else:
            break
    
    shutil.move(path, os.path.join(path_to_move, file_name))
    print('Папка перемещенна')
   # print ('Путь где находился файл', path)

    
create_folder()    
for i in search():
    try:
        move(i)
    except Exception as e:
        with open(os.path.join(path_to_move, 'errors.txt'), 'a') as r:
            r.write(str(e) + '\n' + i + '\n')
print('The search is over')