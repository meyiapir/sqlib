# Sqlib is a small ORM for MariaDB. 
### It provides a simple interface for quick and convenient work with MariaDB

***
**`VERSION: 0.1.8(ALPHA)`**

## Installation(Temporarily not working): 
```bash
pip install sqlib
```

## Usage(example): 
```python
from sqlib import Sqlib

db = Sqlib(host="localhost",
           user="root",
           password="root_pass",
           database="tests")

data = db.select(
    table="table_name", 
    columns=["age", "email"],
    where={"name": "martin"}, 
    limit=2)

for row in data:
    print(row[0], row[1])
```