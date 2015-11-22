# -*- coding: utf-8 -*-
#Also, for each resource, print out the resource types (including the types you perhaps asserted), using a simple text format that can be easily uploaded to a spreadsheet editor (e.g. MS Excel or OO Calc; tip: CSV). Note that the type of each resource should only be printed once. What would be a reasonable type for the LocallyUnknownType and should it be declared? :-) (1 point)


import rdflib
import logging
from rdflib import RDF, Graph, URIRef
from rdflib.parser import Parser

#We use this function to see if certain type is already familiar

def addIfUnseenRes(r,s):
  """Add s to r if so far unseen and of proper type (URIRef or BNode)"""
  if not (type(s) is rdflib.URIRef or type(s) is rdflib.BNode): return
  if not (s in r): r.append(s)

# In order to get error messages straight from rdflib...
logging.basicConfig()

# Creating the graph with parser
g = rdflib.Graph()
result = g.parse("http://data.linked-open-science.org/semantic-dogfood/eswc-2013-complete.rdf", format='application/rdf+xml')

# Create a list of resource types
r = []
for s,p,o in g:
    addIfUnseenRes(r,o)

# Navigate through the triples
for s,p,o in g.triples((None, RDF.type, None)) :
    if (o in r):
        print("%s"%(o))
