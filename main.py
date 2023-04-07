import streamlit as st
import pandas as pd
import snscrape.modules.twitter as sntwitter
from pymongo import MongoClient

st.set_page_config(
    page_title="Twitter scraping",
    page_icon=":smile:",
    layout="centered",
    initial_sidebar_state="expanded",

)

st.title('Twitter Scraping App')
st.image('data:image/png;base64,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')

def scrapetwitter(search_term,start_date,end_date,limit):
    attributes_container = []
# Using TwitterSearchScraper to scrape data and append tweets to list
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(f'{search_term} since:{start_date} until:{end_date}').get_items()):
        if i > limit:
            break
        attributes_container.append([tweet.date, tweet.id, tweet.url, tweet.content, tweet.user.username, tweet.replyCount, tweet.retweetCount,
         tweet.lang, tweet.sourceLabel, tweet.likeCount])

# Creating a dataframe from the tweets list above
    tweets_df = pd.DataFrame(attributes_container, columns=["Date Created", "ID", "URL", "Content", "User", "Replycount", "Retweetcount",
                                  "Language", "Source", "Likecount"])
    return tweets_df


search_term = st.text_input('Enter the Keyword/Hashtag')
start_date = st.date_input('Start date', )
end_date = st.date_input('End date',)
limit = st.slider('How many tweets do you want to get?', 0, 2000, step=100)
submit_button = st.button(label='Search')
upload_button = st.button('Upload to MongoDB')

tweets_df = scrapetwitter(search_term, start_date, end_date, limit)
if submit_button:
    st.dataframe(tweets_df)
    json_string = tweets_df.to_json()

    col1, col2 = st.columns([1, 1])

    with col1:
        st.download_button(
             label="Download CSV ",
             data=tweets_df.to_csv(),
             file_name=f'{search_term}.csv',
             mime='text/csv')
    with col2:
        st.download_button(
            label="Download JSON",
            file_name=f"{search_term}.json",
            mime="application/json",
            data=json_string)


if upload_button:
    client = MongoClient('mongodb://localhost:27017')
    db = client["tweet_database"]
    collection = db["tweet_collection"] #Creating collection in database
    # converting dataframe to json files
    data = tweets_df.to_dict(orient='records')
    collection.insert_one({"index": f"{search_term}", "data": data})
