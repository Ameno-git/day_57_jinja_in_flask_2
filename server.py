from flask import Flask, render_template
import datetime
import requests

app = Flask(__name__)
year = datetime.datetime.now().year
print(year)


@app.route("/")
def main_page():
    return render_template("index.html", current_year=year)


@app.route("/guess/<name>")
def check_name(name):
    age_api = f"https://api.agify.io?name={name}"
    response = requests.get(age_api).json()
    print(response)
    age = response["age"]

    sex_api = f"https://api.genderize.io?name={name}"
    response = requests.get(sex_api).json()
    print(response)
    sex = response["gender"]
    return render_template("guess.html", year_old=age, sex=sex, name=name)



@app.route("/blog")
def blog():
    # blog_url="https://www.npoint.io/docs/5abcca6f4e39b4955965"
    # response=requests.get(blog_url)
    # all_posts=response.json()

    all_posts = [
        {
            "id": 1,
            "title": "t1"
        },
        {
            "id": 2,
            "title": "t2"
        },
        {
            "id": 3,
            "title": "t3"
        }
    ]

    return render_template("blog.html", all_posts=all_posts)
    # todo check api work


if __name__ == "__main__":
    app.run(debug=True)
