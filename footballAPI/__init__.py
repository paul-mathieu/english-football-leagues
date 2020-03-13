# -*- coding: UTF-8 -*-

"""
    football
    ----------
    Football API for Python

    :copyright: (c) 2020 by [entrez vos pseudos github] paul-mathieu
"""

from .core import *
from .players import Players
from .teams import Teams
from .leagues import Leagues


class FootballAPI(Players, Teams, Leagues):
    def __init__(self, *args):
        Players.__init__(self, *args)
        Teams.__init__(self, *args)
        Leagues.__init__(self, *args)

__copyright__ = "Copyright 2016 by [entrez vos pseudos github] paul-mathieu"
__authors__ = ["paul-mathieu", "[entrez vos pseudos github]"]
__source__ = "https://github.com/paul-mathieu/English-football-leagues-API"
__license__ = "MIT"

__all__ = ["Football", "API",]
