import tweepy

# Replace with your own API keys and tokens
# NOTE I am not showing my actual keys and tokens on here for security breach reasons
API_KEY = '38SnqjBSmwVe1vG6'
API_SECRET_KEY = 'b6sP86QiCdc8606UwU1VLUNRT3ybbVv2Wj'
ACCESS_TOKEN = '972704608-V1szOlkmyfJMoDvvwZTcRc'
ACCESS_TOKEN_SECRET = '0CVQv4JxUDQ5eq9zew'

# Authenticate to Twitter
auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# Create API object
api = tweepy.API(auth)

# Test authentication
try:
    api.verify_credentials()
    print("Authentication OK")
except Exception as e:
    print("Error during authentication:", str(e))

# Function to post a tweet
def post_tweet(message):
    try:
        api.update_status(status=message)
        print(f"Successfully tweeted: {message}")
    except Exception as e:
        print(f"Error posting tweet: {str(e)}")

# Example tweet
tweet_message = "Hello from my Twitter bot using Tweepy! #Python #TwitterBot"
post_tweet(tweet_message)
