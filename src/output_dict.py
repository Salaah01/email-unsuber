"""Handle method for writting a dictionary to differnet file types."""

import os
from datetime import datetime
import json
import csv
import pandas


class OutputDict:
    def __init__(self, data: dict, outDir: str, filetype: dict):
        """Handle method for writting a dictionary to differnet file types.
        
        Args:
            data - (dict) Data to output.
            outDir - (str) Path to the output file directory.
            filetype - (str) Output filetype.
        """
        
        self.data = data
        self.outDir = outDir
        self.filetype = filetype

    def write_output(self):
        """Outputs the data in the desired file format to the predefined
        directory.
        """ 
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
        """Outputs the python dict as json."""
        with open(self._output_file('json'), 'w') as jsonFile:
            jsonFile.write(json.dumps(self.data))

    def _csv(self):
        """Outputs the python dict as csv."""
        with open(self._output_file('csv'), 'w') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerows([[email, link] for email, link
                             in self.data.items()])

    def _xlsx(self):
        """Outputs the python dict as xlsx."""
        pandas.DataFrame(data=self.data, index=[0]).transpose()[1:].to_excel(
            self._output_file('xlsx'),
            header=False
        )
