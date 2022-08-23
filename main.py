import csv
import json
import requests
from bs4 import BeautifulSoup


# URL = "https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie"
headers = {
    "accept": "*/*",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36"
}

# req = requests.get(URL, headers=headers)
# with open("index.html", "w") as file:
#     file.write(req.text)

# with open("index.html", "r") as file:
#     src = file.read()
# soup = BeautifulSoup(src, "lxml")

# all_products = soup.find_all("a", class_="mzr-tc-group-item-href")

# products_json = dict()
# for product in all_products:
#     product_title = product.text
#     product_href = "https://health-diet.ru" + product.get("href")
#     products_json[product_title] = product_href

# with open("all_products.json", "w") as file:
#     json.dump(products_json, file, indent=4, ensure_ascii=False)


with open("all_products.json", "r") as file:
    all_products = json.load(file)

size = len(all_products) - 1

count = 0
for product_title, product_href in all_products.items():
    symbol = {" ", "-", ",", "'", ".", "/"}
    for s in symbol:
        if s in product_title:
            product_title = product_title.replace(s, "_")

    product_table_json = list()
    
    req = requests.get(url=product_href, headers=headers)
    src = req.text
    with open(f"data/{count}_{product_title}.html", "w") as file:
        file.write(src)
    
    with open(f"data/{count}_{product_title}.html", "r") as file:
        src = file.read()
    soup = BeautifulSoup(src, "lxml")

    if soup.find(class_="uk-alert-danger") is not None:
        continue

    table_headings = soup.find("thead").find_all("th")
    product = table_headings[0].text
    calories = table_headings[1].text
    proteins = table_headings[2].text
    fats = table_headings[3].text
    carbohydrates = table_headings[4].text

    with open(f"data/{count}_{product_title}.csv", "w", encoding="utf-8-sig") as file:
        writer = csv.writer(file)
        writer.writerow(
            (product, calories, proteins, fats, carbohydrates)
        )

    table_data = soup.find("tbody").find_all("tr")
    for table_item in table_data:
        row_items = table_item.find_all("td")

        title = row_items[0].find("a").text
        calories = row_items[1].text
        proteins = row_items[2].text
        fats = row_items[3].text
        carbohydrates = row_items[4].text

        with open(f"data/{count}_{product_title}.csv", "a", encoding="utf-8-sig") as file:
            writer = csv.writer(file)
            writer.writerow(
                (title, calories, proteins, fats, carbohydrates)
            )
        product_table_json.append(
            {
                "Title": title,
                "Calories": calories,
                "Proteins": proteins,
                "Fats": fats,
                "Carbohydrates": carbohydrates
            }
        )
        with open(f"data/{count}_{product_title}.json", "w") as file:
            json.dump(product_table_json, file, indent=4, ensure_ascii=False)
            
    print(f"#{count} iteration: '{product_title}' is finished...", flush=True)
    count += 1
    if count == size:
        print("====== Website parsing is complete ======")