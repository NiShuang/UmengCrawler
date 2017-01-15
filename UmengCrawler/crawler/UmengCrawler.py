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


    def getEvent(self, start_date, end_date, event_group_id, version):
        self.headers['Referer'] = 'http://mobile.umeng.com/apps/cf41008f4de85e761c647675/events/' + event_group_id + '?version='
        request = urllib2.Request(
            'http://mobile.umeng.com/apps/cf41008f4de85e761c647675/events/load_table_data?page=1&per_page=99999&start_date=' + start_date + '&end_date=' + end_date + '&versions[]=' + version + '&channels[]=&stats=event_group_trend&event_group_id=' + event_group_id,
            headers=self.headers
        )
        try:
            response = urllib2.urlopen(request)
            jsonData = response.read()
            result = json.loads(jsonData, encoding="utf-8")
            print result
            return result['stats']
        except urllib2.URLError, e:
            if hasattr(e, "code"):
                print e.code
            if hasattr(e, "reason"):
                print e.reason


    def getAllEvents(self, start_date, end_date, event_group_id, version):
        self.headers['Referer'] = 'http://mobile.umeng.com/apps/cf41008f4de85e761c647675/events/dashboard?show_all=true'
        request = urllib2.Request(
            'http://mobile.umeng.com/apps/cf41008f4de85e761c647675/events/load_table_data?page=1&per_page=30&versions[]=&stats=count&show_all=true',
            headers=self.headers
        )
        try:
            response = urllib2.urlopen(request)
            jsonData = response.read()
            result = json.loads(jsonData, encoding="utf-8")
            print result['stats']
            return result['stats']
        except urllib2.URLError, e:
            if hasattr(e, "code"):
                print e.code
            if hasattr(e, "reason"):
                print e.reason


    def getVersions(self):
        self.headers['Referer'] = 'http://mobile.umeng.com/apps/cf41008f4de85e761c647675/events/dashboard'
        request = urllib2.Request(
            'http://mobile.umeng.com/apps/cf41008f4de85e761c647675/load_versions?show_all=true',
            headers=self.headers
        )
        try:
            response = urllib2.urlopen(request)
            jsonData = response.read()
            result = json.loads(jsonData, encoding="utf-8")
            datas = result['datas']
            versions = []
            for data in datas:
                versions.append(data['name'])
            return versions

        except urllib2.URLError, e:
            if hasattr(e, "code"):
                print e.code
            if hasattr(e, "reason"):
                print e.reason


    def getShareChannel(self, start_date, end_date):
        event_group_ids = {
            '微信_img': '57afe74767e58ea4ca000428',
            'Facebook_img': '57afe75ce0f55a34db00349c',
            # 'Whatsapp_img': '57afe7a267e58edf73002e91',
            # 'Facebook_video': '57afe6ce67e58eb85a0046e5',
            # 'Pasteboard_video': '5858e1fdf5ade402780010ac',
            # '微信_video': '57afe6bee0f55a480400445a',
            # 'Line_img': '57afe7bce0f55ac27900447b',
            # 'Whatsapp_video': '57afe71b67e58e317b003814',
            # 'Moment_img': '57afe78567e58e3c1f001b74',
            # 'Instagram_video': '5858e1f17666135f19000550',
            # 'Pasteboard_img': '5858e214f5ade44ac9000fce',
            # 'Youtube_video': '57afe6ed67e58e84230001c1',
            # 'Messenger_img': '57afe7af67e58e7837001ac7',
            # 'Line_video': '57afe73767e58e6bc80006b2',
            # 'Instagram_img': '5858e209c895765ac5001b99',
            # '朋友圈_video': '57afe70067e58e86c5003cfe',
            # 'Messenger_video': '57afe728e0f55a7b52002ba4',
            # 'QQ_img': '57afed8667e58e42aa0005da',
            # '微博_video': '57afe70e67e58e5f2f005a1e',
            # 'QQ_video': '57afed9f67e58eb85a004bfd',
            # 'Twitter_img': '57afe76b67e58ef70b003503',
            # '微博_img': '57afe794e0f55ac8e3000e81',
            # 'Qzone_video': '57afedaa67e58e6bc8000c4d',
            # 'Twitter_video': '57afe6dd67e58e86ad000af7',
            # 'Qzone_img': '57afed9267e58e4759002409'
        }
        versions = self.getVersions()
        result = []
        for version in versions:
            if version < '1.5.0':
                continue
            for index in event_group_ids:
                event_group_id = event_group_ids[index]
                data = self.getEvent(start_date, end_date, event_group_id, version)
                temps = index.split('_')
                temp = {
                    'version': version,
                    'event_group_id': event_group_id,
                    'channel': temps[0],
                    'type': temps[1],
                    'data': data
                }
                result.append(temp)
        jsonResult = json.dumps(result)
        return jsonResult


    def shareCount(self, start_date, end_date):
        event_group_ids = {
            'video_success': '576ba13767e58eb24f001ee5',
            'video_try': '576ca33267e58e9c380026a4',
            'img_try': '576ca36067e58ed3450030a8',
            'img_success': '576ba15a67e58e15b2001435'
        }
        versions = self.getVersions()
        result = []
        for version in versions:
            if version < '1.6.0':
                continue
            for index in event_group_ids:
                event_group_id = event_group_ids[index]
                data = self.getEvent(start_date, end_date, event_group_id, version)
                temps = index.split('_')
                temp = {
                    'version': version,
                    'event_group_id': event_group_id,
                    'data': data,
                    'type': temps[0],
                    'flag': temps[1]
                }
                result.append(temp)
        jsonResult = json.dumps(result)
        return jsonResult


if __name__=="__main__":
    crawler = UmengCrawler()
    crawler.start()
    result = crawler.getShareChannel('2016-12-21', '2016-12-25')
    # result = crawler.getVersions()
    print result
