from collections import defaultdict
from tika import parser
from os import listdir
import unicodedata




def detect_collision(paper_name, vec, table):
    for items in vec:
        table[items][paper_name] = 0


if __name__ == '__main__':
   
    path = './pdfs/'
    table = defaultdict(lambda: {})

    for files in listdir(path):
        raw = parser.from_file(path+files)
        pdfstring = unicodedata.normalize('NFKD', raw['content']).encode('ascii', 'ignore')
        detect_collision(files,
            [int(s) for s in pdfstring.split() if s.isdigit() if int(s) > 100000],
            table)
    for keys in table:
        if len(table[keys]) > 1:
            print(keys, table[keys])

        
 
