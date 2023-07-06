import xlrd
import xlwt
import os
import pypinyin

excel_file = '111.xlsx'
sheet_name = '官网APP'


workbook = xlrd.open_workbook(excel_file)  
sheet = workbook.sheet_by_name(sheet_name)

udids = [] 
outfile = open(os.path.join(os.getcwd(), 'multiple-device-upload.txt'), 'w')   

workbook_new = xlwt.Workbook() 
sheet_new = workbook_new.add_sheet(sheet_name)
 
for row_idx in range(sheet.nrows):
    udid = sheet.cell(row_idx, 0).value  
    udid = udid if udid else ''
    udid = str(udid)
    
    if udid in udids:
        continue
        
    udids.append(udid)  
    
    name = sheet.cell(row_idx, 1).value 
    name = name if name else ''  
    
    pinyin_name = ''.join(pypinyin.lazy_pinyin(name))
    sheet_new.write(row_idx, 1, pinyin_name)  
    
    line = udid + '\t' + pinyin_name + '\tios\n' 
    outfile.write(line)       

# workbook_new.save('devices_new.xlsx')   
outfile.close()