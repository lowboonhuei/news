import json
#searchword = ['casino','No.03','Corona Resort']
searchword = ['casino']
with open('./scraped_articles.json') as json_file:
	data = json.load(json_file)
for publisher in data['newspapers']:
	for news in data['newspapers'][publisher]['articles']:
		if(any(n in news['text'] for n in searchword)):
                	print("88888888888888888-------------------------")
                	print(news['title'])
                	print(news['text'])
                	print(news['link'])
                	print(news['published'])
                	print("88888888888888888-------------------------")

#print(data['newspapers'][publisher]['link'])
