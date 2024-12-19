import requests
import numpy as np

payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('https://requests.readthedocs.io/en/latest/user/quickstart/#make-a-request/get', params=payload)
print(r.url)
d = requests.get('https://requests.readthedocs.io/en/latest/user/quickstart/#make-a-request/get', data=payload)
print(d.text)


array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

sum_array = np.sum(array)
mean_array = np.mean(array)
std_array = np.std(array)
max_array = np.max(array)
min_array = np.min(array)

print("Созданный массив:", array)
print("Сумма элементов:", sum_array)
print("Среднее значение:", mean_array)
print("Стандартное отклонение:", std_array)
print("Максимальное значение:", max_array)
print("Минимальное значение:", min_array)
