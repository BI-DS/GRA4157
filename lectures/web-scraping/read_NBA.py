from bs4 import BeautifulSoup as soup
import requests as req
import re
from IPython import embed
import pandas as pd

URL = 'https://en.wikipedia.org/wiki/2021%E2%80%9322_NBA_season'



page = req.get(URL)
src = page.content
document = soup(src, 'lxml')

embed()

