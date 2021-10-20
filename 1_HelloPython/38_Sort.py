# sort() method   = used with lists
# sort() function = used with iterables

Students = ["Squidward", "Sandy", "Patrick", "Spongebob", "Mr.Krabs"]

# sort() method   = used with lists
Students.sort()             #sortowanie alfabetyczne
Students.sort(reverse=True) #sortowanie odwrotnie
for i in Students:
    print(i)

print("--------------------------------")

# sort() function = used with iterables
sorted_Students = sorted(Students, reverse=True)
for i in sorted_Students:
    print(i)



#lista []
students = [("Squidward", "F", 60),
            ("Sandy", "A", 33),
            ("Patrick","D", 36),
            ("Spongebob","B", 20),
            ("Mr.Krabs","C", 78)]

print("alphabetical--------------------------------")
students.sort()

for i in students:
    print(i)

print("grades--------------------------------")

grade = lambda grades: grades[1]
students.sort(key=grade)#,reverse=True)

for i in students:
    print(i)

print("age--------------------------------")

age = lambda ages: ages[2]
students.sort(key=age)#,reverse=True)

for i in students:
    print(i)



#krotka tuple ()
students = (("Squidward", "F", 60),
            ("Sandy", "A", 33),
            ("Patrick","D", 36),
            ("Spongebob","B", 20),
            ("Mr.Krabs","C", 78))

print("age--------------------------------")
age = lambda ages: ages[2]
#students.sort(key=age)#,reverse=True)
sorted_students = sorted(students,key=age)

for i in students:
    print(i)

