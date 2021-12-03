'''
This file contains functions to get additional news articles from the newsapi
'''
import requests
import pandas as pd
from bs4 import BeautifulSoup

url= 'https://newsapi.org/v2/everything?' # API to get news
api_key = "c31d9f572e5d47eeaae9d16463d0c921" #API key

def get_articles(file): 
    article_results = [] 
    for i in range(len(file)):
        article_dict = {}
        article_dict['description'] = file[i]['description']
        article_dict['url'] = file[i]["url"]
        article_results.append(article_dict)
    return article_results



def make_text_files(newsource: str, topic: str):
    '''
    Makes the api call from newsapi.com, scrapes the data from the url given and dumps the text into .txt files
    Input: newsource (str), topic(str)
         newsource: {"cnn.com","foxnews.com"}
         topic: {"covid", "biden", "none"}
    If topic is none, this function would search 100 newsarticles from selected newsource starting from 
    10/1/2021
    '''

    assert isinstance(newsource,str)
    assert isinstance(topic,str)

    parameters_headlines = {
    'q': topic,
    'sortBy':'popularity',
    'pageSize': 100,
    'apiKey': api_key,
    'language': 'en',
    'domains' : format(newsource)  
    }

    #making the API call 
    response_headline = requests.get(url, params = parameters_headlines)
    response_json_headline = response_headline.json()
    responses = response_json_headline["articles"]
    news_articles_df = pd.DataFrame(get_articles(responses))
    urls = news_articles_df["url"]

    
    if(newsource == "cnn.com"):
        print("Getting CNN news articles!")
        #cnn non-video websites end with .html
        #all text are inside zn-body__paragraph
        html_count = 0 # html file count
        for u in urls:
            if(u[-4:] == "html"):
                html_count += 1
                html = requests.get(u)
                soup = BeautifulSoup(html.text, "html.parser")
                paragraphs = soup.find_all(class_='zn-body__paragraph') 
                file_name = f"data/cnn_{topic}.txt"
                with open(file_name, 'a') as f:
                    for p in paragraphs:
                        f.write(p.get_text()+ "\n")
        print(f"Total CNN articles scraped:{html_count}")
    if(newsource == "foxnews.com"):
        print("Getting foxnews article!")
        #all text are inside <p>. This is different from cnn
        webcount = 0
        for u in urls:
            webcount+=1
            html = requests.get(u)
            soup = BeautifulSoup(html.text, "html.parser")
            paragraphs = soup.find_all('p') 
            p_len = len(paragraphs)
            file_name = f"data/foxnews_{topic}.txt"
            with open(file_name, 'a') as f:
                    cur_paragraph = 0
                    for p in paragraphs:
                        if(0< cur_paragraph < p_len - 2):
                            '''
                            Fox always start paragraph with This material may not be ...
                            It is not informative so we remove it
                            The last paragraphs are also useless
                            '''
                            text = p.get_text()
                            if(not ("click here" in text.lower())):
                                f.write(text + "\n")
                        cur_paragraph +=1
    
        print(f"Total Fox articles scraped: {webcount}")

def main():
    ###### IMPORTANT: DON'T run more than one time!
    make_text_files("cnn.com","covid")
    make_text_files("foxnews.com","covid")
if __name__ == "__main__":
    main()
