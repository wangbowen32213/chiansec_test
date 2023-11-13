local _n = {
	_VERSION='3.7.0'
}

---------------- 修改以下内容 -----------------------------------
-- 网关真实物理IP
_n_n.LOCALIP="192.168.20.115"

-- 心跳周期秒
_n.HB_DELAY = 60


-- 网关类型
_n.GATEWAY_TYPE = "WEB"

------------------------------------------------------------------------------

---------------- 修改以上内容 -----------------------------------
return _n
		
通用敏感数据	日期	"2023/4/19"				
							
设备敏感信息	JDBC连接串	"jdbc:mysql://localhost:3306/test?user=root&password=&useUnicode=true&characterEncoding=gbk&autoReconnect=true&failOverReadOnly=false"										
设备敏感信息	IMEI	"35-300109-960506-6"								
设备敏感信息	私网IPv4地址	"192.168.80.126"				
设备敏感信息	公网IPv4地址	"103.186.80.22"				
设备敏感信息	MAC地址	"70-B5-E8-72-C2-10"				
设备敏感信息	MAC地址	"70 B5 E8 72 C2 10"				
设备敏感信息	MAC地址	"70:B5:E8:72:C2:10"						
设备敏感信息	URL链接	"https://ztp.zt.chiansec.com/ztpms/#/DataSecurity/DataPolicy/DataDictionary?tab=dictionary"				
设备敏感信息	URL链接	"/data/chiansec/ztpSevenGW/nginx/sbin"				
个人敏感信息	车辆识别代码	"LFV3A24G5C3090044"							
个人敏感信息	车牌号（中国内地）	"京N8P8F8"				
个人敏感信息	宗教信仰	"佛教"				
个人敏感信息	宗教信仰	"基督教"				
个人敏感信息	宗教信仰	"伊斯兰教教"							
个人敏感信息	军官证	"南3045172"				
个人敏感信息	军官证	"南304517"								
个人敏感信息	护照号（中国内地）	"EF1260892"				
个人敏感信息	护照号（中国内地）	"**1260892"								
个人敏感信息	民族	"蒙古族"				
个人敏感信息	民族	"回族"				
个人敏感信息	民族	"满族"				
个人敏感信息	民族	"藏族"			
个人敏感信息	邮箱	"zhonghuahua@chiansec.com"				
个人敏感信息	邮箱	"123@qq.com"				
个人敏感信息	邮箱	"345@163.com"				
个人敏感信息	邮箱	"ee@126.com"							
个人敏感信息	SSN	"123-11-4532"							
个人敏感信息	性别	"：女"				
个人敏感信息	性别	"：男"								

手机号-内地		手机号："19810431042			
个人敏感信息	身份证（中国香港）	"A123456(0)"				
				
个人敏感信息	电话号码（中国内地）	"(010)56108397"				
个人敏感信息	电话号码（中国内地）	"010-56108397"				
							
位置敏感信息	省份（中国内地）	"河南省"							
位置敏感信息	省份（中国内地）	"内蒙古自治区"				
位置敏感信息	省份（中国内地）	"北京市"				
位置敏感信息	省份（中国内地）	"黑龙江省"				
位置敏感信息	省份（中国内地）	"香港特别行政区"				
位置敏感信息	省份（中国内地）	"澳门特别行政区"								
位置敏感信息	GPS位置	"北纬80.90度,东经123.40度"	
											
密钥敏感信息	OpenAI APIkey	"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"				
密钥敏感信息	GitHub 个人访问令牌	"ghp_lkyJGU3jv1xmwk4SDXavrLDJ4dl2pSJMzj4X"				
密钥敏感信息	Bearer Token	"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2ODAxNjIxNTR9.U9orU6YYqXAtpF8uAiw6MS553tm4XxRzxOhz2IwDhpY"				
密钥敏感信息	AccessKeyId	"AKIDW3web9wvWS5X53AzK3B7t0KXriGgblUH"	
			
报错敏感信息	Mysql报错信息	"You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near ‘'1'' LIMIT 0,1’ at line 1。"				
报错敏感信息	Oracle报错信息	"ORA-00942 table or view does not existd"				
报错敏感信息	SQL Server报错信息	"Microsoft SQL Native Client error ‘80040e14’Unclosed quotation mark after the character string\nSELECT id, name FROM users WHERE id=1 UNION SELECT 1, @@version limit 1, 1"				
报错敏感信息	PHP报错信息	"Warning: include_once(./include/main.inc.php) [function.include-once]: failed to open stream: failed to open stream: No such file or directory in"				
报错敏感信息	Fastjson报错信息	"Exception in thread \\\"\\\"main\\\"\\\" com.alibaba.fastjson.JSONException: exepct '[', but ,, pos 42, json : {\\\"\\\"@type\\\"\\\":\\\"\\\"[com.sun.rowset.JdbcRowSetImpl\\\"\\\",\\\"\\\"dataSourceName\\\"\\\":\\\"\\\"ldap://localhost:1389/badNameClass\\\"\\\", \\\"\\\"autoCommit\\\"\\\":true}\\n    at com.alibaba.fastjson.parser.DefaultJSONParser.parseArray(DefaultJSONParser.java:675)\\n    at com.alibaba.fastjson.serializer.ObjectArrayCodec.deserialze(ObjectArrayCodec.java:183)\\n    at com.alibaba.fastjson.parser.DefaultJSONParser.parseObject(DefaultJSONParser.java:373)\\n    at com.alibaba.fastjson.parser.DefaultJSONParser.parse(DefaultJSONParser.java:1338)\\n    at com.alibaba.fastjson.parser.DefaultJSONParser.parse(DefaultJSONParser.java:1304)\\n    at com.alibaba.fastjson.JSON.parse(JSON.java:152)\\n    at com.alibaba.fastjson.JSON.parse(JSON.java:162)\\n    at com.alibaba.fastjson.JSON.parse(JSON.java:131)\\n    at NEW_JNDIClient.main(NEW_JNDIClient.java:8)\\"				
报错敏感信息	Nginx报错信息	"<html>\n<head><title>404 Not Found<\/title><\/head>\n<body>\n<center><h1>404 Not Found<\/h1><\/center>\n<hr><center>nginx/1.8.0<\/center>\n<\/body>\n<\/html>"				
报错敏感信息	Apache报错信息	"AH01276: Cannot serve directory \/var\/www/html\/: No matching DirectoryIndex (index.html) found, and server-generated directory index forbidden by Options directive"				
"data":
            {
                "message": [],
                "total": 0,
                "api_path":"{}".format(user_name),
                "name":"张三，李四，王五",
                "phone": "14834113307,13868645867",
                "phone2":"13919996470,18906503900",
                "email":"123@163.com,google@asdas.com",
                "email2":"456@163.com,dsadfag@qq.com",
                "ID":"110101199108157236,13010319980426041X",
                "Bank_card":"6222027183530478298,6222024493338009203",
                "yapi":"Mockjs",
                "yapi_geren":"yapi",
                "yapi_weizhi":"username",
                "yapi_shebei":"test",
                "yapi_qiye":"enterprise",
                "yapi_all":"python",
                "yapi_api":"mock",
                "YApi":"YApi",
                "test-user":"test-user",
                "ruomima":"111,222,333,444,555,666,777,123456,，version，test"
            }

