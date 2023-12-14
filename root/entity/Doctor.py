class Doctor:
    def __init__(self, doctor_id=None, first_name=None, last_name=None, specialization=None, contact_number=None):
        self.doctor_id = doctor_id
        self.first_name = first_name
        self.last_name = last_name
        self.specialization = specialization
        self.contact_number = contact_number

    def set_doctor_id(self, doctor_id):
        self.doctor_id = doctor_id

    def get_doctor_id(self):
        return self.doctor_id

    def set_first_name(self, first_name):
        self.first_name = first_name

    def get_first_name(self):
        return self.first_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def get_last_name(self):
        return self.last_name

    def set_specialization(self, specialization):
        self.specialization = specialization

    def get_specialization(self):
        return self.specialization

    def set_contact_number(self, contact_number):
        self.contact_number = contact_number

    def get_contact_number(self):
        return self.contact_number

    def print_doctor_details(self):
        print(f"Doctor ID: {self.doctor_id}")
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Specialization: {self.specialization}")
        print(f"Contact Number: {self.contact_number}")