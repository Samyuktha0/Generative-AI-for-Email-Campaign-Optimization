from flask import Flask, request, render_template
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    content = ""
    if request.method == "POST":
        prompt = request.form["prompt"]
        response = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=150)
        content = response.choices[0].text.strip()
    return render_template("index.html", content=content)

if __name__ == "__main__":
    app.run(debug=True)
