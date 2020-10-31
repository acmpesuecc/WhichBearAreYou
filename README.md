# WhichBearAreYou?

A friendy little website that tells you which bear you are!

For a little more insight into the model behind it, watch [this video!](https://www.youtube.com/watch?v=5zWftQX1YgI)

## Technology Stack

- React
- Flask
- FastAI Model

## How to Run

### Backend Setup

1. `cd backend`
2. `pip3 install -r requirements.txt`
3. Add the model to the backend folder with the name `bears.pkl`. The model can be downloaded from [here](https://drive.google.com/file/d/1XUlSGjbx7m9P2-Lobj7JBq1DH1tPeaJz/view)
4. To test locally, `flask run`

### Frontend Setup

1. `cd frontend`
2. `npm install`
3. To test locally, `npm start`

## FAQs

### What is a base64 image string, and what does it do?

A base-64 image string is an image that has been converted(encoded) to a different format(pixel rgb -> alphabet). The 'search_by_base64_image' function in [backend/app.py](https://github.com/acmpesuecc/WhichBearAreYou/blob/master/backend/app.py) accepts a b64 encoded image string as an arguement, writes/overwrites it to a temp.jpg file after which the model is run on it as an alternative to searching for an image on the internet by URL.

## How do I contribute?

Check out the contributing guidelines to learn more!

## Is this beginner friendly?

YES!

## What if I have a problem?

Contact any of the ACM team members!

**This is one of the Official repositories created by ACM PESUECC for Hacktoberfest 2020!**
