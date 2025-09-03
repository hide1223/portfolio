def add(x,y):
    return x + y


def subtract(x,y):
    return x - y


def multiply(x,y):
    return x * y


def divide(x,y):
    if y != 0:
        return (round(x / y, 3))
    else:
        return "エラー: 0で割ることはできません"
    

num1 = float(input('数字を入力してください:'))

while True:
    choice = input('選択してください (+,-,*,/) またはqで終了:')

    if choice == 'q':
        print('計算を終了します 最終結果:', num1)
        break

    if choice not in ['+', '-', '*', '/']:
        print('無効な選択です。もう一度選んでください。')
        continue

    num2 = float(input('数字を入力してください:'))

    if choice == '+':
        result = add(num1, num2)
        print(f'{num1} + {num2} = {result}')
        num1 = result

    elif choice == '-':
        result = subtract(num1, num2)
        print(f'{num1} - {num2} = {result}')
        num1 = result

    elif choice == '*':
        result = multiply(num1, num2)
        print(f'{num1} * {num2} = {result}')
        num1 = result

    elif choice == '/':
        result = divide(num1, num2)
        print(f'{num1} / {num2} = {result}')
        if isinstance(result, (int, float)):
            num1 = result

    else:
        print('計算できませんでした。')
