# coding: utf-8

"""
Main script for db quepy.
"""

import quepy
db = quepy.install("db")

question = raw_input("Type your query: ")
print(question)
target, query, metadata = db.get_query(str(question))
print query
