# Importing the datetime module to work with dates
import datetime

# This function adds a patient to the list with their details
def add_patient(id, name, bed_number, doctor_assigned, amount_paid, amount_due):
    # Creating a dictionary for the patient and setting the admission date to the current date
    patient = {"id": id, "name": name, "bed_number": bed_number, "doctor_assigned": doctor_assigned, 
               "admission_date": datetime.datetime.now().strftime('%Y-%m-%d'), "amount_paid": amount_paid, "amount_due": amount_due}
    return patient

# This function shows the details of a patient by their name
def show_patient_details(patient_name, patients):
    found = False
    # Searching for the patient in the list
    for patient in patients:
        if patient['name'].lower() == patient_name.lower():  # Checking if the name matches
            found = True
            # If found, print their details
            print(f"\nID: {patient['id']}\nName: {patient['name']}\nBed Number: {patient['bed_number']}\nDoctor Assigned: {patient['doctor_assigned']}\nAdmission Date: {patient['admission_date']}\nAmount Paid: {patient['amount_paid']}\nAmount Due: {patient['amount_due']}")
            break
    if not found:  # If the patient is not found, show this message
        print("Patient not found.")

# This function shows a list of all patients with their names, bed numbers, and doctors assigned
def show_patient_list(patients):
    print("\n--- All Patients ---")
    # Looping through the list of patients and printing their basic details
    for patient in patients:
        print(f"Name: {patient['name']} | Bed: {patient['bed_number']} | Doctor: {patient['doctor_assigned']}")

# This function removes a patient from the list by their name
def remove_patient(patient_name, patients):
    # Loop through the list and remove the patient if the name matches
    for patient in patients:
        if patient['name'].lower() == patient_name.lower():
            patients.remove(patient)
            print(f"Patient {patient_name} removed.")  # Confirm the patient is removed
            return
    print("Patient not found.")  # If the patient is not found, show this message

# This function updates the payment details for a patient using their ID
def update_patient(id, patients, amount_paid, amount_due):
    # Searching for the patient by their ID
    for patient in patients:
        if patient['id'] == id:
            patient['amount_paid'] = amount_paid  # Update the amount paid
            patient['amount_due'] = amount_due  # Update the amount due
            print(f"Details updated for Patient ID {id}.")  # Confirm the update
            return
    print("Patient not found.")  # If the patient is not found, show this message

# This is the main function where the program starts and allows the user to interact with the system
def main():
    patients = []  # Creating an empty list for patients
    
    # Adding some sample patients to the list
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
    
    while True:
        # Display the menu options for the user
        print("\n1. View Patient Details\n2. Show All Patients\n3. Remove Patient\n4. Update Patient Details\n5. Exit")
        choice = input("Enter choice: ")  # Asking user to enter their choice
        
        if choice == '1':  # View patient details
            patient_name = input("\nEnter the patient's name to view details: ")
            show_patient_details(patient_name, patients)
        elif choice == '2':  # Show all patients
            show_patient_list(patients)
        elif choice == '3':  # Remove a patient
            patient_name = input("\nEnter the patient's name to remove: ")
            remove_patient(patient_name, patients)
        elif choice == '4':  # Update a patient's details
            patient_id = int(input("\nEnter the Patient ID to update: "))
            amount_paid = float(input("Enter the updated amount paid: "))
            amount_due = float(input("Enter the updated amount due: "))
            update_patient(patient_id, patients, amount_paid, amount_due)
        elif choice == '5':  # Exit the program
            print("Exiting the program.")
            break
        else:  # If the choice is not valid
            print("Invalid choice. Please try again.")

# This is the starting point of the program
if __name__ == "__main__":
    main()  # Run the main function
