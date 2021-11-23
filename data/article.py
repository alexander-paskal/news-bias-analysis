"""
A class representing an article. These will be the primary objects used in analysis.
They are responsible for lazy-loading article data in the .text property
"""
from dataclasses import dataclass, asdict
from datetime import date
import json


@dataclass
class Article:
    id: str
    path: str
    org: str = None
    date: date = None
    title: str = None
    _text: str = None
    _author: str = None
    _read: bool = False

    def read_json(self):
        with open(self.path, "r", encoding="utf-8") as f:
            content = json.load(f)
            self._text = content["content"]
            self._author = content["author"]

    @property
    def text(self):
        """
        reads and returns the text of an article
        :return:
        :rtype:
        """
        if self._text is None:
            self.read_json()

        return self._text

    @property
    def author(self):
        if self._author is None:
            self.read_json()

        return self._author

    def serialize(self):
        """
        Returns all "public" attributes in a dictionary
        :return:
        :rtype:
        """
        attrs = asdict(self)
        attrs = {k: v for k, v in attrs.items() if not k.startswith("_")}
        attrs["text"] = self.text
        attrs["author"] = self.author
        return attrs
