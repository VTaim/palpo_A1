"""Working with persistent graph stores with SQLAlchemy: Create db

Basically, this means storing RDF models into a database.

Note that you might have to install rdflib-sqlalchemy: see
https://github.com/RDFLib/rdflib-sqlalchemy

ON 2015
"""

from rdflib import plugin, Graph, Namespace
from rdflib.namespace import FOAF
from rdflib.store import Store

store = plugin.get("SQLAlchemy", Store)('rdfstore')

g = Graph(store, identifier="Graph1")
g.open("sqlite:///calvindb", create=True)

# Add some intial data...
n1 = Namespace("http://www.tut.fi/example.org/fi-tut-math-sm-calvin-and-hobbes/")
nt = (n1.Calvin, FOAF.knows, n1.Hobbes)
g.add(nt)

g.close()

