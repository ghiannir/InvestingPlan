#import sqlite3

#conn = sqlite3.connect("rip.s3db")
#cur = conn.cursor()

def main():
    m_expenses = float(input("Monthly expenses: "))
    m_wage = float(input("Monthly wage: "))
    a_int = float(input("Annual average return on investments: "))
    a_inf_rate = 0.018
    inf_rate = a_inf_rate
    l_time = 75
    retired = False
    age = 25
    tot_capital = 0

    while not retired:
        age += 1
        a_net_income = inf_rate*(m_expenses - m_wage)*12
        inf_rate *= a_inf_rate
        tot_capital += a_net_income
        tot_capital *= 1 + a_int
        gain = tot_capital*a_int
        if gain >= inf_rate*m_expenses:
            retired = True

    print(f"You will retire at {age} years after {age-25} years of work")


if __name__ == '__main__':
    main()
