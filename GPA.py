gpa_system = [
    (90, 100, "A+", 4.0),
    (80, 89, "A", 3.6),
    (70, 79, "B+", 3.2),
    (60, 69, "B", 2.8),
    (50, 59, "C+", 2.4),
    (40, 49, "C", 2.0),
    (0, 39, "F", 0.0)
]

print("Welcome to the GPA Calculator")

while True:
    try:
        class_number = int(input("Enter your class (9-12): "))
        if class_number in [9, 10, 11, 12]:
            break
        print("Please enter a class from 9 to 12.")
    except ValueError:
        print("Please enter a number like 9 or 11.")

if class_number == 9 or class_number == 10:
    subjects = [
        "Nepali",
        "English",
        "Science",
        "C.Maths",
        "Social Studies",
        "Optional I (O.Maths/Economics)",
        "Optional II (Account/Computer)"
    ]

else:
    while True:
        stream = input("Enter your stream (science/management): ").strip().lower()
        if stream in ["science", "management"]:
            break
        print("Please enter science or management.")

    if stream == "science":
        while True:
            choice = input("Choose biology or computer: ").strip().lower()
            if choice in ["biology", "computer"]:
                break
            print("Please enter biology or computer.")

        subjects = [
            "Nepali",
            "English",
            "Physics",
            "Chemistry",
            choice.capitalize(),
            "Maths"
        ]

    else:
        while True:
            choice = input("Choose HM, CS or BS: ").strip().lower()
            if choice in ["hm", "cs", "bs"]:
                break
            print("Please enter HM, CS or BS.")

        if choice == "hm":
            subjects = [
                "Nepali",
                "English",
                "HM",
                "Social",
                "Account",
                "Economics"
            ]
        elif choice == "cs":
            subjects = [
                "Nepali",
                "English",
                "Maths/Social",
                "Account",
                "Economics",
                "CS"
            ]
        else:
            subjects = [
                "Nepali",
                "English",
                "Social",
                "Account",
                "Economics",
                "BS"
            ]

marks = []

print("\nEnter your marks out of 100")

for subject in subjects:
    while True:
        try:
            mark = int(input(subject + ": "))
            if 0 <= mark <= 100:
                marks.append(mark)
                break
            print("Marks must be between 0 and 100.")
        except ValueError:
            print("Please enter a whole number like 75.")

total_gp = 0

print("\n--- Result ---")

for i in range(len(subjects)):
    mark = marks[i]

    for min_mark, max_mark, grade, gp in gpa_system:
        if min_mark <= mark <= max_mark:
            print(f"{subjects[i]}: {mark} -> {grade} ({gp:.1f})")
            total_gp = total_gp + gp
            break

overall_gpa = total_gp / len(subjects)
percentage = sum(marks) / len(subjects)

print("-" * 40)
print(f"Total Marks: {sum(marks)} / {len(subjects) * 100}")
print(f"Overall GPA: {overall_gpa:.2f}")
print(f"Percentage: {percentage:.2f}%")
