from CalcEngine import CalcEngine


class AccountingEngine:
    def __init__(self):
        self.calc_engine = CalcEngine()

    def calc_se_taxes(self, income):
        se_taxes_percent = self.get_se_taxes_percent_from_gov()
        return self.calc_engine.percent(income, se_taxes_percent)

    # add 5 complicated methods for tax calculations

    @staticmethod
    def get_se_taxes_percent_from_gov():
        return 16


