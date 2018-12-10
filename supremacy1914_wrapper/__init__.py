
"""
# Supremacy 1914 API Wrapper

This unofficial API wrapper is an implementation of the Supremacy 1914 API.
This wrapper support API data as far as known and is intended to be easy
to use. You'll only need to supply the server URL and the game_id before
you'll be able to get data.
"""

from .wrapper import Supremacy, ServerChangeError, GameDoesNotExistError
