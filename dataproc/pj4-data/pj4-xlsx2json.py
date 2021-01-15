import openpyxl
import json
import os
#import demjson

def xlsx2obj(wb):
    data = {}

    for sheet in wb:
        #print(sheet.title)
        tab = []
        rowcount = 0
        for rows in sheet.values:
            #第一行 
            if(rowcount == 0):
                rowcount = 1
                firstrow = list(rows)
                tmprow = []
                tmprow.append(firstrow[0])
                for i in range(1, len(firstrow)):
                    if(firstrow[i] != None):
                        tmprow.append(firstrow[i])
                    else:
                        break
                tab.append(tmprow)
                continue
                
            if(rows[0] != None):
                tmprow = []
                for item in rows:
                    if(item != None):
                        tmprow.append(item)
                    else:
                        break
                tab.append(tmprow)
        #print(tab)

        sheetdata = {sheet.title:tab}
        data.update(sheetdata)
    return data

if __name__=="__main__":
    projectdir = "./"
    datalist = os.listdir(projectdir)  # 列出文件夹下所有的目录与文件
    #print(datalist)

    for i in range(0, len(datalist)):
        if not datalist[i].endswith('.xlsx'):
            continue
        wb =  openpyxl.load_workbook(os.path.join(projectdir, datalist[i]))
        data = {}
        data.update(xlsx2obj(wb))
        #print(data)

        jsondata = "callback" + str(i + 1) + "("
        jsondata += json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False)
        jsondata += ")"

        with open(projectdir + "/data-" + str(i+1) + ".json", mode='w+', encoding='utf-8') as f:
            f.write(jsondata)
            
        '''    
        jsondata2 += demjson.encode(data)

        with open(projectdir + "/data-" + str(i+1) + ".json", mode='w+', encoding='utf-8') as f:
            f.write(jsondata2)
        '''

    #data.update(xlsx2obj(wb2))
    #print(data)

    #jsondata2 = json.dumps(data, sort_keys=True)
    #jsondata = demjson.encode(data)

#    with open("data.json", mode='w+') as f:
#        f.write(jsondata)
    
#    with open("data2.json", mode='w+') as f:
#        f.write(jsondata2)