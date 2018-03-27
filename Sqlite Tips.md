SQLITE TIPS
===========

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

