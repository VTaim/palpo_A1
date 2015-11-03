"""Working with persistent graph stores with SQLAlchemy: Add statement

Note that you might have to install rdflib-sqlalchemy: see
https://github.com/RDFLib/rdflib-sqlalchemy

ON 2015
"""

from rdflib import plugin, Graph, Namespace, BNode, Literal
from rdflib.namespace import FOAF
from rdflib.store import Store
import datetime

store = plugin.get("SQLAlchemy", Store)('rdfstore')
g = Graph(store, identifier="Graph1")
g.open("sqlite:///calvindb")

# Add some data...
n1 = Namespace("http://www.tut.fi/example.org/fi-tut-math-sm-calvin-and-hobbes/")
nt = (n1.Calvin, n1.updated, \
  Literal(datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')))
g.add(nt)

print "The store now includes:"
print(g.serialize(format="n3"))

g.close()
