tasks= []
tasks.append("buying milk")
tasks.append("buying eggs")
tasks.append("freshup")
tasks.append("breakfast")
tasks.insert(0, "wakeup")
print("Current_tasks",tasks)
print("no.of tasks", len(tasks))
tasks.sort()
print("sorted_tasks", tasks)
tasks.reverse()
print("reversed_tasks", tasks)
tasks.pop(0)
print("remaining_tasks", tasks)

tasks.remove("buying eggs")
print("remaining_tasks", tasks)

another_task= input("enter the list of tasks you want to add: " )
tasks.append(another_task)
print("updated_tasks", tasks)
if "breakfast" in tasks:
    print(tasks.index("breakfast"))
else:
    print(f"task not found")
for item in tasks:
    print(f"- {item}")

print(tasks[-2])
print(tasks[-3])
print(tasks[-4])