#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rdflib
import logging
import codecs
from rdflib import RDF, Graph, URIRef, RDFS, Namespace
from rdflib.parser import Parser
from rdflib.serializer import Serializer

# In order to get error messages straight from rdflib...
logging.basicConfig()

# Creating the graph with parser
g = rdflib.Graph()
g.open("store", create=True)
result = g.parse("elvisimp.rdf", format='application/rdf+xml')

for x in set(g.objects(None, rdflib.RDF.RDFNS["type"])): print x
