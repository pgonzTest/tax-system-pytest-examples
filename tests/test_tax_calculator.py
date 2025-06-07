# NOTE: This repository is for unit test practice and demonstration only.

import pytest
from tax_calculator import TaxCalculator, TaxReturn
from tax_bracketter import TaxBracketter
from badbob_adjuster import BadBobAdjuster

# Shared fixture with all test cases
@pytest.fixture
def tax_return_cases():
    return {
        "typical_case": {
            "income": {"salary": 120000},
            "badbobs": {"class1": [200, 300], "class2": [5000, 7000]}
        },
        "min_after_tax_trigger": {
            "income": {"salary": 21000},
            "badbobs": {"class1": [], "class2": []}
        },
        "below_min_after_tax": {
            "income": {"salary": 15000},
            "badbobs": {"class1": [100], "class2": [300]}
        },
        "max_bracket": {
            "income": {"salary": 1000000},
            "badbobs": {"class1": [], "class2": []}
        }
    }

def test_median_income(tax_return_cases):
    case = tax_return_cases["typical_case"]
    tax_return = TaxReturn(case)
    calc = TaxCalculator(TaxBracketter(), BadBobAdjuster())

    tax = calc.get_tax(tax_return)
    assert tax == pytest.approx(26750.00)
    

def test_min_after_tax_income_rule_applied(tax_return_cases):
    case = tax_return_cases["min_after_tax_trigger"]
    tax_return = TaxReturn(case)
    calc = TaxCalculator(TaxBracketter(), BadBobAdjuster())

    tax = calc.get_tax(tax_return)
    assert tax == 0  # no bracket tax, no adjustments, income is above min threshold


def test_below_min_income_means_zero_tax(tax_return_cases):
    case = tax_return_cases["below_min_after_tax"]
    tax_return = TaxReturn(case)
    calc = TaxCalculator(TaxBracketter(), BadBobAdjuster())

    # total_income = 15000 → max allowed tax = 0
    tax = calc.get_tax(tax_return)
    assert tax == 0


def test_max_tax_applies_highest_bracket(tax_return_cases):
    case = tax_return_cases["max_bracket"]
    tax_return = TaxReturn(case)
    calc = TaxCalculator(TaxBracketter(), BadBobAdjuster())

    tax = calc.get_tax(tax_return)
    assert tax == pytest.approx(315500.00)  # as calculated earlier, with no badbobs

