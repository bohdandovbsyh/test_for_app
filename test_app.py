import pytest


@pytest.mark.regression
def test_01():
    assert 1 == 2

@pytest.mark.smoke
def test_02():
    assert 1 == 4
