IMPORTANT: The API Keys and password in my code are not my actual ones for security and privacy reasons. For the very top section, you would replace that information with yours to use the bot. 

The bot account I created for Reddit is: Responsible-Draw-99

# Reddit Bot Project

This is a Reddit bot created in Python using the `praw` (Python Reddit API Wrapper) library. The bot performs various actions such as retrieving posts, submitting posts, retrieving comments, and replying to comments on Reddit.

## Features

- **Connect to Reddit API:** Authenticate with Reddit using credentials to interact with Reddit's API.
- **Fetch Submissions:** Retrieve top posts from specific subreddits.
- **Submit Posts:** Submit new posts to chosen subreddits.
- **Retrieve Comments:** Extract comments from a Reddit post.
- **Reply to Comments:** Automatically reply to specific comments based on keywords.

## Prerequisites

- **Python 3.6+**: Make sure you have Python installed. You can check your version using:
  ```bash
  python3 --version
- **PRAW Library**: Install PRAW if you haven't already:
  ```bash
  pip install praw

## Setup Instructions 
- **1. Clone the Repository**: 
  ```bash
  git clone https://github.com/yourusername/reddit-bot.git
  cd reddit-bot
- **2. Create a Reddit App**: 
  1. Go to [Reddit's App Preferences](https://www.reddit.com/prefs/apps).
  2. Click on **"Create App"** and set up your Reddit application.
  3. Take note of your `client_id`, `client_secret`, `username`, and `password`.
 
- **3. Configure the Bot**:

  Update the `reddit_bot.py` file with your Reddit API credentials:
  ```python
  username = "YourUsername"   # Your Reddit username
  password = "YourPassword"   # Your Reddit password
  client_id = "YourClientID"  # Your app's client ID
  client_secret = "YourClientSecret"  # Your app's secret key


## How to Run the Bot

1. **Run the script:**
   ```bash
   python3 reddit_bot.py
2. The bot will start performing actions based on the code sections that are uncommented.



