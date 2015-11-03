""" RDFLib examples: SPARQL query (SELECT)

ON 2015
"""

import rdflib

g = rdflib.Graph(); 
g.parse("calvin.ttl",format="turtle")

# Find literals that include the substring "in"

qres = g.query(
  """
  PREFIX : <http://www.tut.fi/example.org/fi-tut-math-sm-calvin-and-hobbes/>
  SELECT ?o
  WHERE {
    ?s ?p ?o .
    FILTER isLiteral(?o)
    FILTER regex(?o, "in", "i")
  }""")

for row in qres: print(row)
