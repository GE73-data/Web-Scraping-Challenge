import datetime as dt


def scrape_all():

    news_title = 'Testing Title'
    news_paragraph = 'Testing Paragraph'
    featured_image = 'https://i.ytimg.com/vi/MPV2METPeJU/maxresdefault.jpg'
    mars_facts = 'Testing Facts'
    hemispheres_list_of_dicts = [
        {"title": "Title of Hemisphere Image",
         "img_url": 'https://i.ytimg.com/vi/MPV2METPeJU/maxresdefault.jpg'},

        {"title": "Title of Hemisphere Image",
         "img_url": 'https://i.ytimg.com/vi/MPV2METPeJU/maxresdefault.jpg'},

        {"title": "Title of Hemisphere Image",
         "img_url": 'https://i.ytimg.com/vi/MPV2METPeJU/maxresdefault.jpg'},

        {"title": "Title of Hemisphere Image",
         "img_url": 'https://i.ytimg.com/vi/MPV2METPeJU/maxresdefault.jpg'},
    ]

    scraped_data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image,
        "facts": mars_facts,
        "hemispheres": hemispheres_list_of_dicts,
        "last_modified": dt.datetime.now()
    }

    return scraped_data
