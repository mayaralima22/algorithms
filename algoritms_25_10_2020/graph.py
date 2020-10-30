import csv

import matplotlib.pyplot


def graph():
    country = input("Informe um país: ")

    with open('algoritms_25_10_2020/planilha.csv') as file:
        file = csv.DictReader(file.readlines())

        for row in file:
            if row['País'] == country:
                pib = row.values()
                ano = row.keys()
                matplotlib.pyplot.plot(ano, pib)

        matplotlib.pyplot.show()