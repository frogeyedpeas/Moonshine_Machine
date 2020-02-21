import gzip 

with gzip.open('stripped.gz', 'rb') as f:
    with open('datadump', 'wb') as g:
        g.write(f.read())


