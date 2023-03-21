# tdmh-2023


Indidual notebooks from the 'Notebooks' folder can be downloaded usng the code below.

```
import requests
from os.path import basename

url = 'https://raw.githubusercontent.com/peterverhaar/tdmh-2023/main/Notebooks/ResearchProject.ipynb'

response = requests.get(url)
if response:
    file_name = basename(url)
    notebook = response.text
    with open(file_name+'2','w',encoding='utf-8') as out:
        out.write(notebook)
```
