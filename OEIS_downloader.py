import requests 

file_url = 'https://oeis.org/stripped.gz'

r = requests.get(file_url)

with open('stripped.gz', 'wb') as f:
    f.write(r.content)



