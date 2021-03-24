"""Logins the user and returns an object to allow interaction with the email
account.
"""

import re
import json
import imaplib
import traceback
from exit_program import exit_program


class Login:
    def __init__(self, email: str, password: str, debug=False):
        """Logins the user and returns an object to allow interaction with the
        email account.

        Args:
            email - (str) Email address.
            pass - (str) Password
            debug - (bool) Debug mode?
        """
        self.email = email
        self.password = password
        self.debug = debug

        self._domain = self._set_domain()
        self._mailServer = self._set_mail_server()

        self._imap = None

    def login(self):
        """Creates an IMAP class with SSL, logins in the user and returns the
        IMAP instance.
        """
        method = getattr(self, self.get_mail_server()['method'])
        try:
            return method()
        except Exception:
            if self.debug:
                raise Exception(traceback.format_exc())
            else:
                print('Login failed.')
                print('Check that you have used the correct credentials.')
                print(
                    'If credentials are correct, check if you need to create an app password.'
                )
                print('Check documention for more information:')
                print('https://github.com/Salaah01/email-unsuber')
                exit_program()

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
