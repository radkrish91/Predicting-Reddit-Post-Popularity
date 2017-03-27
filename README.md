# Predicting-Reddit-Post-Popularity

Reddit is a popular social news website, where users post links, text or images which other users can up vote or down vote. This analytic aims to analyze and predict popularity of reddit content. The data was obtained through reddit’s api which is free of cost. The data set contains around 17 features or columns with number of ups(votes) being one of them. Our aim is to predict the factors that influence this feature with high accuracy. To predict this, we need to be able to identify the causality of up votes. While a post’s popularity is usually related to the post’s content, there are often other factors that determine how successful a post becomes. The focus of this analytic is also to analyze how these factors play a role in predicting how popular a post will become. This included features such as the content of the post and its sentiment, the Subreddit of the post, author of the post, and the time of day the post was created.

# Dataset Used

Reddit released an enormous dataset containing all ~1.7 billion of their publicly available comments. Kaggle hosts a portion of the comments (from May 2015). The database has one table with fields like subreddit_id, link_id, author, score, retrieved_on, controversiality, parent_id etc.

# Findings

* Engagement score of a subreddit
* Top 10 subreddits with highest engagement scores
* Engagement of a subreddit based on timeline (24 hours in a day)
* Classification of top subreddits based on sentiment class (1: 'Highly Positive', 2: 'Moderately positive', 3: 'Neutral', 4: 'Moderately Negative', 5: 'Highly Negative')
* Most popular words in each subreddit for a given sentiment
* Comments by author classified by sentiment
* Author influence on score
* Time influence on score

# API Used

1. Reddit comment dataset
    > `https://www.kaggle.com/reddit/reddit-comments-may-2015`

2. Hackernews post dataset
    > `https://www.kaggle.com/hacker-news/hacker-news-posts`

3. Python NLTK
    > `http://www.nltk.org/api/nltk.html`

4. Vader Sentiment Analyzer
    > `http://www.nltk.org/api/nltk.sentiment.html`
    
# Team members

* Prasanna Chandramouli
* Radhakrishnan Moni
* Varun Elango





