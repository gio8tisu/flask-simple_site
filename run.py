import random

from flask import Flask, render_template
app = Flask(__name__)


IMAGES = {  # {title: image}
    "Italian Trulli": "pic_trulli.jpg",
    "Girl in a jacket": "img_girl.jpg",
    "Flowers in Chania": "img_chania.jpg",
}


@app.route("/")
def template_test():
    title = random.choice(list(IMAGES.keys()))
    image = IMAGES[title]
    return render_template("index.html", title=title, image=image)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
