#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 20:22:52 2018

@author: Linna
"""

import pandas as pd

import requests

from bs4 import BeautifulSoup

from selenium import webdriver

from selenium.webdriver.common.keys import Keys

import time

import os

from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.chrome.options import Options

from time import strptime

import copy

from datetime import datetime

import re

import random

import uuid

import urllib.request

from newspaper import Config, Article, Source

from joblib import Parallel, delayed

from tqdm import tqdm, trange

from nltk import tokenize

from nltk.sentiment.vader import SentimentIntensityAnalyzer

import subprocess

import nltk

nltk.download('punkt') 

pip.main(["install", "tqdm"])

 

def wait_for_internet_connection():
    while True:
        try:
            response = urllib.request.urlopen('https://facebook.com',timeout=1)
            return
        except urllib.request.URLError:
            pass

       

def pause():
    programPause = input("Press the <ENTER> key to continue...")

   

#chromedriver = '\Users\linhenry\chromedriver.exe'


#chromedriver = 'C:\\chromedriver.exe'
#browser = webdriver.Chrome(chromedriver)
#browser.get('http://www.example.com') 

 

#chromedriver = '/Users/linhenry/Downloads/chromedriver'
driver = webdriver.Chrome()

#os.environ["webdriver.chrome.driver"] = chromedriver

 

#chrome_options = Options()

#adblock:


#chrome_options.add_argument('headless')

#driver = webdriver.Chrome(chromedriver, chrome_options=chrome_options)

 

#driver = webdriver.Chrome(chromedriver)                                   

 

appended_data = []
appended_data_0 = []
appended_data_1 = []

 

first = True

bot_warn = 'Our systems have detected unusual traffic from your computer network'

 

for x in range(0, 1):
#for x in range(0, 2):   
    for y in range(7, 8):
        for m in range (9, 13):
            for d in range(1, 32):
                wait_for_internet_connection()
                driver.get('https://www.google.com/search?q=' + str(uuid.uuid4()))
                time.sleep(random.uniform(1, 1.5))
                wait_for_internet_connection()
                driver.get('https://www.google.com/search?q=site:www.forbes.com/sites/*/201' + str(y) +'/' + str('{0:02}'.format(m)) + '/' + str('{0:02}'.format(d)) + '/' +'&filter=' + str(x))
                src = driver.page_source
                if first:
                    pause()
                    first = False
                elif bool(re.search(bot_warn, src)):
                    os.system("printf '\a'"); time.sleep(1); os.system("printf '\a'"); time.sleep(1); os.system("printf '\a'")
                    pause()
                else:
                    time.sleep(random.uniform(61, 63))
                    time.sleep(random.uniform(1, 1.5))
                while True:
                    for i in range(1, 150):
                        try:
                            url = driver.find_element_by_css_selector('.g:nth-child(' + str(i) +") a").get_attribute('href')
                            appended_data.append(url)
                            if x == 0:
                                appended_data_0.append(url)
                            if x == 1:
                                appended_data_1.append(url)
                        except:
                            #print("no more links")
                            break
                    time.sleep(random.uniform(0.5, 1))
                    try:
                        # this is navigate to next page
                        #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                        time.sleep(random.uniform(0.5, 1))
                        button = driver.find_element_by_css_selector('#pnnext .ch+ span')
                        wait_for_internet_connection()
                        button.click()
                        time.sleep(random.uniform(2, 3))
                    except:
                        #print("no more pages")
                        break
                if x == 0:
                    print(str(len(set(appended_data_0))) + '  ' + str(m) + '/' + str(d) + '--' + str(y))
                if x == 1:
                    print(str(len(set(appended_data_1))) + '  ' + str(m) + '/' + str(d) + '--' + str(y))

 

 

# only in filter=0

print(len(list(set(appended_data_0).difference(appended_data_1))))

# only in filter=1

print(len(list(set(appended_data_1).difference(appended_data_0))))

# in both

print(len(list(set(appended_data_0).intersection(appended_data_1))))

 

appended_data2 = set(appended_data)

 

 

config = Config()
config.MAX_TEXT = 1000000

 

def chunkify(lst,n):
    return [ lst[i::n] for i in range(n) ]

 

def process_article(url):
    for x in range(0, 5):
        try:
            article = Article(url, config)
            article.download()
            article.parse()
            headline = article.title
            publish_date = article.publish_date
            authors = article.authors
            fulltext = article.text
            article.nlp()
            keywords = article.keywords
            summary = article.summary
            forbes_all = {'url':url,
                          'date':publish_date,
                          'authors':authors,
                          'headline':headline,
                          'fulltext':fulltext,
                          'summary':summary,
                          'keywords':keywords}
            return forbes_all
        except:
            wait_for_internet_connection()
            time.sleep(0.1)
            continue
        break

 

 

#chromedriver = '/Users/linhenry/Downloads/chromedriver'

#os.environ["webdriver.chrome.driver"] = chromedriver

 

#chrome_options = Options()

#adblock:


#chrome_options.add_argument('headless')

#driver = webdriver.Chrome(chromedriver, chrome_options=chrome_options)

 

#driver = webdriver.Chrome(chromedriver)

 

results = Parallel(n_jobs=-1)(delayed(process_article)(url) for url in tqdm(appended_data2))

 

#results = [x for x in results if x is not None]

#results_df = pd.DataFrame(results)

#results_df.to_csv('forbes_output.csv', index=False)

 

 

#results = [process_article(x) for x in list(appended_data2)]

 

results = [x for x in results if x is not None]

 

results_df = pd.DataFrame(results)

results_df.to_csv('forbes_output.csv', index=False)


url_list = list(appended_data)

driver = webdriver.Chrome()
forbes_views = []
for x in range(0, len(url_list)):
    driver.get(url_list[x])
    try:
        driver.find_element_by_css_selector('.continue-button').click()
    except:
        wait_for_internet_connection()
        time.sleep(0.1)
        continue
    vwc = driver.find_element_by_css_selector('.view-count').get_attribute("innerHTML")
    vwc = vwc.split('\n')[0].replace(',', '')
    vwc = int(vwc)
    forbes_views = forbes_views + [vwc]

    

f_views = pd.DataFrame()
f_views['urls'] = url_list
f_views['views'] = forbes_views

results_df2 = pd.merge(results_df, f_views, how = 'left', left_on = 'url', right_on = 'urls')












