# Previous requirements
Install python 3.11.2

# Installation
1. Clone this repository:

```sh
https://github.com/fireball787b/github-to-twiter
```

2. Navigate to the cloned directory:
```sh
cd github-to-twiter
```

3. Navigate to the cloned directory:
```sh
pip3 install -r requirements.txt
```

# Setup

1. Create a env folder and .env file in the root directory of the project:
```sh
mkdir env && cd env && touch .env && cd ..
```

2. Add the necessary environment variables to the .env file:
```sh
# Twitter API keys and access tokens
API_KEY=your_twitter_api_key
API_SECRET_KEY=your_twitter_api_secret_key
ACCESS_TOKEN=your_twitter_access_token
ACCESS_TOKEN_SECRET=your_twitter_access_token_secret

# Github repository information
GITHUB_OWNER=your_github_repository_owner
GITHUB_REPOSITORY=your_github_repository_name
GITHUB_PERSONAL_TOKEN=your_github_personal_access_token

# Time interval between tweet updates, in seconds
TIME_INTERVAL_SECONDS=60
```

Make sure to replace the values with your own Twitter API and Github repository information. Also, make sure to never share or commit this .env file to a public repository, as it contains sensitive information.

# Docker

1. Build the Docker image using the Dockerfile:
```sh
docker build -t github-twitter-bot .
```

2. Run the Docker container:
```sh
docker run --env-file env/.env github-twitter-bot
```

This will start the script and run it inside the Docker container. The script will run continuously, tweeting out the latest commit message every TIME_INTERVAL_SECONDS seconds.