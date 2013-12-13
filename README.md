paper-browser
=============

`paper-browser` is an attempt by me to learn web scripting in Python using the Flask microframework. It aims at creating a web-app to fully manage and view research papers on a machine.

In order to run this app, the following are required:
* Python 2.6 or above
* The Flask microframework
* A modern web browser (Chrome is recommended)

Implemented Features:
* Adding a paper (pdf/ps/etc files) to `paper-browser` by file upload, including metadata:
  * Title of paper
  * Authors
  * Year of publication
  * Keywords
  * Some notes for the user's personal reference
  * Indication of whether the paper is "important" (depending on your definition of "important")
* Categorization of papers by directory
* Viewing of papers in browser, including very (!) rudimentary directory navigation

Pending features:
* Search of papers by title or metadata
* Deletion of papers
* UI enhancement using CSS

Information about flask can be on the [flask website](http://flask.pocoo.org/).
