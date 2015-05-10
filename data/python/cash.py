def deduct(month_income, cash_in_hand, tax):
	cash_deducted = cash_in_hand / tax
	mod_income =  cash_deducted + month_income
	return mod_income

def calculate_yearly_tax_rate(cash_deducted, tax_per_month):
	tax = cash_deducted + tax_per_month * 12
	return tax

