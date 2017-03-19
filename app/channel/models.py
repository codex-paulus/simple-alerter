'Defines a specific notifier app'
from google.appengine.ext import ndb

class Channel(ndb.Model):
  name = ndb.StringProperty()
  recipient = ndb.StringProperty()
