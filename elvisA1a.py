import rdflib
import logging
from rdflib import RDF, Graph, URIRef
from rdflib.parser import Parser

# Some data has whitespace in URIs, have to fix that (Source: https://github.com/RDFLib/rdflib/issues/412#issuecomment-50247061)

# In order to get error messages straight from rdflib...
logging.basicConfig()

# Creating the graph with parser
g = rdflib.Graph()
g.open("store", create=True)
result = g.parse("elvisimp.rdf", format='application/rdf+xml')

# print out all the triples in the graph, A1a
for subject, predicate, object in g:
    print subject, predicate, object
