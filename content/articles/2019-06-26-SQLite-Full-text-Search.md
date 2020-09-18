Status: published
Date: 2019-06-26 00:23:42
Author: Jerry Su
Slug: SQLite-Full-text-Search
Title: SQLite Full-text Search
Category: SQL
Tags: SQL, Python

[TOC]

### Sqlite Full-text Search

理解虚表

理解全文本查找

[https://www.sqlite.org/fts5.html](https://www.sqlite.org/fts5.html)

[http://www.sqlitetutorial.net/sqlite-full-text-search](http://www.sqlitetutorial.net/sqlite-full-text-search)

### 

```python
    def _is_to_exec(self, sha1):
        """Check whether the query has been run in the past.
        """
        sql = f'''
                SELECT DISTINCT
                    sha1
                FROM
                    queries
                WHERE queries MATCH '{sha1}'
        '''
        if self._conn.execute(sql).fetchall():
            answer = input('The sql has been run.\nAre you sure to run the sql again? (y/[n]): ')
            if answer.strip().lower() != 'y':
                return False
        return True
```

- Don't use match! match is for full-text search. Use ordinary SQL queries please. Just compare the column sha1 with the sha1sum of the query

- Pease refer to the search function to put the matched queries into the srps table so that you can print them to the user.

- Print out details of the matched queries here. You can simply use the function show_srps if you have put the matched queries into the srps table.

- As a related task, please make the command ./spark_sql.py run support option -i 2, --all. You can then add a -f/--force option to force rerun a query.


