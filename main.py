import pytest

from AccountingEngine import AccountingEngine


# 3A Rule
# A - preps
# A - business Action (only 1)
# A - business Assert (only 1)
#def func(x):
#    return x + 1

#def test_answer():
#    result = func(3)
#    assert result == 5

#def test_another_answer():
#    assert func(4) == 5

#def test_final_answer():
#   assert True

if __name__ == '__main__':
    accounting_engine = AccountingEngine()
    income = 600
    taxes = accounting_engine.calc_se_taxes(income)
    print(taxes)

