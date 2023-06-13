CRAWLER TIPS
==============

## Selenium PhantomJS

    * pip install selenium

    * Download (PhantomJS for windows)[http://phantomjs.org/]

    * Extract to self-defined path, remember the path

    * using:

        from selenium import webdriver
        driver = webdriver.PhantomJS(executable_path="<phantomjs.exe path>")

## Selenium Firefox

    * pip install selenium

    * 下载 [geckodriver](https://github.com/mozilla/geckodriver/releases)

    * 将 geckodriver.exe 移至 ~/Anaconda3

    * 检查 ~\Lib\site-packages\selenium\webdriver\firefox\webdriver.py 中 WedDriver.__init__() 的参数

        executable_path="geckodriver"

## browsermob-proxy

    * 下载[browsermob-proxy](https://github.com/lightbody/browsermob-proxy/releases)，解压

    * 如果没有 java 环境，下载 [java](https://www.java.com/zh_CN/)，并将 ~/java/bin 添加到环境变量

    * pip install browsermob-proxy

    * ~\browsermob-proxy\bin\browsermob-proxy.bat 是核心路径

    * 使用方法（以 Phantomjs 为例）：

            from browsermobproxy import Server
            from selenium import webdriver

            server = Server("~\browsermob-proxy\bin\browsermob-proxy.bat")
            server.start()
            proxy = self.server.create_proxy()

            service_args = ["--proxy={}".format(proxy.proxy), '--ignore-ssl-errors=yes']
            cap = dict(webdriver.common.desired_capabilities.DesiredCapabilities.PHANTOMJS)
            cap['phantomjs.page.settings.userAgent'] = (
                'Mozilla/5.0 (X11; Linux x86_64) '
                'AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/60.0.3112.113 Safari/537.36)'
            )

            driver = webdriver.PhantomJS(
                executable_path="~phantomjs.exe",
                desired_capabilities=cap,
                service_args=service_args)

            har = proxy.new_har(options={'captureContent':True})
            driver.get(url)

            print(proxy.har)

            # proxy.har 是一个列表，包含了页面加载的所有 web traffic
            # 从中可以解析需要的 request 和 response，尤其是 XMLHttpRequest 相关


---

## scrapy

scrapy doc: http://doc.scrapy.org/en/latest/index.html#

Chinese: http://scrapy-chs.readthedocs.org/zh_CN/0.24/

---

Install
----------

zope.interface: 

    python setup.py install

w3lib: 

    python setup.py install

scrapy: 

    python setup.py install

service-identity: 

    move .egg to anaconda/scripts then easy_install.exe service-identity.egg 

Install Scrapy

    pip install scrapy

Download and install 2008 Visual C++ Redistributable (compiler)

    http://www.microsoft.com/en-us/download/details.aspx?id=29

Download pywin32 executable and install it

    http://sourceforge.net/projects/pywin32/files/pywin32/

---

Basic Commands
------------------

####1. 创建工程

    cmd: scrapy startproject XXX

####2. 运行scrapy

    cmd: scrapy crawl spiderName

---

Scrapy Cotents
------------------

####3. items: 定义要从页面获取哪些东西

    from scrapy.item import Item, Field

    class XXXItem(Item):
        a = Field()
        b = Field()

**注：** 对Item的实例可以采用类似字典的语法，定义的a、b可以通过instace['a']的方式来赋值和访问


####4. pipelines: 对获取的Item的处理

    class XXXPipeline(object):
        def process_item(self, item, spider):
            file = open('...', 'a')
            file.write(...)
            file.close()
            return item['...']

**注：** pipelines的使用需要在settings.py下加入ITEM_PIPELINES字段

**注：** 注意到process_item的参数中有item和spider，所以可以针对不同的item和spider做不同的处理，这一点在多个Item、多个Pipeline和多个Spider时很有用处

**注：** pipelines返回的东西会在log中打印出来

**注：** 中文的输入输出记得转码


####5. settings：参数设置

各项参数设置，详情见http://doc.scrapy.org/en/latest/topics/settings.html
    
    DOWNLOAD_DELAY = 2                  # 爬取间隔，单位为s
    RANDOMIZE_DOWNLOAD_DELAY = True     # 随机爬取间隔
    # DEPTH_LIMIT = 1                     # 爬取深度，相对start_urls而言
    
    ITEM_PIPELINES = {                  # 加入PIPELINE对ITEM进行处理, 修改XXX!
        'XXX.pipelines.XXXPipeline': 300
        # 'XXX.pipelines.MyImagesPipeline': 1,
        # 'scrapy.contrib.pipeline.images.ImagesPipeline': 1,
    }

    DOWNLOADER_MIDDLEWARES = {          
        # 随机User-Agent, 修改XXX!
        'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
        'XXX.middlewares.RotateUserAgentMiddleware': 400,   
        
        # 加代理, 修改XXX!
        # 'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
        # 'XXX.middlewares.ProxyMiddleware': 100
    }

    # LOG_ENABLED = True                  # 允许输出LOG信息
    # COOKIES_ENABLED = False             # 禁止COOKIES
    # COOKIES_DEBUG = False               # 在输出中打印request和response的cookie信息

    # IMAGES_STORE = '...'                # 图片存储位置，会自动在项目目录下创建
    # IMAGES_MIN_HEIGHT = 110             # 图片最小高度，过滤小图
    # IMAGES_MIN_WIDTH  = 110             # 图片最小宽度，过滤小图

    # DUPEFILTER_CLASS = 'XXX.middlewares.CustomFilter' # 自定义重复url过滤器，修改XXX!
    # DUPEFILTER_DEBUG = True             # 打印所有重复url过滤信息


####6. 在spiders下创建自己的spider

    # -*- coding: utf-8 -*-

    from scrapy.spider import Spider
    from scrapy.http import Request
    from XXX.items import XXXItem   # 修改XXX!

    class XXXSpider(Spider):
        name = '...'
        allowed_domains = [...]
        start_urls = [
            ...
        ]

        def parse_item(self, response):
            sites = response.xpath('...').extract()
            items = []
            for site in sites:
                item = SpiTestItem()
                ...
                items.append(item)
            return items

**注：** Spider类属性

    download_delay = 1            # 爬取速度，单位s
    allowed_domains = [url...]    # 允许域名，控制爬取范围 
    start_urls = [url...]         # 起始爬行页面

**注：** spider的parse输出可以采用yield。如果yield的是item或者item列表，则储存起来后续通过pipelines处理；如果yield的是Request或者Request列表，则会将Request加到后续任务列表中。Request可以直接发起：

    yield Request(url, callback=self.parse_item)

####7. CrawlSpider：自己爬的spider

    from scrapy.contrib.spiders import CrawlSpider, Rule  
    from scrapy.contrib.linkextractors import LinkExtractor
    from scrapy.http import Request
    from XXX.items import XXXItem   # 修改XXX!
      
    class XXXCrawlSpider(CrawlSpider):

        name = ...
        allowed_domains = [...]  
        start_urls = [
            ...
        ]  

        rules = [  
            Rule(LinkExtractor(allow=('...', ), restrict_xpaths=(xpath, )),  
                 callback='parse_item'),  
        ]
      
        def parse_item(self, response):  
            item = XXXItem()
            item[...] = response.xpath(re...).extract()
            yield item

**注：** CrawlSpider类属性

    download_delay = 1            # 爬取速度，单位s
    allowed_domains = [url...]    # 允许域名，控制爬取范围 
    start_urls = [url...]         # 起始爬行页面

**注：** spider的parse输出可以采用yield。如果yield的是item或者item列表，则储存起来后续通过pipelines处理；如果yield的是Request或者Request列表，则会将Request加到后续任务列表中。Request可以直接发起：

    yield Request(url, callback=self.parse_item)

**注：** CrawlSpider的一些重要方法:

* 避免start_url不被处理
    
        def parse_start_url(self, response):
            return self.parse_item(response)

* 避免start_url重复爬取

        def start_requests(self):  
            for url in self.start_urls:
                yield Request(url, dont_filter=False)

* 使用start_url发起request时添加cookies

        def start_requests(self):  
            for url in self.start_urls:
                yield Request(url, cookies=[{...},])

* 处理爬到的links，在Rule中通过process_links调用

        def process_links(self, links):
            for link in links:
                link.url = link.url.replace('aaa', 'bbb')
            return links

* 处理继续爬行的request，在Rule中通过process_request调用

        def process_request(self, request):
            request = request.replace(url='aaa')
            return request



--------

Details
----------------------

####8. XPath Selector：页面元素获取

Selector可以使用XPath语法来获取页面元素，现在scrapy中response也可以直接使用XPath

    from scrapy import Selector

Selector有以下四种方法

* xpath()：返回selectors列表, 每一个select表示一个xpath参数表达式选择的节点
* css()：返回一系列的selectors，每一个select表示一个css参数表达式选择的节点
* extract()：返回一个unicode字符串，该字符串为XPath选择器返回的数据
* re()： 返回unicode字符串列表，字符串作为参数由正则表达式提取出来

以下是一些XPath表达式的例子和他们的含义，更多看 http://www.w3school.com.cn/xpath/

* /html/head/title: 选择HTML文档&lt;head>元素下面的&lt;title> 标签。
* /html/head/title/text(): 选择前面提到的&lt;title>元素下面的文本内容
* //td: 选择所有&lt;td>元素
* //div[@class="mine"]: 选择所有包含class="mine"属性的div标签元素

XPath简单语法

* nodename: 选取此节点的所有子节点。
* /: 从根节点选取。
* //: 从匹配选择的当前节点选择文档中的节点，而不考虑它们的位置。
* .: 选取当前节点。
* ..: 选取当前节点的父节点。
* @: 选取属性。

**注：** 嵌套选择器相关见以下网址

http://doc.scrapy.org/en/0.14/topics/selectors.html#topics-selectors-nesting-selectors
http://doc.scrapy.org/en/0.14/topics/selectors.html#topics-selectors-relative-xpaths

**注：** 如何给XPath选取内容设置默认值?

* XPath选取节点内的文本时，如果节点内容为空，XPath不会返回一个空字符串，而是什么都不返回，对应到列表就是对应的列表项少一项，有时候需要这样的空字符串当默认值。XPath中有一个concat函数可以实现这种效果：

        text = response.xpath("concat(//span/text(), '')").extract()


####8. LinkExtractor：链接提取器，用于增加爬取的Rule

    class scrapy.contrib.linkextractors.LinkExtractor(  
        allow=(), deny=(), allow_domains=(), deny_domains=(), deny_extensions=None,
        restrict_xpaths=(), tags=('a','area'), attrs=('href',), canonicalize=True,
        unique=True, process_value=None)

LinkExtractor含有以下参数，见http://doc.scrapy.org/en/latest/topics/link-extractors.html

* allow：re or list. 满足括号中正则表达式的值会被提取，如果为空，则全部匹配。
* deny：与这个正则表达式(或正则表达式列表)不匹配的URL一定不提取。
* allow_domains：str or list. 会被提取的链接的domains。
* deny_domains：一定不会被提取链接的domains。
* restrict_xpaths：str or list. 使用xpath表达式，和allow共同作用过滤链接，注意这里必须返回迭代器，即结尾不能是@...
* tags：str or list. 指定从哪些标签抓取链接，默认('a', 'area')
* attrs：list. 指定何种类型的属性为链接

**注：** .jpg不属于link，用LinkExtractor抓不出来


####9. Rules：爬行规则

在CrawlSpider当中使用，Rules含有以下参数，见http://doc.scrapy.org/en/latest/topics/spiders.html#scrapy.contrib.spiders.CrawlSpider.rules

* LinkExtractor：提取链接
* callback：处理方法
* process_links：处理link，可以设置过滤器或者替换字段等等，需要自定义方法
* process_request：用于处理request，比如加cookie等等，需要自定义方法
* follow：是否跟进，默认为True


####10. Request: 请求

Request使用的时候多作为人工在处理页面时发起，一般在修改start_request函数或者request时遇到。Request所有的参数如下：

    class scrapy.http.Request(url[, callback, method='GET', headers, body, cookies, meta, encoding='utf-8', priority=0, dont_filter=False, errback])

使用时需要导入：

    from scrapy.http import Request

修改参数通过replace来实现 
    
    request = request.replace(params=...)

* url：网址
* callback：处理方法
* cookies：所带cookies
* dont_filter：url是否进行重复过滤


-----

Extensions
-------------

####11. 页面解析与调试

    cmd: scrapy shell url...
    
    cmd: request = request.replace(cookies=[{'name':...}])  # 在请求中加入cookies
    cmd: fetch(request)  # 刷新回复

    cmd: view(response)  # 在浏览器中看回复
    cmd: response.xpath('//title').extract()  # 使用Selector解析回复
   
    cmd: from scrapy.contrib.linkextractors import LinkExtractor
    cmd: LinkExtractor(allow=('...',), restrict_xpaths=('...',)).extract_links(response)


####12. User-Agent: 防止被ban

User-Agent是中间件的一部分，可通过创建middlewares.py于项目目录下，并在settings.py中加入DOWNLOADER_MIDDLEWARES字段来实现使用自定义的UserAgent中间件：

    # -*-coding:utf-8-*-  
  
    import random
    from scrapy.contrib.downloadermiddleware.useragent import UserAgentMiddleware  

    class RotateUserAgentMiddleware(UserAgentMiddleware):  
      
        def __init__(self, user_agent=''):  
            self.user_agent = user_agent  
      
        def process_request(self, request, spider):  
            ua = random.choice(USER_AGENT_LIST)  
            if ua: request.headers.setdefault('User-Agent', ua)

    USER_AGENT_LIST = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 "  
        "(KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",  
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 "  
        "(KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",  
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 "  
        "(KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",  
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 "  
        "(KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",  
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 "  
        "(KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",  
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 "  
        "(KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",  
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 "  
        "(KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",  
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "  
        "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",  
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 "  
        "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",  
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 "  
        "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",  
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "  
        "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",  
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "  
        "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",  
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "  
        "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",  
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "  
        "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",  
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 "  
        "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",  
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "  
        "(KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",  
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 "  
        "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",  
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 "  
        "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"]


####13. COOKIES

scrapy会将cookie信息一直带着，所以一般而言，只在start_urls中加cookies就够了，如果需要使用cookies访问必须重载Spider中的start_requests

    def start_requests(self):  
        for url in self.start_urls:
            yield Request(url, cookies = [
                {'name': ..., 'value': ..., 'domain': ..., 'path': ...}
            ])

对于CrawlSpider的rules，可以写add_cookies方法，并在其中加入 process_request = 'add_cookies' 参数

    rules = [  
            Rule(LinkExtractor(...),  
                 callback='...', process_request = 'add_cookies') 
        ]

    def add_cookies(self, request):
        request = request.replace(
            cookies=[
                {'name': ..., 'value': ..., 'domain': ..., 'path': ...}
            ]
        )
        return request

对于直接生成的Request，直接在参数中加入cookies字段

    from scrapy.http import Request

    yield Request(url, callback='...', cookies=[{...},])


####14. 代理

在中间件middlewares.py中加入以下类，并在settings.py中添加相应字段

    import base64

    class ProxyMiddleware(object):
        def process_request(self, request, spider):
            request.meta['proxy'] = "http://127.0.0.1:8087"
            proxy_user_pass = "USERNAME:PASSWORD"
            encoded_user_pass = base64.encodestring(proxy_user_pass)
            request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass

####15. 图片

scrapy有内置的图片下载pipeline，如果要下载图片可以直接使用该pipeline。

使用ImagesPipeline之前，必须在Item中定义images和image_urls两个Field：
    
    class XXXItem(Item):  # 修改XXX!
        image_urls = Field()
        images = Field()

随后用xpath把response中的图片链接都爬下来放到image_urls里即可

    item = XXXItem()   # 修改XXX!
    item['image_urls'] = response.xpath('...').extract()

settings中需要启用ImagesPipeline，并且需要加入图片存储和过滤的相关字段：

    IMAGES_STORE = '...'
    IMAGES_MIN_HEIGHT = 110
    IMAGES_MIN_WIDTH  = 110

    ITEM_PIPELINES = {
        'scrapy.contrib.pipeline.images.ImagesPipeline': 1,
    }

最好重写pipeline的部分方法，以使得其可以保存图片原本的文件名和后缀：

    from scrapy.http import Request  
    from scrapy.contrib.pipeline.images import ImagesPipeline  
    from scrapy.exceptions import DropItem  

    class MyImagesPipeline(ImagesPipeline):  
        def file_path(self, request, response=None, info=None):  # 存储目录和文件名 
            image_id = request.url.split('/')[-1]  
            return image_id  

        def get_media_requests(self, item, info):                # 发起链接
            for image_url in item['image_urls']:  
                yield Request(image_url)  

        def item_completed(self, results, item, info):           # logging和后续处理
            image_paths = [x['path'] for ok, x in results if ok]  
            if not image_paths:  
                raise DropItem("Item contains no images")  
            return '\n'.join(item['image_urls'])

此时settings也要适当地改变pipeline的载入字段：
    
    ITEM_PIPELINES = {
        'XXX.pipelines.MyImagesPipeline': 1,  # 修改XXX!
    }


####16. 重复网址过滤器

scrapy有默认的网址过滤器，可以避免爬取重复的页面，但是start_urls里的网址并不会纳入到重复过滤的范围中，为实现这一点，可以重写start_requests:

    def start_requests(self):  
        for url in self.start_urls:
            yield Request(url, dont_filter=False)

此外，如果有特殊的重复过滤需求，比方说根据url中的某个字段来自定义重复过滤，也可以自定义重复过滤器。方法是在middlewares中加入一个新的重复过滤器类：

    from scrapy.dupefilter import RFPDupeFilter

    class CustomFilter(RFPDupeFilter):
        def __init__(self, path=None, debug=False):
            self.urls_seen = set()
            RFPDupeFilter.__init__(self, path, debug)

        def request_seen(self, request):
            url_feature = request.split('/')[2]
            if url_feature in self.urls_seen:
                return True
            else:
                self.urls_seen.add(url_feature)

相应地，需要在settings.py中加入语句来调用自定义的重复过滤器：

    DUPEFILTER_CLASS = 'DBImg.middlewares.CustomFilter'
    DUPEFILTER_DEBUG = True

其中DEBUG为True的目的是打印所有的重复url过滤信息


####17. 并发

对于载入页面时间较长的网页来说，降低并发数量并加长下载时间是比较有效的减少Timeout Error的方法，在settings.py当中可以进行修改相关参数

对于下载时间：

    DOWNLOAD_DELAY
    # The amount of time (in secs) that the downloader should wait before downloading consecutive pages from the same website. This can be used to throttle the crawling speed to avoid hitting servers too hard. Decimal numbers are supported. Example: Default: 0

    DOWNLOAD_TIMEOUT
    # The amount of time (in secs) that the downloader will wait before timing out. Default: 180

对于并发相关：

    CONCURRENT_ITEMS
    # Maximum number of concurrent items (per response) to process in parallel in the Item Processor (also known as the Item Pipeline). Default: 100

    CONCURRENT_REQUESTS
    # The maximum number of concurrent (ie. simultaneous) requests that will be performed by the Scrapy downloader. Default: 16

    CONCURRENT_REQUESTS_PER_DOMAIN
    # The maximum number of concurrent (ie. simultaneous) requests that will be performed to any single domain. Default: 8