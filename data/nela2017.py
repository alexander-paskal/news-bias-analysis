"""
This module contains data representations for the Nela2017 data set and
its constituent articles. Since the dataset is pretty large, only individual
article objects will be loaded upon indexing, and the dataset will largely
serve as an entry point for accessing these articles

The larger dataset can be sorted and filtered by date, organization
Returns a generator


Expects the file structure for the data to be as follows:

root/
    _all_features_NELA2017dataset.csv
    articles/
        [month_dir]/
            [date_dir]/
                [organization]/
                    [article_id].txt

month_dir looks like "1_April", "2_May", ..., "7_October"
date_dir looks like "2017-04-01"
organization looks like "FOX NEWS", "CNN", etc.
article_id looks like "[organization]--[date]--[title]
"""
import os
import calendar
import copy
import datetime as dt
from data.article import Article


class Nela2017:
    _articles_dirname = "articles"

    def __init__(self, root: str):
        """
        Dataset for lazily accessing articles, iterable
        elements are Article instances
        Contains methods for filtering the dataset by organization, article date
        """
        self._root = root
        self._start_date = dt.date(2017, 4, 1)
        self._end_date = dt.date(2017, 10, 31)
        self._organizations = set()

    def __iter__(self):
        self._iter = self._article_paths()
        return self

    def _article_paths(self):
        """
        Generator yielding all article paths in the current dataset
        :return:
        :rtype:
        """
        for date in self._date_range:
            monthdir, daydir = self._datedir(date)

            if len(self._organizations) == 0:
                orgs = os.listdir(self._path(monthdir, daydir))
            else:
                orgs = self._organizations

            for org in orgs:
                dirpath = self._path(monthdir, daydir, org)
                try:
                    for path in os.listdir(dirpath):
                        yield self._path(monthdir, daydir, org, path)

                except FileNotFoundError:
                    continue

    def __next__(self):
        try:
            path = next(self._iter)
            return self._article(path)
        except StopIteration:
            raise StopIteration

    def __len__(self):
        dataset = copy.deepcopy(self)
        dataset.__iter__()
        return len(list(self._iter))

    def _article(self, path):
        path = os.path.normpath(path)
        *_, datedir, orgdir, fname = path.split(os.sep)
        id = os.path.splitext(fname)[0]
        title = id.split("--")[2]
        date = dt.datetime.strptime(datedir, "%Y-%m-%d").date()

        a = Article(
            id=id,
            path=path,
            org=orgdir,
            date=date,
            title=title
        )
        return a

    def _path(self, *subdirs):
        dirs = [self._root, self._articles_dirname]
        dirs.extend(subdirs)
        return os.path.join(*dirs)

    def _datedir(self, date):
        month_name = calendar.month_name[date.month]
        monthdir = f"{date.month - 3}_{month_name}"
        daydir = date.strftime("%Y-%m-%d")
        return monthdir, daydir

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        assert isinstance(value, dt.date)  # datetime is a subclass of date
        if isinstance(value, dt.datetime):
            value = value.date()
        assert dt.date(2017, 4, 1) <= value <= dt.date(2017, 10, 31)
        self._start_date = value

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        assert isinstance(value, dt.date)  # datetime is a subclass of date
        if isinstance(value, dt.datetime):
            value = value.date()
        assert dt.date(2017, 4, 1) <= value <= dt.date(2017, 10, 31)

        self._end_date = value

    def dates(self, start, end):
        assert isinstance(start, dt.date)
        assert isinstance(end, dt.date)

        if isinstance(start, dt.datetime):
            start = start.date()
        if isinstance(end, dt.datetime):
            end = end.date()
        assert dt.date(2017, 4, 1) <= start <= end <= dt.date(2017, 10, 31)

        self._start_date = start
        self._end_date = end

    def organizations(self, *args):
        for arg in args:
            assert isinstance(arg, str)

        self._organizations = set(args)

    @property
    def _date_range(self):
        start_date = self._start_date
        end_date = self._end_date
        delta = dt.timedelta(days=1)

        while start_date <= end_date:
            yield start_date
            start_date += delta


