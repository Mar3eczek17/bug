# 2.4. Python:
# Create good script to create new list, which only contains users from Poland. Try to do it  with List Comprehension.
users = [{"name": "Kamil", "country": "Poland"}, {"name": "John", "country": "USA"}, {"name": "Yeti"}]
lista = [next((sub['name'] for sub in users if sub['country'] == "Poland"), None)]
print(lista)

# Display sum of first ten elements starting from element 5:
numbers = [1, 5, 2, 3, 1, 4, 1, 23, 12, 2, 3, 1, 2, 31, 23, 1, 2, 3, 1, 23, 1, 2, 3, 123]
print(sum(numbers[5:15]))

# Fill list with powers of 2, n [1..20]


def gen(x):
    i = 2
    for n in range(x + 1):
        yield i
        i <<= 1


a = list(gen(19))
print(a)
