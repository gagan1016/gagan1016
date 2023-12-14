class Appointment:
    def __init__(self, appointment_id=None, patient_id= None, doctor_id=None, appointment_date=None, description= None):
        self.appointment_id = appointment_id
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.appointment_date = appointment_date
        self.description = description

    def set_appointment_id(self, appointment_id):
        self.appointment_id = appointment_id

    def get_appointment_id(self):
        return self.appointment_id

    def set_patient_id(self, patient_id):
        self.patient_id = patient_id

    def get_patient_id(self):
        return self.patient_id

    def set_doctor_id(self, doctor_id):
        self.doctor_id = doctor_id

    def get_doctor_id(self):
        return self.doctor_id

    def set_appointment_date(self, appointment_date):
        self.appointment_date = appointment_date

    def get_appointment_date(self):
        return self.appointment_date

    def set_description(self, description):
        self.description = description

    def get_description(self):
        return self.description

    def print_appointment_details(self):
        print(f"Appointment ID: {self.appointment_id}")
        print(f"Patient ID: {self.patient_id}")
        print(f"Doctor ID: {self.doctor_id}")
        print(f"Appointment Date: {self.appointment_date}")
        print(f"Description: {self.description}")