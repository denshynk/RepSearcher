import requests
from bs4 import BeautifulSoup as BS
import os, shutil

begin = input('Введите путь старта')
firsturl = "https://github.com/orgs/HowProgrammingWorks/repositories?page="


r = requests.get(firsturl)
soup = BS(r.content, 'html.parser')
new_folder = soup.find('img', class_="avatar float-left")
new_folder = new_folder.text
new_folder = new_folder.strip()
path_to_move = ('C://Users/densh/Desktop/' + str(new_folder))
os.mkdir(path_to_move)
print('Папка созданна')
problem = ".git"

page = 1

    
def search():
    
    print('Поиск папки', rep_names,)
    for adress, dirs, files in os.walk(begin):
        if adress == path_to_move:
            continue
        for dir in dirs:
            if dir == rep_names:
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
        if os.path.isfile(os.path.join(path_to_move, file_name)):
                file_name = f'(count).'.join(file_name.split('.'))
                count += 1
        else:
            break
    
    get_files = os.listdir(path)
    shutil.move(path, path_to_move)
    print('Папка перемещена', file_name)
    os.remove(path)
 
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
            for i in search():
                try:
                    search2(i)
                except Exception as e:
                    with open(os.path.join(path_to_move, 'errors.txt'), 'a') as r:
                        r.write(str(e) + '\n' + i + '\n')
                                        
        page += 1
    else:
        break