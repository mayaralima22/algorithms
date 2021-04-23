import csv


def request_pib():
    country = input("Informe um país: ")
    year = input("Informe um ano entre 2013 e 2020: ")

    with open('algoritms_25_10_2020/planilha.csv') as file:
        file = csv.DictReader(file.readlines())
        found_country = False

        for row in file:
            if row['País'] == country:
                found_country = True
                if 2012 < int(year) < 2021:
                    print(f'PIB {country} em {year}: US${row[year]} trilhões')

                    break

                print("Ano não disponível")

                break

            x = (100 * float(row['2020']) / float(row['2013'])) - 100
            print(f"{row['País']}: Variação de {round(x, 2)}% entre 2013 e 2020.")

        if found_country is False:
            print("País não disponível")


#teste