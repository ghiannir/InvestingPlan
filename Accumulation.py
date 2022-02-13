import sqlite3

conn = sqlite3.connect('Investment.s3db')
cur = conn.cursor()
#cur.execute("DELETE investments")
cur.execute("""
CREATE TABLE investments(
    Year integer,
    Total integer,
    Net gain integer
)""")
conn.commit()


def main():
    i_capital = float(input('Your initial invested capital: '))
    accumulation = float(input('Your monthly accumulation: '))
    a_rate = float(input('Profit annual rate in %: ')) / 100
    tot_capital = i_capital
    m_rate = a_rate / 12
    for i in range(30):
        tot_capital += tot_capital * a_rate + 12*accumulation
        i_capital += 12*accumulation
        if tot_capital < 20000:
            tot_capital *= 99 / 100
        else:
            tot_capital *= 99.3 / 100
        cur.execute("""INSERT INTO investments VALUES(?, ?, ?)""", (i+1, round(tot_capital, 2), round(tot_capital - i_capital, 2)))
        conn.commit()
        print('-' * 40)
        print(f'|Year: {i+1} |Tot: {round(tot_capital, 2)} |Net Gain: {round(tot_capital - i_capital, 2)}|')


if __name__ == '__main__':
    main()
