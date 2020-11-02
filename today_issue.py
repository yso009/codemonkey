import re
import requests
from bs4 import BeautifulSoup

def creat_soup(url):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"}
    res = requests.get(url, headers = headers)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "lxml")
    return soup

def scrape_weather():
    print("[오늘의 날씨]")
    url = "https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%EC%B2%AD%EC%A3%BC+%EB%82%A0%EC%94%A8"
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    f1 = soup.find("div", attrs = {"class" : "info_data"}).find("ul").find("li")
    now = soup.find("div", attrs = {"class" : "info_data"}).find("p")
    lowest = soup.find("div", attrs = {"class" : "info_data"}).find("span", attrs = {"class" : "min"})
    highest = soup.find("div", attrs = {"class" : "info_data"}).find("span", attrs = {"class" : "max"})
    rain_rate_morning = soup.find("li", attrs = {"class" : "date_info today"}).find("span", attrs = {"class" : "point_time morning"}).find("span" , attrs = {"class" : "rain_rate"})
    rain_rate_afternoon = soup.find("li", attrs = {"class" : "date_info today"}).find("span", attrs = {"class" : "point_time afternoon"}).find("span" , attrs = {"class" : "rain_rate"})
    dust = soup.find("dl", attrs = {"class" : "indicator"}).find_all("dd")
    
    print(f1.get_text())
    print("현재 :",now.get_text(), "(최저 :",lowest.get_text(), "/ 최고", highest.get_text(),")")
    print("오전 :",rain_rate_morning.get_text(), "오후 :",rain_rate_afternoon.get_text())
    print("미세먼지 :",dust[0].get_text())
    print("초미세먼지 :", dust[1].get_text())
    print("")

def scrape_headline_news():
    print("[헤드라인 뉴스]")
    url = "https://news.naver.com/"
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"}
    res = requests.get(url, headers = headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    
    
    news1 = soup.find("ul", attrs = {"class" : "hdline_article_list"}).find_all("li", limit =3)
    for index, news in enumerate(news1):
        # head = news.find_all("div", attrs = {"class" : "hdline_article_tit"})
        head = news.find("a").get_text().strip()
        link = url + news.find("a")["href"]

        print("{}. {}".format(index+1 , head))
        print("  (링크 :{})".format(link))
    print("")    

def scrape_it_news():
    print("[IT 뉴스]")
    url = "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=105&sid2=230"
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"}
    res = requests.get(url, headers = headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    it_news = soup.find("ul", attrs ={"class" : "type06_headline"}).find_all("li", limit = 3)
    for index, news in enumerate(it_news):
        a_idx = 0
        photo = news.find("dl").find("dt", attrs = {"class" : "photo"})
        if photo:
            a_idx = 1

        a_tag = news.find_all("a")[a_idx]
        head = a_tag.get_text().strip()
        link = a_tag["href"]
        print("{}. {}".format(index+1, head))
        print("   (링크 :{})".format(link))
    print("")

def scrape_eng():
    print("[오늘의 영어 회화]")
    url = "https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english#;"
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    sentences = soup.find_all("div", attrs = {"id" : re.compile("^conv_kor_t")})
    print("(영어 지문)")
    for sentence in sentences[len(sentences)//2:]: # 한글지문과 영어지문의 attribute가 같아서 총 element 수의 반을 나눈 몫 ~ index[end]
        print(sentence.get_text().strip())
        print("")
    print("(한글 지문)")
    for sentence in sentences[:len(sentences)//2]: # index[0] ~ 같은 attribute의 element를 반으로 나눈 몫
        print(sentence.get_text().strip())
        print("")

if __name__ =="__main__":
    scrape_weather() # 오늘 날씨 정보 가져오기
    scrape_headline_news() # 헤드라인 뉴스 가져오기
    scrape_it_news()
    scrape_eng()