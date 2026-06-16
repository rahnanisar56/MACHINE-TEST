students = [{"id": 1, "name": "Rajesh"},
            {"id": 2, "name": "Rahul"},
            {"id": 3, "name": "Sruthi"}]

search_id = int(input("Enter student ID: "))

for student in students:
    if student["id"] == search_id:
        print(student["name"])
        break
else:
    print("Student not found")