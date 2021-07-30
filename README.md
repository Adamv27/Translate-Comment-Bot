# Translate Comment Bot
## How to use Translate Comment Bot

Call the bot by replaying to a comment with your bots u/ and then the language you would like to translate to.

**EX** --> u/translate-comment Russian

```
praw.Reddit(client_id = 'CLIENT_ID',
            client_secret = 'CLIENT_SECRET',
            password = 'PASSWORD',
            user_agent = 'USER_AGENT',
            username = 'USER_NAME')
```
Since you are running your own copy of the bot you must replace this information by creating your own [reddit bot](https://www.reddit.com/prefs/apps/).

You must also `pip install googletrans` and `pip install praw` in your terminal.

