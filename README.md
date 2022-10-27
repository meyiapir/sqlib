# Sqlib is a small ORM for MariaDB. 
### It provides a simple interface for quick and convenient work with MariaDB

***
**`VERSION: 0.2.0(ALPHA)`**

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
## New in 0.2.0(ALPHA)
- Fixed some bugs 
- Added new Create(create_table) method
- Added new Insert method
- Fixed some problems 