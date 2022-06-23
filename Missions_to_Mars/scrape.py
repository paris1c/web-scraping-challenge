from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


def scrape():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    
    url = 'https://redplanetscience.com/'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup (html, 'html.parser')
    results = soup.find_all('div',  id='news', class_="container")
    
    mars_dic = {}
    news_title = []
    news_p = []
    
    for result in results:
        try:
            title = result.find('div', class_='content_title').text
            news_title.append(title)
            p = result.find('div', class_='article_teaser_body').text
            news_p.append(p)
        except AttributeError as e:
            print(e)

    mars_dic ['news_title'] = news_title [0]
    mars_dic['news_p'] = news_p [0]
      
    print(news_title)
    print(news_p)
    
    ## JPL Mars Space Images—Featured Image
    url = 'https://spaceimages-mars.com/'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    images = soup.find_all('img', class_="headerimage fade-in")
    for image in images:
        #get image source; src
        src=image['src']
    featured_image_url = 'https://spaceimages-mars.com/'+src
    print (' Here is the link to the fullsize feature image:\n', featured_image_url)
    
    mars_dic['featured_image_url'] = featured_image_url

    ## Mars Facts
    url = 'https://galaxyfacts-mars.com/'
    table = pd.read_html(url, match = 'Equatorial Diameter')
    table
    df = table[0]
    df
    html_table = df.to_html()
    
    mars_dic['facts'] = html_table

    ## Mars Hemispheres
    ### Cerberus Hemisphere Enhanced
    hemisphere_image_urls = []
    url = 'https://marshemispheres.com/cerberus.html'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    hems = soup.find_all('img', class_="wide-image")
    for hem in hems:
        cerberus_url = hem['src']
        print (cerberus_url)

    cerberus_title = soup.find('h2', class_='title').text
    print(cerberus_title)

    dic1 = {"title":cerberus_title, "image_url": cerberus_url}
    hemisphere_image_urls.append(dic1)

    url = 'https://marshemispheres.com/schiaparelli.html'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    hems = soup.find_all('img', class_="wide-image")
    for hem in hems:
        schiaparelli_url = hem['src']
        print (schiaparelli_url)

    schiaparelli_title = soup.find('h2', class_='title').text
    print(schiaparelli_title)

    dic2 = {"title":schiaparelli_title, "image_url": schiaparelli_url}
    hemisphere_image_urls.append(dic2)

    url = 'https://marshemispheres.com/syrtis.html'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    hems = soup.find_all('img', class_="wide-image")
    for hem in hems:
        syrtis_url = hem['src']
        print (syrtis_url)

    syrtis_title = soup.find('h2', class_='title').text
    print(syrtis_title)

    dic3 = {"title":syrtis_title, "image_url": syrtis_url}
    hemisphere_image_urls.append(dic3)

    url = 'https://marshemispheres.com/valles.html'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    hems = soup.find_all('img', class_="wide-image")
    for hem in hems:
        valles_url = hem['src']
        print (valles_url)

    valles_title = soup.find('h2', class_='title').text
    print(valles_title)

    dic4 = {"title":valles_title, "image_url": valles_url}
    hemisphere_image_urls.append(dic4)

    browser.quit()
    
    mars_dic['hemisphere_image_url'] = hemisphere_image_urls

    return mars_dic
    






