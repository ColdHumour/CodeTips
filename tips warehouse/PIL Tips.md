PIL TIPS
=============

---

Windows Vista/7 下show命令无法正常运行解决办法：

    ..\python27\Lib\site-packages\PIL\ImageShow.py

    第99行

    return "start /wait %s && del /f %s" % (file, file) 

    改为

    return "start /wait %s && PING 127.0.0.1 -n 5 > NUL && del /f %s" % (file, file)

---

## 图片和base64字符串互转

    import base64, StringIO
    from PIL import Image

    f = open(r'image.jpg', 'rb')
    imagestr = base64.b64encode(f.read()) 
    f.close()

    im = Image.open(StringIO.StringIO(ls_f.decode('base64')))
    im.show()

    f = open(r'image_new.jpg', 'wb')
    f.write(imagestr.decode('base64'))
    f.close()

## 打开图像

    im = Image.open(r'image.jpg')

## 预览图像

    im.show()

## 改变大小

    out = im.resize((len, wid))

## 裁剪图像

    box = (left, up, right, bottom)
    region = im.crop(box) # 不会影响原图像数据

## 几何变换

    out = im.rotate(degree)                         # 逆时针旋转
    out = im.transpose(Image.FLIP_LEFT_RIGHT)       # 左右翻转
    out = im.transpose(Image.FLIP_TOP_BOTTOM)       # 上下翻转
    out = im.transpose(Image.ROTATE_90)             # 逆时针旋转  90 度
    out = im.transpose(Image.ROTATE_180)            # 逆时针旋转 180 度
    out = im.transpose(Image.ROTATE_270)            # 逆时针旋转 270 度

## 转换色彩模式

    out = im.convert(mode) # 一般RGBA用得比较多，因为可以应用其他颜色通道函数

    '''
    mode   explanation
    1      1位像素，黑和白，存成8位的像素
    L      8位像素，黑白
    P      8位像素，使用调色板映射到任何其他模式
    RGB    3×8位像素，真彩
    RGBA   4×8位像素，真彩+透明通道
    CMYK   4×8位像素，颜色隔离
    YCbCr  3×8位像素，彩色视频格式
    I      32位整型像素
    F      32位浮点型像素
    '''