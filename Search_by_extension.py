import os, shutil

def search():
    
    DISK = ['D:/', 'E:/', 'C:/']
    for j in range(len(DISK)):
        for adress, dirs, files in os.walk(DISK[j]):
            if adress == path_to_move:
                continue
            for dir in dirs:   
                result = dir in LIST
                if result is True:
                    for i in range(len(LIST)):
                        if dir == LIST[i]:
                            yield os.path.join(adress, dir)
                            break
        j += 1
                    
def search_for_git(path):
    for adress, dirs, files in os.walk(path):
        for dir in dirs:
            if dir.endswith('.git') and '$Recycle.Bin' not in path:
                return move(path)

def create_folder():
    
    r = requests.get(firsturl)
    soup = BS(r.content, 'html.parser')
    new_folder = soup.find('img', class_="avatar float-left")
    new_folder = new_folder.text
    new_folder = new_folder.strip()
    global path_to_move
    path_random = 'C://Users/densh/Desktop/'
    path_to_move = ('C://Users/densh/Desktop/' + str(new_folder)) 
    if os.path.isdir(os.path.join(path_random, new_folder)):
        path_to_move = os.path.join(path_random, new_folder)
    else:
        os.mkdir(os.path.join(path_random, new_folder))

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