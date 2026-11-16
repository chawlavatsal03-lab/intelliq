
import pandas as pd
import numpy as np
import requests
import pytest
from dotenv import load_dotenv


def test_pandas():
    assert pd.__version__ is not None


def test_numpy():
    assert np.__version__ is not None


def test_requests():
    assert requests.__version__ is not None


def test_python_dotenv():
    assert callable(load_dotenv)
