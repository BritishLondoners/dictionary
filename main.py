# dictionary of students (id -> details)
student_data = {
    "id1" : {"name": "Julia", "class": "V-Blue", "subject_integration": "English Language, BD Studies, History"},
    "id2" : {"name": "Andrew", "class": "V-Red", "subject_integration": "Algebra, Free Writing, Science"},
    "id3" : {"name": "Lavinia", "class": "V-Yellow", "subject_integration": "English Literature, Computing, Bangla"},
    #duplicate of id1
    "id4" : {"name": "Elizabeth", "class": "V-Yellow", "subject_integration": "History, Science, Computing"},
      }

result = {}
seen_keys = [] #usinga list instead of set

for student_id, details in student_data.items():
    unique_key = (details["name"], details["class"], details["subject_integration"])
    if unique_key not in seen_keys:
        seen_keys.append(unique_key)
        result[student_id] = details

#print output line by line
for k, v in result.items():
    print(k, ":", v)
    