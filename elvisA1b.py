# -*- coding: utf-8 -*-
#A1b: The program must then navigate through all the resources (identified by URIs or Blank nodes) in the model. If the type (rdf:type) of the resource is not known, add an asserted statement to the model (in memory) that declares that the type of the resource is LocallyUnknownType (suggest proper URI etc.). (1 point)
#For each statement, check which URIRefs and BNodes appear in each statement. For those resources x (i.e. URIRefs and BNodes) for which there is no asserted statement about their type (i.e. something like (x, rdf:type, y)), add a new statement (x, rdf:type : LocallyUnknownType). How to do this in practice, check section 3 and RDFLib examples in Moodle Lecture Material section, or browse RDFLIb documentation.

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
result = g.parse("http://data.linked-open-science.org/semantic-dogfood/eswc-2013-complete.rdf", format='application/rdf+xml')

# Navigate through the triples, A1b
for s, p, o in g.triples((None, RDF.type, None)) :
    print "%s %s"%(s,o)
