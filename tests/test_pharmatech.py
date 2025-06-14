"""Test suite for the pharmatech package."""
import pytest
from pharmatech import __version__

def test_version():
    """Test version is a string."""
    assert isinstance(__version__, str)
