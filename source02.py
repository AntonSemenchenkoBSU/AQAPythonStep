from source01 import Human, Parent, Kid

firstHuman = Human("Ivan", "Ivanov")
firstParent = Parent("Ivan", "Ivanov", 18, "Office", 500)
firstKid = Kid("Anna", "Ivanov", "School")

print(firstHuman)
print(firstParent)
print(firstKid)

parents = [Parent("Ivan", "Ivanov", 20, "Office", 500), Parent("Petr", "Petrov", 30, "BSU", 700), Parent("Sidr", "Sidorov", 40, "School", 1000), Parent("Anton", "Semenchenko", 35, "School", 400)]
min_salary = 600
average_salary = 0
count = 0

#for cur_parent in parents:
cur_parent_id = 0
while(cur_parent_id < len(parents)):
    cur_parent = parents[cur_parent_id]
    cur_parent_id +=1

    count +=1
    average_salary += cur_parent.salary

    if (cur_parent.age < 40):
        print("This is Yang Parent")

    if (cur_parent.work != "Office" and cur_parent.salary > min_salary):
        print(cur_parent.name)
        print(cur_parent.surname)
        print(cur_parent.work)
        print(cur_parent.salary)
        print("++++++++++++++++++++++++++")
    elif (cur_parent.work == "Office" and cur_parent.salary < min_salary):
        print("We have found him!!!")
        print("++++++++++++++++++++++++++")
        break
    else:
        continue
        #print("=================")

print("Sum salary = ")
print(average_salary)
print("Amount of calculations = ")
print(count)
print("Avgerage salary = ")
print(average_salary / count)