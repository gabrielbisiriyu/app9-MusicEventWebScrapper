import requests
import selectorlib
import functions
import time
url="http://programmer100.pythonanywhere.com/tours/"  
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'} 
# Headers tell the server that the script is a browser
# Some servers do not want scripts but browsers 
def Scrape(url):
    '''scrape the page source from the url'''
    response=requests.get(url,HEADERS) 
    content=response.text 
    extractor=selectorlib.Extractor.from_yaml_file("extract.yaml") 
    value=extractor.extract(content)["tours"]
    return value
 




info=Scrape(url)   
if info != "No upcoming tours" :  
    print(info)
    stores=functions.storage(info)
    if stores[0] == "True":
        band=stores[1][0]
        city=stores[1][1]
        date=stores[1][2]
        functions.send_email(message=f'''Band: {band}\n City: {city}\n Date: {date}''')


