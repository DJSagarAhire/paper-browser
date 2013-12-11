import sqlite3

def get_papers(cat="_all"):
    """ Returns a list of dicts for all papers in database
    """

    conn = sqlite3.connect("data/paper-browser.db")
    cur = conn.cursor()

    if cat != "_all":
        cur.execute("select * from papers where category = ?", [cat])
    else:
        cur.execute("select * from papers")

    paper_list = []

    for row in cur:
        paper_dict = {}
        paper_dict["paperid"] = row[0]
        paper_dict["title"] = row[1]
        paper_dict["authors"] = get_list(row[2])
        paper_dict["year"] = row[3]
        paper_dict["category"] = row[4]
        paper_dict["keywords"] = get_list(row[5])
        paper_dict["path"] = row[6]

        paper_list.append(paper_dict)

    return paper_list

def get_cats():
    """ Returns a list of all categories in database
    """

    conn = sqlite3.connect("data/paper-browser.db")
    cur = conn.cursor()

    cur.execute("select distinct category from papers")
    cat_list = [row[0] for row in cur]

    return cat_list

def get_list(string):
    """ Accepts a string having comma-separated values and returns a list of those values
    """
    return [val.strip() for val in string.split(",")]
