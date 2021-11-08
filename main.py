from flask import Flask,jsonify,request
import csv

all_articals = []

with open("articals.csv",encoding = "UTF-8")as f:
    reader = csv.reader(f)
    data = list(reader)
    all_articals = data[1:]

liked_articals = []
not_liked_articals = []

app = Flask(__name__)

@app.route("/get-artical")
def get_artical():
    return jsonify({
        "data":all_articals[0],
        "status":"success"
    })

@app.route("/liked-artical",methods = ["POST"])
def liked_artical():
    global all_artical
    artical = all_articals[0]
    all_articals = all_articals[1:]
    all_articals.append(artical)
    return jsonify({
        "status":"success"
    }),201

@app.route("/unliked-artical",methods = ["POST"])
def not_liked_articals():
    global all_articals
    artical = all_articals[0]
    all_articals = all_articals[1:]
    all_articals.append(artical)
    return jsonify({
        "status":"success"
    }),201

if __name__ == "__main__":
    app.run()