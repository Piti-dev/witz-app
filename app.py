from flask import Flask, jsonify
import random

app = Flask(__name__)

witze = [
    "Chuck Norris kann Drehtüren zuschlagen",
    "Chuck Norris hat bis unendlich gezählt, zweimal",
    "Chuck Norris kann Zwiebeln zum weinen bringen"
]

@app.route("/witz", methods=["GET"])
def witz():
    return jsonify({"witz": random.choice(witze)})

if __name__ == "__main__":
    app.run()