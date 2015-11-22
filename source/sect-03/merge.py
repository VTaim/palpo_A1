"""Merge two graphs, analyze the results.

Note: Perfoming

g1 = Graph()
g1.parse(input1)

g2 = Graph()
g2.parse(input2)

graph = g1 + g2

...is syntactically ok but might *not* give the desired result since it may lead 
into collapsing different blank nodes into one (it is assumed that BNodes are
shred between graphs, i.e. they are part of a bigger collection). 

ON 2015
"""

import rdflib
  
def localish(s): 
  """Return the (almost) local name part of a URI, 
  e.g., http:///www.ex.org/foo -> /foo"""
  a = s.rfind('/'); b = s.rfind('#'); 
  if a==-1 and b==-1: return s 
  return s[max(a,b):]
  
# The simplest & safest way to merge is to parse graph from several files: 
g = rdflib.Graph()
g.parse("part1.ttl",format="turtle")
g.parse("part2.ttl",format="turtle")

n1 = rdflib.Namespace("http://www.tut.fi/example.org/fi-tut-math-sm-calvin-and-hobbes/")

print "This has been asserted about Calvin:"

for p,o in g.predicate_objects(n1.Calvin):
  print "  ",localish(p),localish(o)

print "And in n3:"

g2 = rdflib.Graph()
for s, p, o in g.triples((n1.Calvin, None, None)):
  g2.add((s,p,o))
print(g2.serialize(format="n3"))
