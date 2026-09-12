students = {"alice":60,"bob":56,"david":78,"ram":89,"gopu":23,"priya":45}
passed = {}
failed = {}
for key,value in students.items():
    if value>50:
        passed[key] = value
    else:
        failed[key] = value
print("Passed students: ",passed)
print("Failed students: ",failed)