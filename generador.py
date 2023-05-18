import timeit
import asyncio
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import aiohttp
import sys
from contextlib import closing
from urllib3 import HTTPConnectionPool
from urllib.error import URLError
from asincrono import download

import urllib.request
from functools import partial

def get_images_src_from_html(html_doc):
    soup= BeautifulSoup(html_doc, "html.parser")
    return [img.get("src") for img in soup.find_all("img")]

def get_uri_from_images_src(base_uri, images_src):
    parsed_base = urlparse(base_uri)
    for src in images_src:
        parsed= urlparse(base_uri)
        if parsed.netloc=="":
            path = parsed.path
            if parsed.query:
                path += "?" + parsed.query
            if path[0] != "/":
                if parsed_base.path == "/" :
                    path = "/" + path
                else:
                    path = "/" + "/".join(parsed_base.path.split("/")[:-1]) + "/" + path
            
            yield parsed_base.scheme + "://" + parsed_base.netloc + path
        
        else:
            yield parsed.geturl()

def wget(uri):
    try:
        response = urllib.request.urlopen(uri)
        if response.status == 200:
            print(response.reason, file=sys.stderr)
            return 
        print("Ok")
        return response.read()
    except URLError as e:
        print("Error", e)

def get_image(page_uri):
    html= wget(page_uri)
    if not html:
        print("Error no se ha encontrado ninguna imagen", sys.stderr)
        return None
    images_src = get_images_src_from_html(html)
    images_uri =get_uri_from_images_src(page_uri, images_src)
    for img_uri1 in images_uri:
        print("Descarga de €s" % img_uri1)
        wget(img_uri1)

if __name__ == "__main__":
    print("---Descarga de imagenes---")
    web_page_uri= "http://www.formationpython.com/"
    print(timeit.timeit("get_image(web_page_uri)", number=10, setup="from __main__ import get_image, web_page_uri"))