import instaloader
import os

from dotenv import load_dotenv
load_dotenv()
L = instaloader.Instaloader()
USER = os.getenv("LOGIN")
PASSWORD = os.getenv("PASSWORD")
def getDownloadLink(post_url):
    post = instaloader.Post.from_shortcode(L.context, post_url.split('reel/')[1].split("/")[0])
    return post.video_url