import datetime  # Importing datetime module for handling dates and times

# Dictionary to store exams information, with subject name as key, and date and time as values
exams = {
    'math': {'date': '2025-01-10', 'time': '10:00'},
    'physics': {'date': '2025-01-12', 'time': '14:00'}
}

# Dictionary to store assignment information, with subject name as key, and due date as value
assignments = {
    'math': {'due_date': '2025-01-05'},
    'physics': {'due_date': '2025-01-07'}
}

# Dictionary to store class timetable, with days as keys and a list of subjects and times for each day
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

# Function to add exam details to the exams dictionary
def add_exam(subject, date, time):
    exams[subject] = {'date': date, 'time': time}
    print(f"exam for {subject} added on {date} at {time}.")

# Function to add assignment details to the assignments dictionary
def add_assignment(subject, due_date):
    assignments[subject] = {'due_date': due_date}
    print(f"assignment for {subject} added, due by {due_date}.")

# Function to add class schedule details to the classes dictionary
def add_class(subject, day, time):
    if day not in classes:  # Check if the day already exists in the dictionary
        classes[day] = []  # If not, create an empty list for that day
    classes[day].append({'subject': subject, 'time': time})
    print(f"class for {subject} added on {day} at {time}.")

# Function to view all upcoming exams
def view_exams():
    if not exams:
        print("no exams added.")  # If no exams are added, print this message
    else:
        print("upcoming exams:")
        for subject, details in exams.items():
            print(f"subject: {subject}, date: {details['date']}, time: {details['time']}")

# Function to view all upcoming assignments
def view_assignments():
    if not assignments:
        print("no assignments added.")  # If no assignments are added, print this message
    else:
        print("upcoming assignments:")
        for subject, details in assignments.items():
            print(f"subject: {subject}, due date: {details['due_date']}")

# Function to view the class timetable for the entire week
def view_classes():
    if not classes:
        print("no classes scheduled.")  # If no classes are scheduled, print this message
    else:
        print("class timetable:")
        for day, subjects in classes.items():
            print(f"day: {day.capitalize()}:")  # Capitalize the first letter of the day for better readability
            for subject in subjects:
                print(f"  subject: {subject['subject']}, time: {subject['time']}")

# Function to check reminders for today's exams and assignments
def check_reminders():
    today = datetime.date.today()  # Get today's date
    print(f"\ntoday's date: {today}")

    print("\nupcoming exams:")
    for subject, details in exams.items():
        exam_date = datetime.datetime.strptime(details['date'], '%Y-%m-%d').date()  # Convert exam date from string to date object
        if exam_date == today:  # If the exam is today, print a reminder
            print(f"exam for {subject} is today at {details['time']}.")

    print("\nupcoming assignments:")
    for subject, details in assignments.items():
        due_date = datetime.datetime.strptime(details['due_date'], '%Y-%m-%d').date()  # Convert due date from string to date object
        if due_date == today:  # If the assignment is due today, print a reminder
            print(f"assignment for {subject} is due today.")

# Main function to run the college management system
def college_management_system():
    while True:  # Infinite loop to keep the system running
        print("\ncollege exam and reminder system")  # Display the menu
        print("1. add exam")
        print("2. view exams")
        print("3. add assignment")
        print("4. view assignments")
        print("5. add class schedule")
        print("6. view class timetable")
        print("7. check reminders")
        print("8. exit")
        
        choice = input("enter your choice: ")  # User input to select an option

        # Depending on the user's choice, call the corresponding function
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
            print("exiting the system.")  # Exit message
            break  # Exit the while loop

        else:
            print("invalid choice, please try again.")  # If the user enters an invalid choice

if __name__ == "__main__":
    college_management_system()  # Run the college management system
