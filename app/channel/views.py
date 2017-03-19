import jinja2
import logging
import os
import webapp2

from channel.models import Channel

SHARED_TEMPLATES = os.path.dirname(os.path.dirname(__file__))
APP_TEMPLATES = os.path.dirname(__file__)
TEMPLATES = [SHARED_TEMPLATES, APP_TEMPLATES]

JINJA_ENVIRONMENT = jinja2.Environment(
  loader=jinja2.FileSystemLoader(TEMPLATES),
  extensions=['jinja2.ext.autoescape'],
  autoescape=True
)

class CreateHandler(webapp2.RequestHandler):
  def get(self):
    template = JINJA_ENVIRONMENT.get_template('create.html')
    self.response.write(template.render({}))

  def post(self):
    channel = self.request.get('channel')
    recipient = self.request.get('recipient')

    variables = {}
    if not channel:
      variables = {'error': 'Channel Name is required'}

    elif not recipient:
      variables = {'error': 'Recipient is required'}

    else:
      existing_channel = Channel.query(Channel.name == channel).get()

      if existing_channel:
        variables = {'error': 'Channel already exists'}

      else:
        # Create channel and success message
        new_channel = Channel(name=channel, recipient=recipient)
        new_channel.put()
        variables = {'success': 'Channel added!'}

    template = JINJA_ENVIRONMENT.get_template('create.html')
    self.response.write(template.render(variables))
