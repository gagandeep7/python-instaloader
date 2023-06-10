from flask import Flask,request,jsonify
import instaloader
import os

from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

class APIAuthError(Exception):
  code = 403
  description = "Authentication Error"

L = instaloader.Instaloader()

@app.route("/download")
def getDownloadLink():
    args = request.args
    post_url = args.get("url")
    try:
        post = instaloader.Post.from_shortcode(L.context, post_url.split('reel/')[1].split("/")[0])

        return  jsonify({"DATA":post.video_url})
    except:
        return "An exception occurred"
