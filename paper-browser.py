from flask import Flask, render_template, request, redirect, url_for
from db import get_papers, get_cats, add_paper
import time
import os.path

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

@app.route("/add", methods=["GET", "POST"])
def add():
    """ Enables adding of a paper
    On method GET, Displays form to add paper
    On method POST, Attempts to add paper
    If no errors, redirects to index
    Else shows error page
    """
    cat_list = sorted(get_cats())

    if request.method == "POST":

        title = request.form["title"]
        # print title
        if is_empty(title):
            error = "Error: Title should be specified"
            return render_template("add.html", cats=cat_list, title="Add Paper", error=error)

        authors = request.form["authors"]
        author_list = comma_list(authors)
        # print author_list
        if is_empty(author_list):
            error = "Error: Authors should be specified"
            return render_template("add.html", cats=cat_list, title="Add Paper", error=error)

        year = request.form["year"]
        # print year
        if (not is_empty(year)) and (not year.isdigit()):
            error = "Error: Year should be numeric"
            return render_template("add.html", cats=cat_list, title="Add Paper", error=error)

        category = request.form["cat_sel"] if request.form["cat_sel"] != "_other" else request.form["cat_text"]
        category = category if category.startswith("/") else ("/" + category)
        # print category

        keywords = request.form["keywords"]
        keyword_list = comma_list(keywords)
        # print keyword_list

        notes = request.form["notes"]
        # print notes

        important = 1 if "important" in request.form else 0

        upfile = request.files["file"]
        if is_empty(upfile.filename):
            error = "Error: Specify a file to upload"
            return render_template("add.html", cats=cat_list, title="Add Paper", error=error)

        filename = "{0}{1}".format(time.time(), os.path.splitext(upfile.filename)[1])
        filepath = "{0}/{1}".format(get_papers_path(), filename)
        upfile.save(filepath)

        # Now actually add paper
        paper = [title, author_list, year, category, keyword_list, filename, notes, important]
        add_paper(paper)

        return redirect(url_for("index"))

    else:
        return render_template("add.html", cats=cat_list, title="Add Paper")

##############################
# Utility functions

def is_empty(string):
    return string == ""

def comma_list(string):
    """ Accepts a comma-separated string which may contain several embedded spaces, and converts it to a standard comma-separated string
    """
    return ",".join([s.strip() for s in string.split(",")])

def get_papers_path():
    currpath = os.path.dirname(os.path.realpath(__file__))
    return currpath + "/static/papers"

if __name__ == "__main__":
    app.run(debug=True)
