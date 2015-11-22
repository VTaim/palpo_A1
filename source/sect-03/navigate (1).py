"""RDFLib navigation example(s).

Create a list of all resources and print their local(ish) names. Print all
that has been asserted about Calvin.

ON 2015
"""

import rdflib

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
  
g = rdflib.Graph()
g.parse("calvin.ttl",format="turtle")

# Add some blank nodes, just for fun (and to see how BNodes are encoded)
n1 = rdflib.Namespace("http://www.tut.fi/example.org/fi-tut-math-sm-calvin-and-hobbes/")
bn = rdflib.BNode()
nt = (n1.Calvin, rdflib.namespace.FOAF.knows, bn)
g.add(nt)

# Create a list of all resources (r)
r = []
for s,p,o in g:
  addIfUnseenRes(r,s)
  addIfUnseenRes(r,p)
  addIfUnseenRes(r,o)

print "Found total %s resources", len(r), "namely:",
for n in r: print localish(n),
print 

print "Btw. This is what we know that has been asserted about Calvin:"

g2 = rdflib.Graph()
for s, p, o in g.triples((n1.Calvin, None, None)):
  g2.add((s,p,o))
print(g2.serialize(format="n3"))
