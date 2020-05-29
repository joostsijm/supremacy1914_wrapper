"""Supremacy test"""

import os

import pytest
from dotenv import load_dotenv


@pytest.mark.vcr()
def test_supremacy_score(supremacy):
    """Test an API call to get score"""
    result = supremacy.score(1)

    assert isinstance(result, dict), "Result should be a dict" 
    assert isinstance(result["ranking"], dict), "ranking should bea dict"
    assert isinstance(result["ranking"]["ranking"], list), "ranking hould be a lit"

@pytest.mark.vcr()
def test_supremacy_players(supremacy):
    """Test an API call to get players"""
    result = supremacy.players()

    assert isinstance(result, dict), "Result should be a dict" 
    assert isinstance(result["players"], dict), "players should be a dict" 

@pytest.mark.vcr()
def test_supremacy_market(supremacy):
    """Test an API call to get market"""
    result = supremacy.market()

    assert isinstance(result, dict), "Result should be a dict" 
    assert isinstance(result["asks"], list), "asks should be a dict" 
    assert isinstance(result["bids"], list), "bids should be a dict" 
    assert isinstance(result["prices"], list), "price should be a dict" 

@pytest.mark.vcr()
def test_supremacy_coalitions(supremacy):
    """Test an API call to get coalitions"""
    result = supremacy.coalitions()

    if result:
        assert isinstance(result, dict), "Result should be a dict" 

@pytest.mark.vcr()
def test_supremacy_relations(supremacy):
    """Test an API call to get relations"""
    result = supremacy.relations()

    assert isinstance(result, dict), "Result should be a dict"
    assert isinstance(result["relations"], dict), "relations should be a dict"
    assert isinstance(result["relations"]["neighborRelations"], dict), \
        "neighborRelations should be a dict"

