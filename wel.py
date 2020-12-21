from flask import Flask

app = Flask(__name__)

@app.route('/')  # Fill this in!
def index():
    return "<h1>Go to 'puppy_latin/name' to get the latin name of your puppy!</h1>"

@app.route('/puppy_latin/<name>')  # Fill this in!
def puppy_latin(name):
    x = len(name)
    latin = ""

    if name[x - 1] == 'y':
        latin = name[:-1] + "iful"
    else:
        latin = name + "y"

    return "<h1>Latin: {}</h1>".format(latin)

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)