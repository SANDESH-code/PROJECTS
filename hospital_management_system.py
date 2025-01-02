import datetime
import random

class Patient:
    def __init__(self, id, name, bed_number, doctor_assigned, amount_paid, amount_due):
        self.id = id
        self.name = name
        self.bed_number = bed_number
        self.doctor_assigned = doctor_assigned
        self.admission_date = datetime.datetime.now().strftime('%Y-%m-%d')
        self.amount_paid = amount_paid
        self.amount_due = amount_due

    def get_patient_info(self):
        return {
            "ID": self.id,
            "Name": self.name,
            "Bed Number": self.bed_number,
            "Doctor Assigned": self.doctor_assigned,
            "Admission Date": self.admission_date,
            "Amount Paid": self.amount_paid,
            "Amount Due": self.amount_due
        }

    def update_payment(self, new_amount_paid):
        self.amount_paid = new_amount_paid
        self.amount_due = round(self.amount_due - new_amount_paid, 2)

class Doctor:
    def __init__(self, id, name, specialization):
        self.id = id
        self.name = name
        self.specialization = specialization

    def __str__(self):
        return f"Dr. {self.name}, {self.specialization}"

class Hospital:
    def __init__(self, name):
        self.name = name
        self.patients = []
        self.doctors = []

    def add_doctor(self, doctor):
        self.doctors.append(doctor)

    def add_patient(self, patient):
        self.patients.append(patient)

    def get_doctor_by_id(self, doctor_id):
        for doctor in self.doctors:
            if doctor.id == doctor_id:
                return doctor
        return None

    def show_patient_details(self, patient_name):
        for patient in self.patients:
            if patient.name.lower() == patient_name.lower():
                patient_info = patient.get_patient_info()
                print("\n--- Patient Details ---")
                for key, value in patient_info.items():
                    print(f"{key}: {value}")
                break
        else:
            print("Patient not found.")

    def show_all_patients(self):
        if self.patients:
            print("\n--- All Patients ---")
            for patient in self.patients:
                patient_info = patient.get_patient_info()
                print(f"\nPatient Name: {patient_info['Name']}")
                for key, value in patient_info.items():
                    print(f"{key}: {value}")
        else:
            print("No patients in the system.")

    def update_patient_payment(self, patient_name, new_amount_paid):
        for patient in self.patients:
            if patient.name.lower() == patient_name.lower():
                patient.update_payment(new_amount_paid)
                print(f"Payment updated for {patient_name}.")
                break
        else:
            print("Patient not found.")

    def remove_patient(self, patient_name):
        for patient in self.patients:
            if patient.name.lower() == patient_name.lower():
                self.patients.remove(patient)
                print(f"{patient_name} has been discharged and removed from the system.")
                break
        else:
            print("Patient not found.")

    def search_doctors_by_specialization(self, specialization):
        print(f"\n--- Doctors with {specialization} specialization ---")
        found = False
        for doctor in self.doctors:
            if doctor.specialization.lower() == specialization.lower():
                print(f"{doctor}")
                found = True
        if not found:
            print(f"No doctors found with {specialization} specialization.")

    def track_revenue(self):
        total_revenue = sum(patient.amount_paid for patient in self.patients)
        print(f"\n--- Total Revenue ---")
        print(f"Total amount collected: {total_revenue}")

def main():
    hospital = Hospital("City Hospital")

    # Adding doctors
    doctor1 = Doctor(1, "John Smith", "Cardiologist")
    doctor2 = Doctor(2, "Sarah Lee", "Orthopedic Surgeon")
    hospital.add_doctor(doctor1)
    hospital.add_doctor(doctor2)

    # Collecting patient details (only name input required)
    print("Welcome to the Hospital Management System!")
    patient_name = input("Enter Patient Name: ")

    # Generating random patient ID, bed number, doctor, amount paid, and amount due for simulation
    patient_id = random.randint(100, 999)
    bed_number = f"Bed{random.randint(1, 100)}"
    doctor_choice = random.choice([doctor1, doctor2])
    doctor_assigned = doctor_choice.name
    amount_paid = round(random.uniform(1000, 5000), 2)
    total_amount = round(random.uniform(5000, 10000), 2)
    amount_due = total_amount - amount_paid

    # Create patient and add to the hospital
    patient = Patient(patient_id, patient_name, bed_number, doctor_assigned, amount_paid, amount_due)
    hospital.add_patient(patient)

    # Show patient details
    hospital.show_patient_details(patient_name)

    # Additional actions
    while True:
        print("\nChoose an option:")
        print("1. View All Patients")
        print("2. Update Payment")
        print("3. Remove Patient")
        print("4. Search Doctors by Specialization")
        print("5. Track Total Revenue")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")
        
        if choice == "1":
            hospital.show_all_patients()
        elif choice == "2":
            patient_name = input("Enter the patient's name to update payment: ")
            new_payment = float(input("Enter the new payment amount: "))
            hospital.update_patient_payment(patient_name, new_payment)
        elif choice == "3":
            patient_name = input("Enter the patient's name to remove: ")
            hospital.remove_patient(patient_name)
        elif choice == "4":
            specialization = input("Enter the specialization (e.g., Cardiologist): ")
            hospital.search_doctors_by_specialization(specialization)
        elif choice == "5":
            hospital.track_revenue()
        elif choice == "6":
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
