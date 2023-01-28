from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
    "https://media4.giphy.com/media/3o6Zt481isNVuQI1l6/200w.webp?cid=ecf05e47ycqp0d5woww638uaq2ga8wqfx19l01ftnk5esm5h&rid=200w.webp&ct=g",
    "https://media1.giphy.com/media/BzyTuYCmvSORqs1ABM/200w.webp?cid=ecf05e47ycqp0d5woww638uaq2ga8wqfx19l01ftnk5esm5h&rid=200w.webp&ct=g",
    "https://media3.giphy.com/media/mlvseq9yvZhba/giphy.webp?cid=ecf05e47ycqp0d5woww638uaq2ga8wqfx19l01ftnk5esm5h&rid=giphy.webp&ct=g",
    "https://media0.giphy.com/media/VbnUQpnihPSIgIXuZv/giphy.webp?cid=ecf05e47ycqp0d5woww638uaq2ga8wqfx19l01ftnk5esm5h&rid=giphy.webp&ct=g",
    "https://media2.giphy.com/media/9IRX12VhoXoR2/200w.webp?cid=ecf05e47377uieka1o2d6vr8bo1rfa4n1xt2ilu34e9lw7cn&rid=200w.webp&ct=g"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
