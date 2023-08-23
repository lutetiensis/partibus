"""
High level tests for lemmatize().
"""

import partibus


def test_lemmatize():
    """
    Test lemmatize()
    """
    assert partibus.lemmatize("partibus") is not None
