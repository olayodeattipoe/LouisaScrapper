from bs4 import BeautifulSoup
import lxml
from selenium import webdriver
import json
from database import create_table
from selenium.webdriver.edge.service import Service

webdriver_path = "C:/Users/user/Downloads/edgedriver_win64/msedgedriver.exe"

service = Service(webdriver_path)


def get_source_code(url):
    # this function returns the html source code for scrapping
    driver = webdriver.Edge(service=service)
    print("scraping ..........")
    print("This may take a few seconds to minutes")
    driver.get(url)
    html = driver.page_source
    driver.close()
    return BeautifulSoup(html, "lxml")


def scrape_from_geeks_for_geeks(url, database_name):

    workable_object = None
    question_to_add = []

    soup = get_source_code(url)
    soup = soup.find_all(name='script', type='application/ld+json')

    for i in soup:
        if i and "hasPart" in str(i):
            workable_object = json.loads(i.get_text())
            break

    for item in workable_object['hasPart']:
        index = 0
        options_ = {}
        for index, option in enumerate(item["suggestedAnswer"]):
            if option is not None and 'text' in option:
                options_[f"data{index}"] = (option['text'])
        options_[f"data{index+1}"] = item['acceptedAnswer']['text']

        data_set = {
                "Question": item['text'],
                "Options": options_,
                "Correct_Answer": item['acceptedAnswer']['text'],
                "Comment": item['acceptedAnswer']['answerExplanation']['text']
        }

        question_to_add.append(data_set)

    create_table(database_name, question_to_add)


if __name__ == '__main__':
    scrape_from_geeks_for_geeks('https://www.geeksforgeeks.org/quizzes/file-handling-gq/', 'Peter')