
if __name__ == '__main__':
    phone_book = {}
    n = int(input())
    # Populate phone book dict
    for _ in range( n ):
        name, phone_number = input().split(' ')
        phone_book[name] = int(phone_number)


# Use try/except to query dict for values
for _ in range(n):
    try:
        lookup_name = input()
        if lookup_name in phone_book:
            print('{}={}'.format(lookup_name, phone_book[lookup_name]))
        else:
            print("Not found")
    except EOFError:
        break
