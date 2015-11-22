import rdflib
import logging
from rdflib import RDF, Graph, URIRef
from rdflib.parser import Parser

def localish(s):
  """Return the (almost) local name part of a URI,
  e.g., http:///www.ex.org/foo -> /foo"""
  a = s.rfind('/'); b = s.rfind('#');
  if a==-1 and b==-1: return s
  return s[max(a,b):]

def addIfUnseenRes(r,s):
  """Add s to r if so far unseen and of proper type (URIRef or BNode)"""
  if not (type(s) is rdflib.URIRef or type(s) is rdflib.BNode): return
  if not (s in r): r.append(s)


# In order to get error messages straight from rdflib...
logging.basicConfig()

# Creating the graph with parser
g = rdflib.Graph()
result = g.parse("http://www.snee.com/rdf/elvisimp.rdf", format='application/rdf+xml')

#print everything

for s, p, o in g.triples((None, None, None)):
  g.add((s,p,o))
print(g.serialize(format="application/rdf+xml"))

