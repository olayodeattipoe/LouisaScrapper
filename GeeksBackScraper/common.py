
from bs4 import BeautifulSoup
from selenium.webdriver.edge.service import Service
from selenium import webdriver

webdriver_path = "C:/Users/user/Downloads/edgedriver_win64/msedgedriver.exe"

service = Service(webdriver_path)


def scrape_questions(url):
    driver = webdriver.Edge(service=service)
    print("scraping ..........")
    print("This may take a few seconds to minutes")
    driver.get(url)
    html = driver.page_source
        # Check if the request was successful
            # Parse the content with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find all question elements - you may need to adjust the selector based on the page structure
    question_elements = soup.find_all('a', class_='title')

    # Extract and print questions
    questions = []
    for element in question_elements:
        question_text = element.get_text(strip=True)
        question_link = element.get('href', '')
        questions.append((question_text, question_link))

    return questions


def main():
    # Example URL - you should replace this with the URL of the page you want to scrape
    url = 'https://www.geeksforgeeks.org/category/competitive-programming/'

    questions = scrape_questions(url)

    if questions:
        print("Scraped Questions:")
        for question in questions:
            print(f"Question: {question[0]}")
            print(f"Link: {question[1]}")
            print()
    else:
        print("No questions found.")


if __name__ == "__main__":
    main()
