# final_amt is "final amount" 
def final_amt(p, r, n, t):
    """ apply the compound interest formula"""
    # p = princpal
    # r = interest rate
    # n = frequency
    # t = length of time in years

    a = p * (1 + r/n) ** (n*t)
    return round(a,2)

print()
to_invest = float(input("How much do you want to invest?\n"))
invest_amount = final_amt(to_invest, 0.08, 12, 5)
print("Expected income:", "$" + str(invest_amount),"\n")