import pytest

import long_subseq

def test_case1():
    integers = '6 1 5 9 2'
    expect_result = [1, 5, 9]
    assert expect_result == long_subseq.long_subseq(integers)
