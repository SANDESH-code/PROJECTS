import datetime
def add_patient(id, name, bed_number, doctor_assigned, amount_paid, amount_due):
    patient = {"id": id, "name": name, "bed_number": bed_number, "doctor_assigned": doctor_assigned, "admission_date": datetime.datetime.now().strftime('%Y-%m-%d'), "amount_paid": amount_paid, "amount_due": amount_due}
    return patient
def show_patient_details(patient_name, patients):
    found = False
    for patient in patients:
        if patient['name'].lower() == patient_name.lower():
            found = True
            print(f"\nID: {patient['id']}\nName: {patient['name']}\nBed Number: {patient['bed_number']}\nDoctor Assigned: {patient['doctor_assigned']}\nAdmission Date: {patient['admission_date']}\nAmount Paid: {patient['amount_paid']}\nAmount Due: {patient['amount_due']}")
            break
    if not found:
        print("Patient not found.")
def show_patient_list(patients):
    print("\n--- All Patients ---")
    for patient in patients:
        print(f"Name: {patient['name']} | Bed: {patient['bed_number']} | Doctor: {patient['doctor_assigned']}")
def remove_patient(patient_name, patients):
    for patient in patients:
        if patient['name'].lower() == patient_name.lower():
            patients.remove(patient)
            print(f"Patient {patient_name} removed.")
            return
    print("Patient not found.")
def update_patient(id, patients, amount_paid, amount_due):
    for patient in patients:
        if patient['id'] == id:
            patient['amount_paid'] = amount_paid
            patient['amount_due'] = amount_due
            print(f"Details updated for Patient ID {id}.")
            return
    print("Patient not found.")
def main():
    patients = []
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
        print("\n1. View Patient Details\n2. Show All Patients\n3. Remove Patient\n4. Update Patient Details\n5. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            patient_name = input("\nEnter the patient's name to view details: ")
            show_patient_details(patient_name, patients)
        elif choice == '2':
            show_patient_list(patients)
        elif choice == '3':
            patient_name = input("\nEnter the patient's name to remove: ")
            remove_patient(patient_name, patients)
        elif choice == '4':
            patient_id = int(input("\nEnter the Patient ID to update: "))
            amount_paid = float(input("Enter the updated amount paid: "))
            amount_due = float(input("Enter the updated amount due: "))
            update_patient(patient_id, patients, amount_paid, amount_due)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
