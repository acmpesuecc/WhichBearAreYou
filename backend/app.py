from fastai.vision.all import *
from flask import Flask, request
from flask_cors import CORS, cross_origin
import urllib
import base64
import torch

if not hasattr(torch.Tensor, "_old_H"):
    torch.Tensor._old_H = torch.Tensor.H

    @property
    def safe_H(self):
        if self.ndim < 2:
            return self
        return self._old_H

    torch.Tensor.H = safe_H

app = Flask(__name__)
cors = CORS(app)

learn_inf = load_learner("bears.pkl")


def search_by_base64_image(b64imgstring):
    """
    Accepts a Base64-encoded image as a string, and runs the model on it
    """
    destination_filename = "temp.jpg"
    with open(destination_filename, "wb") as image:
        image.write(base64.decodebytes(b64imgstring.encode()))
    val = learn_inf.predict(destination_filename)
    return [val[0], val[2][0].item(), val[2][1].item(), val[2][2].item()]


def search_by_url(url):
    dest = "temp.jpg"
    urllib.request.urlretrieve(url, dest)
    val = learn_inf.predict(dest)
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
    b64data = request.get_data(as_text=True)
    ans = search_by_base64_image(b64data)
    print(ans)
    return {"prediction": ans}
