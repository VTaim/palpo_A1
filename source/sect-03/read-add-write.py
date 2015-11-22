# coding=utf-8

""" RDFLib examples: Read graph, add statement(s), write graph.

ON 2015

Notes: 
  * Pay attention to the use of namespaces and local names (e.g. ":Calvin")
  * Once you get the hang of python, you might introduce shorthands for
    RDFLib names, e.g. as from rdflib import Namespace, Graph (etc.)
  * Python 2.x is somewhat notorious from issues with Unicode (you have to
    deal with the codecs etc. by yourself) but works with ASCII like a charm ;-)
  * Instead of reading and writing rdf models as files, you might wish to rely
    on RDF "stores" instead (see the persistence-*.py examples).
"""

import rdflib
import codecs

g = rdflib.Graph(); 
g.parse("calvin.ttl",format="turtle")

# Introduce the example namespace
n1 = rdflib.Namespace("http://www.tut.fi/example.org/fi-tut-math-sm-calvin-and-hobbes/")

# Add new triple (or statement): Calvin knows UncleMax 
nt = (n1.Calvin, rdflib.namespace.FOAF.knows, n1.UncleMax)
g.add(nt)

# Add some literal values (potential source of errors with Unicode...)
nt = (n1.Calvin, rdflib.namespace.RDFS.comment, rdflib.Literal("Tarpeeton lisäys?",\
  lang="fi")) # In Python one can use \ to split long lines
g.add(nt)
nt = (n1.Calvin, rdflib.namespace.RDFS.comment, rdflib.Literal("Unnecessary addition?",\
  lang="en"))
g.add(nt)
nt = (n1.Calvin, rdflib.namespace.FOAF.age, rdflib.Literal("8",\
  datatype=rdflib.namespace.XSD.integer))
g.add(nt)

# Add some blank nodes
bn = rdflib.BNode()
nt = (n1.Calvin, rdflib.namespace.FOAF.knows, bn)
g.add(nt)
nt = (bn, rdflib.namespace.FOAF.knows, n1.Calvin)
g.add(nt)

file = codecs.open("out.ttl", "w", "utf-8")
file.write(g.serialize(format="turtle").decode('utf8'))
file.close()

print "Been there, done that."