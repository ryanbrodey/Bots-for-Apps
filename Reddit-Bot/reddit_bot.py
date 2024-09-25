#!/usr/bin/env python3

import praw

# This section connects to the Reddit API using Python Code
# Define the credentials for connecting to Reddit's API
username = "Responsible-Draw-99"   # Your Reddit username
password = "tokoyami8"             # Your Reddit password
client_id = "6DIPzFIUKu3OZF4J6jdxtw"  # Unique ID for your Reddit app
client_secret = "ucuYqaeO10yeU8AkmQSpmMGfTIu6pg"  # Secret key for the Reddit app

# Create an instance of the Reddit API using the provided credentials
reddit_instance = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    username=username,
    password=password,
    user_agent="test_bot"  # Custom user agent to identify the bot
)

# Optional: Print the username of the bot's account to verify connection
# print(reddit_instance.user.me())


# This section retrieves submissions from subreddits
# (This part is commented out, but it demonstrates how to fetch posts from a subreddit)
# subreddit = reddit_instance.subreddit("Nintendo")  # Access the "Nintendo" subreddit
# top_25_submissions = subreddit.top(limit=25, time_filter="week")  # Get the top 25 posts from the past week
# for submission in top_25_submissions:
#     print(submission.title)  # Print the title of each post


# This section submits posts in any subreddit you choose with any message
# (This part is commented out, but it demonstrates how to submit a post to a subreddit)
# subreddit = reddit_instance.subreddit("testingground4bots")  # Access a test subreddit
# subreddit.submit(title="This is my test post from Ryan's bot", selftext="Hello ZipLaunch")  # Submit a post


# # This section solely gets comments from a subreddit post
# # Get the Reddit submission (post) by its ID
# submission = reddit_instance.submission(id="1fmpv2m")  # Replace "1ev919g" with the actual post ID

# # Loop through the top-level comments of the submission
# for comment in submission.comments:
#     print(f"Comment: {comment.body}")  # Print the text of each comment


# This section gets comments from a subreddit post and replies to specific ones
try:
    # Get the Reddit submission (post) by its ID
    submission = reddit_instance.submission(id="1fh8ien")  # Replace with the post ID you want to interact with

    # Replace "MoreComments" objects to ensure all comments are loaded
    submission.comments.replace_more(limit=0)  # Use limit=0 to load all comments

    # Loop through the top-level comments of the post
    for comment in submission.comments:
        # Check if the comment contains the phrase "network unavailable" (case-insensitive)
        if "doll" in comment.body.lower():
            print(f"Found a comment: {comment.body}")  # Print the comment text
            comment.reply("uhhhhhhh")  # Reply to the comment
            print("Replied to the comment")

except Exception as e:
    # Catch and print any errors that occur while interacting with comments
    print(f"Error interacting with comments: {e}")
