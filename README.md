# PythonWebScraping
Python scraping of web pages using ___beautifulsoup4___, ___lxml___, ___requests___, ___json___ and ___csv___ libraries.

Link to the web page used in this project: https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie<br>
This web page contains information about various food products. It was necessary to get all the data about each type of food, in particular, its name, the amount of calories, proteins, fats and carbohydrates contained in it, and then save this information in json and csv (Excel) formats.

This python script uses _requests_ library to get the contents of the web page, and then passes it to an HTML file. To process the page content, the _BeautifulSoup_ library was used with the _lxml_ library. The resulting content is stored in a json file (all_products.json), which contains the product names and corresponding links. The same techniques were used to extract data from each link and transfer it to json and csv format files for storage in a separate folder.
