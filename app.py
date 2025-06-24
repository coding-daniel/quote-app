from flask import Flask, jsonify, render_template_string
import requests

app = Flask(__name__)

TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Random Quote</title>
    <style>
        body { font-family: sans-serif; padding: 2rem; max-width: 600px; margin: auto; }
        blockquote { font-size: 1.5rem; font-style: italic; }
        footer { margin-top: 1rem; text-align: right; font-weight: bold; }
    </style>
</head>
<body>
    <h1>💬 Random Quote</h1>
    <blockquote>{{ quote }}</blockquote>
    <footer>– {{ author }}</footer>
</body>
</html>
'''

@app.route("/")
def home():
    res = requests.get("https://api.quotable.io/random")
    data = res.json()
    return render_template_string(TEMPLATE, quote=data["content"], author=data["author"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
