import sqlite3
import os

def get_papers(cat="_all"):
    """ Returns a list of dicts for all papers in database
    """

    conn = sqlite3.connect(get_db_path())
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
        paper_dict["notes"] = row[7]

        paper_list.append(paper_dict)

    return paper_list

def add_paper(paper):
    """ Accepts a paper as a list and adds it to the database
    """

    conn = sqlite3.connect(get_db_path())
    cur = conn.cursor()

    cur.execute("""insert into papers (title, authors, year, category, keywords, path, notes, important)
values (?, ?, ?, ?, ?, ?, ?, ?)""", paper)

    conn.commit()
    conn.close()

def del_paper(paperid):
    """ Removes paper with specified paperid from database
    Also returns path to file containing the paper
    """

    conn = sqlite3.connect(get_db_path())
    cur = conn.cursor()

    cur.execute("select path from papers where paper_id = ?", [paperid])
    path = cur.fetchone()[0]

    cur.execute("delete from papers where paper_id = ?", [paperid])
    conn.commit()
    conn.close()

    return path

def get_cats():
    """ Returns a list of all categories in database
    """

    conn = sqlite3.connect(get_db_path())
    cur = conn.cursor()

    cur.execute("select distinct category from papers")
    cat_list = [row[0] for row in cur]

    return cat_list

def get_list(string):
    """ Accepts a string having comma-separated values and returns a list of those values
    """
    return [val.strip() for val in string.split(",")]

def get_db_path():
    currpath = os.path.dirname(os.path.realpath(__file__))
    return currpath + "/data/paper-browser.db"
