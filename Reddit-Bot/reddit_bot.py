import praw

# This code below connects to the Reddit API using Python Code
username="Responsible-Draw-99"
password="YOUR_PASSWORD"
client_id="YOUR_ID"
client_secret="YOUR_SECRET_ID"

reddit_instance = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    username=username,
    password=password,
    user_agent="test_bot"
)

# print(reddit_instance.user.me())

# Section 1
# This section retrieves submissions from subreddits
# subreddit = reddit_instance.subreddit("Nintendo")
# top_25_submissions = subreddit.top(limit=25, time_filter="week")
# for submission in top_25_submissions:
#    print(submission.title)

# Section 2
# This section submits post in any subreddit you choose with any message 
subreddit = reddit_instance.subreddit("testingground4bots")
subreddit.submit(title="This is my test post from my bot", selftext="Hellow how are you doing")

# Section 3
# This section gets comments from a subreddit post, and has a part that is also capable of replying to comments 
# submission = reddit_instance.submission("1ev919g")
# comments = submission.comments

# for comment in comments:
#     if "green" in comment.body:
#         print(comment.body)
