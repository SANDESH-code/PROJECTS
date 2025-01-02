import datetime

# exams data with date and time
exams = {
    'math': {'date': '2025-01-10', 'time': '10:00'},
    'physics': {'date': '2025-01-12', 'time': '14:00'}
}

# assignments data with due date
assignments = {
    'math': {'due_date': '2025-01-05'},
    'physics': {'due_date': '2025-01-07'}
}

# class schedule with subjects, day, and time
classes = {
    'monday': [
        {'subject': 'math', 'time': '08:00'},
        {'subject': 'physics', 'time': '10:00'}
    ],
    'tuesday': [
        {'subject': 'chemistry', 'time': '09:00'},
        {'subject': 'biology', 'time': '11:00'}
    ]
}

# function to add a new exam
def add_exam(subject, date, time):
    exams[subject] = {'date': date, 'time': time}
    print(f"exam for {subject} added on {date} at {time}.")

# function to add a new assignment
def add_assignment(subject, due_date):
    assignments[subject] = {'due_date': due_date}
    print(f"assignment for {subject} added, due by {due_date}.")

# function to add a class schedule
def add_class(subject, day, time):
    if day not in classes:
        classes[day] = []
    classes[day].append({'subject': subject, 'time': time})
    print(f"class for {subject} added on {day} at {time}.")

# function to view all exams
def view_exams():
    if not exams:
        print("no exams added.")
    else:
        print("upcoming exams:")
        for subject, details in exams.items():
            print(f"subject: {subject}, date: {details['date']}, time: {details['time']}")

# function to view all assignments
def view_assignments():
    if not assignments:
        print("no assignments added.")
    else:
        print("upcoming assignments:")
        for subject, details in assignments.items():
            print(f"subject: {subject}, due date: {details['due_date']}")

# function to view the class timetable
def view_classes():
    if not classes:
        print("no classes scheduled.")
    else:
        print("class timetable:")
        for day, subjects in classes.items():
            print(f"day: {day.capitalize()}:")
            for subject in subjects:
                print(f"  subject: {subject['subject']}, time: {subject['time']}")

# function to check today's reminders
def check_reminders():
    today = datetime.date.today()
    print(f"\ntoday's date: {today}")

    print("\nupcoming exams:")
    for subject, details in exams.items():
        exam_date = datetime.datetime.strptime(details['date'], '%Y-%m-%d').date()
        if exam_date == today:
            print(f"exam for {subject} is today at {details['time']}.")

    print("\nupcoming assignments:")
    for subject, details in assignments.items():
        due_date = datetime.datetime.strptime(details['due_date'], '%Y-%m-%d').date()
        if due_date == today:
            print(f"assignment for {subject} is due today.")

# main function for the college management system
def college_management_system():
    while True:
        print("\ncollege exam and reminder system")
        print("1. add exam")
        print("2. view exams")
        print("3. add assignment")
        print("4. view assignments")
        print("5. add class schedule")
        print("6. view class timetable")
        print("7. check reminders")
        print("8. exit")
        
        choice = input("enter your choice: ")

        if choice == '1':
            subject = input("enter subject name: ")
            date = input("enter exam date (yyyy-mm-dd): ")
            time = input("enter exam time (hh:mm): ")
            add_exam(subject, date, time)

        elif choice == '2':
            view_exams()

        elif choice == '3':
            subject = input("enter subject name: ")
            due_date = input("enter assignment due date (yyyy-mm-dd): ")
            add_assignment(subject, due_date)

        elif choice == '4':
            view_assignments()

        elif choice == '5':
            subject = input("enter subject name: ")
            day = input("enter class day: ")
            time = input("enter class time (hh:mm): ")
            add_class(subject, day, time)

        elif choice == '6':
            view_classes()

        elif choice == '7':
            check_reminders()

        elif choice == '8':
            print("exiting the system.")
            break

        else:
            print("invalid choice, please try again.")

# run the program
if __name__ == "__main__":
    college_management_system()
