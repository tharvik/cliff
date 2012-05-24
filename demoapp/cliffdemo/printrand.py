import logging
import random

from cliff.create import CreateOne


class Random(CreateOne):
    "Print a random number"

    log = logging.getLogger(__name__)

    def create(self, parsed_args):
        return random.random()

    def get_display_values(self, parsed_args, created_obj):
        return (('Random',), (created_obj,))
