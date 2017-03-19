#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import logging
import webapp2

from channel.views import CreateHandler
from channel.models import Channel
from util import email

class MainHandler(webapp2.RequestHandler):
  def get(self):
    self.response.write('OK')


class NotifyHandler(webapp2.RequestHandler):
  def get(self):
    self.response.write('OK')

  def post(self):
    channel = self.request.get('channel')
    headline = self.request.get('headline')
    details = self.request.get('details', '')

    requested_channel = Channel.query(Channel.name == channel).get()

    if not headline or not requested_channel:
      logging.error('Missing headline or channel not found')
      self.error(500)
      return

    email.notify(requested_channel, headline, details)


app = webapp2.WSGIApplication([
  ('/', MainHandler),
  ('/api/notify', NotifyHandler),
  ('/channel/create', CreateHandler)
], debug=True)
