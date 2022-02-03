users = [{"name": "Kamil", "country": "Poland"}, {"name": "John", "country": "USA"}, {"name": "Yeti"}]
list = [next((sub['name'] for sub in users if sub['country'] == "Poland"), None)]
print(list)
print(type(list))

