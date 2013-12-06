paper-browser
=============

`paper-browser` is an attempt by me to learn web scripting in Python using the Flask microframework. It aims at creating a web-app to fully manage and view all the research papers on my machine.

This will include:
* Adding a paper (pdf/ps/etc files) to `paper-browser`, including all its metadata (authors, year of publication, etc)
* Categorizing the papers by area of research (Example: NLP vs. AI vs. Machine Learning, etc)
* Viewing the papers in the browser
* Search of papers by title or metadata
* Deleting (temporarily?) a paper from the app

I aim at storing a paper in the app using a file upload mechanism and an sqlite3 database at the backend for the added information about the paper.

Information about flask can be on the [flask website](http://flask.pocoo.org/).
