import os
import shutil
import json
import csv
import pandas


class OutputDict:
    def __init__(self, data: dict, filetype: dict):
        self.outputRoot = 'output'
        self.data = data
        self.filetype = filetype

    def write_output(self):
        shutil.rmtree(self.outputRoot, True)
        os.mkdir(self.outputRoot)

        getattr(self, f'_{self.filetype.lower()}')()

    @staticmethod
    def valdidate_filetype(filetype: str):
        """Checks if the filetype is supported."""
        return str(filetype).lower() in ('json', 'csv', 'xlsx')

    def _json(self):
        with open(
            os.path.join(self.outputRoot, 'links.json'),
            'w'
        ) as jsonFile:
            jsonFile.write(json.dumps(self.data))

    def _csv(self):
        with open(
            os.path.join(self.outputRoot, 'links.csv'),
            'w'
        ) as csvFile:
            writer = csv.writer(csvFile)
            writer.writerows([[email, link] for email, link
                             in self.data.items()])

    def _xlsx(self):
        pandas.DataFrame(data=self.data, index=[0]).transpose()[1:].to_excel(
            os.path.join(self.outputRoot, 'links.xlsx'),
            header=False
        )
