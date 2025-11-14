#if არის კოდი რომელიც მოიცავს პირობას
#elif არის კოდი რომელიც მოიცავს განსხვავებულ პირობას
#else არის კოდი რომელიც წერს ტექსტს იმ შემთხვევაში თუ არცერთი პირობა დაემთხვა მომხმარებლის შემოყვანილ პასუხს


#Break აჩერებს კოდს უსასროლო გამეორებისგან


age = int(input("გთხოვთ შეიყვანოთ თქვენი ასაკი:"))

if age <12:
    print("ბავშვი")
elif age >13 and age <19:
    print("თინეიჯერი")
else:
    print("ზრდასრული")

score = int(input("please enter your points:"))

if score >= 90 and score <= 100:
    print("grade: A")
elif score >= 80 and score <= 89:
    print("grade: B")
elif score >= 70 and score <= 79:
    print("grade: C")
elif score >= 60 and score <= 69:
    print("grade: D")
elif score >= 0 and score <= 59:
    print("grade: F")