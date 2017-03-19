'Servive for sending email'
from google.appengine.api import mail
from google.appengine.api.app_identity import get_application_id

def notify(channel, subject, body):
  app_name = get_application_id()
  sender = '%s@%s.appspotmail.com' % (channel.name, app_name)
  mail.send_mail(sender=sender, to=channel.recipient, subject=subject, body=body)
