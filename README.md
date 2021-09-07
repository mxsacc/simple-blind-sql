# simple-blind-sql
blind-sql of pikachu
用dnslog+python3在pikachu靶场进行盲注测试的脚本工具，
目前仅支持输入 "select user" \ "select database" \ "select version" 这三个参数，后期会做进一步优化扩展。
用法：在pyhton3环境中直接运行脚本，C:\python\pyfile>python dnslog.py "select user"
