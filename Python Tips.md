PYTHON TIPS
===============

主要用于记录各种疑难杂症的解决方案，免得重复劳动。

---

## Jupyter Notebook 输出渲染

转换成 html：

        > jupyter nbconvert --to html -template classic "XXXX.ipynb"   # 渲染 html

转换成 pdf，渲染图片和 mathjax：

        > 浏览器打开 XXXX.html，等 Mathjax 加载完成后“另存网页为 - 全部（.htm, .html)”，一般会存下来一个 XXXX.htm 文件和一个文件夹 XXXX_files

        安装 [wkhtmltopdf](https://wkhtmltopdf.org/)，有需要的话添加环境变量

        > wkhtmltopdf --allow "..\XXXX_files" "XXXX.htm" XXXX.pdf

        即可获得品质较高的 pdf 文件

另一种转成 pdf 的方法，可以应对mathjax等有异步渲染的情况，达到所见即所得：firefox高清截图 + 转写成仅含截图的 html + wkhtmltopdf

    - selenium firefox 打开页面等待渲染完成
    
    - 放大4倍后滚动截图，尽量无损 resize 截图文件到宽为1000，然后用 PIL 拼成一个图
    
    - 写一个html文件，用base64格式写入拼好的图即可
    
    - wkhtml2pdf 转这个新写的html

    - 代码示例

        import os
        import base64
        from io import BytesIO
        from PIL import Image
        from selenium import webdriver

        FIREFOX = r"C:\Program Files\Mozilla Firefox\firefox.exe"
        GECKODRIVER = r"C:\Program Files\Mozilla Firefox\geckodriver.exe"

        target_folder = os.path.join(os.path.expanduser("~"), "Downloads")
        os.chdir(target_folder)

        driver = webdriver.Firefox(firefox_binary=FIREFOX, executable_path=GECKODRIVER)

        driver.set_window_size(1000, 1000)
        driver.execute_script("document.body.style.transform='scale(1)';")
        driver.get("XXX.html")

        # scale 72 dpi to 288 dpi to be printable

        driver.set_window_size(2000, 2000)
        inner_width = driver.execute_script("return window.innerWidth;")
        inner_height = driver.execute_script("return window.innerHeight;")
        # scroll_width = driver.execute_script("return document.body.scrollWidth;")
        scroll_height = driver.execute_script("return document.body.scrollHeight")
        zoomed_width = 4700 + 2000 - inner_width
        zoomed_height = inner_height * 4 + 2000 - inner_height

        driver.execute_script("return document.body.style.overflow='auto';")
        driver.set_window_size(zoomed_width, zoomed_height)
        driver.execute_script("document.body.style.transform='scale(4)';")
        driver.execute_script('document.body.style.MozTransformOrigin="top"');

        onestep = inner_height * 4
        for i in range(scroll_height // inner_height):
            driver.execute_script("window.scrollTo(0, {})".format(i * onestep))
            driver.save_screenshot(os.path.join(target_folder, "{}-{:0>2d}.png".format(title, i)))

        i += 1
        last_height = scroll_height - inner_height * i
        driver.set_window_size(zoomed_width, last_height * 4 + 2000 - inner_height)
        driver.execute_script("window.scrollTo(0, {})".format(i * onestep))
        driver.save_screenshot(os.path.join(target_folder, "{}-{:0>2d}.png".format(title, i)))

        # merge screenshots

        width = 1000
        total_height = 0

        imgs = []
        for f in os.listdir(target_folder):
            if f.startswith(title) and f.endswith("png"):
                im = Image.open(os.path.join(target_folder, f))
                height = int(width/im.size[0]*im.size[1])
                im_resized = im.resize((width, height), Image.ANTIALIAS)
                total_height += height
                imgs.append(im_resized)

        img_merge = Image.new(imgs[0].mode, (width, total_height))
        y = 0
        for img in imgs:
            img_merge.paste(img, (0, y))
            y += img.height

        # output

        file = open(html_path, "w")
        file.write("<!DOCTYPE html><html><head></head><body width=\"{}px\">".format(width))

        buffer = BytesIO()
        img_merge.save(buffer, format="PNG", quality=100)
        file.write("<img style=\"padding:0;margin:0;border:0;\" src=\"data:image/png;base64,")
        file.write(base64.b64encode(buffer.getvalue()).decode('utf-8'))
        file.write("\">")

        file.write("</body></html>")
        file.close()

        os.system("wkhtmltopdf \"{}\" \"{}\"".format(html_path, pdf_path))

--------

## Win32com 各种报错

`AttributeError: module 'win32com.gen_py.xxxxxxx' has no attribute 'CLSIDToClassMap'`：

运行

        import win32com
        print(win32com.__gen_path__)

如果用 jupyter notebook 运行的话先重启 kernal，再打开代码输出的路径，删掉所有文件，重新运行


