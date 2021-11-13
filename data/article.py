"""
A class representing an article. These will be the primary objects used in analysis
"""
from dataclasses import dataclass, asdict
from datetime import datetime


@dataclass(frozen=True)
class Article(str):
    id: str
    text: str
    title: str = None
    org: str = None
    date: datetime = None
