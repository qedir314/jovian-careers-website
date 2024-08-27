from flask import Flask, render_template, url_for, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Software Engineer',
        'location': 'Baku, Azerbaijan',
        'salary': '2000 AZN',
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Baku, Azerbaijan',
        'salary': '3000 AZN',
    },
    {
        'id': 3,
        'title': 'Product Manager',
        'location': 'Ankara, Turkey',
        'salary': '10000 TL'
    },
    {
        'id': 4,
        'title': 'Machine Learning Engineer',
        'location': 'Paris, France',
        'salary': '6000 EURO'
    }
]


@app.route("/")
def hello_world():
    return render_template("home.html",
                           jobs=JOBS,
                           company_name="Jovian")

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
