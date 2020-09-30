import requests
import re
import sys
import base64
import threading

u = sys.argv[1]
c = sys.argv[2]
qbase64 = qbase64 = (base64.b64encode(u.encode('utf-8'))).decode('utf-8')
cookies={
    "_fofapro_ars_session" : c
}

def req(uu):
    r = requests.get(uu,cookies=cookies)
    content = r.text
    result = re.findall('<a target="_blank" href="(.*)">', content)
    for s in result:
            print(s)


for i in range(5): #非会员只能翻五页
    url = 'https://fofa.so/result?q="'+u+'"&qbase64='+qbase64+str(i)
    threading.Thread(target=req,args=(url,)).start()