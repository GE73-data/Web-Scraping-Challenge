from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


def scrape_mars_news():


   # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # Visit url
    mars_news_url = "https://redplanetscience.com/"
    browser.visit(mars_news_url)

    time.sleep (1)

    #   Scrape page into soup
    mars_news_html = browser.html
    news_soup = bs(mars_news_html, "html.parser")

    # Get mars title
    news_title = news_soup.find('div', class_="content_title").text
   
    # collect latest title and paragraph
    news_para = news_soup.find('div', class_="article_teaser_body").text
 
   

    #Visit Image url
    featured_image_url = 'https://spaceimages-mars.com/'
    browser.visit(featured_image_url)

    #Browser
    featured_image_html = browser.html
    img_soup = bs(featured_image_html, 'html.parser')

    #Get image
    relative_image_url_scraped_from_site = img_soup.find("a", class_="showimg fancybox-thumbs")["href"]
    featured_image_url = f'https://spaceimages-mars.com/{relative_image_url_scraped_from_site}'

    mars_df = pd.read_html('https://galaxyfacts-mars.com')[0]
    header = mars_df.iloc[0]
    mars_df = mars_df[1:]
    mars_df.rename(columns=header,inplace=True)

    mars_facts_html = mars_df.to_html()
    ##################
    #mars hemisphere
    mars_hemispheres_url = 'https://marshemispheres.com/'
    browser.visit(mars_hemispheres_url)

    mars_hemispheres_html = browser.html
    hemisphere_soup = bs(mars_hemispheres_html, 'html.parser')

    items = hemisphere_soup.find_all("div", class_="item")

    main_url = 'https://marshemispheres.com/'
    mars_hemisphere_urls =[]

    for item in items:
        mars_hemisphere_urls.append(f"{main_url}{item.find('a',class_='itemLink')['href']}")
    hemisphere_image_urls = []

    for url in mars_hemisphere_urls:
        # url=mars_hemisphere_urls[0]
        browser.visit(url)
        hemisphere_html=browser.html
        hemisphere_soup = bs(hemisphere_html, 'html.parser')
        relative_image_url=hemisphere_soup.find("img", class_="wide-image")["src"]
        image_url=main_url + relative_image_url
        # print(image_url)
        hemisphere_title=hemisphere_soup.find("h2", class_="title").text
        hemisphere_dict={
            "title": hemisphere_title,
            "image_url": image_url
        }
        hemisphere_image_urls.append(hemisphere_dict)
    # Close the browser after scraping
    browser.quit()

    # Store data in a dictionary
    mars_data = {
    "news_title": news_title,
    "news_para": news_para,
    "featured_image": featured_image_url,
    "mars_facts": mars_facts_html,
    "hemispheres": hemisphere_image_urls
    }

    # Return results
    return mars_data
