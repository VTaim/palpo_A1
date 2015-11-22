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

# Navigate through the triples, A1b
for s, p, o in g.triples((None, RDF.type, None)) :
    print "%s %s"%(s,o)
