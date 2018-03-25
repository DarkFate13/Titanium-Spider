import csv
import sys
from requests import get
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

def parse(file_name):
	res = list()
	with open(file_name) as f:
		d = csv.reader(f, delimiter=',')
		for row in d:
			if(row[0] != ''):
				res.append(tuple(row[:2]))
	res.pop(0)
	return res

def scrape(website):
	# request = urllib.request.Request(website)
	headers = {'User-Agent': 'Mozilla/5 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
	req = Request(website, headers={'User-Agent': 'Mozilla/5.0'})
	webpage = urlopen(req).read()
	soup = BeautifulSoup(webpage, 'html.parser')
	return soup.find('span', attrs={'class': 'destination-info__details'}).text
	
if __name__ == "__main__":
	print(parse(sys.argv[1]))
	print(len(parse(sys.argv[1])))
	print(scrape('http://www.holiday-weather.com/bangalore/averages/june/'))