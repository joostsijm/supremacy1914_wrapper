
"""
Supremacy 1914 API wrapper.

This unofficial API wrapper is a implementation of the supremacy 1914 API as
far as known. This wrapper is inteded to be easy to use. You'll only need to
supply the server url and the gameID before you'll be able to get data.
"""

from .wrapper import Supremacy, ServerChangeError, GameDoesNotExistError

name = "python_supremacy1914"
