# NOTE: This repository is for unit test practice and demonstration only.

import pytest
from tax_bracketter import TaxBracketter
from tax_calculator import TaxReturn

@pytest.fixture
def bracket_test_cases():
    return {
        "income_120k": {
            "data": {
                "income": {"salary": 120000},
                "badbobs": {"class1": [], "class2": []}
            },
            "expected_tax": 14500  # 70k @ 15% + 20k @ 20%
        },
        "income_250k": {
            "data": {
                "income": {"salary": 250000},
                "badbobs": {"class1": [], "class2": []}
            },
            "expected_tax": 40500  # 70k @ 15% + 150k @ 20%
        },
        "income_1M": {
            "data": {
                "income": {"salary": 1000000},
                "badbobs": {"class1": [], "class2": []}
            },
            "expected_tax": 315500  # 500k @ 40% + 115.5k from lower tiers
        }
    }


def test_bracket_income_120k(bracket_test_cases):
    case = bracket_test_cases["income_120k"]
    tax_return = TaxReturn(case["data"])
    tax = TaxBracketter().determine_base_tax(tax_return)
    assert tax == case["expected_tax"]


def test_bracket_income_250k(bracket_test_cases):
    case = bracket_test_cases["income_250k"]
    tax_return = TaxReturn(case["data"])
    tax = TaxBracketter().determine_base_tax(tax_return)
    assert tax == case["expected_tax"]


def test_bracket_income_1M(bracket_test_cases):
    case = bracket_test_cases["income_1M"]
    tax_return = TaxReturn(case["data"])
    tax = TaxBracketter().determine_base_tax(tax_return)
    assert tax == case["expected_tax"]
