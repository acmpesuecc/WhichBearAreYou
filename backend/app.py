from fastai.vision.all import *
from flask import Flask, request
from flask_cors import CORS, cross_origin
import urllib
import base64


app = Flask(__name__)
cors = CORS(app)


learn_inf = load_learner("bears.pkl")


def search_by_base64_image(b64imgstring):
    """
    Accepts a Base64-encoded image as a string, and runs the model on it
    """
    destination_filename = "temp.jpg"
    with open(destination_filename, "wb") as image:
        image.write(base64.decodebytes(b64imgsting.encode()))
    val = learn_inf.predict("temp.jpg")
    return [val[0], val[2][0].item(), val[2][1].item(), val[2][2].item()]


def search_by_url(url):
    dest = "temp.jpg"
    # download_url(url, dest)
    urllib.request.urlretrieve(url, dest)
    val = learn_inf.predict("temp.jpg")
    return [val[0], val[2][0].item(), val[2][1].item(), val[2][2].item()]


@app.route("/")
@cross_origin()
def hello_world():
    return "Hello, World!"


@app.route("/api/url/bear", methods=["POST"])
@cross_origin()
def bear_hunt():
    data = request.json
    ans = search_by_url(data["url"])
    print(ans)
    return {"prediction": ans}


@app.route("/api/url/bear_base64", methods=["POST"])
@cross_origin()
def bear_hunt_base64():
    data = request.json
    ans = search_by_base64_image(data["img_base64_string"])
    print(ans)
    return {"prediction": ans}
