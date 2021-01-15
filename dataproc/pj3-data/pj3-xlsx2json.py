import openpyxl
import json
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
    wb1 = openpyxl.load_workbook('1.xlsx')
    wb2 = openpyxl.load_workbook('2.xlsx')

    data = {}
    data.update(xlsx2obj(wb1))
    data.update(xlsx2obj(wb2))
    #print(data)

    jsondata = "demo("
    jsondata = json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False)
    jsondata += ")"

    #jsondata2 = json.dumps(data, sort_keys=True)
    #jsondata = demjson.encode(data)

    with open("data.json", mode='w+') as f:
        f.write(jsondata)
    
    #with open("data2.json", mode='w+') as f:
    #    f.write(jsondata2)