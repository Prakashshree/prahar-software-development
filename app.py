from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': "Bengluru , India",
        'Salary': 'Rs. 10,00,000'
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': "chennai , India",
        'Salary': 'Rs. 15,50,000'
    },
    {
        'id': 3,
        'title': 'Frontend Engineer',
        'location': "Delhi, India",
        'Salary': 'Rs. 5,00,000'
    },
    {
        'id': 4,
        'title': 'Backend Engineer',
        'location': " lucknow, India",
        'Salary': 'Rs. 8,00,000'
    },
    {
        'id': 5,
        'title': 'Full stack Engineer',
        'location': "Skudai, Singapore",
        'Salary': 'Rs. 13,45,000'
    },
]


@app.route("/")
def hello_world():
    return render_template("great.html", jobs=JOBS, company_name='jovin')


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
