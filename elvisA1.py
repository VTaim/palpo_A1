from rdflib import Graph, URIRef, Literal

g = Graph()
result = g.parse("http://www.snee.com/rdf/elvisimp.rdf")

print ("graph has %s statements." % len(g))

