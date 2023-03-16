import os
import time
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
import tweepy


# Load environment variables from .env file
load_dotenv()
github_owner = os.getenv("GITHUB_OWNER")
github_repository = os.getenv("GITHUB_REPOSITORY")
github_personal_token = os.getenv("GITHUB_PERSONAL_TOKEN")
twitter_api_key = os.getenv("API_KEY")
twitter_api_secret_key = os.getenv("API_SECRET_KEY")
twitter_access_token = os.getenv("ACCESS_TOKEN")
twitter_access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")
time_interval_seconds = int(os.getenv("TIME_INTERVAL_SECONDS"))


# Initialize Twitter API client
auth = tweepy.OAuthHandler(twitter_api_key, twitter_api_secret_key)
auth.set_access_token(twitter_access_token, twitter_access_token_secret)
api = tweepy.API(auth)


def get_last_commit():
    """
    Returns the last commit message and timestamp from Github.
    """
    url = f"https://api.github.com/repos/{github_owner}/{github_repository}/commits"
    headers = {
        "Authorization": f"Token {github_personal_token}"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    commits = response.json()
    last_commit = commits[0]
    commit_message = last_commit['commit']['message']
    commit_timestamp = last_commit['commit']['author']['date']
    return commit_message, commit_timestamp


if __name__ == '__main__':
    while True:
        try:
            commit_message, commit_timestamp = get_last_commit()
            tweet_text = f"Last commit for {github_repository}: {commit_message} ({commit_timestamp})"
            api.update_status(tweet_text)
            print("Tweeted successfully!")
        except Exception as e:
            print("Error while tweeting:", e)
        time.sleep(time_interval_seconds)
