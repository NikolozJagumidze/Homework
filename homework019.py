# .append() - ამატებს სიტყვას ბოლო ინდექსზე
# .pop() - შლის სიტყვას ჩვენს მიერ მონიშნული ინდექსიდან
#len - გამოაქვს სიის ზომა
# .sort() - ალაგებს სიას ზრდის ან ანბანის მიხედვით
# .clear() - ასუფთავებს სიას
# .reverse() - ატრიალებს სიის ინდექსების მდებარეობას
# .index() - გამოაქვს სიაში მდებარე ელემენტის ინდექსი
# .remove() - შლის ელემენტის ჩაწერილ სახელს
# .insert() - ამატებს ელემენტს ჩვენს მითითებულ ინდექსზე

list=[2, 5, 12, 7, 30, 2]
list.pop(0)
print(list)


list.clear()
list=["Nika", "Gio"]
list.insert(1, "Vaja")
print(list)

list1=[2, 5, 10, 7, 30, 2]

if 10 == list1[5]:
    print(list1.pop(-1))
elif 10 != list1[5]:
    list1.insert(5, 10)
    print(list1)


list2 = ["nika", "gio", "sandro", "dato", "ilia", "luka"]
print(list2.append("aleqsandre"))
print(list2.pop(4))
print(len(list2))
print(list2.sort())
print(list2.clear())
print(list2.reverse())
print(list2.index("nika"))
print(list2.remove("luka"))
print(list2.insert(-1, "dachi"))

