#!/usr/bin/python
"""
Couchbase first script.
"""

from couchbase import Couchbase
client = Couchbase.connect(host='127.0.0.1', bucket='default')

# Store a document
rv = client.set('first', {'hello': 'world'})
cas = rv.cas
print rv

# Get the document
item = client.get('first')
print "item: %s" % item
print "key: %s" % item.key
print "value: %s" % item.value

# Delete the document only if the CAS value matches (it would also
# work without a cas value)
client.delete('first', cas=rv.cas)
