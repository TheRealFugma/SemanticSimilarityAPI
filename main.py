import os
import spacy
from flask import Flask, jsonify, request

app = Flask(__name__)

nlp = spacy.load("en_core_web_lg")


@app.route("/api", method="POST")
def api():
    if (request.json is None
        or "text1" not in request.json
        or "text2" not in request.json):
        return "Can't do JSON", 400
    text1 = nlp(request.json["text1"])
    text2 = nlp(request.json["text2"])

    return jsonify({"similarity": text1.similarity(text2)})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

