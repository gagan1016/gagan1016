from dao.HospitalServiceImpl import HospitalServiceImpl
from root.entity.Appointment import Appointment
from root.entity.Doctor import Doctor
from root.entity.Patient import Patient
from root.exception.CustomException import PatientNumberNotFoundException
from root.util.DBConnUtil import DBConnUtil

class MainModule:
    def __init__(self):
        self.hospital_service =HospitalServiceImpl()

    def allfunctions(self):
        while True:
            print("\n Menu:")
            print("1.Get appointment by id.")
            print("2.Get appointment by patient")
            print("3.get appointment by Doctor")
            print("4.Schedule appointment")
            print("5. update appointment")
            print("6. cancel appointment")
            print("7. Exit")

            choice = input("Enter your choice: ")
            if choice =='1':
                self.get_appointment_by_id()
            elif choice=='2':
                self.get_appointment_for_patient()
            elif choice=='3':
                self.get_appointment_for_doctor()
            elif choice=='4':
                self.schedule_appointment()
            elif choice=='5':
                self.update_appointment()
            elif choice=='6':
                self.cancel_appointment()
            elif choice =='7':
                break;
            else:
                print("Invalid selection of choice.Please try again")

    def get_appointment_by_id(self):
        try:
            appointment_id = int(input("Enter Appointment ID: "))
            appointment = self.hospital_service.get_appointment_by_id(appointment_id)
            if appointment:
                print("Appointment Details for Appointment are")
                print(appointment)
            else:
                print("appointment not found in database")
        except ValueError:
            print("Invalid input. Please enter valid appointment id")
        except Exception as e:
            print(f'Error:{e}')

    def get_appointments_for_patient(self):
        try:
            patient_id = int(input("Enter Patient ID: "))
            appointments = self.hospital_service.get_appointments_for_patient(patient_id)
            if appointments:
                print("Appointments for Patient:")
                for appointment in appointments:
                    print(appointment)
            else:
                print("No appointments found for the patient.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except PatientNumberNotFoundException as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error: {e}")

    def get_appointments_for_doctor(self):
        try:
            doctor_id = int(input("Enter Doctor ID: "))
            appointments = self.hospital_service.get_appointments_for_doctor(doctor_id)
            if appointments:
                print("Appointments for Doctor:")
                for appointment in appointments:
                    print(appointment)
            else:
                print("No appointments found for the doctor.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except PatientNumberNotFoundException as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error: {e}")

    def schedule_appointment(self):
        try:
            # Get appointment details from the user
            patient_id = int(input("Enter Patient ID for the appointment: "))
            doctor_id = int(input("Enter Doctor ID for the appointment: "))
            appointment_date = input("Enter Appointment Date (YYYY-MM-DD): ")
            description = input("Enter Appointment Description: ")

            # Create an Appointment object
            appointment = Appointment(patient_id=patient_id, doctor_id=doctor_id,
                                      appointment_date=appointment_date, description=description)

            # Call the corresponding method in the hospital service to schedule the appointment
            success = self.hospital_service.schedule_appointment(appointment)

            if success:
                print("Appointment scheduled successfully.")
            else:
                print("Unable to schedule the appointment.")
        except ValueError:
            print("Invalid input. Please enter valid information.")
        except Exception as e:
            print(f"Error: {e}")

    def update_appointment(self):
        try:
            # Get updated appointment details from the user
            appointment_id = int(input("Enter Appointment ID to update: "))
            description = input("Enter updated Appointment Description: ")
            date = input("Enter new Date")
            # Create an Appointment object with updated information

            # Call the corresponding method in the hospital service to update the appointment
            success = self.hospital_service.update_appointment(date, description, appointment_id)

            if success:
                print("Appointment updated successfully.")
            else:
                print("Unable to update the appointment.")
        except ValueError:
            print("Invalid input. Please enter valid information.")
        except Exception as e:
            print(f"Error: {e}")

    def cancel_appointment(self):
        try:
            appointment_id = int(input("Enter Appointment ID to cancel: "))
            success = self.hospital_service.cancel_appointment(appointment_id)
            if success:
                print("Appointment canceled successfully.")
            else:
                print("Unable to cancel the appointment.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except PatientNumberNotFoundException as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    MainModule.allfunctions()


