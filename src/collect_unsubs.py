import re
from datetime import datetime
import email
from login import Login
from output_dict import OutputDict
from etaprogress.progress import ProgressBar


class CollectUnsubs:
    def __init__(self, filetype: str):
        if not OutputDict.valdidate_filetype(filetype):
            raise ValueError(
                'Invalid filetype. Valid outputs: json, csv, xlsx'
            )
        self.filetype = filetype
        self._imap = self._set_imap()
        self._links = {}

    def fetch_unsub_links(self):
        """Fetches the unsubscribe links."""

        imap = self.get_imap()
        imap.select('INBOX')

        _, messageNumbersRaw = imap.search(None, 'ALL')

        messageNumbers = messageNumbersRaw[0].split()
        progressBar = ProgressBar(len(messageNumbers))
        startTime = datetime.now()
        print(f"({startTime.strftime('%H:%M:%S')}) Parsing emails... Start")

        for messageNumber in messageNumbers:
            _, msg = imap.fetch(messageNumber, '(RFC822)')

            # Parse the email.
            if msg and msg[0]:
                message = email.message_from_bytes(msg[0][1])
            else:
                continue

            emailFrom = self.extract_email(message['from'])

            # If sender's email could not be found or the sender email is
            # already stored, then move on.
            if not emailFrom or email in self.get_links():
                continue

            if message.is_multipart():
                for part in message.walk():
                    multipartPayload = message.get_payload()
                    for subMessage in multipartPayload:
                        try:
                            link = self.extract_unsub_link(
                                subMessage.get_payload(decode=True).decode()
                            )

                            if link:
                                self.add_link(emailFrom, link)

                        except (UnicodeDecodeError, AttributeError):
                            pass
            else:
                # message.get_payload(decode=True).decode()
                pass

            progressBar.numerator = int(messageNumber)
            print(progressBar, end='\r')

        endTime = datetime.now()
        duration = str(endTime - startTime).split('.')[0]
        print(f"({endTime.strftime('%H:%M:%S')}) Parsing emails... Done")
        print(f"({datetime.now().strftime('%H:%M:%S')}) Duration: {duration}")

    def output(self):
        OutputDict(self.get_links(), self.filetype).write_output()

    @staticmethod
    def extract_email(text: str):
        """Parses a block of text and parses the fist email found."""
        pattern = re.compile(
            '(([^<>()[\]\.,;:\s@\"]+(\.[^<>()[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})'
        )
        try:
            email = re.search(pattern, text)
            if email:
                return email[0]
            else:
                return None
        except TypeError:
            return None

    @staticmethod
    def extract_unsub_link(text: str) -> list:
        pattern = re.compile('href=[\'"](http.*?unsubscribe.*?)[\\\'";]')
        try:
            match = re.search(pattern, text)
        except TypeError:
            pass

        return match.groups()[0] if match else []

    @staticmethod
    def _set_imap():
        login = Login()
        login.login()
        return login.get_imap()

    def get_imap(self):
        return self._imap

    def add_link(self, emailFrom, unsubLink):
        self._links[emailFrom] = unsubLink

    def get_links(self):
        return self._links


if __name__ == '__main__':
    unsubs = CollectUnsubs('xlsx')
    unsubs.fetch_unsub_links()
    unsubs.output()
