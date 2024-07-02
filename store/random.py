import random

def generate_distinct_names(num_students):
    names = set()
    
    while len(names) < num_students:
        first_name = random.choice(["John", "Jane", "Alex", "Emily", "Michael", "Sarah"])
        last_name = random.choice(["Doe", "Smith", "Johnson", "Brown", "Davis", "Miller"])
        full_name = f"{first_name} {last_name}"
        names.add(full_name)
    
    return list(names)

def generate_random_marks(num_subjects):
    return [random.randint(40, 100) for _ in range(num_subjects)]

def generate_student_data(num_students):
    names = generate_distinct_names(num_students)
    data = []
    
    for student_id in range(1, num_students + 1):
        name = names[student_id - 1]
        subjects = generate_random_marks(15)
        gender = random.choice(['Male', 'Female'])
        demographic = random.choice(['Urban', 'Rural'])
        course_of_study = random.choice(['Engineering', 'Medicine', 'Business', 'Computer Science'])
        parental_education = random.choice(["Master's Degree", "Bachelor's Degree", "High School"])
        study_hours = random.randint(10, 30)
        
        data.append([student_id, name] + subjects + [gender, demographic, course_of_study, parental_education, study_hours])
    
    return data

# Generate dataset with 500 students
dataset = generate_student_data(500)

# Print the first few rows of the dataset
for row in dataset[:5]:
    print(row)
