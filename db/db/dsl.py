# coding: utf-8

"""
Domain specific language for db quepy.
"""
from quepy.dsl import FixedRelation

class IsDefinedIn(FixedRelation):
    relation = "rdfs:comment"
    reverse = True
