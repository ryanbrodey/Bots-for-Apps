import tweepy

# Replace with your own API keys and tokens
API_KEY = '38SXmEkz463znqjBSmwVe1vG6'
API_SECRET_KEY = 'b6sP86QiqFp9dsTCdc8606UwU1VLUNRT3ypun9IhbvAbbVv2Wj'
ACCESS_TOKEN = '972704302622916608-V1szOLXpx0GpvUlkmyfJMoDvvwZTcRc'
ACCESS_TOKEN_SECRET = '0CVQv4JxUDEls6Y0aAoLYYVg7I1ar68cpiH6ZQ5eq9zew'

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
