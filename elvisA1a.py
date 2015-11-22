import rdflib
import logging
from rdflib import RDF, Graph, URIRef
from rdflib.parser import Parser

# In order to get error messages straight from rdflib...
logging.basicConfig()

# Creating the graph with parser
g = rdflib.Graph()
g.open("store", create=True)
result = g.parse("http://data.linked-open-science.org/semantic-dogfood/eswc-2013-complete.rdf", format='application/rdf+xml')

# print out all the triples in the graph, A1a
for subject, predicate, object in g:
    print subject, predicate, object
