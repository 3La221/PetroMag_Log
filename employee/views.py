from django.shortcuts import render,redirect
import json 
from openpyxl import load_workbook
import shutil
from .models import Employee
from datetime import datetime


def home(request):
    current_month = datetime.now().month
    today = datetime.now().day 
    default_excel = "./excel/default.xlsx"
    employees = Employee.objects.all()
    data = []
    cells = []
    for employee in employees:
        tmp = {}
        path=f"./excel/{employee.matricule}2024.xlsx"
        # print(path)
        try:
            worbook = load_workbook(path)
            sheet = worbook.active 
        except:
            shutil.copy(default_excel,path)
            worbook = load_workbook(path)
            sheet = worbook.active 
            sheet['U6'] = employee.matricule
            sheet['B6'] = employee.nom 
            sheet['B7'] = employee.prenom 
            sheet['B8'] = employee.fonction
            sheet['AG6'] = employee.date_recrut
            sheet['AG8'] = employee.date_detach
            sheet['AG9'] = employee.affect_origine
            sheet['AG10'] = employee.sit_fam
            sheet['AG11'] = employee.nbr_enfant
            worbook.save(f"./excel/{employee.matricule}2024.xlsx")
        tmp['employee'] = employee
        tmp['results'] = []
        
        if today <= 10:
            for i in range(ord('B'), ord('K')+1):
                cell_value = sheet[f'{chr(i)}{str(current_month+13)}'].value
                tmp['results'].append(cell_value)
                cells.append(f'{chr(i)}{str(current_month+13)}')
            days = [1,2,3,4,5,6,7,8,9,10]
            
        elif today <=20 :
            for i in range(ord('L'), ord('U')+1):
                cell_value = sheet[f'{chr(i)}{str(current_month+13)}'].value
                tmp['results'].append(cell_value)
                cells.append(f'{chr(i)}{str(current_month+13)}')               
            days = [11,12,13,14,15,16,17,18,19,20]
            
        elif today <=31:
            for i in range(ord('V'), ord('Z')+1):
                cell_value = sheet[f'{chr(i)}{str(current_month+13)}'].value
                tmp['results'].append(cell_value)
                cells.append(f'{chr(i)}{str(current_month+13)}')               
                
            for i in range(ord('A') , ord('D')+1):
                cell_value = sheet[f'A{chr(i)}{str(current_month+13)}'].value
                tmp['results'].append(cell_value)
                days = [21,22,23,24,25,26,27,28,29]
                cells.append(f'A{chr(i)}{str(current_month+13)}') 
            if current_month != 2 :
                cell_value = sheet[f'AE{str(current_month+13)}'].value
                tmp['results'].append(cell_value)
                cells.append(f'AE{chr(i)}{str(current_month+13)}') 
                days.append(30)
                if current_month not in [4,6,9,11]:
                    cell_value = sheet[f'AF{str(current_month+13)}'].value
                    cells.append(f'AF{chr(i)}{str(current_month+13)}') 
                    tmp['results'].append(cell_value)
                    days.append(31)         
        data.append(tmp)
    worbook.close()
    
    if request.method == "POST":
        for employee in employees :
            path=f"./excel/{employee.matricule}2024.xlsx"
            data = json.loads(request.body.decode('utf-8'))

            worbook = load_workbook(path)
            sheet = worbook.active 
            
            inner_dict = data[str(employee.matricule)]
            print(employee.matricule , inner_dict)
            
            for index,value in inner_dict.items():
                if value != '-':
                    print(cells[int(index)-1])
                    sheet[cells[int(index)-1]] = value
            worbook.save(f"./excel/{employee.matricule}2024.xlsx")    
        worbook.close()
        return render(request,'main/home.html',{'data':data,'month':current_month,'days':days})
    
    
    return render(request,'main/home.html',{'data':data,'month':current_month,'days':days})




def read(request):
    
    default_excel = "./excel/default.xlsx"
    path = "./excel/2232024.xlsx"
    
    
    try:
        worbook = load_workbook(path)
    except:
        print("not found")
        shutil.copy(default_excel,path)
        worbook = load_workbook(path)
        
        sheet = worbook.active
        sheet['B6'] = "Abach"
        sheet['B7'] = "Alaa Eddine"
        sheet['B8'] = "web developer"
        
        worbook.save("./excel/2232024.xlsx")
    
    worbook.close()
    return render(request, 'main/read.html')

def test(request):
    
    if request.method == "POST":
        try:
            data = json.loads(request.body.decode('utf-8'))
            print(data)  
        except:
            print("NO")      
    return render(request,'main/test.html')