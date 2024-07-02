import random

def generate_student_data(num_students):
    names = generate_distinct_names(num_students)
    data = []
    
    for student_id in range(1, num_students + 1):
        name = names[student_id - 1]
        subjects = generate_random_marks(15)
        gender = random.choice(['Male', 'Female'])
        demographic = random.choice(['Urban', 'Rural'])
        course_of_study = random.choice(['Engineering' , 'medicine' , 'Business' , 'Law' , 'Education' , 'Humanities' , 'Arts' ])
        Parental_Education = random.choice(['Masters Degree' , 'Bachelors Degree' , 'High school'])
        Study_Hours_per_week = random.choice(['12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30'])

