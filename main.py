from flask import Flask,request
import instaloader
import os

from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

class APIAuthError(Exception):
  code = 403
  description = "Authentication Error"

L = instaloader.Instaloader()
# USER = os.getenv("LOGIN")
# PASSWORD = os.getenv("PASSWORD")
# L.login(USER,PASSWORD)

@app.route("/download")
def getDownloadLink():
    args = request.args
    post_url = args.get("url")
    try:
        post = instaloader.Post.from_shortcode(L.context, post_url.split('reel/')[1].split("/")[0])
        return  post.video_url
    except:
        return "An exception occurred"
