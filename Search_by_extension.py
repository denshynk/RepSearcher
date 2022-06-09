import os, shutil

def create_folder():
    
    new_folder = 'Repositories'
    path_random = 'C://Users/densh/Desktop/'
    global path_to_move
    path_to_move = ('C://Users/densh/Desktop/' + str(new_folder)) 
    if os.path.isdir(os.path.join(path_random, new_folder)):
        path_to_move = os.path.join(path_random, new_folder)
    else:
        os.mkdir(os.path.join(path_random, new_folder))

def search():
    
    DISK = ['C:/Users\densh\Desktop'] #, 'E:/', 'D:/'
    for j in range(len(DISK)):
        for adress, dirs, files in os.walk(DISK[j]):
            if adress == path_to_move:
                continue
            for dir in dirs: 
                if '$' not in adress: 
                    if dir.endswith('.git') and '.idx' not in adress:  
                        yield adress
        #j += 1
            
                    
#def search_for_git(path):
    
#   for adress, dirs, files in os.walk(path):
#        for dir in dirs:
#            if dir.endswith('.git') and '$Recycle.Bin' not in path:
#                return move(path)


def move(path):
    
    print('Перемещение папки', path)
    file_name = os.path.split(path)[-1]
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
    
create_folder()    
for i in search():
    try:
        move(i)
    except Exception as e:
        with open(os.path.join(path_to_move, 'errors.txt'), 'a') as r:
            r.write(str(e) + '\n' + i + '\n')