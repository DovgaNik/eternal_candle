from flask import Flask

import generate_question

app = Flask(__name__)

@app.route("/gen-question")
def gen_question():
    return generate_question.generate_random_question().to_dict()

if __name__ == "__main__":
    app.run(debug=True)