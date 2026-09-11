from flask import Flask, render_template, request
from mentor import generate_project_plan

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    result = ""

    if request.method == "POST":

        idea = request.form["idea"]

        if idea:
            result = generate_project_plan(idea)

    return render_template(
        "index.html",
        result=result
    )

if __name__ == "__main__":
    app.run()
