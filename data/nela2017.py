"""
This module contains data representations for the Nela2017 data set and
its constituent articles. Since the dataset is pretty large, only individual
article objects will be loaded upon indexing, and the dataset will largely
serve as an entry point for accessing these articles

The larger dataset can be sorted and filtered by date, organization
Returns a generator

"""
from collections.abc import Sequence
from .article import Article

# TODO implement Nela2017
class Nela2017(Sequence):
    def __init__(self, root: str):
        """
        Dataset for accessing lazily accessing documents, List-Like
        elements are Article instances
        Contains methods for filtering the dataset by organization, article date
        """


    def __getitem__(self, item):
        # TODO implement __getitem__

        pass

    def __len__(self):  ...


    




