import requests                                                                    # request module to connect the server with python
import json                                                                        # json module to print in json format
from bs4 import BeautifulSoup                                                      # beautifulsoup to parser the html page





def fetch(lat,log):                                                                 # Request the server with latitude and longitude  
	url = "http://127.0.0.1:8000/search?latitude={}&longitude={}".format(lat,log)   # Here requesting from local server adjust URL according to the server.
	response = requests.get(url)
	soup = BeautifulSoup(response.text,'html.parser')                               # Response would collected 
	result = soup.find('h3').text.strip()                                           # Parsing the response
	return result                                                                   # returning the parser string 



def list_of_coordinates(res):                                                       # the function takes string and return the list of top3 coordiantes
	string = '' 
	for char in res[1:-1]:                                                          # joining the string 
		if char == ']' or char == '[':
			continue
		string = string + char
	res = [i.strip(' ') for i in string.split(',')]
	result = [res[i:i + 6][:-1] for i in range(0, len(res), 6)]                     # making sublist according the output
	return result


if __name__ == "__main__":                                                          
	Latitude = float(input("Enter Latitude ::"))                                   
	Longitude = float(input("Enter Longitude ::"))
	output = fetch(Latitude,Longitude)
	result = list_of_coordinates(output)
	# print(result)
	data = []
	for i in result:                                                               # converting the list data into a dictionary
		dic = {'id':i[0],'driver':i[1],'number_plate':i[2],'latitude':i[3],'longitude':i[4]}
		data.append(dic)
	print(json.dumps(data,indent=1))                                               # making dictionary into json format for output




## Acctually here there is no need to parser according to api but I had rendered the output into a page with GUI and maps 
## for that reson here it's needed to parsed

## This is just a basic api like program, but the actuall was designed with GUI.











