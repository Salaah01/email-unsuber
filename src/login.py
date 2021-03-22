import os
import re
import json
import email
from email.header import decode_header
import imaplib
import webbrowser

try:
    from creds import email, password
except ImportError:
    email = input('email')
    password = input('password')


class Login:
    def __init__(self, email=email, password=password):
        self.email = email
        self.password = password

        self._domain = self._set_domain()
        self._mailServer = self._set_mail_server()

        self._imap = None

    def login(self):
        """Creates an IMAP class with SSL, logins in the user and returns the
        IMAP instance.
        """
        return getattr(self, self.get_mail_server()['method'])()

    def logout(self):
        """Logs out the user."""
        if self._imap:
            self._imap.logout()

    def _set_domain(self):
        """Fetches the domain from the user"""
        return self.email.split('@')[1].split('.')[0]

    def _set_mail_server(self):
        """Returns the mailing server settings for the user's domain."""
        with open('mail_servers.json', 'r') as jsonFile:
            mailServers = json.load(jsonFile)

        for mailServer in mailServers.keys():
            if re.search(mailServer, self.get_domain()):
                return mailServers[mailServer]

    def get_domain(self):
        """Returns the user's email domain."""
        return self._domain

    def get_mail_server(self):
        """Returns the mailing server settings."""
        return self._mailServer

    def get_imap(self):
        """Returns the imap connection."""
        return self._imap

    def _generic(self):
        """A generic login method."""
        self._imap = imaplib.IMAP4_SSL(self.get_mail_server()['server'])
        self._imap.login(self.email, self.password)


if __name__ == '__main__':
    login = Login()
    login.login()
