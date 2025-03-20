from dotenv import load_dotenv
from ice_braker import ice_breaker
from flask import Flask, request, jsonify, render_template

load_dotenv()

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/ice_breaker", methods=["POST"])
def ice_breaker_route():
    prompt = request.form["name"]
    summary_and_facts, picture_url = ice_breaker(name=prompt)
    return jsonify(
        {
            "summary_and_facts": summary_and_facts.to_dict(),
            "picture_url": picture_url,
        }
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
