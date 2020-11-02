from selenium import webdriver
from bs4 import BeautifulSoup as soups

def search_selenium(search_name, search_path, search_limit) :
    search_url = "https://www.google.com/search?q=" + str(search_name) + "&hl=ko&tbm=isch"
    
    browser = webdriver.Chrome("./chromedriver")
    browser.get(search_url)
    
    image_count = len(browser.find_elements_by_tag_name("img"))
    
    print("로드된 이미지 개수 : ", image_count)

    browser.implicitly_wait(2)

    for i in range( search_limit ) :
        image = browser.find_elements_by_tag_name("img")[i]
        image.screenshot("C:\\Users\\yso00\\OneDrive\\바탕 화면\\pythonworkspace\\practice_project\\김승연\\" + str(i) + ".jpg")
        # search_path = image.screenshot("./Mr_Moon/" + str(i) + ".png")
    browser.close()

if __name__ == "__main__" :

    search_name = input("검색하고 싶은 키워드 : ")
    search_limit = int(input("원하는 이미지 수집 개수 : "))
    search_path = "C:\\Users\\yso00\\OneDrive\\바탕 화면\\pythonworkspace\\practice_project\\이병철"
    # search_maybe(search_name, search_limit, search_path)
    search_selenium(search_name, search_path, search_limit)