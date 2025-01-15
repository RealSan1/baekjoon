book = []
total = int(input())
for i in range(9):
    price = int(input())
    book.append(price)

print(total - sum(book))