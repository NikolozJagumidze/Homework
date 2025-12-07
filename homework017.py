# .append ამატებს ელემენტს სიაში
# .pop შლის ინდექსით მითითებულ ელემენტს სიიდან
#len გამოაქვს სიის სიგრძე


nums = [1, 2, 3, 4, 5]

nums.reverse()
print(nums)


nums1 = [1, 2, 3, 4, 5, 6, 7]

nums1.pop(-1)
nums1.append(8)
print(nums1)


names = ["nika", "luka","demetre","dato","ilia","sandro"]

if len(names) > 4:
    names.append("rati")
    print(names)
elif len(names) < 4:
    names.pop(-1)
    print(names)
else:
    print(names)


fruits = ["banana", "orange", "pear", "cherry", "lemon", "waterlemon"]

fruit_input = input("Please enter a fruit:")

if fruit_input == fruits:
    fruits.pop(fruit_input)
    print(fruits)
elif fruit_input != fruits:
    fruits.append(fruit_input)
    print(fruits)

