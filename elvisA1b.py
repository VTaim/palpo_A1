# -*- coding: utf-8 -*-
#A1b: The program must then navigate through all the resources (identified by URIs or Blank nodes) in the model. If the type (rdf:type) of the resource is not known, add an asserted statement to the model (in memory) that declares that the type of the resource is LocallyUnknownType (suggest proper URI etc.). (1 point)
#For each statement, check which URIRefs and BNodes appear in each statement. For those resources x (i.e. URIRefs and BNodes) for which there is no asserted statement about their type (i.e. something like (x, rdf:type, y)), add a new statement (x, rdf:type : LocallyUnknownType). How to do this in practice, check section 3 and RDFLib examples in Moodle Lecture Material section, or browse RDFLIb documentation.

import rdflib
import logging
from rdflib import RDF, Graph, URIRef, BNode
from rdflib.parser import Parser

def localish(s):
  """Return the (almost) local name part of a URI, e.g., http:///www.ex.org/foo -> /foo"""
  a = s.rfind('/'); b = s.rfind('#');
  if a==-1 and b==-1: return s
  return s[max(a,b):]

def addIfUnseenRes(r,s):
  """Add s to r if so far unseen and of proper type (URIRef or BNode)"""
  if not (type(s) is rdflib.URIRef or type(s) is rdflib.BNode): return
  if not (s in r): r.append(s)

# In order to get error messages straight from rdflib...
logging.basicConfig()

# Parse the rdf file and add it to graph g
g = rdflib.Graph()
g.parse("elvisimp.rdf", format="application/rdf+xml")

# Create a list of all resources (r)
r = []
for s,p,o in g:
  addIfUnseenRes(r,s)
  addIfUnseenRes(r,p)
  addIfUnseenRes(r,o)

print("Found total %s resources, namely:"%len(r))
for n in r: print localish(n),
print

