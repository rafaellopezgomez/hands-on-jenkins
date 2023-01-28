from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
    "https://media2.giphy.com/media/3oriO0OEd9QIDdllqo/200.webp?cid=ecf05e477luwdr6zny4dtuwp1woq7ztqs19dsz5ct3a890xm&rid=200.webp&ct=g",
    "https://media1.giphy.com/media/BzyTuYCmvSORqs1ABM/200w.webp?cid=ecf05e47ycqp0d5woww638uaq2ga8wqfx19l01ftnk5esm5h&rid=200w.webp&ct=g",
    "https://media3.giphy.com/media/mlvseq9yvZhba/giphy.webp?cid=ecf05e47ycqp0d5woww638uaq2ga8wqfx19l01ftnk5esm5h&rid=giphy.webp&ct=g",
    "https://media0.giphy.com/media/VbnUQpnihPSIgIXuZv/giphy.webp?cid=ecf05e47ycqp0d5woww638uaq2ga8wqfx19l01ftnk5esm5h&rid=giphy.webp&ct=g",
    "https://media3.giphy.com/media/LYd7VuYqXokv20CaEG/giphy.webp?cid=ecf05e47ajes90u2vf3tpcoelr85v5d39ku6019jcxly0q3l&rid=giphy.webp&ct=g",
    "https://media1.giphy.com/media/tBxyh2hbwMiqc/giphy.webp?cid=ecf05e472p7xsbd1qpddn73jdxvecgkgc4t98jueydc8kpwf&rid=giphy.webp&ct=g"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
