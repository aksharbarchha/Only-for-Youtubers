# Youtube-Comments-Sentiment-Analysis
Basic sentiment analysis of comments on a youtube video using a builtin python package "Vader Lexicon Sentiment Analyser" and "TextBlob Sentiment Analyser".

## How it is made
I have simply used "Youtube Data API" which is available on "Google Developers Console" to scrap youtube comments of a particular video. Then I have made use of python library called "NLTK", a platform for building python programs to work with Human language data. More specifically, what I have used is called VADER (Valence Aware Dictionary and Sentiment Reasoner) which is a lexicon and rule-based sentiment analysis tool that is specifically attuned to sentiments expressed on social media. I have also used TextBlob Sentiment Analyser and compared it with vader lexicon to give a machine generated report on sentiments of comments that are posted (Expressed) on a particular video.

## Scoring Procedure
The basic idea behind sentiment analysis using vader lexicon and TextBlob is that it contains a dictionary of words with some value assigned to it. Eg a word like **"Good"** or **"Amazing"** would have some **Positive value** assigned to it and a word like **"Bad"** or **"sad"** would have a **Negative value** assigned to it. So what I did is that I made a program that reads all the comments on a particular youtube video and then calculate `Compound Score` for each line and label it according to the following relation:-

1. `Weakly Positive sentiment: compound score <= 0.3`
2. `Positive sentiment: compound score >= 0.3 and <= 0.6`
3. `Strongly Positive sentiment: compound score >= 0.6`
4. `Neutral sentiment: compound score = 0`
5. `Weakly Negative sentiment: compound score <= 0 and > -0.3`
6. `Negative sentiment: compound score <= -0.3 and > -0.6`
7. `Strongly Negative sentiment: compound score <= -0.6`

## To run this
You will have to install some libraries. I have provided requirements.txt file so open command prompt and `Run:`
1. `pip install -r requirements.txt`

**Running the program**

First of all enter your developer key in the code where it is written `#PutYourKeyHere`. Then type in your terminal `python youtube_comments_sentiment_analysis.py`.

## Output

![Image](https://github.com/aksharbarchha/Youtube-Comments-Sentiment-Analysis/blob/master/image.png)
