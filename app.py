import os
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
    port = int(os.environ.get("PORT", 10000))  # Render setzt automatisch die PORT-Variable
    app.run(host="0.0.0.0", port=port)