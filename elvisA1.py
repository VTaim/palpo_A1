from rdflib import RDF, Graph, URIRef
from rdflib.parser import Parser

g = Graph()
g.open("store", create=True)
result = g.parse("http://www.snee.com/rdf/elvisimp.rdf", format='application/rdf+xml')

# print out all the triples in the graph
for subject, predicate, object in g:
    print subject, predicate, object
