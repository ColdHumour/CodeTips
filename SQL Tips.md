SQL TIPS
===



## SQLite

1. Python 调用

       import sqlite3
       
       db = r"E:\lab\test.db"
       conn = sqlite3.connect(db)
       cursor = conn.cursor()

2. 数据库整体架构

       res = cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
       res.fetchall()
       
       for row in conn.execute("pragma table_info('user')").fetchall():
       print(row)
       
       res = cursor.execute("SELECT * FROM sqlite_stat1 LIMIT 1;")
       res.fetchall()

---



## MS SQL Server

### 1、Win7 下远程通过 SSL VPN 访问

- 登录 SSL VPN

- 打开 `控制面板 - 系统与安全- 管理工具 - 数据源（ODBC)`

- `添加 - SQL Server`

- 填写 `名称（DSN），服务器地址`，`下一步`

- `使用用户输入登录 ID 和密码的 SQL Server 验证，登录ID，密码`

- 连接数据库

  ```python
  import sqlalchemy
  
  engine = sqlalchemy.create_engine('mssql+pyodbc://<username>:<password>@<DSN>')
  conn = engine.connect()
  res = conn.execute("XXX")
  res.fetchone()
  ```

  

