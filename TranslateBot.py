import praw
import time
from googletrans import Translator, constants
from praw import const


reddit = praw.Reddit(client_id='your client id',
                    client_secret='your client secret',
                    user_agent='Translate-Comment 1.0',
                    username='your username',
                    password='your password'
                    )


translator = Translator()

while True:
    for message in reddit.inbox.unread(limit=None):
        message.mark_read()
        # Bot has been called
        if message.type == 'username_mention' and message.was_comment and message.parent_id:
            if len(message.body.split()) >= 2:
                requested_language_name = message.body.split()[1].lower()

                try:
                    comment_to_translate = message.parent().body
                except AttributeError:
                    print('Comment was not a reply')
                    continue

                try:
                    #Search requested language in googles dictionary of languages to find the shortened language
                    language = list(constants.LANGUAGES.keys())[list(constants.LANGUAGES.values()).index(requested_language_name)]

                    translation = translator.translate(comment_to_translate, dest=language).text

                    original_comment = "Original Comment"
                    if requested_language_name != 'english':
                        original_comment = translator.translate(original_comment, dest=language).text

                    footer = '\n\n\n ^(this bot was developed by u/Adamv27) \n ^([Source Code](https://github.com/Adamv27/Translate-Comment-Bot))'
                    message.reply(f'{original_comment}: {comment_to_translate} \n\n {requested_language_name.capitalize()}: {translation} {footer}')
                    print('Successfully translated comment!')
                    
                except ValueError:
                    print('Language requested was invalid')


        
    time.sleep(5)

