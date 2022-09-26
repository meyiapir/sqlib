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

## Documentation:
### Creating a table
```python
db.create_table('users', {
    'id': 'int',
    'name': 'varchar(255)',
    'age': 'int'
})
```
### Inserting data
```python
db.insert('users', {
    'id': 1,
    'name': 'John',
    'age': 20
})
```
### Getting data
```python
db.get('users', {
    'id': 1
})
```
### Getting all data
```python
db.get_all('users')
```
### Updating data
```python
db.update('users', {
    'id': 1
}, {
    'name': 'John',
    'age': 20
})
```
### Deleting data
```python
db.delete('users', {
    'id': 1
})
```
### Deleting table
```python
db.drop_table('users')
```
### Checking table
```python
db.table_exists('users')
```
### Checking column
```python
db.column_exists('users', 'name')
```
### Adding column
```python
db.add_column('users', 'name', 'varchar(255)')
```
### Deleting column
```python
db.drop_column('users', 'name')
```
### Checking index
```python
db.index_exists('users', 'name')
```
### Creating index
```python
db.create_index('users', 'name')
```
### Deleting index
```python
db.delete_index('users', 'name')
```
### Getting column type
```python
db.get_column_type('users', 'name')
```
### Getting column size
```python
db.get_column_size('users', 'name')
```
### Getting column default
```python
db.get_column_default('users', 'name')
```