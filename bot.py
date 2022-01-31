import time
import feedparser
import requests
import os

chat_id = -1001789110861
bot_token = "5299386335:AAGXz22rE-zWa_k1YHy899KpYyJeCMkaVu8"
feed_url = "https://www.reddit.com/r/memes/new/.rss"

bin = 5
l_bin = 7

while bin <= l_bin:
  blog_feed = feedparser.parse(feed_url)
  blog_feed.feed.title
  blog_feed.feed.link
  len(blog_feed.entries)
  link = (blog_feed.entries[0].link)
  #print(link)
  
  response = requests.get(f'https://redditsave.com/info?url={link}')
  qq = response.text
  def slicetext(text, start, end):
    try:
      return text.split(start)[1].split(end)[0]
    except:
      return ""
      
  ww = slicetext(f"{qq}", "https://i.redd.it/", "\" class")
  #print(ww)
  with open('last.txt') as f:
    lines = f.readlines(0)
    #print(lines)
    ww2 = f'[\'{ww}\']'
    if str(lines)==ww2:
      #print(ww2)
      print('Nope')
    else:
      url = f'https://api.telegram.org/bot{bot_token}/sendPhoto?chat_id={chat_id}&photo=https://i.redd.it/{ww}&caption=Join+Us+@MemeWorldNo1'
      r = requests.get(url, allow_redirects=True)
      #print(r.text)
      with open('last.txt', 'w') as f:
        f.write(f'{ww}')
      time.sleep(5)
