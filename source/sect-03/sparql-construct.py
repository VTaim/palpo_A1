""" RDFLib examples: SPARQL query (CONSTRUCT)

ON 2015
"""

import rdflib

g = rdflib.Graph(); 
g.parse("calvin.ttl",format="turtle")

# Find statements that include literals with the substring "in"

qres = g.query(
  """
  PREFIX : <http://www.tut.fi/example.org/fi-tut-math-sm-calvin-and-hobbes/>
  CONSTRUCT { ?s ?p ?o }
  WHERE {
    ?s ?p ?o .
    FILTER isLiteral(?o)
    FILTER regex(?o, "in", "i")
  }""")

g2 = rdflib.Graph()
for row in qres: 
  g2.add(row) # now works because the row makes a well-formed triple
print(g2.serialize(format="n3"))