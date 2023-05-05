from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://www.cvbankas.lt').text
soup = BeautifulSoup(source, 'html.parser')

blokai = soup.find_all('article', class_="list_article list_article_rememberable jobadlist_list_article_rememberable jobadlist_article_vip")
a = input("ieskoti: ")

with open("skelbimu1.csv", "w", encoding="UTF-8", newline='') as failas:
    csv_writer = csv.writer(failas)
    csv_writer.writerow(['pareigos', 'alga', 'i rankas ar ne', 'linkas'])

    for blokas in blokai:
        pavadinimas = blokas.find('h3', class_='list_h3').text.strip()
        if a in pavadinimas:
            alga = blokas.find('span', class_="salary_amount").text.strip()
            eurai = blokas.find('span', class_="salary_period").text.strip()
            koks_budas = blokas.find('span', class_='salary_calculation').text.strip()
            linkas = blokas.find('a', class_="list_a can_visited list_a_has_logo")['href']
            csv_writer.writerow([pavadinimas, alga, eurai, koks_budas, linkas])
            print(pavadinimas, alga, eurai, koks_budas, linkas)
        else:
            pass

