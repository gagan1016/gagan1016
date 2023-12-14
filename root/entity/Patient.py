class Patient:
    def __init__(self, patient_id=None, first_name=None, last_name=None, date_of_birth=None, gender=None, contact_number=None, address=None):
        self.patient_id = patient_id
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.contact_number = contact_number
        self.address = address

    def set_patient_id(self, patient_id):
        self.patient_id = patient_id

    def get_patient_id(self):
        return self.patient_id

    def set_first_name(self, first_name):
        self.first_name = first_name

    def get_first_name(self):
        return self.first_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def get_last_name(self):
        return self.last_name

    def set_date_of_birth(self, date_of_birth):
        self.date_of_birth = date_of_birth

    def get_date_of_birth(self):
        return self.date_of_birth

    def set_gender(self, gender):
        self.gender = gender

    def get_gender(self):
        return self.gender

    def set_contact_number(self, contact_number):
        self.contact_number = contact_number

    def get_contact_number(self):
        return self.contact_number

    def set_address(self, address):
        self.address = address

    def get_address(self):
        return self.address

    def print_patient_details(self):
        print(f"Patient ID: {self.patient_id}")
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Date of Birth: {self.date_of_birth}")
        print(f"Gender: {self.gender}")
        print(f"Contact Number: {self.contact_number}")
        print(f"Address: {self.address}")