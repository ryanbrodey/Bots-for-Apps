import praw

# This section connects to the Reddit API using Python Code
username="Responsible-Draw-99"
password="tokoyami8"
client_id="6DIPzFIUKu3OZF4J6jdxtw"
client_secret="ucuYqaeO10yeU8AkmQSpmMGfTIu6pg"

reddit_instance = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    username=username,
    password=password,
    user_agent="test_bot"
)

# print(reddit_instance.user.me())

# This section retrieves submissions from subreddits
# subreddit = reddit_instance.subreddit("Nintendo")
# top_25_submissions = subreddit.top(limit=25, time_filter="week")
# for submission in top_25_submissions:
#    print(submission.title)

# This section submits post in any subreddit you choose with any message 
subreddit = reddit_instance.subreddit("testingground4bots")
subreddit.submit(title="This is my test post from my bot", selftext="Hellow how are you doing")

# This section gets comments from a subreddit post, and has a part that is also capable of replying to comments 
# submission = reddit_instance.submission("1ev919g")
# comments = submission.comments

# for comment in comments:
#     if "green" in comment.body:
#         print(comment.body)
