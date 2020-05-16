def get_book(index):

    items = ['note', 'notebook', 'sketchbook']

    try:
        return items[index]
    except (IndexError, TypeError) as e:
        print(f'例外が発生しました:{e}')
        return '範囲外です'

# IndexErrorを発生させる

print(get_book(3))