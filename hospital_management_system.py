import datetime

# Function to add patient details
def add_patient(id, name, bed_number, doctor_assigned, amount_paid, amount_due):
    patient = {
        "id": id,
        "name": name,
        "bed_number": bed_number,
        "doctor_assigned": doctor_assigned,
        "admission_date": datetime.datetime.now().strftime('%Y-%m-%d'),
        "amount_paid": amount_paid,
        "amount_due": amount_due
    }
    return patient

# Function to display all patients
def show_all_patients(patients):
    if not patients:
        print("\nNo patients found in the system.")
    else:
        print("\n--- All Patient Details ---")
        for patient in patients:
            print(f"ID: {patient['id']}, Name: {patient['name']}, Bed Number: {patient['bed_number']}, "
                  f"Doctor: {patient['doctor_assigned']}, Admission Date: {patient['admission_date']}")

# Function to show patient details by name
def show_patient_details(patient_name, patients):
    found = False
    for patient in patients:
        if patient['name'].lower() == patient_name.lower():
            found = True
            print("\n--- Patient Details ---")
            print(f"ID: {patient['id']}")
            print(f"Name: {patient['name']}")
            print(f"Bed Number: {patient['bed_number']}")
            print(f"Doctor Assigned: {patient['doctor_assigned']}")
            print(f"Admission Date: {patient['admission_date']}")
            print(f"Amount Paid: {patient['amount_paid']}")
            print(f"Amount Due: {patient['amount_due']}")
            break
    if not found:
        print("Patient not found.")

# Function to update payment details of a patient
def update_payment(patient_name, patients, payment):
    found = False
    for patient in patients:
        if patient['name'].lower() == patient_name.lower():
            found = True
            patient['amount_paid'] += payment
            patient['amount_due'] -= payment
            print(f"\nUpdated payment for {patient_name}: Amount Paid: {patient['amount_paid']}, Amount Due: {patient['amount_due']}")
            break
    if not found:
        print("Patient not found.")

# Function to remove a patient
def remove_patient(patient_name, patients):
    found = False
    for patient in patients:
        if patient['name'].lower() == patient_name.lower():
            found = True
            patients.remove(patient)
            print(f"\nPatient {patient_name} has been removed from the system.")
            break
    if not found:
        print("Patient not found.")

# Main function to run the program
def main():
    # List to store patient details
    patients = []

    # Add patients manually
    patients.append(add_patient(1, "Alice Johnson", "Bed1", "Dr. John Smith", 2200, 8000))
    patients.append(add_patient(2, "Bob Brown", "Bed2", "Dr. Sarah Lee", 1500, 7000))
    patients.append(add_patient(3, "Charlie Davis", "Bed3", "Dr. John Smith", 1800, 5500))
    patients.append(add_patient(4, "David White", "Bed4", "Dr. Sarah Lee", 2000, 4500))
    patients.append(add_patient(5, "Eve Martin", "Bed5", "Dr. John Smith", 2500, 7500))
    patients.append(add_patient(6, "Frank Harris", "Bed6", "Dr. Sarah Lee", 2700, 9300))
    patients.append(add_patient(7, "Grace Thompson", "Bed7", "Dr. John Smith", 3500, 6200))
    patients.append(add_patient(8, "Henry Lee", "Bed8", "Dr. Sarah Lee", 3000, 7100))
    patients.append(add_patient(9, "Isla Adams", "Bed9", "Dr. John Smith", 2100, 8800))
    patients.append(add_patient(10, "James Scott", "Bed10", "Dr. Sarah Lee", 2300, 5700))

    # Menu for the user
    while True:
        print("\n--- Hospital Management System ---")
        print("1. Show all patients")
        print("2. Show patient details by name")
        print("3. Update payment details")
        print("4. Remove a patient")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            show_all_patients(patients)
        elif choice == "2":
            patient_name = input("Enter the patient's name: ")
            show_patient_details(patient_name, patients)
        elif choice == "3":
            patient_name = input("Enter the patient's name: ")
            payment = float(input("Enter the payment amount: "))
            update_payment(patient_name, patients, payment)
        elif choice == "4":
            patient_name = input("Enter the patient's name to remove: ")
            remove_patient(patient_name, patients)
        elif choice == "5":
            print("Exiting the system...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
