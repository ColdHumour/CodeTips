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