from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
from webdriver_manager.chrome import ChromeDriverManager


def scrape_mars_news():


   # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # Visit url
    mars_news_url = "https://redplanetscience.com/"
    browser.visit(mars_news_url)

    time.sleep (1)

# Scrape page into soup
    mars_news_html = browser.html
    news_soup = bs(mars_news_html, "html.parser")

# Get mars title
    news_title = news_soup.find('div', class_="content_title").text
   
# collect latest title and paragraph
    news_para = news_soup.find('div', class_="article_teaser_body").text
 
# Store data in a dictionary
    mars_data = {
    "news_title": news_title,
    "news_para": news_para
}

#Visit Image url
    featured_image_url = 'https://spaceimages-mars.com'
    browser.visit(featured_image_url)

#Browser
    featured_image_html = browser.html
    img_soup = bs(featured_image_html, 'html.parser')

#Get image
    relative_image_url_scraped_from_site = image.soup.find("a", class_="showing fancybox-thumbs")["href"]
    relative_image_url_scraped_from_site


# Close the browser after scraping
    browser.quit()

# Return results
    return mars_data
