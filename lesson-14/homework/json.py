# write a Python script that reads the students.jon JSON file and prints details of each student.
import json
with open('extra_practise\\students.json') as file:
    data = json.load(file)
    for i in data:
        for j in data['students']:
            print(j)
