from typing import Generator, Tuple
import requests
from bs4 import BeautifulSoup

url = 'https://www.indeed.co.uk/jobs?q=python&l='

def find_job(location: str = 'london') -> Generator[Tuple[str, str], None, None]:
	soup = BeautifulSoup(requests.get(url + location).content, 'html.parser')

	for job in soup.find_all("div", attrs={"data-tn-component":"organicJob"}):
		job_title = job.find("a", attrs={"data-tn-element":"jobTitle"}).text.strip()
		company_name = job.find("span", {"class": "company"}).text.strip()
		yield job_title, company_name


if __name__ == "__main__":
    for i, job in enumerate(find_job("London, Greater London"), 1):
        print(f"Job {i:>2} is {job[0]} at {job[1]}")
