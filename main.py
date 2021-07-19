from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)
NPOINT_API = "https://www.npoint.io/docs/5abcca6f4e39b4955965"

# todo del next dictionary and check requests
all_posts = [
    {
        "id": 1,
        "title": "title1",
        "subtitle": "subtitle1",
        "body": "body1",
    },
    {
        "id": 2,
        "title": "title2",
        "subtitle": "subtitle2",
        "body": "body2",
    },
    {
        "id": 3,
        "title": "title3",
        "subtitle": "subtitle3",
        "body": "body3",
    }
]
# response=requests.get(NPOINT_API)
# print(response.status_code)
# all_posts=response.json()

post_list = []
for post in all_posts:
    post_obj = Post(post_id=post["id"], title=post["title"], subtitle=post["subtitle"], body=post["body"])
    post_list.append(post_obj)

@app.route('/')
def home():
    return render_template("index.html", post_list=post_list)


@app.route('/post/<int:blog_id>')
def blog(blog_id):
    return render_template("post.html", post=post_list[blog_id-1])


if __name__ == "__main__":
    app.run(debug=True)
