# Independent-development-tools——get_related_ip.py
通过爬取fofa结果得到某域名的关联ip（如多域名公用https证书的情况，可获取站群IP）

## 用法 ##

    python3 get_related_ip.py  'domain'  'cookie_for_fofa'

cookie填入` _fofapro_ars_session`字段的值即可