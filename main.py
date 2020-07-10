from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
from selenium.webdriver.common.by import By

d=os.path.abspath("chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(executable_path = "C:\\Users\\abarc\\Downloads\\chromedriver_win32\\chromedriver")
def data(url):
    comments=[]
    names=[]
    driver.get(url)
    driver.maximize_window()
    height =driver.get_window_size()['height']
    comment_section = driver.find_element_by_xpath('//*[@id="contents"]')
    driver.execute_script("arguments[0].scrollIntoView();", comment_section)
    time.sleep(7)
    oh=driver.execute_script("return document.documentElement.scrollHeight")
    while True:
        try:
            driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
            time.sleep(2)
            nh = driver.execute_script("return document.documentElement.scrollHeight")
            if nh == oh:
                break   
            oh=nh
        except StaleElementReferenceException:
            break
    names=driver.find_elements_by_xpath('//*[@id="author-text"]')
    comments=driver.find_elements_by_xpath('//*[@id="content-text"]')
    return [names,comments]



import pandas as pd
url=input("Enter url: ")
data1=data(url)
name=[]
comment=[]
for i in data1[0]:
    name.append(i.text)
for i in data1[1]:
    comment.append(i.text)
driver.close()
df=pd.DataFrame(list(zip(name,comment)),columns=['Name','Comment'])


import nltk
import emoji
import re 
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sid=SentimentIntensityAnalyzer()
def preprocess(x):
    text=emoji.demojize(x)
    txt=re.sub("[:,_]"," ",text)
    return sid.polarity_scores(txt)['compound']

positive = 0
wpositive = 0
spositive = 0
negative = 0
wnegative = 0
snegative = 0
neutral = 0

df['Score']=df['Comment'].apply(lambda x: preprocess(x))

print("\n\nNumber of comments extracted is: " + str(len(df['Score'])))
print("\nTop "+str(len(df['Score'])) + " comments are: \n")
print(df)
print()
print("-----------------------------------------------------------------------------------------------------------------------")
print()

NoOfTerms = len(df['Score'])

for i in df['Score']:
    if (i == 0):  
        neutral += 1
    elif (i > 0 and i <= 0.3):
        wpositive += 1
    elif (i > 0.3 and i <= 0.6):
        positive += 1
    elif (i > 0.6 and i <= 1):
        spositive += 1
    elif (i > -0.3 and i <= 0):
        wnegative += 1
    elif (i > -0.6 and i <= -0.3):
        negative += 1
    elif (i > -1 and i <= -0.6):
        snegative += 1

positive = format(100 * float(positive) / float(NoOfTerms), '0.2f')
wpositive = format(100 * float(wpositive) / float(NoOfTerms), '0.2f')
spositive = format(100 * float(spositive) / float(NoOfTerms), '0.2f')
negative = format(100 * float(negative) / float(NoOfTerms), '0.2f')
wnegative = format(100 * float(wnegative) / float(NoOfTerms), '0.2f')
snegative = format(100 * float(snegative) / float(NoOfTerms), '0.2f')
neutral = format(100 * float(neutral) / float(NoOfTerms), '0.2f')



Final_score = df['Score'].describe().loc['mean']

if Final_score>0:
    print("Using Vader Sentiment Analyzer: ")
    print("    Overall Reviews are Positive with Score "+ str(format(100 * Final_score , '0.2f')+"% \n"))
elif Final_score<0:
    print("Using Vader Sentiment Analyzer: \n")
    print("Overall Reviews are Negative with Score "+ str(format(100 * Final_score , '0.2f')+"% \n"))
else :
    print("Using Vader Sentiment Analyzer: \n")
    print("Overall Reviews are Moderate with Score "+ str(format(100 * Final_score , '0.2f')+"% \n"))


print()
print("Detailed Report: ")
print(str(positive) + "% people thought it was positive")
print(str(wpositive) + "% people thought it was weakly positive")
print(str(spositive) + "% people thought it was strongly positive")
print(str(negative) + "% people thought it was negative")
print(str(wnegative) + "% people thought it was weakly negative")
print(str(snegative) + "% people thought it was strongly negative")
print(str(neutral) + "% people thought it was neutral")



print()
print("-----------------------------------------------------------------------------------------------------------------------")
print()


from textblob import TextBlob
def preprocesss(x):
    text=emoji.demojize(x)
    txt=re.sub("[:,_]"," ",text)
    analysis = TextBlob(txt)
    return analysis.sentiment.polarity

positive1 = 0
wpositive1 = 0
spositive1 = 0
negative1 = 0
wnegative1= 0
snegative1 = 0
neutral1 = 0

df['Score']=df['Comment'].apply(lambda x: preprocesss(x))



for i in df['Score']:
    if (i == 0):  
        neutral1 += 1
    elif (i > 0 and i <= 0.3):
        wpositive1 += 1
    elif (i > 0.3 and i <= 0.6):
        positive1 += 1
    elif (i > 0.6 and i <= 1):
        spositive1 += 1
    elif (i > -0.3 and i <= 0):
        wnegative1 += 1
    elif (i > -0.6 and i <= -0.3):
        negative1 += 1
    elif (i > -1 and i <= -0.6):
        snegative1 += 1

positive1 = format(100 * float(positive1) / float(NoOfTerms), '0.2f')
wpositive1 = format(100 * float(wpositive1) / float(NoOfTerms), '0.2f')
spositive1 = format(100 * float(spositive1) / float(NoOfTerms), '0.2f')
negative1 = format(100 * float(negative1) / float(NoOfTerms), '0.2f')
wnegative1 = format(100 * float(wnegative1) / float(NoOfTerms), '0.2f')
snegative1 = format(100 * float(snegative1) / float(NoOfTerms), '0.2f')
neutral1 = format(100 * float(neutral1) / float(NoOfTerms), '0.2f')



Final_score1 = df['Score'].describe().loc['mean']

if Final_score1>0:
    print("Using TextBlob Sentiment Analyzer: ")
    print("    Overall Reviews are Positive with Score "+ str(format(100 * Final_score1 , '0.2f')+"% \n"))
elif Final_score1<0:
    print("Using TextBlob Sentiment Analyzer: \n")
    print("Overall Reviews are Negative with Score "+ str(format(100 * Final_score1 , '0.2f')+"% \n"))
else :
    print("Using TextBlob Sentiment Analyzer: \n")
    print("Overall Reviews are Moderate with Score "+ str(format(100 * Final_score1 , '0.2f')+"% \n"))


print()
print("Detailed Report: ")
print(str(positive1) + "% people thought it was positive")
print(str(wpositive1) + "% people thought it was weakly positive")
print(str(spositive1) + "% people thought it was strongly positive")
print(str(negative1) + "% people thought it was negative")
print(str(wnegative1) + "% people thought it was weakly negative")
print(str(snegative1) + "% people thought it was strongly negative")
print(str(neutral1) + "% people thought it was neutral")


