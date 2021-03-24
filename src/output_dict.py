import os
from datetime import datetime
import json
import csv
import pandas


class OutputDict:
    def __init__(self, data: dict, outDir: str, filetype: dict):
        self.data = data
        self.outDir = outDir
        self.filetype = filetype

    def write_output(self):
        os.makedirs(self.outDir, exist_ok=True)
        getattr(self, f'_{self.filetype.lower()}')()

    @staticmethod
    def valdidate_filetype(filetype: str):
        """Checks if the filetype is supported."""
        return str(filetype).lower() in ('json', 'csv', 'xlsx')

    def _output_file(self, extension: str):
        """Returns the path to the output file.
        Args:
            extension - (str) File extension.
        """
        return os.path.join(
            self.outDir,
            f'link_{hex(int(datetime.now().timestamp()))}.{extension}'
        )

    def _json(self):
        with open(self._output_file('json'), 'w') as jsonFile:
            jsonFile.write(json.dumps(self.data))

    def _csv(self):
        with open(self._output_file('csv'), 'w') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerows([[email, link] for email, link
                             in self.data.items()])

    def _xlsx(self):
        pandas.DataFrame(data=self.data, index=[0]).transpose()[1:].to_excel(
            self._output_file('xlsx'),
            header=False
        )
