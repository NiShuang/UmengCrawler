#-*- coding: UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import datetime
import urllib2
import json

class UmengCrawler:
    def __init__(self):
        cap = webdriver.DesiredCapabilities.PHANTOMJS
        cap["phantomjs.page.settings.resourceTimeout"] = 1000
        cap["phantomjs.page.settings.loadImages"] = False
        cap["phantomjs.page.settings.localToRemoteUrlAccessEnabled"] = True
        self.driver = webdriver.PhantomJS(desired_capabilities=cap)
        # self.driver = webdriver.Chrome()
        self.host = 'mobile.umeng.com'
        self.username = 'develop@arashivision.com'
        self.password = ')8x3CpA$'
        self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0'
        self.cookie = ''

        self.headers = {}
        self.headers['User-Agent'] = self.user_agent
        self.headers['Host'] = self.host
        self.headers['X-Requested-With'] = 'XMLHttpRequest'
        self.headers['Connection'] = 'keep-alive'
        self.headers['Cache-Control'] = 'max-age=0'
        self.headers['Accept'] = '*/*'
        self.headers['Accept-Language'] = 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3'
        self.headers['X-CSRF-Token'] = 'gnRA365zNecgXvbLpUca20a4uSLO40G/gFNp1sCqJZA='
    def start(self):
        self.driver.get("https://i.umeng.com/")

        element = self.driver.find_element_by_xpath("//*[@id='ump']/div[1]/div/form/div[1]/ul/li[1]/div/label/input")
        element.clear()
        element.send_keys(self.username)

        element = self.driver.find_element_by_xpath("//*[@id='ump']/div[1]/div/form/div[1]/ul/li[2]/label/input")
        element.clear()
        element.send_keys(self.password)

        element = self.driver.find_element_by_id("submitForm")
        element.click()

        wait = WebDriverWait(self.driver, 10)
        element = wait.until(
            lambda x: x.find_element_by_xpath("//*[@id='app']/div/div/main/div/div[1]/div/div/a[2]"))
        element.click()

        cookies = self.driver.get_cookies()
        for cookie in cookies:
            # print cookie['name'] + ' : ' + cookie['value']
            self.cookie = self.cookie + cookie['name'] + '=' + cookie['value'] + ';'
        self.driver.quit()
        self.headers['Cookie'] = self.cookie

    def getNewUser(self, start_date, end_date):
        self.headers['Referer'] = 'http://mobile.umeng.com/apps/cf41008f4de85e761c647675/reports/installation'
        request = urllib2.Request('http://mobile.umeng.com/apps/cf41008f4de85e761c647675/reports/load_table_data?page=1&per_page=99999&start_date='+start_date+'&end_date='+end_date+'&versions[]=&channels[]=&segments[]=&time_unit=daily&stats=installations', headers=self.headers)
        try:
            response = urllib2.urlopen(request)
            jsonData = response.read()
            result = json.loads(jsonData, encoding="utf-8")
            # print result['stats']
            return result['stats']
        except urllib2.URLError, e:
            if hasattr(e, "code"):
                print e.code
            if hasattr(e, "reason"):
                print e.reason

    def getActiveUser(self, start_date, end_date):
        self.headers['Referer'] = 'http://mobile.umeng.com/apps/cf41008f4de85e761c647675/reports/active_user'
        request = urllib2.Request('http://mobile.umeng.com/apps/cf41008f4de85e761c647675/reports/load_table_data?page=1&per_page=99999&start_date='+start_date+'&end_date='+end_date+'&versions[]=&channels[]=&segments[]=&time_unit=daily&stats=active_users', headers=self.headers)
        try:
            response = urllib2.urlopen(request)
            jsonData = response.read()
            result = json.loads(jsonData, encoding="utf-8")
            # print result['stats']
            return result['stats']
        except urllib2.URLError, e:
            if hasattr(e, "code"):
                print e.code
            if hasattr(e, "reason"):
                print e.reason

    def getDuration(self, date):
        self.headers['Referer'] = 'http://mobile.umeng.com/apps/cf41008f4de85e761c647675/reports/duration'
        request = urllib2.Request('http://mobile.umeng.com/apps/cf41008f4de85e761c647675/reports/load_chart_data?start_date='+date+'&end_date='+date+'&versions[]=&channels[]=&segments[]=&time_unit=daily&stats=duration&stat_type=daily', headers=self.headers)
        try:
            response = urllib2.urlopen(request)
            jsonData = response.read()
            result = json.loads(jsonData, encoding="utf-8")
            # print result['summary']['value']
            return result['summary']['value']
        except urllib2.URLError, e:
            if hasattr(e, "code"):
                print e.code
            if hasattr(e, "reason"):
                print e.reason

    def getTotalError(self, start_date, end_date):
        self.headers['Referer'] = 'http://mobile.umeng.com/apps/cf41008f4de85e761c647675/error_types/trend'
        request = urllib2.Request('http://mobile.umeng.com/apps/cf41008f4de85e761c647675/reports/load_chart_data?start_date=' + start_date + '&end_date=' + end_date + '&stats=error_count', headers=self.headers)
        try:
            response = urllib2.urlopen(request)
            jsonData = response.read()
            result = json.loads(jsonData, encoding="utf-8")
            return result['stats'][0]['data']
        except urllib2.URLError, e:
            if hasattr(e, "code"):
                print e.code
            if hasattr(e, "reason"):
                print e.reason

    def getErrorDetail(self, start_date, end_date):
        # start_date 必须在今天的前15天之后
        self.headers['Referer'] = 'http://mobile.umeng.com/apps/cf41008f4de85e761c647675/error_types'
        request = urllib2.Request('http://mobile.umeng.com/apps/cf41008f4de85e761c647675/error_types/search?start_date=' + start_date + '&end_date=' + end_date + '&versions[]=1.2.0&versions[]=1.2.1&versions[]=1.1.0&message_type=legit&per_page=99999&page=0&order_by=desc_error_count', headers=self.headers)
        try:
            response = urllib2.urlopen(request)
            jsonData = response.read()
            result = json.loads(jsonData, encoding="utf-8")
            return result['result']
        except urllib2.URLError, e:
            if hasattr(e, "code"):
                print e.code
            if hasattr(e, "reason"):
                print e.reason

    def getUserCityDistribution(self, start_date, end_date):
        self.headers['Referer'] = 'http://mobile.umeng.com/apps/cf41008f4de85e761c647675/reports/location?which=cities'
        request = urllib2.Request('http://mobile.umeng.com/apps/cf41008f4de85e761c647675/reports/load_table_data?page=1&per_page=99999&start_date=' + start_date + '&end_date=' + end_date + '&versions[]=&channels[]=&segments[]=&time_unit=daily&stats=location_cities', headers=self.headers)
        try:
            response = urllib2.urlopen(request)
            jsonData = response.read()
            result = json.loads(jsonData, encoding="utf-8")
            return result['stats']
        except urllib2.URLError, e:
            if hasattr(e, "code"):
                print e.code
            if hasattr(e, "reason"):
                print e.reason

    def getUserCountryDistribution(self, start_date, end_date):
        self.headers['Referer'] = 'http://mobile.umeng.com/apps/cf41008f4de85e761c647675/reports/location?which=countries'
        request = urllib2.Request('http://mobile.umeng.com/apps/cf41008f4de85e761c647675/reports/load_table_data?page=1&per_page=99999&start_date=' + start_date + '&end_date=' + end_date + '&versions[]=&channels[]=&segments[]=&time_unit=daily&stats=location_countries', headers=self.headers)
        try:
            response = urllib2.urlopen(request)
            jsonData = response.read()
            result = json.loads(jsonData, encoding="utf-8")
            return result['stats']
        except urllib2.URLError, e:
            if hasattr(e, "code"):
                print e.code
            if hasattr(e, "reason"):
                print e.reason

    def getUserDistribution(self, start_date, end_date):
        start = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
        end = datetime.datetime.strptime(end_date, '%Y-%m-%d').date()
        result = []
        for i in range((end - start).days + 1):
            date = (end - datetime.timedelta(days=i)).strftime('%Y-%m-%d')
            city = self.getUserCityDistribution(date, date)
            for item in city:
                temp = {'date':date, 'location':item['date'], 'activeUser':item['active_data'], 'is_city':1}
                result.append(temp)
            country = self.getUserCountryDistribution(date, date)
            for item in country:
                temp = {'date':date, 'location':item['date'], 'activeUser':item['active_data'], 'is_city':0}
                result.append(temp)
        return result


    def getUseCondition(self, start_date, end_date):
        result = []
        newUser = self.getNewUser(start_date, end_date)
        activeUser = self.getActiveUser(start_date, end_date)
        start = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
        end = datetime.datetime.strptime(end_date, '%Y-%m-%d').date()
        for i in range((end - start).days + 1):
            date = (end - datetime.timedelta(days=i)).strftime('%Y-%m-%d')
            duration = self.getDuration(date)
            # print date,newUser[i]['data'],activeUser[i]['data'],duration
            temp = {'date':date, 'newUser':newUser[i]['data'], 'activeUser':activeUser[i]['data'], 'duration':duration}
            result.append(temp)
        jsonResult = json.dumps(result)
        return jsonResult

if __name__=="__main__":
    crawler = UmengCrawler()
    crawler.start()
    result = crawler.getUserDistribution('2016-07-30', '2016-08-07')
    print result
