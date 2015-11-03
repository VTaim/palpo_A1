"""Simple SPARQL (1.1) query processor (or a wrapper of)

This is only for learning simple sparql, i.e. playing with simple semantic 
models. If you need a real tool, please consider using, e.g., Pellet instead.
(You might also get easier to understand error messages from real tools.)

Synopsis: python sparql.py data_file query_file [-localish]

Example: python sparql.py calvin.ttl basic-select.rq 

The switch localish prints only (# or / and) local names (ignores IRI suffix).

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

qres = g.query(qs)

localishSw = False
if len(sys.argv)>=4 and sys.argv[3] == "-localish": 
  localishSw = True
  
for row in qres: 
  for e in row: 
    if localishSw: print(localish(e)),
    else: 
      print(e),
  print

g.close()
