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
