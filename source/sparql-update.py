"""Simple SPARQL (1.1) UPDATE query processor (or a wrapper of)

Perfoms SPARQL update and prints the resulting graph in N3 (or Turtle).

Synopsis: python sparql.py data_file query_file [-localish]

Example: python sparql.py calvin.ttl insert-data.rq 

You might wish to merge this with the the simple sparql.py utility (and 
add store support while at it).

...or even better, migrate into using a real SPARQL processor.

ON 2015
"""

import rdflib
import sys

def localish(s): 
  """Return the (almost) local name part of a URI, 
  e.g., http:///www.ex.org/foo -> /foo
  
  Gives bad results for literals that start with http://...
  """
  if s is None or not s.startswith("http://"): return s
  
  a = s.rfind('/'); b = s.rfind('#'); 
  if a==-1 and b==-1: return s 
  return s[max(a,b):]
  
if len(sys.argv)<3:
  print "Simple SPARQL query processor"
  print "Synopsis: python sparql.py data_file query_file [-localish]"
  print "(Premature exit because one or more input arguments is missing.)"
  sys.exit(0)

g = rdflib.Graph(); 

dfile = sys.argv[1]
if dfile.endswith(".ttl"): # Make sure (at least) Turtle is recognized...
  g.parse(dfile,format="turtle") 
else:  
  g.parse(dfile,rdflib.util.guess_format(dfile))

f = open(sys.argv[2], 'r')  # Now assume a simple ASCII file is used ... ;-)
qs = f.read()
f.close()

g.update(qs)

g2 = rdflib.Graph()
for row in g:
  g2.add(row)
print(g2.serialize(format="n3"))

g.close()
