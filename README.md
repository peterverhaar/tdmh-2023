# tdmh-2023


Indidual notebooks from the 'Notebooks' folder can be downloaded usng the code below.

```
import requests
from os.path import basename

urls = ['https://raw.githubusercontent.com/peterverhaar/tdm_tutorial/master/Solutions/7 Sentiment_analysis.ipynb',
'https://raw.githubusercontent.com/peterverhaar/tdm_tutorial/master/10 Named_Entity_Recognition.ipynb',
'https://raw.githubusercontent.com/peterverhaar/tdm_tutorial/master/9 Diction.ipynb' ]

for url in urls:
    response = requests.get(url)
    if response:

        file_name = basename(url)
        notebook = response.text
        with open(file_name,'w',encoding='utf-8') as out:
            out.write(notebook)
```
