import csv


def variation_pib():
    with open('algoritms_25_10_2020/planilha.csv') as file:
        file = csv.DictReader(file.readlines())

        for row in file:
            pib_2013 = float(row['2013'])
            pib_2020 = float(row['2020'])

            variation = (100*pib_2020/pib_2013) - 100
            print(f"{row['País']}: Variação de {round(variation, 2)}% entre 2013 e 2020.")