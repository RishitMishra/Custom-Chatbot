import requests
from bs4 import BeautifulSoup

def extract_course_names(url,css_selector):

    try:
        r = requests.get(url)

        soup = BeautifulSoup(r.content,"html5lib")
        extracted = soup.css.select(css_selector)

        course_names = []
        for i in extracted:
            course_names.append(i.string + " URL:https://brainlox.com" + i.get("href"))
   
        return course_names
    
    except Exception as e:
        print(f"Error extracting course names: {e}")
        return []




