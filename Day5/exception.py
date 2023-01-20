a= 50
b=8

try:
    print(a/b)
except Exception as e:
    print("Hey! you cannot divide a number by zero:", e)

finally:
    print('code run closed')

