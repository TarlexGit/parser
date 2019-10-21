from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from collections import Counter

html = urlopen('https://docs.python.org/3/library/multiprocessing.html')
soup = BeautifulSoup(html, 'html.parser')

def getText(html):
    
    fout = open('scraper', 'wt')

    for tag in soup.find_all(re.compile("^p")):
        text = tag.text
        print(text, file=fout)
    fout.close()

def search():
    input_filename = 'scraper'
    result_filename = 'result'
    inputfile = open(input_filename, mode='r')
    resaultfile = open(result_filename, mode='w')

    lookfor = r"[\w]+"
    mytext = inputfile.read()
    results = re.findall(lookfor, mytext)

    word_list = []
    for word in results:
        clear_word = ''
        for letter in word:
            if letter.isalpha():
                clear_word += letter.lower()
        word_list.append(clear_word)

    def display_inventory(inventory):
        for k, v in inventory.items():
            if v > 20 and len(k) > 3 :
                print(str(v) + ' ' + k)
            else: pass



    lis = Counter(word_list)

    print(lis, file=resaultfile)
    display_inventory(lis)

search()
