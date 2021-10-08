from requests_html import HTMLSession
from bs4 import BeautifulSoup
from pprint import pprint
import json
import click

with open('tag.json', 'r') as config_file:
	config = json.load(config_file)

MY_TAGS = config.get("my_favorite_tags")

def get_all_workshop():
	session = HTMLSession()
	resp = session.get("https://workshops.aws")
	resp.html.render()

	soup = BeautifulSoup(resp.html.html, "lxml")
	all_workshop = []

	for workshop in soup.find_all("aws-workshop-card"):
		details = []
		
		for element in workshop.find_all("div", class_="detail"):
			details.append(element.getText().lstrip())

		for detail in details:
			if "Level" in detail:
				workshop_level = detail.split(':')[1].strip()
			if "schedule" in detail:
				workshop_time = ' '.join([detail.split()[1],detail.split()[2]])
			if "Categories" in detail:
				workshop_cat = detail.split(":")[1].strip().lower()
			if "Tags" in detail:
				workshop_tags = detail.split(':')[1].strip().lower()


		workshop_title = workshop.find("div", class_="mat-headline").getText()
		workshop_url = workshop.find("a", class_="mat-focus-indicator").get("href")
		
		all_workshop.append({'titre':workshop_title, 'level':workshop_level, 'time':workshop_time, 'tag': workshop_tags, 'url':workshop_url})
	
	return all_workshop

def get_workshop_by_level(wks_lvl, workshops):
	if wks_lvl:
		workshop_lvl = []
		for w in workshops:
			if w['level'] == str(wks_lvl) or str(wks_lvl) in w['level']:
				workshop_lvl.append(w)
		return (workshop_lvl)
	else:
		return "Error bad value for wks_lvl"

def get_workshop_filtred(tags, workshop):
	filtred_workshop = []
	for w in workshop:
		for t in tags:
			if t in w['tag'].split(','):
				filtred_workshop.append(w)
				break
	return filtred_workshop

@click.group()
def workshop_parser():
    pass

@workshop_parser.command(help="filtre l'ensemble des workshops par niveau")
@click.option('--level', required= True, help='indiquer un niveau entre 100 et 400')
def by_level(level):
	result = get_workshop_by_level(level, get_all_workshop())
	pprint(result)
	print(len(result))

@workshop_parser.command(help="filtre les workshops par centre d'interet cf:tag.json")
@click.option('--all-wks', is_flag=True, required=False, help="Recupére tous les workshop par centre d'interet")
@click.option('--by-level', type=int, default=None, required=False, help="Recupere les workshop par niveau et par centre d'interet value: entre 100 et 400")
def filtred(all_wks, by_level):
	if all_wks: 
		result = get_workshop_filtred(MY_TAGS, get_all_workshop())
	elif by_level!=None:
		filtered = get_workshop_filtred(MY_TAGS, get_all_workshop())
		result = get_workshop_by_level(by_level, filtered)
	pprint(result)
	print(len(result))

if __name__ == "__main__":
	workshop_parser()
