from splinter import Browser
from bs4 import BeautifulSoup as bs
import time

import pandas as pd
import requests


def init_browser():
    executable_path = {'executable_path': 'chromedriver.exe'}

    return Browser("chrome", **executable_path, headless=False)


def scrape():

    browser = init_browser()


    #---------------------------------
    # Title and Paragraph
    #---------------------------------

    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    time.sleep(1)

    title_list = []
    paragraph_list = []

        
    # HTML object
    html = browser.html

    # Parse HTML with Beautiful Soup
    soup = bs(html, 'html.parser')
    
    #### find titles
    titles = soup.find_all('div', class_='content_title')
    
    for tl in titles:
        if (tl.a):
            if (tl.a.text):
                if tl not in title_list:
                    title_list.append(tl.text)
                
        
    ##### find titles
    paragraphs = soup.find_all('div', class_='article_teaser_body')
    
    for pl in paragraphs:
        if (pl):
            if (pl.text):
                if pl not in paragraph_list:
                    paragraph_list.append(pl.text)

    title_list_1 = title_list[0]
    print(title_list_1)

    paragraph_list_1 = paragraph_list[0]
    print(paragraph_list_1)

    #---------------------------------
    # Featured Image
    #---------------------------------

    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    url_main_img = 'https://www.jpl.nasa.gov'
    browser.visit(url)

    time.sleep(1)

    # HTML object
    html = browser.html

    # Parse HTML with Beautiful Soup
    soup = bs(html, 'html.parser')

    #### image link
    result = soup.find('article', class_= 'carousel_item')
    #print (result)

    img_url = result['style']
    print(img_url)

    img_url = img_url.replace('background-image: url(', '').replace(')', '').replace("'", "").replace(';', '')
    full_img_url = url_main_img+img_url
    print(full_img_url)

    full_img_url_dict = [{'full_img_url' : full_img_url}]
    full_img_url_dict


    #---------------------------------
    # Latest Tweet
    #---------------------------------

    url = 'https://twitter.com/marswxreport?lang=en'
    response = requests.get(url)

    time.sleep(1)


    # Parse HTML with Beautiful Soup
    soup = bs(response.text, 'html.parser')
    # print(soup.prettify())


    #### image link
    latest_tweet = soup.find_all('div' , class_ = 'js-tweet-text-container')
    #print (latest_tweet)

    Latest_Tweet_List = []

    for i in latest_tweet:
        if (i.p):
            if (i.p.text):
                if tl not in Latest_Tweet_List:
                    #if , string='high'
                    Latest_Tweet_List.append(i.p.text)

    Latest_Tweet_List
                
    Latest_Weather_Tweet = [k for k in Latest_Tweet_List if 'InSight sol' in k][0]
    Latest_Weather_Tweet


    #---------------------------------
    # Mars Facts table
    #---------------------------------

    url = 'https://space-facts.com/mars/'
    browser.visit(url)

    time.sleep(1)

    # HTML object
    html = browser.html

    # Parse HTML with Beautiful Soup
    soup = bs(html, 'html.parser')

    table_Col1 = []
    table_Col2 = []

    table = soup.find('table', class_='tablepress tablepress-id-p-mars')

    Col_1 = table.find_all('td', class_='column-1')
    Col_2 = table.find_all('td', class_='column-2')

    for i in Col_1:
        table_Col1.append(i.text)
        
    for j in Col_2:
        table_Col2.append(j.text)
        
    print(table_Col1)

    print(table_Col2)

    table_df = pd.DataFrame({'Description' : table_Col1, 'Value' : table_Col2})

    table_df = table_df.set_index('Description')

    table_df = table_df.to_html()

    table_df = table_df.replace('\n  ', '')

    table_df = table_df.replace('\n', '')

    table_df = table_df.replace("'", '')


    #---------------------------------
    # Mars Hemisphere
    #---------------------------------


    # Image #1
    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'
    browser.visit(url)

    time.sleep(1)

    # HTML object
    html = browser.html

    # Parse HTML with Beautiful Soup
    soup = bs(html, 'html.parser')    

    #### image link
    result_img = soup.find('img', class_='wide-image')
    print (result_img)

    img_url = result_img['src']
    url_img = 'https://astrogeology.usgs.gov'

    full_img_url_1 = url_img+img_url
    print(full_img_url_1)

    #### title
    title_1 = soup.find('h2', class_='title').text
    print (title_1)


    # Image #2
    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'
    browser.visit(url)

    time.sleep(1)

    # HTML object
    html = browser.html

    # Parse HTML with Beautiful Soup
    soup = bs(html, 'html.parser')

    #### image link
    result = soup.find('img', class_='wide-image')
    print (result)

    img_url = result['src']
    url_img = 'https://astrogeology.usgs.gov'

    full_img_url_2 = url_img+img_url
    print(full_img_url_2)

    #### title
    title_2 = soup.find('h2', class_='title').text
    print (title_2)


    # Image #3
    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'
    browser.visit(url)

    time.sleep(1)

    # HTML object
    html = browser.html

    # Parse HTML with Beautiful Soup
    soup = bs(html, 'html.parser')

    #### image link
    result = soup.find('img', class_='wide-image')
    print (result)

    img_url = result['src']
    url_img = 'https://astrogeology.usgs.gov'

    full_img_url_3 = url_img+img_url
    print(full_img_url_3)

    #### title
    title_3 = soup.find('h2', class_='title').text
    print (title_3)


    # Image #4
    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'
    browser.visit(url)

    time.sleep(1)

    # HTML object
    html = browser.html

    # Parse HTML with Beautiful Soup
    soup = bs(html, 'html.parser')

    #### image link
    result = soup.find('img', class_='wide-image')
    print (result)

    img_url = result['src']
    url_img = 'https://astrogeology.usgs.gov'


    full_img_url_4 = url_img+img_url
    print(full_img_url_4)

    #### title
    title_4 = soup.find('h2', class_='title').text
    print (title_4)


    #---------------------------------
    # Final dictionary
    #---------------------------------
    Final_Mars_Dict =  {'Titles_1'                    : title_list_1, 
                        'Paragraphs_1'                : paragraph_list_1, 
                        'Featured_img'                : full_img_url, 
                        'Latest_Mars_Weather_Tweet'   : Latest_Weather_Tweet, 

                        'table'                       : table_df,

                        'Table_table_Col1'            : table_Col1,
                        'Table_table_Col2'            : table_Col2,   

                        'Img_1'                       : full_img_url_1, 
                        'Img_1_title'                 : title_1, 
                        'Img_2'                       : full_img_url_2,
                        'Img_2_title'                 : title_2,
                        'Img_3'                       : full_img_url_3,
                        'Img_3_title'                 : title_3,
                        'Img_4'                       : full_img_url_4,
                        'Img_4_title'                 : title_4

                        }


    # Close the browser after scraping
    browser.quit()
    
    return Final_Mars_Dict

init_browser()















































































