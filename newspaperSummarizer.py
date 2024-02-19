import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article
 
# news api
import requests

# news api  8fb05a75535a4174b04a5fab022be346

def getNewsApi(n, topic):
    url = ('https://newsapi.org/v2/everything?'
            'q=' + str(topic) + '&'
            'sortBy=relevancy&'
            'apiKey=8fb05a75535a4174b04a5fab022be346'
            )
        
    response = requests.get(url)
    articles = response.json().get('articles')[: n]
    titles = [article['title'] for article in articles if 'title' in article]

    summary.config(state='normal')
    summary.delete('1.0', 'end')
    summary.insert('1.0', '\n'.join(titles))
    summary.config(state='disabled')


# def getNews(n: int, topic):
#     pages = []

#     for i in range(0, n+1):
#         url = 'https://www.allsides.com/story/admin?tid=&field_story_topic_tid=' + \
#             str(topic) + '&page=' + str(i)
#         pages.append(url)
#     summary.config(state='normal')
#     summary.delete('1.0', 'end')
#     summary.insert('1.0', '\n'.join(pages))
#     summary.config(state='disabled')
    
def summarize():
    
    url = utext.get('1.0', 'end').strip()

    article = Article(url)

    article.download()
    article.parse()

    article.nlp()
    
    title.config(state='normal')
    author.config(state='normal')
    publication.config(state='normal')
    summary.config(state='normal')
    sentiment.config(state='normal')
    
    title.delete('1.0', 'end')
    title.insert('1.0', article.title)

    author.delete('1.0', 'end')
    author.insert('1.0', article.authors)

    publication.delete('1.0', 'end')
    publication.insert('1.0', article.publish_date)

    summary.delete('1.0', 'end')
    summary.insert('1.0', article.summary)

    analysis = TextBlob(article.text)
    sentiment.delete('1.0', 'end')
    sentiment.insert('1.0', f'Polarity: {analysis.polarity}, Sentiment: {"positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral"}')

    title.config(state='disabled')
    author.config(state='disabled')
    publication.config(state='disabled')
    summary.config(state='disabled')
    sentiment.config(state='disabled')


root = tk.Tk()
root.title("News Summarizer")
root.geometry("480x600")

topicLabel = tk.Label(root, text='Topic')
topicLabel.pack()

topic = tk.Entry(root, width=40)
topic.pack()

tlabel = tk.Label(root, text='Title')
tlabel.pack()

title = tk.Text(root, height=1, width=40)
title.config(state='disabled', bg="#dddddd")
title.pack()

alabel = tk.Label(root, text='Author')
alabel.pack()

author = tk.Text(root, height=1, width=40)
author.config(state='disabled', bg="#dddddd")
author.pack()

plabel = tk.Label(root, text='Publishing Date')
plabel.pack()

publication = tk.Text(root, height=1, width=40)
publication.config(state='disabled', bg="#dddddd")
publication.pack()

slabel = tk.Label(root, text='Summary')
slabel.pack()

summary = tk.Text(root, height=15, width=40)
summary.config(state='disabled', bg="#dddddd")
summary.pack()

selabel = tk.Label(root, text='Sentiment Analysis')
selabel.pack()

sentiment = tk.Text(root, height=1, width=40)
sentiment.config(state='disabled', bg="#dddddd")
sentiment.pack()

ulabel = tk.Label(root, text='URL')
ulabel.pack()

utext = tk.Text(root, height=1, width=40)
utext.pack()

btn = tk.Button(root, text='Summarize', command=summarize)
btn.pack()

getNewsBtn = tk.Button(root, text='Get News', command=lambda: getNewsApi(1, topic.get()))
getNewsBtn.pack()


root.mainloop()
