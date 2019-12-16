import openpyxl

file1 =open("DEntry.txt",'r',encoding = 'utf-8')

cnt=0
while file1.readline():
       cnt+=1

file1.close()
file1 =open("DEntry.txt",'r',encoding = 'utf-8')

wb = openpyxl.load_workbook('DExcel.xlsx')
sheet = wb.active
sheet = wb.get_sheet_by_name('Sheet1')



for a in sheet['A1':'E10000']: #you can set the range here
    for cell in a:
        cell.value = None #set a value or null here


sheet['A1'] = 'Q'
sheet['B1'] = 'A1'
sheet['C1'] = 'A2'
sheet['D1'] = 'A3'
sheet['E1'] = 'A4'

j=2
for i in range((cnt//6)+1):
    q=str(file1.readline().strip())
    ans1=str(file1.readline().strip())
    ans2=str(file1.readline().strip())
    ans3=str(file1.readline().strip())
    ans4 =str(file1.readline().strip())
    ans=str((file1.readline().strip()))

    if ans=='1':
        ans4,ans1=ans1,ans4
    elif ans=='2':
        ans4, ans2 = ans2, ans4
    elif ans=='3':
        ans4, ans3 = ans3, ans4

    sheet['A'+str(j)] = q
    sheet['B' + str(j)] = ans1
    sheet['C' + str(j)] = ans2
    sheet['D' + str(j)] = ans3
    sheet['E' + str(j)] = ans4
    j+=1




wb.save('DExcel.xlsx')
file1.close()




