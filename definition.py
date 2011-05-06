"""
	Fetch a definition from wordnet
"""

# Import CherryPy global namespace
import cherrypy
import json
import api
from nltk.corpus import wordnet as wn

class Definition:
    """ Fetch definition from wordnet. """

    def index(self, word = None):
	defs = api.definitions(word)
	return json.dumps(defs)

    index.exposed = True


import os.path
conf = os.path.join(os.path.dirname(__file__), 'definition.conf')

if __name__ == '__main__':
    cherrypy.quickstart(Definition(), config=conf)
else:
    # This branch is for the test suite; you can ignore it.
    cherrypy.tree.mount(HelloWorld(), config=conf)
