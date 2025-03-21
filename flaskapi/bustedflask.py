#!/usr/bin/python3

from flask import Flask, request, redirect, url_for

app = Flask(__name__)

### NOTE FROM CHAD: There is nothing wrong with the HTML
html= '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Trivia Time</title>
    <style>
        body {
            background-color: black;
            text-align: center;
            color: white;
            font-family: Arial, Helvetica, sans-serif;
        }
    </style>
</head>
<body>

    <h1>TRIVIA TIME</h1>
    <p>What is the meaning of life, the universe, and everything?</p>
    <img src="https://stevetobak.com/wp-content/uploads/2021/02/dont-panic.png" alt="Avatar" style="width:200px">

    <form action="/login" method="POST">
        <p><input type="text" name="nm"></p>
        <p><input type="submit" value="submit"></p>
    </form>

</body>
</html>'''

@app.route("/ok")
def success():
    return f"That is correct!"

@app.route("/")
def start():
    return html

@app.route("/login", methods = ["POST"])
def login():
        if request.form.get("nm"):
            answer = request.form.get("nm")
            if answer == "42":
                return redirect(url_for("success"))
            else:
                return redirect("/")
        else:
            return redirect("/")

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224)
