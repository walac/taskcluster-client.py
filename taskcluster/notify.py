# coding=utf-8
#####################################################
# THIS FILE IS AUTOMATICALLY GENERATED. DO NOT EDIT #
#####################################################
# noqa: E128,E201
from .client import BaseClient
from .client import createApiClient
from .client import config
from .client import createTemporaryCredentials
from .client import createSession
_defaultConfig = config


class Notify(BaseClient):
    """
    The notification service, typically available at `notify.taskcluster.net`
    listens for tasks with associated notifications and handles requests to
    send emails and post pulse messages.
    """

    classOptions = {
        "baseUrl": "https://notify.taskcluster.net/v1"
    }

    def email(self, *args, **kwargs):
        """
        Send an Email

        Send an email to `address`. The content is markdown and will be rendered
        to HTML, but both the HTML and raw markdown text will be sent in the
        email. If a link is included, it will be rendered to a nice button in the
        HTML version of the email

        This method takes input: ``http://schemas.taskcluster.net/notify/v1/email-request.json``

        This method is ``experimental``
        """

        return self._makeApiCall(self.funcinfo["email"], *args, **kwargs)

    def pulse(self, *args, **kwargs):
        """
        Publish a Pulse Message

        Publish a message on pulse with the given `routingKey`.

        This method takes input: ``http://schemas.taskcluster.net/notify/v1/pulse-request.json``

        This method is ``experimental``
        """

        return self._makeApiCall(self.funcinfo["pulse"], *args, **kwargs)

    def irc(self, *args, **kwargs):
        """
        Post IRC Message

        Post a message on IRC to a specific channel or user, or a specific user
        on a specific channel.

        Success of this API method does not imply the message was successfully
        posted. This API method merely inserts the IRC message into a queue
        that will be processed by a background process.
        This allows us to re-send the message in face of connection issues.

        However, if the user isn't online the message will be dropped without
        error. We maybe improve this behavior in the future. For now just keep
        in mind that IRC is a best-effort service.

        This method takes input: ``http://schemas.taskcluster.net/notify/v1/irc-request.json``

        This method is ``experimental``
        """

        return self._makeApiCall(self.funcinfo["irc"], *args, **kwargs)

    def ping(self, *args, **kwargs):
        """
        Ping Server

        Respond without doing anything.
        This endpoint is used to check that the service is up.

        This method is ``stable``
        """

        return self._makeApiCall(self.funcinfo["ping"], *args, **kwargs)

    funcinfo = {
        "irc": {           'args': [],
            'input': u'http://schemas.taskcluster.net/notify/v1/irc-request.json',
            'method': u'post',
            'name': u'irc',
            'route': u'/irc',
            'stability': u'experimental'},
        "ping": {           'args': [],
            'method': u'get',
            'name': u'ping',
            'route': u'/ping',
            'stability': u'stable'},
        "email": {           'args': [],
            'input': u'http://schemas.taskcluster.net/notify/v1/email-request.json',
            'method': u'post',
            'name': u'email',
            'route': u'/email',
            'stability': u'experimental'},
        "pulse": {           'args': [],
            'input': u'http://schemas.taskcluster.net/notify/v1/pulse-request.json',
            'method': u'post',
            'name': u'pulse',
            'route': u'/pulse',
            'stability': u'experimental'},
    }


__all__ = ['createTemporaryCredentials', 'config', '_defaultConfig', 'createApiClient', 'createSession', u'Notify']
