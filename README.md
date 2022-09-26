# Sqlib is a small ORM for MariaDB. 
### It provides a simple interface for quick and convenient work with MariaDB

## Installation: 
```bash
pip install sqlib
```

## Usage(example): 
```python
from sqlib import Sqlib
db = Sqlib('localhost', 'root', 'password', 'database')
db.create_table('users', {
    'id': 'int',
    'name': 'varchar(255)',
    'age': 'int'
})
```