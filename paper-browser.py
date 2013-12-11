from flask import Flask, render_template, request
from db import get_papers, get_cats

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    """ Serves the index page. Here, the user can:
    1: View lists of papers of a particular directory
    2: Change directory (default "/")
    """

    cat = request.args.get("cat")
    if cat is None:
        papers = get_papers("/")
    else:
        papers = get_papers(cat)

    cat_list = sorted(get_cats())

    return render_template("index.html", title="Viewing Papers", papers=papers, cats=cat_list)

if __name__ == "__main__":
    app.run(debug=True)
