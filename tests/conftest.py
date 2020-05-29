"""test configuration"""

import os

import pytest
from dotenv import load_dotenv

from supremacy1914_wrapper import Supremacy


load_dotenv()

@pytest.fixture(scope='module')
def vcr_cassette_dir():
    """Change cassette location"""
    test_game_id = os.environ.get('TEST_GAME_ID', None)
    return os.path.join('tests/cassettes', test_game_id)

@pytest.fixture(scope="module")
def supremacy():
    """Set up wrapper before test"""
    test_game_id = os.environ.get('TEST_GAME_ID', None)
    test_game_url = os.environ.get('TEST_GAME_URL', None)
    return Supremacy(test_game_id, test_game_url)
