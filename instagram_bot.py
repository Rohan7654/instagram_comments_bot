import os
import logging
import time
from instagram_private_api import Client, ClientCompatPatch

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class InstagramBot:
    def __init__(self, username, password):
        self.api = Client(username, password)
        ClientCompatPatch.user_agent = self.api.user_agent

    def like_recent_comments(self, user_id):
        # TODO: Implement fetching of recent comments
        recent_media = self.api.user_feed(user_id, count=10)
        for media in recent_media.get('items', []):
            comments = self.api.media_comments(media['id'])
            for comment in comments.get('comments', []):
                if not comment['has_liked_comment']:
                    self.api.post_like_comment(comment['id'])
                    logger.info(f"Liked comment {comment['id']} at {time.ctime()}")

def initialize():
    username = os.environ['INSTAGRAM_USERNAME']
    password = os.environ['INSTAGRAM_PASSWORD']
    target_user_id = os.environ['TARGET_USER_ID']
    bot = InstagramBot(username, password)
    while True:
        try:
            bot.like_recent_comments(target_user_id)
            time.sleep(60)  # Wait for a minute before checking again
        except Exception as e:
            logger.error(f"Error during operation: {e}")
            time.sleep(60)  # Wait for a minute before retrying
