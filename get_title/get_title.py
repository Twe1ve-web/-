import requests
import re
import sys
import threading

def get_title(target):
    r = requests.get(target,timeout=5,allow_redirects=True) #允许302跳转
    if r.status_code == 200:
        content = r.text.strip()
        if content.startswith("<script") and content.endswith("</script>"):  #js跳转跟随
            dir = re.search('window.location.href="(.*)"', content).group(1)  #finadll 返回列表，search返回第一个结果
            target = target + str(dir)
            r = requests.get(target)
            content = r.text
        title = re.findall('<title>(.*)</title>', content)
        print("目标：%s ；标题：%s"%(target,title))

def url_process(url):
    try:
        if 'http' in url:
            get_title(url)
        else:
            url1 = 'http://' + url
            get_title(url1)
            # url2 = 'https://' + url
            # get_title(url2)
    except:
        pass

if __name__ == '__main__':
    file = sys.argv[1]
    url_process('hh88899.com')
    with open(file,'r') as f:
        for url in f:
            url = url.strip()
            threading.Thread(target=url_process,args=(url,)).start() #仅有一个参数时args的格式需要注意
