import requests
from bs4 import BeautifulSoup
import concurrent.futures

file = "./demo1.html"

def get_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = set()
    for link in soup.find_all('a', href = True):
        href = link['href']
        if href.startswith(('http://', 'https://')):
            links.add(href)
    return list(links)

def write_content(url, filename):
    response = requests.get(url)
    html_code = response.text
    with open(filename, 'a' , encoding='utf-8') as f:  
        f.write(html_code)
print(f"Successfully wrote html content ")
       
    
def process(url, filename):
    links = get_links(url)
    if links :
        write_content(url, filename)
    return links

if __name__ == "__main__":
    target = "https://www.meesho.com/"
    
    multiple_link = get_links(target)
    
    if multiple_link :
        with concurrent.futures.ThreadPoolExecutor() as pool:
            futures = [pool.submit(process, link,file) for link in multiple_link]
            result = [future.result() for future in futures]
           # write_content(result, file)
