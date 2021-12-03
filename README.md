# News Bias Analysis
## An analysis of bias in the News, particularly focused on CNN vs Fox reporting during the early Trump era. 

### Introduction

Some people read only from certain news sources, but each news source has its own biases.
We hope to reveal such biases for notable news outlets such as CNN and Fox News.
Our goal is to make readers appreciate the biases in the different news articles and to be appropriately skeptical.

To this end, we perform a variety of analyses of news articles from two different periods. These analyses employ a variety of 
natural language techniques to extract valuable insights about the content, style, and intent of the text being analyzed.



### Dependencies and Installation


For this project, we used an anaconda environment (3.8). We would recommend to do the following. To create the environment locally,
run the following from the anaconda prompt:

	>>>  conda env create --name your-env --file=environments.yml

Alternatively, if you prefer to use pip, run the following from the command prompt:

	>>> pip install -r requirements.txt 



### Project Organization


    ├── LICENSE
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── article.py     <- Data Structure for online scraped news.
    │   └── nela2017.py    <- Loading Nela2017 data and some preprocessing.
    │   └── txt files      <- biden,covid articles extracted from Fox or CNN
    ├── utils              <- top folder containing basic text analysis/preprocessing and plotting
    │   ├── plotting       <- Contains a file with plotting functions
    │   └──  text          <- Contains files for preprocessing and analyzing text
    │   
    ├── gather_recent_news.py  <- gather news from online with specific news provider and topic   
    │
    ├── plots.ipynb <- Summary of our analysis
    │
    │__ environment.yml    <- The .yml file for creating the conda environment necessary to reproduce the results
    └── requirements.txt   <- The requirements file for installing with pip



### Data


We use the NELA2017 dataset, which accumulates thousands of news articles from nearly 100 different news organizations over a 7-month
period in 2017. Citations and links to the dataset and accompanying article can be found below.

We also scraped news articles from October 2021 and performed similar analyses, in order to extract insights about the news coverage of more (at the time of writing) recent events.



### Data


We use the NELA2017 dataset, which accumulates thousands of news articles from nearly 100 different news organizations over a 7-month
period in 2017. Citations and links to the dataset and accompanying article can be found below.

We also scraped news articles from October 2021 and performed similar analyses, in order to extract insights about the news coverage of more (at the time of writing) recent events.


### Results


Our analyses are synthesized and visualized in the 'plots.ipynb' jupyter notebook. Here are a couple of highlights:

![alt text](https://github.com/alexander-paskal/news-bias-analysis/blob/main/data/wordcloud.png?style=centerme)<br>

*Word Cloud of FOX news in 2017. Trump dominated the headlines*<br>
![alt text](https://github.com/alexander-paskal/news-bias-analysis/blob/main/images/polarity.png?style=centerme)<br>

*Polarity distribution of CNN, BBC and FOX for sentences referencing 'trump'. As can be seen, polarity was remarkably similar across all three organizations.*<br>

![alt text](https://github.com/alexander-paskal/news-bias-analysis/blob/main/images/difficulty.png?style=centerme)<br>

*TTR(a difficulty measure) distribution of CNN, BBC and FOX. BBC clearly used more elevated language with consistency.*



### Citation

Dataset:
```
https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/ZCXSKG
```

Sentimental analysis and readability analysis:
```
https://github.com/farooq96/News-Sentiment-Analysis-in-Python
```








