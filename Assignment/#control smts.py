data = {
    1: {'name': 'rice', 'price': 23},
    2: {'name': 'oli', 'price': 223},
    3: {'name': 'tea', 'price': 233},
    4: {'name': 'coffe', 'price': 523},
    5: {'name': 'cook', 'price': 283},
    6: {'name': 'bread', 'price': 1283}
}

for i in data:
    print(f"{i}.   {data[i]['name']}   - $ {data[i]['price']}")

items = list(map(int, input("Enter the product indexes(1 2 3 4): ").split()))

total = 0
s = set()
for i in items:
    if i not in s:
        c = items.count(i)
        print(f"{data[i]['name']}-{c} x ${data[i]['price']} = ${data[i]['price'] * c}")
        total += data[i]['price'] * c
        s.add(i)

print(f"Total biller: ${total}")
