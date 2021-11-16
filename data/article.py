"""
A class representing an article. These will be the primary objects used in analysis.
They are responsible for lazy-loading article data in the .text property
"""
from dataclasses import dataclass, asdict
from datetime import date


@dataclass
class Article:
    id: str
    path: str
    title: str = None
    org: str = None
    date: date = None
    _text: str = None

    @property
    def text(self):
        """
        reads and returns the text of an article
        :return:
        :rtype:
        """
        if self._text is None:
            with open(self.path, "r") as f:
                self._text = f.read()

        return self._text
