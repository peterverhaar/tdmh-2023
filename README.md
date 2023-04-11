# tdmh-2023


Indidual notebooks can be downloaded usng the code below.

```
import requests
from os.path import basename

urls = [ 'https://raw.githubusercontent.com/peterverhaar/tdm_tutorial/master/Metadata.ipynb' , 
'https://raw.githubusercontent.com/peterverhaar/tdm_tutorial/master/Research Project.ipynb' , 
'https://raw.githubusercontent.com/peterverhaar/tdm_tutorial/master/9 Diction.ipynb' ]

for url in urls:
    response = requests.get(url)
    if response:

        file_name = basename(url)
        notebook = response.text
        with open(file_name,'w',encoding='utf-8') as out:
            out.write(notebook)
```


```
urls = [ 'import requests
from os.path import basename

urls = [ 'https://raw.githubusercontent.com/peterverhaar/tdmh-2023/main/Husz%C3%A1r/Corpus/The_Chamber_of_Secrets.txt' ,
'https://raw.githubusercontent.com/peterverhaar/tdmh-2023/main/Husz%C3%A1r/Corpus/The_Deathly_Hallows.txt',
'https://raw.githubusercontent.com/peterverhaar/tdmh-2023/main/Husz%C3%A1r/Corpus/The_Goblet_of_Fire.txt',
'https://raw.githubusercontent.com/peterverhaar/tdmh-2023/main/Husz%C3%A1r/Corpus/The_Half_Blood_Prince.txt',
'https://raw.githubusercontent.com/peterverhaar/tdmh-2023/main/Husz%C3%A1r/Corpus/The_Order_of_the_Phoenix.txt',
'https://raw.githubusercontent.com/peterverhaar/tdmh-2023/main/Husz%C3%A1r/Corpus/The_Philosophers_Stone.txt',
'https://raw.githubusercontent.com/peterverhaar/tdmh-2023/main/Husz%C3%A1r/Corpus/The_Prisoner_of_Azkaban.txt' ]

for url in urls:
    response = requests.get(url)
    if response:

        file_name = basename(url)
        notebook = response.text
        with open(file_name,'w',encoding='utf-8') as out:
            out.write(notebook)']
            
 ```
