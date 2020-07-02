import requests
from bs4 import BeautifulSoup

def main():
    """
    Download word.txt from http://thinkpython2.com/code/words.txt
    """
    
    url = "http://thinkpython2.com/code/words.txt"
    r = requests.get(url)
    with open('word.txt', 'w') as f:
        for word in r.text.split():
            f.write(word+'\n')
        
if __name__ == "__main__":
    main()  