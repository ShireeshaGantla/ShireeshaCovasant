import requests
from bs4 import BeautifulSoup
import asyncio
import aiohttp

file = "./demo2.html"

async def get_links(url):
    async with aiohttp.ClientSession() as sess:
        async with sess.get(url) as response:
            html_content = await response.text()
            soup = BeautifulSoup(html_content, 'html.parser')
            links = set()
            for link in soup.find_all('a', href = True):
                href = link['href']
                if href.startswith(('http://', 'https://')):
                    links.add(href)
            return list(links)
            
async def fetch_link(url):
    async with aiohttp.ClientSession() as sess:
        async with sess.get(url) as response:
            return await response.text()
        
async def write_content(filename, html_content):
    async with aiohttp.ClientSession() as sess:
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(html_content + '\n')
print(f"Successfully wrote html content to {file}")
    
async def process(link, filename):
    html_content = await fetch_link(link)
    if html_content :
        await write_content(filename, html_content)

async def main():
    target = "https://www.meesho.com"
    links = await get_links(target)
    single_url = [process(link, file) for link in links]
    await asyncio.gather(*single_url)

if __name__ == "__main__":
    asyncio.run(main())
