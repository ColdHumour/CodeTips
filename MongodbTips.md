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
    
    (1) find

        clt.find()                     # 集合中的所有文档
        clt.find({key: val})           # 集合中所有键key的值为val的文档

    (2) curser

        # find相关方法返回的对象称为curser
        >> clt.find()
        <pymongo.cursor.Cursor at ...>

        # curser可以看作一个文档生成器，每次以字典的形式生成一个文档
        for item in clt.find():
            ...

    (3) find_one

        # 另外还有find_one，该方法直接返回一个item
        clt.find_one({key: val})       # 集合中所有键key的值为val的某个文档

    (4) _id

        # 如果想按唯一的'_id'查的话需要导入，当然也可以重定义一个'id'为'_id'的string值
        from bson.objectid import ObjectId

- 改

        clt.update(dict1, dict2) # 将dict1更新成dict2，注意update成功的结果是dict1必须唯一，并且不会保留dict1原来的任何信息
    

高级数据操作
-------------

- 查：

    (1) 筛选key

        clt.find({}, {key1: 1, key2: 1})  # 在查询结果中仅留某些key
        clt.find({}, {key1: 0, key2: 0})  # 在查询结果中剔除某些key
    
    (2) 数值比较
    
        clt.find({key: {'$lt':  val}})    # 查询键key的值<val的文档
        clt.find({key: {'$lte': val}})    # 查询键key的值<=val的文档
        clt.find({key: {'$gt':  val}})    # 查询键key的值>val的文档
        clt.find({key: {'$gte': val}})    # 查询键key的值>=val的文档
        clt.find({key: {'$ne':  val}})    # 查询键key的值!=val的文档
        clt.find({key: {'$mod': [val1, val2]}})  # 查询键key的值mod(val1)==val2的文档

    (3) 列表

        clt.find({key: {'$in': [val1, val2, ...]}})   # 查询键key的值在列表中的文档
        clt.find({key: {'$nin': [val1, val2, ...]}})  # 查询键key的值不在列表中的文档
        clt.find({key: {'$all': [val1, val2, ...]}})  # 按数组内容查询，只要$all中的包含于文档即会返回，另外MongoDB中的数组在查询的时候是没有顺序概念的
        clt.find({key: {'$size': n}})  # 查询长度为n的数组
        clt.find(criteria, {key, {'$slice': n}})  # 按数组切片查询，n表示前n个，为负则返回倒数n个，注意$slice默认返回文档的所有键
        clt.find(criteria, {key, {'$slice': [s, n]}})  # [s, n]表示偏移，即数组从s开始的n个元素做切片

    (4) 条件逻辑

        clt.find({key1: val1, key2: val2, ...})  # 查询满足列表中所有条件的文档
        clt.find({'$or': [{key1: val1}, {key2: val2}, ...]}})  # 查询满足列表中任意一项条件的文档

        # AND类型查询最好将最严苛的条件放在最前面，而OR类型查询最好将最宽松的条件放在最前面

        clt.find({key: {'$not': {'$...': ...}})  # 查询键key中不满足某项条件的文档

        # 一个key可以使用多个条件进行查询，但不能对应多个update方法

    (5) 正则表达式

        import re
        clt.find({key: re.compile('.*')})  # 正则匹配查询

    (6) 嵌套文档

        clt.find({key1.key11: val, ...})  # 嵌套文档查询，按值匹配
        clt.find({key: {'$elemMatch': {criterion1, criterion2, ...}}})  # 嵌套文档查询，按条件匹配

    (7) 后续方法        
        
        clt.find(...).limit(n)         # 查询结果只返回前n条
        clt.find(...).skip(n)          # 查询结果跳过前n条

        # skip太多文档会有性能问题，一般建议按需要略过的最后一条文档进行查询，而后进行后续操作

        clt.find(...).sort(key)        # 查询结果按键key的值排序，默认升序
        clt.find(...).sort(key, 1)     # 查询结果按键key的值排序，1表示升序，-1表示降序
        clt.find(...).sort([(key1, 1), (key2, -1), ...]) # 查询结果按多个键排序

        clt.count()                    # 集合中的文档个数
        clt.find(...).count()          # 查询结果中的文档个数

        # 逻辑通的话，方法之间可以连用

    (8) 取随机样本

        最优性能的方法是给每个文档加个random字段，然后按随机样本值查询

- 改

    (1) $set

        clt.update(dict, {'$set': {key: val}})  # 将dict中的键key的值设为val，可以修改key的数据类型（！），key可以是嵌套文档（！）
        clt.update(dict, {'$unset': {key: 1}})  # 将dict中的键key删除
        clt.update(dict, {'$set': {key.0.attr: val}}) # 定位修改，$inc也支持
        clt.update({key.attr: val}, {'$set': {key.$.attr: val2}}) # 未知位置的定位修改，其中第一个参数用作查询定位

    (2) $inc

        clt.update(dict, {'$inc': {key: int}})  # 将dict中的键key的值增加int，只对数字类型有效
        
    (3) stack operation
        
        clt.update(dict, {'$push': {key: val}}) # 向dict中的键key压入一个元素，默认键key的值是数组，而添加的值val可以是文档（！）
        clt.update(dict, {'$pop': {key: 1}})    # 从dict中的键key删除一个元素，1表示从尾部删除，而-1表示从头部删除
        clt.update(dict, {'$pull': {key: val}}) # 从dict中的键key删除值为val的元素

    (4) $addToSet

        clt.update(dict, {'$addToSet': {key: val}}) # 与$push类似但是可以防止键key的元素重复
        clt.update(dict, {'$addToSet': {key: {'$each': [...]}}}) # $each的用处是一次add多个val到key中去

    (5) upsert

        clt.update({}, {'$..': ...}, true)         # upsert，如果查询不到就直接insert
        clt.update({}, {'$..': ...}, false, true)  # 全量更新，对所有的匹配结果都更新




