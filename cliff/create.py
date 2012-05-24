"""Application base class for creating an object and then displaying the results.
"""
import abc
import itertools
import logging

from .display import DisplayCommandBase


LOG = logging.getLogger(__name__)


class CreateOne(DisplayCommandBase):
    """Command base class for creating an object and then displaying its properties.
    """
    __metaclass__ = abc.ABCMeta

    @property
    def formatter_namespace(self):
        return 'cliff.formatter.show'

    @property
    def formatter_default(self):
        return 'table'

    @abc.abstractmethod
    def create(self, parsed_args):
        """Create an object and return some command-defined
        representation of it.
        """

    @abc.abstractmethod
    def get_display_values(self, parsed_args, created_obj):
        """Return a two-part tuple with a tuple of column names
        and a tuple of values.
        """

    def run(self, parsed_args):
        obj = self.create(parsed_args)
        column_names, data = self.get_display_values(parsed_args, obj)
        if not parsed_args.columns:
            columns_to_include = column_names
        else:
            columns_to_include = [c for c in column_names
                                  if c in parsed_args.columns]
            # Set up argument to compress()
            selector = [(c in columns_to_include)
                        for c in column_names]
            data = list(itertools.compress(data, selector))
        formatter = self.formatters[parsed_args.formatter]
        formatter.emit_one(columns_to_include, data, self.app.stdout, parsed_args)
        return 0
