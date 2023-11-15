import os
import sys
import argparse
import posixpath

try:
    from html import escape
except ImportError:
    from cgi import escape
import shutil
import mimetypes
import re
import signal
from io import StringIO, BytesIO

if sys.version_info.major == 3:
    # Python3
    from urllib.parse import quote
    from urllib.parse import unquote
    from http.server import HTTPServer
    from http.server import BaseHTTPRequestHandler

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    server_version = "simple_http_server/" + "0.3.1"

    def do_GET(self):
        """Serve a GET request."""
        fd = self.send_head()
        if fd:
            shutil.copyfileobj(fd, self.wfile)
            fd.close()

    def do_HEAD(self):
        """Serve a HEAD request."""
        fd = self.send_head()
        if fd:
            fd.close()

    def do_POST(self):
        """Serve a POST request."""
        r, info = self.deal_post_data()
        print(r, info, "by: ", self.client_address)
        f = BytesIO()
        f.write(b'<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">')
        f.write(b"<html>\n<title>Upload Result Page</title>\n")
        f.write(b"<body>\n<h2>Upload Result Page</h2>\n")
        f.write(b"<hr>\n")
        if r:
            f.write(b"<strong>Success:</strong>")
        else:
            f.write(b"<strong>Failed:</strong>")
        f.write(info.encode('utf-8'))
        f.write(b"<br><a href=\".\">back</a>")
        f.write(b"<hr><small>Powered By: freelamb, check new version at ")
        # 原始代码地址 可以参考
        f.write(b"<a href=\"https://github.com/freelamb/simple_http_server\">")
        f.write(b"here</a>.</small></body>\n</html>\n")
        length = f.tell()
        f.seek(0)
        self.send_response(200)
        self.send_header("Content-type", "text/html;charset=utf-8")
        self.send_header("Content-Length", str(length))
        self.end_headers()
        if f:
            shutil.copyfileobj(f, self.wfile)
            f.close()

    def deal_post_data(self):
        boundary = self.headers["Content-Type"].split("=")[1].encode('utf-8')
        remain_bytes = int(self.headers['content-length'])
        line = self.rfile.readline()
        remain_bytes -= len(line)
        if boundary not in line:
            return False, "Content NOT begin with boundary"
        line = self.rfile.readline()
        remain_bytes -= len(line)
        fn = re.findall(r'Content-Disposition.*name="file"; filename="(.*)"', line.decode('utf-8'))
        if not fn:
            return False, "Can't find out file name..."
        path = translate_path(self.path)
        fn = os.path.join(path, fn[0])
        while os.path.exists(fn):
            fn += "_"
        line = self.rfile.readline()
        remain_bytes -= len(line)
        line = self.rfile.readline()
        remain_bytes -= len(line)
        try:
            out = open(fn, 'wb')
        except IOError:
            return False, "Can't create file to write, do you have permission to write?"

        pre_line = self.rfile.readline()
        remain_bytes -= len(pre_line)
        while remain_bytes > 0:
            line = self.rfile.readline()
            remain_bytes -= len(line)
            if boundary in line:
                pre_line = pre_line[0:-1]
                if pre_line.endswith(b'\r'):
                    pre_line = pre_line[0:-1]
                out.write(pre_line)
                out.close()
                return True, "File '%s' upload success!" % fn
            else:
                out.write(pre_line)
                pre_line = line
        return False, "Unexpect Ends of data."

    def send_head(self):
        """
        GET和HEAD命令的通用代码。
		这将发送响应代码和MIME标头。
		返回值要么是文件对象
		（除非命令是HEAD，否则调用方必须将其复制到输出文件中，
		并且在任何情况下都必须由调用方关闭），
		要么是None，在这种情况下，调用方无需进一步操作。
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


        """
        path = translate_path(self.path)
        if os.path.isdir(path):
            if not self.path.endswith('/'):
                # redirect browser - doing basically what apache does
                self.send_response(301)
                self.send_header("Location", self.path + "/")
                self.end_headers()
                return None
            for index in "index.html", "index.htm":
                index = os.path.join(path, index)
                if os.path.exists(index):
                    path = index
                    break
            else:
                return self.list_directory(path)
        content_type = self.guess_type(path)
        try:
			#始终以二进制模式读取。以文本模式打开文件可能会导致
			#换行翻译，使内容的实际大小
			#传输*小于*内容长度！
            f = open(path, 'rb')
        except IOError:
            self.send_error(404, "File not found")
            return None
        self.send_response(200)
        self.send_header("Content-type", content_type)
        fs = os.fstat(f.fileno())
        self.send_header("Content-Length", str(fs[6]))
        self.send_header("Last-Modified", self.date_time_string(fs.st_mtime))
        self.end_headers()
        return f

    def list_directory(self, path):
        """
        帮助程序生成目录列表（缺少index.html）。
		返回值为file对象或None（表示错误）。
		无论哪种情况，都会发送标头接口与send_head（）相同。
        """
        try:
            list_dir = os.listdir(path)
        except os.error:
            self.send_error(404, "No permission to list directory")
            return None
        list_dir.sort(key=lambda a: a.lower())
        f = BytesIO()
        display_path = escape(unquote(self.path))
        f.write(b'<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">')
        f.write(b"<html>\n<title>Directory listing for %s</title>\n" % display_path.encode('utf-8'))
        f.write(b"<body>\n<h2>Directory listing for %s</h2>\n" % display_path.encode('utf-8'))
        f.write(b"<hr>\n")
        f.write(b"<form ENCTYPE=\"multipart/form-data\" method=\"post\">")
        f.write(b"<input name=\"file\" type=\"file\"/>")
        f.write(b"<input type=\"submit\" value=\"upload\"/></form>\n")
        f.write(b"<hr>\n<ul>\n")
        for name in list_dir:
            fullname = os.path.join(path, name)
            display_name = linkname = name
            # Append / for directories or @ for symbolic links
            if os.path.isdir(fullname):
                display_name = name + "/"
                linkname = name + "/"
            if os.path.islink(fullname):
                display_name = name + "@"
                # Note: a link to a directory displays with @ and links with /
            f.write(
                b'<li><a href="%s">%s</a>\n' % (quote(linkname).encode('utf-8'), escape(display_name).encode('utf-8')))
        f.write(b"</ul>\n<hr>\n</body>\n</html>\n")
        length = f.tell()
        f.seek(0)
        self.send_response(200)
        self.send_header("Content-type", "text/html;charset=utf-8")
        self.send_header("Content-Length", str(length))
        self.end_headers()
        return f

    def guess_type(self, path):
        """
        参数是PATH（文件名）。
		返回值是表单类型/子类型的字符串，
		可用于MIME内容类型标头。
		默认实现在self.extensions_map表中查找文件的扩展名，默认使用application/octet流；
        """
        base, ext = posixpath.splitext(path)
        if ext in self.extensions_map:
            return self.extensions_map[ext]
        ext = ext.lower()
        if ext in self.extensions_map:
            return self.extensions_map[ext]
        else:
            return self.extensions_map['']

    if not mimetypes.inited:
        mimetypes.init()  # try to read system mime.types
    extensions_map = mimetypes.types_map.copy()
    extensions_map.update({
        '': 'application/octet-stream',  # Default
        '.py': 'text/plain',
        '.c': 'text/plain',
        '.h': 'text/plain',
    })

def translate_path(path):
    # abandon query parameters
    path = path.split('?', 1)[0]
    path = path.split('#', 1)[0]
    path = posixpath.normpath(unquote(path))
    words = path.split('/')
    words = filter(None, words)
    # 获取你的py文件存放的路径
    path = os.getcwd()
    # 可在此自定义路径（如果有其路径）
    path = path+"/file"
    #path = path+"\\save_file"
    print(path)
    for word in words:
        drive, word = os.path.splitdrive(word)
        head, word = os.path.split(word)
        if word in (os.curdir, os.pardir):
            continue
        path = os.path.join(path, word)
    return path
def signal_handler(signal, frame):
    print("You choose to stop me.")
    exit()

# 版本设置 自定义
__version__ = "0.3.1"
def _argparse():
    parser = argparse.ArgumentParser()
    # 一般用户电脑用做服务器，每次开机后，ip4地址可能会发生变化
    # ip = input("请输入IP地址:")
    ip = "192.168.20.240"
    parser.add_argument('--bind', '-b', metavar='ADDRESS', default=ip,
                        help='Specify alternate bind address [default: all interfaces]')
    parser.add_argument('--version', '-v', action='version', version=__version__)
    parser.add_argument('port', action='store', default=9050, type=int, nargs='?',
                        help='Specify alternate port [default: 9050]')
    return parser.parse_args()

def main():
    args = _argparse()
    # print(args)
    server_address = (args.bind, args.port)
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    server = httpd.socket.getsockname()
    print(
        "server_version: " + SimpleHTTPRequestHandler.server_version + ", python_version: " + SimpleHTTPRequestHandler.sys_version)
    print("sys encoding: " + sys.getdefaultencoding())
    print("Serving http on: " + str(server[0]) + ", port: " + str(server[1]) + " ... (http://" + server[0] + ":" + str(
        server[1]) + "/)")
    httpd.serve_forever()


if __name__ == '__main__':
    main()
