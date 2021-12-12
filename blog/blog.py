#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask, render_template
import psycopg2
from config import config

app = Flask(__name__)


@app.route("/")
def dump_entries():
    params = config()
    db = psycopg2.connect(**params)
    cursor = db.cursor()
    cursor.execute("select id, date, title, content from entries order by date")
    rows = cursor.fetchall()
    output = ""
    for r in rows:
        #debug(str(dict(r)))
        output += str(r)
        output += "\n"
    return "<pre>" + output + "</pre>"


@app.route("/browse")
def browse():
    params = config()
    db = psycopg2.connect(**params)
    cursor = db.cursor()
    cursor.execute("select id, date, title, content from entries order by date")
    rowlist = cursor.fetchall()
    print(rowlist)
    return render_template("browse.html", entries=rowlist)

if __name__ == "__main__":
    app.run()
