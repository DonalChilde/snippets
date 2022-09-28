"""
Created on Nov 4, 2017

@author: croaker
"""
import collections
import logging

# setting up logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# TODO read this article, https://realpython.com/python-filter-function/
class ContentFilter(object):
    """Accepts a single filter or a collection of filters"""

    def __init__(self, filters=None):
        self._filters = list()
        if filters is not None:
            if isinstance(filters, collections.Iterable):
                for item in filters:
                    if hasattr(item, "filter"):
                        self._filters.append(item)
            else:
                if hasattr(filters, "filter"):
                    self._filters.append(filters)

    def filter(self, content):
        if not self._filters:
            logging.info("Filter has no actions")
        for f in self._filters:
            content = f.filter(content)
        return content


class FilterRecentMarketHistory(object):
    def __init__(self, dateLimit):
        self.dateLimit = dateLimit

    def filter(self, content):
        filteredContent = list()
        for item in content:
            if "date" in item:
                if item["date"] >= self.dateLimit:
                    filteredContent.append(item)
        return filteredContent
