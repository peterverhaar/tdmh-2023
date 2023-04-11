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


