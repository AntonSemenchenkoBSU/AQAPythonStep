import pytest

from CalcEngine import CalcEngine


# DDT = Data Driven Testing
# a, b, expected_result
# 10, 12, 22
# 10, 12, -2
class TestCalcEngine:
    def test_add(self):
        calc_engine = CalcEngine()
        a = 10
        b = 12
        expected_result = 22
        result = calc_engine.add(a, b)
        assert result == expected_result

    def test_sub(self):
        calc_engine = CalcEngine()
        a = 10
        b = 12
        expected_result = -2
        result = calc_engine.sub(a, b)
        assert result == expected_result

    def test_mul(self):
        calc_engine = CalcEngine()
        a = 10
        b = 12
        expected_result = 120
        result = calc_engine.mul(a, b)
        assert result == expected_result

    def test_div(self):
        calc_engine = CalcEngine()
        a = 100
        b = 10
        expected_result = 10
        result = calc_engine.div(a, b)
        assert result == expected_result

    def test_div_by_zero(self):
        calc_engine = CalcEngine()
        a = 100
        b = 0
        #SystemExit
        with pytest.raises(ZeroDivisionError):
            result = calc_engine.div(a, b)




