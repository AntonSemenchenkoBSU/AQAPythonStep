from AccountingEngine import AccountingEngine


class TestAccountingEngine:
    def test_calc_se_taxes(self):
        accounting_engine = AccountingEngine()
        income = 800
        expected_result = 128
        result = accounting_engine.calc_se_taxes(income)
        assert result == expected_result

    def test_calc_se_taxes_with_zero_income(self):
        accounting_engine = AccountingEngine()
        income = 0
        expected_result = 0
        result = accounting_engine.calc_se_taxes(income)
        assert result == expected_result

    def test_calc_se_taxes_with_huge_income(self):
        accounting_engine = AccountingEngine()
        income = 1000000
        expected_result = 160000
        result = accounting_engine.calc_se_taxes(income)
        assert result == expected_result

    def test_get_se_taxes_percent_from_gov(self):
        expected_result = 16
        se_taxes_percent = AccountingEngine.get_se_taxes_percent_from_gov()
        assert se_taxes_percent == expected_result
