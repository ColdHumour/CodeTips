MONGODB TIPS
=================

---

MongoDB: http://www.mongodb.org/

PyMongo: http://api.mongodb.org/python/current/index.html 

RoboMongo: http://www.robomongo.org/

---

MongoDB下载与安装
-------------------

- 官网下载安装包

- 解压到安装目录

PyMongo下载与安装
-------------------

    cmd: pip install pymongo
    cmd: pip install --upgrade pymongo

RoboMongo下载与安装
-------------------

- 官网下载安装包，直接安装

---

MongoDB服务器启动
------------------

- 创建自定义数据库目录

- 执行以下命令

        cmd: cd D:\...\MongoDB\bin          # 安装路径
        cmd: mongod --dbpath F:\lab\...     # 数据库路径

    出现 

        waiting for connections on port XXXX

- 在浏览器中输入

        http://localhost:XXXX/

    出现 
        You are trying to access MongoDB on the native driver port. For http diagnostic access, add 1000 to the port number

    则启动成功

RoboMongo启动
---------------

- 双击打开，根据服务器ip和端口连接即可

- 在可视化界面中，可以看到数据库名称和内容

PyMongo启动
-------------

- 在ipython或ipython notebook环境下：

        import pymongo

- 创建与服务器的连接：

        conn = pymongo.Connection('localhost', XXXX)    # 端口与上面服务器的port一致
        # conn = pymongo.Connection(host = '127.0.0.1', port = 27017)

        >> conn
        Connection('localhost', XXXX)

---

数据库操作
-------------

- 连接数据库

        db = conn.db_name    # 数据库名不清楚可通过Robomongo查询

        >> db
        Database(Connection('localhost', XXXX), db_name)      

- 连接集合
        
        db.collection_names()    # 查询所有可用集合的名称

        clt = db.clt_name

        >> clt
        Collection(Database(Connection('localhost', XXXX), db_name), clt_name) 

    由此进入对数据的直接操作

简单数据操作
--------------

- 增

        clt.insert({'text': 'hello world'})               # 插入文档
        clt.insert([{'text': 'new1'}, {'text': 'new2'}])  # 批量插入文档

        # 向某个集合中插入的字典在MongoDB中被称之为“文档”
        # 批量插入比执行多次插入更快

- 删

        clt.remove()                   # 清空集合
        clt.remove({'text': 'new1'})   # 清除所有键text的值为new1的文档

        # 删除无法恢复！

        # 如果要清空集合，一个更快速的方法是直接在数据库层面删除集合
        db.drop_collection(clt_name)

- 查

        clt.find()                     # 集合中的所有文档
        clt.find({key: val})           # 集合中所有键key的值为val的文档
        clt.find(...).sort('text')     # 查找结果按键text的值排序

        clt.count()                    # 集合中的文档个数
        clt.find(...).count()          # 查找结果中的文档个数

        # find相关方法返回的对象称为curser
        >> clt.find()
        <pymongo.cursor.Cursor at ...>

        # curser可以看作一个文档生成器，每次以字典的形式生成一个文档
        for item in clt.find():
            ...

        # 另外还有find_one，该方法直接返回一个item
        clt.find_one({key: val})       # 集合中所有键key的值为val的某个文档

        # 如果想按唯一的'_id'查的话需要导入，当然也可以重定义一个'id'为'_id'的string值
        from bson.objectid import ObjectId

- 改

        clt.update(dict1, dict2) # 将dict1更新成dict2

        # 注意update成功的结果是dict1必须唯一，并且不会保留dict1原来的任何信息

        clt.update(dict, {'$set': {key: val}})  # 将dict中的键key的值设为val，可以修改key的数据类型（！），key可以是嵌套文档（！）
        clt.update(dict, {'$unset': {key: 1}})  # 将dict中的键key删除

        clt.update(dict, {'$inc': {key: int}})  # 将dict中的键key的值增加int，只对数字类型有效
        
        clt.update(dict, {'$push': {key: val}}) # 向dict中的键key压入一个元素，默认键key的值是数组，而添加的值val可以是文档（！）
        clt.update(dict, {'$pop': {key: 1}})    # 从dict中的键key删除一个元素，1表示从尾部删除，而-1表示从头部删除
        clt.update(dict, {'$pull': {key: val}}) # 从dict中的键key删除值为val的元素

        clt.update(dict, {'$addToSet': {key: val}}) # 与$push类似但是可以防止键key的元素重复
        clt.update(dict, {'$addToSet': {key: {'$each': [...]}}}) # $each的用处是一次add多个val到key中去

        clt.update(dict, {'$set': {key.0.attr: val}}) # 定位修改，$inc也支持
        clt.update({key.attr: val}, {'$set': {key.$.attr: val2}}) # 未知位置的定位修改，其中第一个参数用作查询定位

        clt.update({}, {'$..': ...}, true)         # upsert，如果查询不到就直接insert
        clt.update({}, {'$..': ...}, false, true)  # 全量更新，对所有的匹配结果都更新

高级数据操作
-------------

- 查：
        clt.find({}, {key1: 1, key2: 1})  # 在查询结果中仅留某些key
        clt.find({}, {key1: 0, key2: 0})  # 在查询结果中剔除某些key


