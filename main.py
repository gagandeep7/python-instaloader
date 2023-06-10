from flask import Flask,request
import utils
app = Flask(__name__)

@app.route("/download")
def hello_world():
    args = request.args
    url = args.get("url")
    return utils.getDownloadLink(url)