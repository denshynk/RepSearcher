import requests
from bs4 import BeautifulSoup as BS
import os, shutil
import string

firsturl = "https://github.com/orgs/HowProgrammingWorks/repositories" + "?page="
LIST = []


def create_folder():
    
    r = requests.get(firsturl)
    soup = BS(r.content, 'html.parser')
    global new_folder
    new_folder = soup.find('img', class_="avatar float-left")
    new_folder = new_folder.text
    new_folder = new_folder.strip()
    global path_to_move
    path_random = os.path.expanduser('~') + '/Desktop/'
    path_to_move = (os.path.expanduser('~') +'/Desktop/' + str(new_folder)) 
    if os.path.isdir(os.path.join(path_random, new_folder)):
        path_to_move = os.path.join(path_random, new_folder)
        print("The folder " + new_folder + "was found on the desktop, the repositories will be moved to it")
    else:
        os.mkdir(os.path.join(path_random, new_folder))
        print("The folder " + new_folder + "was create on the desktop, the repositories will be moved to it")
    

def search():
    
    for j in range(len(DISK)):
        for adress, dirs, files in os.walk(DISK[j]):
            for dir in dirs:
                new_dir  = dir
                for y in range(20):
                    if f'({y})' in dir:
                        new_dir = dir.replace(f'({y})', '')   
                        break
                if f'{new_folder}' not in adress:
                    result = new_dir in LIST
                    if result is True:
                        for i in range(len(LIST)):
                            if new_dir == LIST[i]:
                                yield os.path.join(adress, dir)
                                break
        j += 1
              
                    
def search_for_git(path):
    
    for adress, dirs, files in os.walk(path):
        for dir in dirs:
            if '$Recycle.Bin' not in path:
                if '.git' == dir:
                    return move(path)
            
               
def move(path):
    
    file_name = os.path.split(path)[-1]
    print('Moving a', file_name)
    for y in range(100):
                    if f'({y})' in file_name:
                        file_name = file_name.replace(f'({y})', '')   
                        break
    count = 1 
    while True:
        if os.path.isdir(os.path.join(path_to_move, file_name)):
            if f'({count - 1})' in file_name:
                    file_name = file_name.replace(f'({count - 1})', '')     
            file_name = file_name + f'({count})'
            count += 1
        else:
            break
    
    shutil.move(path, os.path.join(path_to_move, file_name))
    print ('The repository was on this path', path)
    open(os.path.join(path_to_move, 'The path where the Repositories was located.txt'), 'a').write(str(path) + '\n')
      

def parsing (): 
    
    page = 1 
    while True:
    
        url = str(firsturl) + str(page)
        r = requests.get(url)
        soup = BS(r.content, 'html.parser')
        rep_name = soup.find_all('h3', class_="wb-break-all")
        if(len(rep_name)):
            for rep_names in rep_name:
                rep_names = rep_names.find("a", {'class':'d-inline-block'})
                if rep_names is not None:
                    rep_names = rep_names.text
                    rep_names = rep_names.strip()
                    LIST.append(rep_names)
                                                
            page += 1
        else:
            break
        

def get_disklist():
    global DISK
    DISK = []
    for c in string.ascii_uppercase:
        disk = c+':/'
        if os.path.isdir(disk):
            DISK.append(disk)

create_folder()    
parsing ()
get_disklist()
for i in search():
    try:
        search_for_git(i)
    except Exception as e:
        with open(os.path.join(path_to_move, 'errors.txt'), 'a') as r:
            r.write(str(e) + '\n' + i + '\n')
print('The search is over')
