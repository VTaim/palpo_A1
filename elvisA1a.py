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
result = g.parse("http://data.linked-open-science.org/semantic-dogfood/eswc-2013-complete.rdf", format='application/rdf+xml')

#print everything
print("Found total %s resources, namely:"%len(r))
for n in r: print localish(n),
print
