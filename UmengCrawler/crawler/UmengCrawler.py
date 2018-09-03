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
        self.username = '****@arashivision.com'
        self.password = '****'
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
        cookie = cookielib.CookieJar()
        handler = urllib2.HTTPCookieProcessor(cookie)
        opener = urllib2.build_opener(handler)

        values = {
            'loginId': self.username,
            'password2': self.password,
            'checkCode': '',
            'appName': 'youmeng',
            'appEntrance': 'default',
            'bizParams': '',
            'ua': '099#KAFEc7E9EG5E6YTLEEEEE6twSXv7V6D1DXRqD6VqZRso+fPTguBIn6VcZXC6+fYBYRXjAIdBYc37DIgFDcZj+MtTYRwYgybTET/sudyl0yaSt3xRO9uRSf8D8lCgPow3YXc0dqSLE7EjllsllVRC4/l0Py80g6R0bKEnE7EKt37Bldcdt3bi4GFEJcBNlllPbaTk8yxPrMOm8OXFVovK8PchQUiNCo49E7EFD67EEwoTETillAlldsaSurhJby1TSV3W8OXgLybTET9llC3ldRaSt3ilG/uRSf8D8lCgPowm41qTETJll/llV/Wxlt8Dr08FSP8G4RbTET9llC3ldRaSt3ilL3uRSf8D8lCgPowm4K5TEEiStEE7JGFET6i5EE1lE7EFNIaHF7oTEEySl3llsyCzE7TxT1ywEF2So87YqIWoyeHSoZdYkfMl+wDzkLp6mCXGkLKo3jk36OT26HGbvFdWVwICRJ9yk8lDqwP+M6A0pu7WoZjDB0ANtkj26HA3nkps0kVZkUoTEja5R713aquYSpXfNV9c1e95zqbVcLSpr6hZDahG3MesD/rkPwoq+yLBbtUnHda3rM2QZiXaEm1dQs90FswcazOsrfCX/IS3rfCWnjcGabWjlWwxbwXp1u86bfXGrbn3dUhYZi2CAA14GX8IrLe6csy9O/WGc7U6zVOCvRoWAMZDSM9SPCbq1WcXU6pWbLP6rdu9uOIQAMZaZOeJqsw6LOhB/oW8PSUqr6nzLsEZLY/C4295KOj6Lc8TU67Qr5TtuQrDAO4QL5WYLeJqbLXR3y9Mr02ArMVtr6XaZLX4xSWDZRh9by8ccWyIbISMHlWusflLDzry3/lvSXwk8Azlapw5zKWBNdQpztx4Ca4W37uVnROfHsh6w9rBrtCS6WSTE1LSt3llsyaSt3iSE6iP/37mt377mXZdtl9StTTmsyaZR/iSFHBP/3MrJ7FE13iSEJv5+WmkOGFET/yZTEwyL25TEEi5D7EE6GFE19iS0llR/3iurioTETilla3ldOaSl871by1TSV3W8OXgLioTETillC3ldRaSlgTZby1TSV3W8OXgLjdTEEi5DEEEJGFET6i5EE1iE7ExllllluZa5w20PpZV+Pk2PVnVIGFEHuB4lll+XKRlZykV8MixZ28mVbv0YbW7JGFET6i5EEELE7EBVXBlluKX4/l0Py80g6R0e0B8Cf81azELE7EjllllllAh4/l0Py80g6R0bKE9E7EFD67EE1qTETJlllll4L+xlt8Dr08FSP8G4E==',
            'hsid': '1e9bc7bacdcf45193faa7c688b1ca2e4',
            'rdsToken': '',
            'umidToken': '9f7b57fb270885cb6aa7d1aaac45f259dba7a08a',
            'isRequiresHasTimeout': 'false',
            'isRDSReady': 'true',
            'isUMIDReady': 'isUMIDReady',
            'umidGetStatusVal': '255',
            'lrfcf': '',
            'lang': 'zh_cn',
            'scene': '',
            'isMobile': 'false',
            'screenPixel': '1366x768',
            'navlanguage': 'zh-CN',
            'navUserAgent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
            'navAppVersion': '',
            'navPlatform': '',
            'token': '',
            'nocAppKey': '',
            'csessionid': '',
            'sig': '',
            'captchaToken': '',
            '_csrf_token': '94mc6VOhSa3QP56XjC6IK2'
        }
        headers = {}
        headers['X-Requested-With'] = 'XMLHttpRequest'
        headers['User-Agent'] = self.user_agent
        headers['Host'] = 'passport.alibaba.com'
        headers['Origin'] = 'https://passport.alibaba.com'
        headers['X-Requested-With'] = 'XMLHttpRequest'
        headers['Connection'] = 'keep-alive'
        headers['Referer'] = 'https://passport.alibaba.com/mini_login.htm?lang=zh_cn&appName=youmeng&appEntrance=default&styleType=auto&bizParams=&notLoadSsoView=true&notKeepLogin=false&isMobile=false&cssLink=https://passport.umeng.com/css/loginIframe.css&rnd=0.10927577253646747'
        headers['Accept'] = '*/*'
        headers['Accept-Language'] = 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3'
        headers[
            'Cookie'] = 't=8c2104b33f867314978f96da2f8a0ebf; _uab_collina=149579075934407755601457; l=Ao2N3XY1fYyFMIEwisLgeAJFHaMHZcE8; umdata_=70CF403AFFD707DF176342C07955D504071D3D712F4B45002F4EEB3197D2A03B38176EB3779BD52FCD43AD3E795C914C8C2179C0ABC2185A05246EC8E1B8CA84; v=0; cookie2=1e9bc7bacdcf45193faa7c688b1ca2e4; _tb_token_=e5a655781be1b; cna=9/yQEVjJDyQCAdOiUVw1VeHL; _umdata=BA335E4DD2FD504FDB20DB1838C74A33177126C1B6E55BEEC360D0D04DFD01DA81AB19C07EE20598CD43AD3E795C914CF0C3A6A1F8AEEFE87C3135A0A02F5B22; isg=At_f4Zou-n_1YP5j2EQ7wzBgbjMbkMWq9fiRWnEsSw7VAPyCexRxNtWWtqeE'
        data = urllib.urlencode(values)
        request = urllib2.Request(url='https://passport.alibaba.com/newlogin/login.do?fromSite=-2&appName=youmeng', data=data, headers=headers)
        result = opener.open(request)
        print result.read()
        for c in cookie:
            self.cookie += c.name + '=' + c.value + ';'
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
