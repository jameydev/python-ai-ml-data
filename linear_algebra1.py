import numpy as np
## Element-wise multiplication without utilizing linear algebra

x = [1, 2, 3]
y = [4, 5, 6]

product = []
for i in range(len(x)):
    product.append(x[i] * y[i])

print('product: ')
for item in product:
    print(item)
print('\n')

## Element-wise multiplication utilizing linear algebra
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

print(x * y)