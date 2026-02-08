#1.
numbers = [1, 2, 3, 4, 5]
result = [n * n for n in numbers]
print(result)

#2.
nums = [3, 10, 15, 20, 25, 30]
evens = [num for num in nums if num % 2 == 0]
print(evens)

#3.
names = ["dan", "sara", "noa"]
upper_names = [name.upper() for name in names]
print(upper_names)

#4.
nums = [20, 55, 70, 10, 90]
result = [n / 2 for n in nums if n > 50 ]
print(result)

#5.
words = ["hi", "python", "is", "awesome"]
lengths = [len(w) for w in words if len(w) > 2]
print(lengths)

#6.
squares = []
for i in range(10):
    squares.append(i * i)

#7.
evens = []
for i in range(50):
    if i % 2 == 0:
        evens.append(i)

#8.
first_letters = []
for name in ["Alice", "Bob", "Charlie"]:
    first_letters.append(name[0])

#9.
small_nums = []
for n in nums:
    if n < 100:
        small_nums.append(n)

#10.
modified = []
for n in nums:
    if n > 10:
        modified.append(n + 5)
    else:
        modified.append(n)

#11.
multiplied_by_3 = [n * 3 for n in range(1,20)]

#12.
divisible_by_5 = [n for n in nums if n % 5 == 0]

#13.
reversed_words = [w[::-1] for w in words]

#14.
squares_divisible_by_3 = [n * n for n in range(30) if n % 3 == 0]

#15.
if_even = [True if n % 2 == 0 else False for n in range(1,15)]

#16.
temperatures = [15, 30, 45, 60, 75, 90]
weather_list = ["HOT" if t > 30 else "OK" if 20 <= t <= 30 else "COLD" for t in temperatures]

#17.
first_names = ["Dan", "Noa", "Yossi"]
last_names = ["Levi", "Cohen", "Mizrahi"]
names_combination = [first_names[i] + " " + last_names[i] for i in range(len(first_names))]

#18.
nums1 = [0, 1, 2]
nums2 = [0, 1, 2]
combination = [(i, j) for i in nums1 for j in nums2]

#19.
combination = [(x,y) for x in range(1, 20) for y in range(1,20) if 1 <= x <= 10 or 1 <= y <= 10 or (x + y) % 4 == 0]

#20.
users = [
{"name": "Dan", "age": 17},
{"name": "Noa", "age": 25},
{"name": "Yossi", "age": 15},
{"name": "Maya", "age": 31}
]
names = [dict["name"] for dict in users if dict["age"] >= 18]
