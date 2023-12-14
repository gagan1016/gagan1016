from IHospitalService import IHospitalService
from DBConnUtil import DBConnUtil
from CustomException import PatientNumberNotFoundException

class HospitalServiceImpl(IHospitalService):
    def query(self, query, values=None):
        connection=None
        cursor = None
        try:
            connection =DBConnUtil.get_connection()
            cursor = connection.cursor(dictonary=True)
            cursor.execute(query,values)
            return cursor.fetchall()
        except Exception as e:
            print(f'Error executing query :{e}')
            return None
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()
    def update(self,query, values=None):
        connection = None
        cursor = None
        try:
            connection = DBConnUtil.get_connection()
            cursor = connection.cursor()
            cursor.execute(query, values)
            connection.commit()
            return True
        except Exception as e:
            print(f'Error executing update: {e}')
            return False
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()



    def get_appointment_by_id(self, appointment_id):
        query ="select * from appointment where appointment_id=%s"
        result = self.query(query,(appointment_id))
        return result
    def get_appointments_for_patient(self, patient_id):
        query="select * from appointment where patient_id=%s"
        result = self.query(query, (patient_id))
    def get_appointments_for_doctor(self, doctor_id):
        query ='select * from appointment where doctor_id="%s'
        return self.query(query,(doctor_id))

    def schedule_appointment(self, appointment):
        query = "insert into appointment(patient_id,doctor_id,appointment_date, description) values(%s,%s,%s,%s)"
        values= (appointment.patient_id,appointment.doctor_id,appointment.appointment_date,appointment.description)
        return self.update(query,values)
    def update_appointment(self, date, description,appointment_id):
        query ='update appoint set appointment_date=%s, description=%s, where appointment_id=%s'
        values = (date, description,appointment_id)
        return self.update(query,values)

    def cancel_appointment(self, appointment_id):
        query ='delete from appointment where appointment_id=%s'
        return self.update(query, appointment_id)
