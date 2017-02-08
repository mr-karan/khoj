# coding: utf-8

"""
Main script for db quepy.
"""

import quepy
db = quepy.install("db")
target, query, metadata = db.get_query("what is a blowtorch?")
print query
