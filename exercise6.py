student_names = ["Lisa", "Liam", "Leo", "Larry", "Linda"]

for name in student_names:
    print("%s Evans" % name)

new_name = input("[Enter your name]")
student_names.append(new_name)

for name in student_names:
    print("%s Evans" % name)
