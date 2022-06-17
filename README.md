# RepSearcher

### There are two separate python files

## First code
["Search by extension"](https://github.com/denshynk/RepSearcher/blob/master/Search_by_extension.py) is a script that iterates through all the folders on the computer while looking for git repositories.
It determines that the folder is a git repository 
through the `.git` folder nested in it. Then he moves it to the folder he created or already existing on the desktop `Repositories`. 

## Second code
["Search by parsing git"](https://github.com/denshynk/RepSearcher/blob/master/Search_by_extension.py)
 this code was written to sort repositories by github group. In the example, I used the link to the repositories ["HowProgrammingWorks"](https://github.com/orgs/HowProgrammingWorks/repositories). We got the names of all the repositories and added them to the list. Next, the code does a disk search looking for a folder from the list
 ```python
result = new_dir in LIST
    if result is True:
```
 and  then checks this one for the presence of the ".git" folder
  ```python
 for dir in dirs:
            if '$Recycle.Bin' not in path:
                if '.git' == dir:
                    return move(path)
```

### Next comes the common part for the first and second code - moving the repository

We move the found folder to the created folder with the name of the group. But if such a folder has already been moved, we will not be able to place another one of the same, otherwise the folder will be 
moved with replacement. For this I wrote the code
```python
while True:
        if os.path.isdir(os.path.join(path_to_move, file_name)):
            if f'({count - 1})' in file_name:
                    file_name = file_name.replace(f'({count - 1})', '')     
            file_name = file_name + f'({count})'
            count += 1
        else:
            break
```
it looks for the presence of a folder with the same name, and if it finds it, it will add "(number(1++))" to the name of the folder being moved.
## .TXT
Also in our folder where we move the repositories, two .txt files are created. 

### The first "The path where the Repositories was located.txt"  
-  a file in which the path where the moved file was located is written.

## The second is "errors.txt" 
- code execution error. In particular, I had only one error displayed, this is the error of moving the "running code".
