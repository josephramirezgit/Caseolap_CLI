import json
import requests
import pandas as pd
from re import search

# Open json file
f = open('pmids.json')
pmids = json.load(f)

# Save base URL
URL = 'https://www.ncbi.nlm.nih.gov/pmc/utils/idconv/v1.0/?ids='

# 
d = {}
for pmid in pmids:
    url = URL + pmid
    request = requests.get(url)
    for i in request.text.split():
        if search("pmcid", request.text):
            if "pmcid=" in i:
                text = i[7:]
                text = text.split('.', 1)
                d[pmid] = text[0]
        else:
            d[pmid] = ""

df = pd.DataFrame.from_dict(d)

df.to_csv("pmid_to_pmc.csv")

