import dataset

db = dataset.connect('sqlite:///shopping_list.db')

try:
    db['list'].drop()
except:
    pass

db.begin()
try:
    table = db['list']
    items = [
        { "description": 'Laptop' },
        { "description": 'Mobile' },
        { "description": 'Monitor' },
        { "description": 'Chair' },
        { "description": 'Headphones' }
        ]
    table.insert_many(items)
    db.commit()
    print("Data inserted successfully.")
except:
    db.rollback()
