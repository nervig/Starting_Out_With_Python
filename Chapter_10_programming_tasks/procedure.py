class Procedure:
    def __init__(self, procedure_name, procedure_date, doctor_made_procedure, procedure_cost):
        self.__procedure_name = procedure_name
        self.__procedure_date = procedure_date
        self.__doctor_made_procedure = doctor_made_procedure
        self.__procedure_cost = procedure_cost

    def set_procedure_name(self, procedure_name):
        self.__procedure_name = procedure_name

    def set_procedure_date(self, procedure_date):
        self.__procedure_date = procedure_date

    def set_doctor_made_procedure(self, doctor_made_procedure):
        self.__doctor_made_procedure = doctor_made_procedure

    def set_procedure_cost(self, procedure_cost):
        self.__procedure_cost = procedure_cost

    def get_procedure_name(self):
        return self.__procedure_name

    def get_procedure_date(self):
        return self.__procedure_date

    def get_doctor_made_procedure(self):
        return self.__doctor_made_procedure

    def get_procedure_cost(self):
        return self.__procedure_cost
