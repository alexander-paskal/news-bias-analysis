# news-bias-analysis
## An analysis of bias in the News, particularly focused on CNN vs Fox reporting during the early Trump era. 

### introduction

Some people read only from certain news sources, but each news source has its own biases.
We hope to reveal such biases for notable news outlets such as CNN and Fox News.
Our goal is to make readers appreciate the biases in the different news articles and to be appropriately skeptical.

### Dependency and Installatioin

```
pip install requirements.txt 
```

### Running Analysis

biden_sentiment.ipynb: sentiment analysis for news related to biden in CNN news and Fox news.
covid_sentiment.ipynb: sentiment analysis for news related to covid in CNN news and Fox news.
nela_eda.ipynb: introduction of the Nela2017 dataset and visualization.
nela_features.ipynb: the readability anaysis for Nela2017.
nela_ngram.ipynb, nela_sentiment.ipynb: the sentiment analysis and its visualization for Nela2017.
wordclouds.ipynb: the visualization for the common words for each topic from each news provider.

### Project Organization


    ├── LICENSE
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── article.py     <- Data Structure for online scraped news.
    │   └── nela2017.py    <- Loading Nela2017 data and some preprocessing.
    │
    ├── scripts             
    │   └── _gather_news_data_.py  <- gather news from online with specific news provider and topic
    │
    │
    ├── notebooks          
    │   ├── ArticleEDA.ipynb
    │   ├── biden_sentiment.ipynb
    │   ├── covid_sentiment.ipynb
    │   ├── nela_eda.ipynb
    │   ├── nela_features.ipynb
    │   ├── nela_ngram_seaborn.ipynb
    │   ├── nela_ngram.ipynb
    │   ├── nela_sentiment.ipynb
    │   └── wordclouds.ipynb
    │
    │
    └── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
                             generated with `pip install requirements.txt`



--------

### Citation

Dataset:
```
https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/ZCXSKG
```

Sentimental analysis and readability analysis:
```
https://github.com/farooq96/News-Sentiment-Analysis-in-Python
```








