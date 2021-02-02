import patient
import procedure

list_of_procedure = []
patient_demo = patient.Patient('John Dou', 'LA New Road 223', '+11233345678', 'Jane Dou +11234442354')
print('Name: ' + patient_demo.get_name())
print('Address: ' + patient_demo.get_address())
print('Phone number: ' + patient_demo.get_phone())
print('Emergency phone number: ' + patient_demo.get_emergency_name())

procedure_1 = procedure.Procedure('Medical examination', 'today', 'Irvin', '250.00')
print('Procedure 1: ')
print('Name of procedure: ' + procedure_1.get_procedure_name())
print('Data: ' + procedure_1.get_procedure_date())
print('Name of doctor: ' + procedure_1.get_doctor_made_procedure())
print('Cost of procedure: ' + procedure_1.get_procedure_cost())
print()

procedure_2 = procedure.Procedure('Fluoroscopy', 'today', 'Jamison', '500.00')
print('Procedure 2: ')
print('Name of procedure: ' + procedure_2.get_procedure_name())
print('Data: ' + procedure_2.get_procedure_date())
print('Name of doctor: ' + procedure_2.get_doctor_made_procedure())
print('Cost of procedure: ' + procedure_2.get_procedure_cost())
print()

procedure_3 = procedure.Procedure('A blood test', 'today', 'Smith', '200.00')
print('Procedure 3: ')
print('Name of procedure: ' + procedure_3.get_procedure_name())
print('Data: ' + procedure_3.get_procedure_date())
print('Name of doctor: ' + procedure_3.get_doctor_made_procedure())
print('Cost of procedure: ' + procedure_3.get_procedure_cost())
print()

print('Cost of all procedure: ' + str(float(procedure_1.get_procedure_cost()) + float(procedure_2.get_procedure_cost()) + float(procedure_3.get_procedure_cost())))
print()

list_of_procedure.append(procedure_1)
list_of_procedure.append(procedure_2)
list_of_procedure.append(procedure_3)
for item in list_of_procedure:
    print(item.get_procedure_name())
