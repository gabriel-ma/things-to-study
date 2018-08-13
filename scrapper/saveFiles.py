from bs4 import BeautifulSoup
from urllib2 import urlopen
from urllib2 import Request
import urllib


# use this image scraper from the location that 
#you want to save scraped images to

def make_soup(url):
    req = Request(url, headers={'User-Agent' : "Magic Browser"}) 
    html = urlopen(req)
    return BeautifulSoup(html, 'html.parser')

def get_images(url, page):
    soup = make_soup(url)
    #this makes a list of bs4 element tags
    images = [img for img in soup.findAll('img', {'class', 'art-image'})]
    print (str(len(images)) + "images found.")
    print 'Downloading images to current working directory.'
    #compile our unicode list of image links
    image_links = [each.get('src') for each in images]
    
    for each in image_links:
        urllib.urlretrieve(each,  '%d.jpg' % (page))
        page = page + 1
    return page

#a standard call looks like this
page = 1
page = get_images('https://tapas.io/episode/1091785', page)
page = get_images('https://tapas.io/episode/1099734', page)
page = get_images('https://tapas.io/episode/1100708', page)
#get_images('https://tapas.io/episode/1075059', page)