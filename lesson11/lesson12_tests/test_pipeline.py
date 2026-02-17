# lesson12_tests/test_pipeline.py
import sys
import os

# Directorul folderului părinte al lesson11
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(BASE_DIR)

from lesson10 import pipeline
import pytest
@pytest.mark.parametrize(
    "input_list,expected",
    [
        ([1, 2, 3], 56),    # (1*2)^2 + (2*2)^2 + (3*2)^2 = 4 + 16 + 36 = 56
        ([-1, 0, 4], 64),  # (4*2)^2 = 64
        ([], 0)
    ]
)
def test_pipeline(input_list, expected):
    assert pipeline(input_list) == expected
