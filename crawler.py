#!/usr/bin/python

"""This script extracts data and informations contained in web pages and saves them in .json files."""

from bs4 import BeautifulSoup
import getopt, requests, sys, os, re, json, glob

def urlredux(url):
    """Remove everything from an url after a '#' or a '?'."""
    inc = 0
    if url:
        for car in url:
            if car == '?' or car == '#':
                url = url[:inc]
            inc += 1
        return url

def extract(url_site):
    """Get the title, the description, the keywords and the links from a web page."""
    dicto = {} # Dictionnary with all keys associated with the URL
    liste_url = [] # List of URLs contained by the parsed URL
    data = (requests.get(url_site)).text
    soup = BeautifulSoup(data, "html.parser")
    for meta in soup.find_all('meta'):
        if meta.get('name') == 'description':
            dicto["description"] = meta.get('content')
        if meta.get('name') == 'keywords':
            dicto["keywords"] = meta.get('content')
    if soup.title:
        dicto["title"] = soup.title.text # Retrieving the title and putting it in the dictionnary
    for link in soup.find_all('a'): # Retrieving the links
        liste_url.append(urlredux(link.get('href')))
    dicto["links"] = liste_url # The URL list is put inside the dictionnary
    return dicto

def crawl(url, depth, directory, outside):
    """Crawl the web sites depending of the 'depth' parameter."""
    list_all = []
    list_wait = []
    list_exec = [url]
    index = 0
    while index < depth + 1:
        for url in list_exec:
            dicto_all = {}
            if url and url.startswith("http://") and outside:
                dicto = extract(url)
                list_wait = list_wait+dicto["links"]
                dicto_all[url] = dicto
                save(directory, dicto_all)
        list_exec = list_wait
        list_all = list_all+list_wait
        list_wait = []
        index += 1

def save(directory, datas):
    """Save the data in a .json file."""
    if not os.path.exists(directory):
        os.makedirs(directory)
    for key in datas:
        datas[key]["url"] = key
        file_name = [car for car in key if re.search("([A-Za-z0-9])", car)]
        file_out = open(directory+''.join(file_name)+'.json', 'w')
        json.dump(datas[key], file_out, indent=4)
        file_out.close()

def load(dir_):
    """Load a .json file et returns a dictionnary."""
    dictionnaire = {}
    read_files = glob.glob(dir_+'*.json')
    for fic in read_files:
        dictionnaire[fic] = json.loads(open(fic).read())
    return dictionnaire

def main():
    """Retrieve all arguments and starts the crawler."""
    opts = ["depth=", "outside=", "output="]
    try:
        args, opts = getopt.getopt(sys.argv[2:], "ho:v", opts)
    except getopt.GetoptError as error:
        print(error)
        sys.exit(2)

    # Default values
    go_outside = True
    depth = 2
    directory = "results/"

    # Retrieving all options and their respective values
    for option, val in args:
        if option == '--depth' and int(val) >= 0:
            depth = int(val)
        elif option == '--outside':
            go_outside = val
        elif option == '--output':
            directory = val
    url_site = sys.argv[1]
    crawl(url_site, depth, directory, go_outside)

if __name__ == "__main__":
    main()
