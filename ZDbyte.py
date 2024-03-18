import time
import os 
import datetime
import requests
from ftplib import FTP
from os import walk #for get_list_of_namefile_in_dirctory() fun 
import json
import ast
import platform
import hashlib
import threading

allflist = ['Get_time_now','s','m','h','datenow','create_file_not_exist','readtxt','writetxt',
'createfile','exist_file','createfolder','colosroot','logwrite','countlinetext','getpcname',
'removefile','readlineslected','locktext','unlocktext']


VER = "1.2"
BUILD = "1005"
Me = "N"

infolist = [VER,"+20",0] #number1 ver - number2 function active - number 3 disable function
                                                                                                                                                                                   


# VERTION : NOT LAST VERTION * 

# time now


def Get_time_now():
    secence = time.strftime('%S')
    min = time.strftime('%M')
    hours = time.strftime('%H')

    timenow = f'{hours}:{min}:{secence}'
    return timenow


# all time now

def S():
    secence = time.strftime('%S')
    times = secence
    return times

def M():
    min = time.strftime('%M')
    times = min
    return times

def H():
    hours = time.strftime('%H')
    times = hours
    return times

#----------------------------

def finisht(number):
    number2 = 0
    if number != 0:
        while not number2 == number:
            number2 += 1
            os.system('start')
    else:
        print("Erorr : pleas enter number , TMX to infinity number")
    


def date_now():
    x = datetime.datetime.now()
    x = str(x)
    # x = x[0]+x[1]+x[3]+x[3]+x[4]+x[5]+x[6]+x[7]+x[8]+x[9]+x[10]+x[11]+x[12]+x[13]+x[14]+x[15]+x[16]+x[17]+x[18]+x[19]+x[20]+x[21]+x[22]+x[23]+x[24]+x[25]
    x = x.split(' ')
    x = x[0]
    return x


def create_file_not_exist(filepach):
    zedbytere = False
    try:
        with open(filepach ,  encoding='utf-8') as f:pass
    except IOError as e:
        zedbytere = True

    if zedbytere == True:
        dnsc = open(filepach, 'w+' ,  encoding='utf-8')
        

def read_txt(filepach):

    zedbyteread = open(filepach,'r' ,  encoding='utf-8')
    Zedbytereadd = zedbyteread.read()
    zedbyteread.close()
    return Zedbytereadd

def write_txt(filepach,str):
    zedbytewrite = open(filepach,'w' ,  encoding='utf-8')
    zedbytewrite.write(str)
    zedbytewrite.close()

def create_file(filepach):
    zedbytecreatefile = open(filepach,'w+' ,  encoding='utf-8')
    zedbytecreatefile.close()

def exist_file(filepach):
    result = True
    try:
        with open(filepach ,  encoding='utf-8') as f:pass
    except IOError as e:
        result = False
    return result

def create_folder(directory):
    os.system(f'mkdir {directory}')



def colos_root(root):
    return root.destroy()



def log_write(logdirectory,massege,date,timechaneg,timechangevalue):
    if timechaneg == True:
        timechanegg = timechaneg
        cmdd = timechangevalue
        cmd = '-'
        cmdd = int(cmdd)

        time = Get_time_now()
        datenows = date_now()
        datelist = datenows.split('-')


        year = datelist[0]
        month = datelist[1]
        day = datelist[2]

        year = int(year)
        month = int(month)
        day = int(day)


        if cmd == '-':
            day = day - cmdd
            if day < 0:
                month  = month - 1
                dday = 30
                day = dday + day


        finaldate = f'{year}-{month}-{day}'
        

        time2 = Get_time_now()
        dateee = f'[{time2} {finaldate}]' 

        a = open(logdirectory,'a' ,  encoding='utf-8')
        a.writelines(f'{dateee} {massege} \n')
        a.close()


    if timechaneg == False:
        if date == True:
            time = Get_time_now()
            datenows = date_now()
            datee = f'[{time} {datenows}]'
            a = open(logdirectory,'a' ,  encoding='utf-8')
            a.writelines(f'{datee} {massege} \n')
            a.close()

        if date == False:
            a = open(logdirectory,'a' ,  encoding='utf-8')
            a.writelines(f'{massege} \n')
            a.close()
        else:
            time = Get_time_now()
            datenows = date
            datee = f'[{time} {datenows}]'
            a = open(logdirectory,'a' ,  encoding='utf-8')
            a.writelines(f'{datee} {massege} \n')
            a.close()           


def count_of_line_text(filepach):
    file = open(f'{filepach}','r')
    Lines = file.readlines()
    count = 0
    for line in Lines:
        count += 1
    return count


def get_device_name():
    import platform
    return platform.node()


def remove_file(filepach):
    os.remove(filepach)



def read_line_slected(filepach,count):
    count = int(count)
    count = count - 1
    file = open(filepach,'r')
    Lines = file.readlines()
    s = Lines[count]
    s = s[0:-1]
    return s




def lock_text(key,str):
    codetext = ''

    fakelist = ["a", "b", 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 'b',"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
                's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', " ","!","@","#","$","%","^","&","*",'(',")","-","=","+","/","+",".","_","\\","\n","\t"," ","'",'"',":","[",
                "]","{","}",",","|","<",">","?","`","~","─","_"]


    orglist = ["a", "b", 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 'b',"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
                's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', " ","!","@","#","$","%","^","&","*",'(',")","-","=","+","/","+",".","_","\\","\n","\t"," ","'",'"',":","[",
                "]","{","}",",","|","<",">","?","`","~","─","_"]
    
    num = 0
    for i in key:
        indexed = orglist.index(i)
        num += indexed

    for i in range(num):
        fakenum = fakelist[0]
        fakelist.remove(fakenum)
        fakelist.append(fakenum)

    for c in str:

        codetext += fakelist[orglist.index(c)]
    return codetext




def unlock_text(key,str):
    # fakelist = ['l', 'g', 'u', '?', 'j', 'd', 't', 'a', '1', 'x', 'f', 'c', '3', 'r', 'v', 'q', 'b',
    #         '0', 'p', 'k', 'w', 'h', 'i', '2', 'm', 'e', '6', 's', '8', 'n', 'z', '7', 'y', 'o', '4', '9', '5',"!","@","#","$","%","^","&","*",'(',")","-","=","+","/","+","."]


    # orglist = ["a", "b", 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
    #         's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', " ","!","@","#","$","%","^","&","*",'(',")","-","=","+","/","+","."]
    fakelist = ["a", "b", 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 'b',"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
                's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', " ","!","@","#","$","%","^","&","*",'(',")","-","=","+","/","+",".","_","\\","\n","\t"," ","'",'"',":","[",
                "]","{","}",",","|","<",">","?","`","~","─","_"]


    orglist = ["a", "b", 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 'b',"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
                's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', " ","!","@","#","$","%","^","&","*",'(',")","-","=","+","/","+",".","_","\\","\n","\t"," ","'",'"',":","[",
                "]","{","}",",","|","<",">","?","`","~","─","_"]

    num = 0

    
    for i in key:
        indexed = orglist.index(i)
        num += indexed

    for i in range(num):
        fakenum = fakelist[0]
        fakelist.remove(fakenum)
        fakelist.append(fakenum)

    normaltext = ''
    for c in str:
        normaltext += orglist[fakelist.index(c)]
   
    return normaltext
    

def read_lock_text(filepach,key,line=False):
    if line != False:
        txt = read_line_slected(filepach,line)
    if line == False:
        txt = read_txt(filepach)
    txt = unlock_text(key,txt)
    return txt



def write_locked_txt(filepach,key,str):
    s = False
    try:
        code = lock_text(key,str)
        write_txt(filepach,code)
    except:
        s = True
        return 'some wrong'
    if s == False:
        return 'sucssefuly writed!'
        

def connecten_test(server,timeoutint):
    url = server
    try:
        request = requests.get(url, timeout=timeoutint)
        return True
    except (requests.ConnectionError, requests.Timeout) as exception:
        return False
    




def sendtext(files):
    create_file_not_exist('C:\zdbyte\\textedit\serial\serial.txt')
    serial = read_txt('C:\zdbyte\\textedit\serial\serial.txt')
    if serial == '':
        serial = 0
    serial = int(serial)
    serial += 1
    write_txt('C:\zdbyte\\textedit\serial\serial.txt',str(serial))
    files = files.split('/')
    totoalfile = ''
    for s in files:
        totoalfile = totoalfile + '\\' + s
    files = totoalfile[1:10000000000000000000]
    print(files)
    namepc = get_device_name()
    print('connecting...')
    ftp = FTP("ftpupload.net", "epiz_30477847", "I5OGF4OakMf")
    print('connected!')
    try:
        ftp.mkd(f'htdocs/TextEditor/{namepc}')
        print('folder created!')
    except:
        None
    ftp.cwd(f"htdocs/TextEditor/{namepc}")
    print('folder opend')

    filess = files.split('\\')
    namefilee = filess[-1]
    f = open(files, "rb")
    print('file opened')
    print(f)
    ftp.storbinary(f"STOR serial : {serial} name : {namefilee}", f)
    print('sucssefully uploaded!')


    f.close()
    ftp.quit()





end = False
# def download_req_file(List,dic,namefiles):
#     from PyQt5 import QtCore,QtWidgets
#     import urllib.request











#     create_folder(dic)
#     powershellbutton = '''

#             QPushButton
#             {
#                 color: white;
#                 background: #252526;
#                 border: 1px black solid;
#                 padding: 5px 10px;
#                 border-radius: 8px;
#                 font-size: 9pt;
#                 outline: none;
#                 border: 1px solid white;

#             }
#             QPushButton:hover{
#                 border: 1px black solid;
#                 color: white;
#                 background: #FF1A1A;
#                 border: 1px solid #FF1A1A;
#             }

#     '''
#     powershellbuttonstart = '''

#             QPushButton
#             {
#                 color: white;
#                 background: #252526;
#                 border: 1px black solid;
#                 padding: 5px 10px;
#                 border-radius: 8px;
#                 font-size: 9pt;
#                 outline: none;
#                 border: 1px solid white;

#             }
#             QPushButton:hover{
#                 border: 1px black solid;
#                 color: white;
#                 background: #2DB37A;
#                 border: 1px solid #2DB37A;
#             }

#     '''
#     powershellprogressbar= '''
#     QProgressBar
#     {
#     border:1px  solid #787878;
#     border-radius: 10px;
#     color: #2DB37A;

#     }
#     QProgressBar::chunk 
#     {
#     background-color: #2DB37A;
#     border-radius :9px;
#     }    
#     '''
#     class Ui_MainWindow(object):
#         def setupUi(self, MainWindow):
#             MainWindow.setObjectName("MainWindow")
#             MainWindow.resize(554, 135)
#             MainWindow.setStyleSheet("background-color:#252526;")
#             MainWindow.setWindowOpacity(0.98)
#             self.centralwidget = QtWidgets.QWidget(MainWindow)
#             self.centralwidget.setObjectName("centralwidget")
#             self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
#             self.progressBar.setGeometry(QtCore.QRect(30, 20, 501, 31))
#             self.progressBar.setStyleSheet(powershellprogressbar)
#             self.progressBar.setProperty("value",5)
#             self.progressBar.setTextVisible(False)
#             self.progressBar.setObjectName("progressBar")
#             self.label = QtWidgets.QLabel(self.centralwidget)
#             self.label.setGeometry(QtCore.QRect(30, 60, 481, 30))
#             self.label.setStyleSheet("color:white;")
#             self.label.setObjectName("label")
#             self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
#             self.pushButton_2.setGeometry(QtCore.QRect(200, 90, 131, 31))
#             self.pushButton_2.setStyleSheet(powershellbuttonstart)
#             self.pushButton_2.clicked.connect(self.start)

#             self.pushButton_2.setObjectName("pushButton_2")
#             MainWindow.setCentralWidget(self.centralwidget)
#             self.menubar = QtWidgets.QMenuBar(MainWindow)
#             self.menubar.setGeometry(QtCore.QRect(0, 0, 554, 21))
#             self.menubar.setObjectName("menubar")
#             MainWindow.setMenuBar(self.menubar)

#             self.retranslateUi(MainWindow)
#             QtCore.QMetaObject.connectSlotsByName(MainWindow)

#         def retranslateUi(self, MainWindow):
#             _translate = QtCore.QCoreApplication.translate
#             MainWindow.setWindowTitle(_translate("MainWindow", "installer"))
#             self.progressBar.setFormat(_translate("MainWindow", "%p%"))
#             self.label.setText(_translate("MainWindow", "total size : 841 KB"))
#             self.pushButton_2.setText(_translate("MainWindow", "start"))
            
#         def start(self):
#             global count
#             global end
            

#             _translate = QtCore.QCoreApplication.translate
#             if end == False:
#                 count = 0
#                 darsad = 0
#                 count2 = -1
#                 for link in List:
#                     count += 1
#                 for link in List:
#                     count2 += 1
#                     darsad_add = round(100 / count)
#                     darsad += darsad_add
#                     # filename = link.split('/')
#                     # filename = filename[-1]
#                     filename = namefiles[count2]

#                     self.pushButton_2.setStyleSheet(powershellbutton)

#                     self.pushButton_2.setText(_translate("MainWindow", "cancel"))
#                     self.label.setText(_translate("MainWindow", f"downloading {filename}  {count2+1}/{count}"))
#                     urllib.request.urlretrieve(link, dic[count2],self.show_progress)




#                     self.progressBar.setProperty("value",darsad)
#                     if darsad >= 100:
#                         self.progressBar.setProperty("value",100)
#                         self.label.setText(_translate("MainWindow", "Download successfully finisht \nPleas open again app"))
#                         self.pushButton_2.setText(_translate("MainWindow", "colos"))    



    
#                 end = True        
#             if end == True:
#                 self.pushButton_2.clicked.connect(QtWidgets.qApp.quit)
#                 end = True


#         def show_progress(self ,block_num, block_size, total_size):
            
#             global count
                        
#             downloaded = block_num * block_size
#             darsad = round(downloaded / total_size,2)
#             darsad = round(darsad * 100)
            
#             self.progressBar.setProperty("value",darsad)
            


#     for file in dic:
#         file1 = exist_file(file)
#         print(file1)
#         if file1 == True:
#             None
#         else:    
#             if __name__ == "__main__":
#                 import sys
#                 app = QtWidgets.QApplication(sys.argv)
#                 MainWindow = QtWidgets.QMainWindow()
#                 ui = Ui_MainWindow()
#                 ui.setupUi(MainWindow)
#                 MainWindow.show()
#                 sys.exit(app.exec_())


def count_str_selected(filepach,str):
    count3 = 0
    while True:
        count3 += 1
        s = read_line_slected(filepach,count3)
        if s == str:
            return count3
            
def get_list_of_namefile_in_dirctory(DICpath):
    f = []
    for (dirpath, dirnames, filenames) in walk(DICpath):
        f.extend(filenames)
        return f
        
def json_string_to_json(string):
    data_dict = json.loads(string)
    return data_dict


def json_exist_key(dircory,value):
    #if return false key is not exist
    with open(dircory ,  encoding='utf-8') as f:
        data = json.load(f)

    keyofjsonfile = list(data.keys())

    if value in keyofjsonfile:
        return True
    else:
        return False      

def json_write(dircory , dict:dict):

    with open(dircory , encoding='utf-8') as f:
        data = json.load(f)

    keyofjsonfile = list(data.keys())

    for item in keyofjsonfile:
        itme2 = data[item]
        dict[item] = itme2



    with open(dircory, 'w', encoding='utf-8') as outfile:
        json.dump(dict,outfile, ensure_ascii=False, indent=4)


def json_replace(dircory , dict):
    with open(dircory, 'w', encoding='utf-8') as outfile:
        json.dump(dict,outfile, ensure_ascii=False, indent=4)


def json_write_value_key(dircory,key,newvlaue):
    """and you can add new `key.value` to json recomment for this use `ZDbyte.json_write()`"""
    with open(dircory) as f:
        data = json.load(f)
    data[key] = newvlaue


    json_replace(dircory,data)


def json_load(dircory):
    with open(dircory , encoding='utf-8') as f:
        data = json.load(f)
    return data


def json_delet_key(dircory,key):
    with open(dircory) as f:
        data = json.load(f)

    data.pop(key)


    with open(dircory, 'w') as outfile:
        json.dump(data, outfile, sort_keys = True, indent = 4,
                ensure_ascii = False)    

def json_update(dircory:str,dictionary:dict):
    D = json_load(dircory)
    D.update(dictionary)
    json_replace(dircory,D)

# class Zjson():
#     """Power from `json` Lib"""
#     file = ""
#     def connectFile(self,file):
#         self.file = file
#         return f'UPDATED TO "{self.file}"'

#     def read(self):
#         """ return `DICT` file """
        
#         if read_txt(self.file) != "": 
#             with open(self.file , encoding='utf-8') as f:
#                 data = json.load(f)
#             return data
#         return {}

#     def replace(self,dict):
#         """delete all data in file and replace full whit new data"""

#         with open(self.file, 'w', encoding='utf-8') as outfile:
#             json.dump(dict,outfile, ensure_ascii=False, indent=4)

#     def append(self,dict:dict):
#         """if key exsist old value replace whit new"""



#         if read_txt(self.file) == "": 
#             write_txt(self.file,"{}")

#         for key , value in dict.items():

#             with open(self.file) as f:
#                 data = json.load(f)
#             data[key] = value

#             json_replace(self.file,data)             

#     def removeKey(self,key):
#         with open(self.file) as f:
#             data = json.load(f)

#         data.pop(key)


#         with open(self.file, 'w') as outfile:
#             json.dump(data, outfile, indent = 4,ensure_ascii = False)    

#     def exsist(self,key):
#         """cheak key exsist"""
#         return json_exist_key(self.file,key)

# FIXED 
# Zjson NOT TESTED YET

class Zjson():
    """Power from `json` Lib"""
    file = ""
    lock = threading.Lock()  # Add a lock for concurrent write protection

    def connectFile(self, file):
        self.file = file
        return f'UPDATED TO "{self.file}"'

    def read(self):
        """ return `DICT` file """
        # if read_txt(self.file) != "":
        with self.lock:
            with open(self.file,  "r" , encoding='utf-8' ) as f:
                data = json.load(f)
            return data
        # return {}
    
    def replace(self, dict):
        """delete all data in file and replace full with new data"""
        with self.lock:  # Acquire lock before writing
            with open(self.file, 'w', encoding='utf-8') as outfile:
                json.dump(dict, outfile, ensure_ascii=False, indent=4)

    # def append(self, dict: dict):
    #     """if key exists old value replace with new"""
    #     with self.lock:  # Acquire lock before writing
    #         if os.path.getsize(self.file) > 1024 * 1024 * 10:  # Limit file size to 10 MB, adjust as needed
    #             # If the file size exceeds the limit, replace the content with new data
    #             # self.replace(dict)
    #             pass
    #         else:
    #             if read_txt(self.file) == "":
    #                 write_txt(self.file, "{}")

    #             with open(self.file, 'r', encoding='utf-8') as f:
    #                 data = json.load(f)

    #             for key, value in dict.items():
    #                 data[key] = value

    #             with open(self.file, 'w', encoding='utf-8') as outfile:
    #                 json.dump(data, outfile, ensure_ascii=False, indent=4)
    def append(self, data_to_append: dict):
        """If key exists, old value is replaced with new."""
        with self.lock:
            try:
                with open(self.file, 'r', encoding='utf-8') as file:
                    existing_data = json.load(file)
            except (json.JSONDecodeError, FileNotFoundError):
                # Handle JSON decoding errors or file not found exceptions
                existing_data = {}

            existing_data.update(data_to_append)

            with open(self.file, 'w', encoding='utf-8') as file:
                json.dump(existing_data, file, ensure_ascii=False, indent=4)


    def removeKey(self, key):
        with self.lock:  # Acquire lock before writing
            with open(self.file) as f:
                data = json.load(f)

            data.pop(key)

            with open(self.file, 'w') as outfile:
                json.dump(data, outfile, indent=4, ensure_ascii=False)

    def exsist(self, key):
        """check if key exists"""
        return json_exist_key(self.file, key)


def color_generator(Mode="html"):
    import random
    if Mode == "html":
        hexadecimal = ["#"+''.join([random.choice('ABCDEF0123456789') for i in range(6)])]
        return hexadecimal
    elif Mode == "rgb":
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        rgb = [r,g,b]
        return rgb
    else:
        return("mode just get html or rgb")





def sqlite_exsist_table(directory,table_name):
    import sqlite3
    conn = sqlite3.connect(directory)
    c = conn.cursor()
    c.execute(f''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='{table_name}' ''')

    if c.fetchone()[0]==1 : 
        conn.commit()
        conn.close()
        return True
    else:
        conn.commit()
        conn.close()
        return False

    







class request_old: 
    domain = "http://192.168.1.102:5000"

    def create_table(self,table_name,paragraf,password):
        req = requests.get(f"{self.domain}/create_table/{table_name}/{paragraf}/{password}")
        #example syntax of paragraf : id integer PRIMARY KEY,username text NOT NULL,password text NOT NULL" 
        #sqlite syntax
        back = req.text
        return back
            
    def read_table(self,table_name,password):

        req = requests.get(f"{self.domain}/read_database/{table_name}/{password}")
        back = req.text
        res = ast.literal_eval(back)
        return res

    def clear(self,table_name,password):

        req = requests.get(f"{self.domain}/clear_table/{table_name}/{password}")
        back = req.text
        return back

    def delet(self,table_name,password):

        req = requests.get(f"{self.domain}/delet_table/{table_name}/{password}")
        back = req.text
        return back


    def delet_record(self,table_name,selector_record,select,password):

        req = requests.get(f"{self.domain}/delet_record_database/{table_name}/{selector_record}/{select}/{password}")
        back = req.text
        return back

    def append(self,table_name,items,value,password):


        list_value = value.split(",")
        new_value = ""


        for_count = 0
        for item in list_value:
            
            if for_count == 0:
                new_value = new_value +"'" + item + "'"
                
            else:
                new_value = new_value + ",'" + item + "'"
            for_count += 1



        print(list_value)
        print(new_value)
        req = requests.get(f"""{self.domain}/append_database/{table_name}/{items}/{new_value}/{password}""")
        back = req.text
        return back
        # syntax : append('my_table','id,username,mahdi','4,mahdi,123',my_table_password)  
        # sqlite syntax.


def re(res):
    domain = "https://server56.pythonanywhere.com"
    url = requests.get(f"{domain}/{res}")
    htmltext = url.text
    return htmltext            


class request:
    folder = str
    password = str
    def connect(self,folder,password):
        url = requests.get(f"https://server56.pythonanywhere.com/check/{folder}/{password}")
        back = url.text
        if back == "True":
            self.folder = folder
            self.password = password
            return "connected"
        elif back == "False":
            return "FOLDER OR PASS NOT VALUED"


    def create_folder(self,folder,password):
        back = re(f"/create_folder/{folder}/{password}")
        return back

    def create_db(self,db_name):
        if self.folder and self.password == None:
            return "please connect to folder white connect(folder,password)"
        else:
            back = re(f"/create_db/{self.folder}/{self.password}/{db_name}")
            return back

    def create_table(self,db,table,query):
        # example query  : id integer PRIMARY KEY , msg text NOT NULL
        # sqlite  query
        if self.folder and self.password == None:
            return "please connect to folder white connect(folder,password)"
        else:
            back = re(f"/create_table/{self.folder}/{self.password}/{db}/{table}/{query}")
            return back        


    def append(self,db,table,items,value_items):
        # example:
        # item : id,text
        # value_itme : 1,hello_world
        list_items = value_items.split(",")
        final_items = ""
        count = 0
        for i in list_items:
            if count == 0:
                final_items = final_items + "'" + i + "'"
            else:
                final_items = final_items + ",'" + i + "'"
            count += 1
        print(final_items)
        back = re(f"""/append/{self.folder}/{self.password}/{db}/{table}/{items}/{final_items}""")
        return back
        
    
    def delet_all_table(self,db):
        back = re(f"/delet_all_table/{self.folder}/{self.password}/{db}")
        return back




    def clear_table(self,db,table):
        back = re(f"/clear_tb/{self.folder}/{self.password}/{db}/{table}")
        return back
    




    def del_db(self,db):
        back = re(f"/del_db/{self.folder}/{self.password}/{db}")
        return back
    


    def del_table(self,db,table):
        back = re(f"/del_tb/{self.folder}/{self.password}/{db}/{table}")
        return back



    def del_record(self,db,table,selector,select):
        back = re(f"/del_record/{self.folder}/{self.password}/{db}/{table}/{selector}/{select}")
        return back




    def execute(self,db,query):
        back = re(f"/execute/{self.folder}/{self.password}/{db}/{query}")
        # query : query of sqlite command
        return back

    def read_table(self,db,table_name):
        back = re(f"/read/{self.folder}/{self.password}/{db}/{table_name}")
        res = ast.literal_eval(back)
        return res


    def close(self):
        self.folder = None
        self.password = None

def decode_web(str):
    to_change = ['"',"'",',',"/","\\","?","$"," ","."]
    # change_to = ["%10","%20","%30","%40","%50","%60","%70","%85","%100"]
    change_to = ["{10}","{20}","{30}","{40}","{50}","{60}","{70}","{85}","{100}"]
    count = 0
    for item in to_change:
        str = str.replace(item,change_to[count])        
        count += 1
    return str

def uncode_web(str):
    change_to = ['"',"'",',',"/","\\","?","$"," ","."]
    # to_change = ["%10","%20","%30","%40","%50","%60","%70","%85","%100"]
    to_change = ["{10}","{20}","{30}","{40}","{50}","{60}","{70}","{85}","{100}"]
    count = 0
    for item in to_change:
        str = str.replace(item,change_to[count])        
        count += 1
    return str


def decode(str):
    to_change = ['"',"'",',',"/","\\","?","$"," ","."]
    change_to = ["%10","%20","%30","%40","%50","%60","%70","%85","%100"]

    count = 0
    for item in to_change:
        str = str.replace(item,change_to[count])        
        count += 1
    return str

def uncode(str):
    change_to = ['"',"'",',',"/","\\","?","$"," ","."]
    to_change = ["%10","%20","%30","%40","%50","%60","%70","%85","%100"]

    count = 0
    for item in to_change:
        str = str.replace(item,change_to[count])        
        count += 1
    return str

class math:
    def _abs(self,number:int):
        if  number < 0:
            return abs(number)
        elif number > 0:
            number = str(number)
            number = "-" + number
            return int(number) 
        else:
            return number

    def _index(self,str:str,index:int,to:str):
        str = list(str)
        str[index] = to
        str = ''.join(str)
        print(str)
        return str

    def _abs_(self,str:str):
        str =  "-" + str
        return str



    def Equation(self,your_Equation:str):
        Equation = str(your_Equation)
        Equation_Equal = Equation.split("=")
        try:
            s = Equation_Equal[2]
            return "DONT ENTER MANY ="
        except:
            INDEX = 0
            NUMBER_RIGHT = list()
            for i in Equation_Equal[0].split(" "):
                try:
                    i = int(i)
                    NUMBER_RIGHT.append(i)

                    
                    INDEX += 1
                except:
                    pass
            anserw_right = 0
            for i in NUMBER_RIGHT:
                anserw_right += i


            INDEX = 0
            NUMBER_LEFT = list()
            for i in Equation_Equal[1].split(" "):
                try:
                    i = int(i)
                    NUMBER_LEFT.append(i)
                    # Equation_Equal[1] = Equation_Equal[1] + f" {i}" 
                    # Equation_Equal_left = Equation_Equal[0]
                    
                    INDEX += 1
                except:
                    pass
            anserw_left = 0
            for i in NUMBER_LEFT:
                anserw_left += i


            



            LETTERS_LEFT = list()
            for i in Equation_Equal[0].split(" "):
                try:
                    i = int(i)
                except:
                    if not i == "" and " ":
                        LETTERS_LEFT.append(i)
            total_left = str()
            for i in LETTERS_LEFT:
                total_left = total_left + " " + str(i)



            LETTERS_RIGHT = list()
            for i in Equation_Equal[1].split(" "):
                try:
                    i = int(i)
                except:
                    if not i == "" and " ":
                        LETTERS_RIGHT.append(i)
            total_right = str()

            for i in LETTERS_RIGHT:
                total_right = total_right + " " + str(i)
                


            #main
            anserw_right = self._abs(anserw_right)
            anserw_num = anserw_left + anserw_right
            NEW_TOTAL_RIGHT = list()
            for i in total_right.split(" "):
                NEW_TOTAL_RIGHT.append(self._abs_(i)) 
            NEW_TOTAL_RIGHT2 = list()
            for i in NEW_TOTAL_RIGHT:
                i = i[0:-1]
                NEW_TOTAL_RIGHT2.append(i)
            NEW_TOTAL_LEFT = list()


            TOTAL_LEFT = list()
            for i in total_left.split(" "):
                TOTAL_LEFT.append(i)
            for i in TOTAL_LEFT:

                i = i[0:-1]    
                NEW_TOTAL_LEFT.append(i)

            ANSERW_LETERS_RIGHT = int()
            for i in NEW_TOTAL_RIGHT2:
                try:
                    int(i)
                    ANSERW_LETERS_RIGHT = int(ANSERW_LETERS_RIGHT) + int(i)
                except:
                    pass





            ANSERW_LETERS_LEFT = int()
            for i in NEW_TOTAL_LEFT:
                try:
                    int(i)
                    ANSERW_LETERS_LEFT = int(ANSERW_LETERS_LEFT) + int(i)
                except:
                    pass
            ANSERW_LETERS = ANSERW_LETERS_LEFT + ANSERW_LETERS_RIGHT
            return f"{ANSERW_LETERS}x = {anserw_num}"


    def num_to_percent(count:int,All:int):
        return (count * 100) / All

    def percent_to_number(percent:int,All:int):
        return (All * percent) / 100
        
    def randomInt(start:int,end:int):
        number = range(start,end + 1)
        NUMBER = list()
        for i in number:
            NUMBER.append(str(i))
        Set = set()
        Set.update(NUMBER)
        for j in Set:
            return int(j)

    def randomStr(ListOfStr:list):
        Set = set()
        Set.update(ListOfStr)
        for j in Set:
            return str(j)

class Zfile:
    def create_file_not_exist(self,filepach):
        zedbytere = False
        try:
            with open(filepach) as f:pass
        except IOError as e:
            zedbytere = True

        if zedbytere == True:
            dnsc = open(filepach, 'w+')


    def read_txt(self,filepach):

        zedbyteread = open(filepach,'r')
        Zedbytereadd = zedbyteread.read()
        zedbyteread.close()
        return Zedbytereadd

    def write_txt(self,filepach,str):
        zedbytewrite = open(filepach,'w')
        zedbytewrite.write(str)
        zedbytewrite.close()

    def create_file(self,filepach):
        zedbytecreatefile = open(filepach,'w+')
        zedbytecreatefile.close()

    def exist_file(self,filepach):
        result = True
        try:
            with open(filepach) as f:pass
        except IOError as e:
            result = False
        return result

    def create_folder(self,directory):
        os.mkdir(f'mkdir {directory}')
        

def log_write(logdirectory,massege,date,timechaneg=False,timechangevalue=0):
    if timechaneg == True:
        timechanegg = timechaneg
        cmdd = timechangevalue
        cmd = '-'
        cmdd = int(cmdd)

        time = Get_time_now()
        datenows = date_now()
        datelist = datenows.split('-')


        year = datelist[0]
        month = datelist[1]
        day = datelist[2]

        year = int(year)
        month = int(month)
        day = int(day)


        if cmd == '-':
            day = day - cmdd
            if day < 0:
                month  = month - 1
                dday = 30
                day = dday + day


        finaldate = f'{year}-{month}-{day}'
        

        time2 = Get_time_now()
        dateee = f'[{time2} {finaldate}]' 

        a = open(logdirectory,'a')
        a.writelines(f'{dateee} {massege} \n')
        a.close()


    if timechaneg == False:
        if date == True:
            time = Get_time_now()
            datenows = date_now()
            datee = f'[{time} {datenows}]'
            a = open(logdirectory,'a')
            a.writelines(f'{datee} {massege} \n')
            a.close()

        if date == False:
            a = open(logdirectory,'a')
            a.writelines(f'{massege} \n')
            a.close()
        else:
            time = Get_time_now()
            datenows = date
            datee = f'[{time} {datenows}]'
            a = open(logdirectory,'a')
            a.writelines(f'{datee} {massege} \n')
            a.close()           


    def count_of_line_text(filepach):
        file = open(f'{filepach}','r')
        Lines = file.readlines()
        count = 0
        for line in Lines:
            count += 1
        return count




    def remove_file(filepach):
        os.remove(filepach)



    def read_line_slected(filepach,count):
        count = int(count)
        count = count - 1
        file = open(filepach,'r')
        Lines = file.readlines()
        s = Lines[count]
        s = s[0:-1]
        return s




    def lock_text(key,str):
        codetext = ''

        fakelist = ["a", "b", 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 'b',"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
                    's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', "-*-","!","@","#","$","%","^","&","*",'(',")","-","=","+","/","+",".","_"]


        orglist = ["a", "b", 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 'b',"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
                    's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', " ","!","@","#","$","%","^","&","*",'(',")","-","=","+","/","+",".","_"]

        
        num = 0
        for i in key:
            indexed = orglist.index(i)
            num += indexed

        for i in range(num):
            fakenum = fakelist[0]
            fakelist.remove(fakenum)
            fakelist.append(fakenum)

        for c in str:

            codetext += fakelist[orglist.index(c)]
        return codetext




    def unlock_text(key,str):
        # fakelist = ['l', 'g', 'u', '?', 'j', 'd', 't', 'a', '1', 'x', 'f', 'c', '3', 'r', 'v', 'q', 'b',
        #         '0', 'p', 'k', 'w', 'h', 'i', '2', 'm', 'e', '6', 's', '8', 'n', 'z', '7', 'y', 'o', '4', '9', '5',"!","@","#","$","%","^","&","*",'(',")","-","=","+","/","+","."]


        # orglist = ["a", "b", 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
        #         's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', " ","!","@","#","$","%","^","&","*",'(',")","-","=","+","/","+","."]
        fakelist = ["a", "b", 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 'b',"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
                    's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', "~","!","@","#","$","%","^","&","*",'(',")","-","=","+","/","+",".","_"]


        orglist = ["a", "b", 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 'b',"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
                    's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', " ","!","@","#","$","%","^","&","*",'(',")","-","=","+","/","+",".","_"]

        num = 0
        for i in key:
            indexed = orglist.index(i)
            num += indexed

        for i in range(num):
            fakenum = fakelist[0]
            fakelist.remove(fakenum)
            fakelist.append(fakenum)

        normaltext = ''
        for c in str:
            normaltext += orglist[fakelist.index(c)]
    
        return normaltext
        

    def read_lock_text(filepach,key,line=False):
        if line != False:
            txt = read_line_slected(filepach,line)
        if line == False:
            txt = read_txt(filepach)
        txt = unlock_text(key,txt)
        return txt



    def write_locked_txt(filepach,key,str):
        s = False
        try:
            code = lock_text(key,str)
            write_txt(filepach,code)
        except:
            s = True
            return 'some wrong'
        if s == False:
            return 'sucssefuly writed!'





def generade_character(count:int):
    from random import randint
    li = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
     'x', 'y', 'z',"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    string = str()
    for i in range(0,count):
        num = randint(0,51)
        string = string + li[num]
    return string


def setInterval(func, sec):
    import threading
    def func_wrapper():
        setInterval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t




# replace = [",","'"]


# txt = f"hello,wrold%20 fwafwa96%sadfaw 'sadw22t% '"


# decoder failed

# replace = [",","'"]


# txt = f"hello,wrold%20 fwafwa96%sadfaw 'sadw22t% '"



# replace = list(set(replace))
# replace_to = list()
# COUNT = 0
# for i in replace:
#     COUNT += 1
#     # if COUNT * 6 > 100:
#     #     replace_to.append(str(int(COUNT*6 / 10))+"%")
#     # else:
#     replace_to.append(str(COUNT*6)+"%")





# INDEX = 0
# for i in replace_to:
#     if i in txt:
#         i_number = int(i.replace("%",""))
#         try_number = 0
#         while True:
#             i_number += 4
#             i2 = str(i_number) + f"t{try_number}%"
#             if i2 in txt:
#                 try_number += 1
#             else:
#                 replace_to[INDEX] = i2
#                 break
#     INDEX += 1

# INDEX = 0
# for i in replace:
#     txt = txt.replace(i,replace_to[INDEX])
#     INDEX += 1

# print(replace_to)
# print(txt)
# # def decode(txt:str,replace:list):
    



def literal_eval(String:str):
    import ast
    List = ast.literal_eval(String)
    return List
    




class FormatError(Exception):
    """cant read this format just .z format"""


    def __init__(self, message="cant read this format just .z format"):
        self.message = message
        super().__init__(self.message)




class ExsistErorr(Exception):
    """Cant find this file"""
    def __init__(self, message="Cant find this file"):
        self.message = message
        super().__init__(self.message)


class NotopenErorr(Exception):
    """please frist openfile"""
    def __init__(self, message="please frist openfile"):
        self.message = message
        super().__init__(self.message)



class Zfile:
    repeat = True
    path = None
    def open(self,path,repeat=True):
        """open just `.z` file Or `.zd` file"""
        formaT = path.split('.')[-1]
        if formaT in ["z","zd"]:
            create_file_not_exist(path)
            exsist = exist_file(path)
            if exsist == True:
                self.path = path
                self.repeat = repeat
                return "succsess"
            else:
                create_file_not_exist(path)
        else:
            raise FormatError

    def _ch1_(self):
        """`Don't` use this is `Bild-in` function"""
        if self.path == None:
            raise NotopenErorr
        else:
            pass

    def _delr_(self):
        """`Don't` use this is `Bild-in` function"""
        self._ch1_()
        txt = read_txt(self.path)
        txt = txt[0:-1].split(",\n")
        DICT = dict()
        for i in txt:
            i = i.split("=")
            try:
                DICT[i[0]] = i[1]
            except:
                print(i)
        txt = ""
        for key , value in DICT.items():
            val = key + "=" + value
            txt = txt + val + ",\n"
        write_txt(self.path,txt[0:-3])

    def _wr_(self,v):
        """`Don't` use this is `Bild-in` function"""
        self._ch1_()
        file_object = open(self.path, 'a')
        file_object.write(v + ",\n")
        file_object.close()



    def write(self,item:dict,lock:bool):
        """send `dict` to fnction"""
        self._wr_("temp=dont-del-this:hide")
        from urllib.parse import quote 
        self._ch1_()
        if lock == True:
            pass
        elif lock == False:
            for key , value in item.items():
                type_of_val = type(value)
                value = str(value)
                key = quote(key) 
                value = quote(value)


                
                if type_of_val == int:
                    val = key + "=" + value + ":int"
                elif type_of_val == str :
                    val = key + "=" + value + ":str"
                elif type_of_val == bool :
                    val = key + "=" + value + ":bool"
                elif type_of_val == list :
                    val = key + "=" + value + ":list"
                elif type_of_val == tuple :
                     val = key + "=" + value + ":tuple"
                else:
                    val = key + "=" + value

                self._wr_(val)
        if self.repeat == True:
            self._delr_()






    def read(self,passwordIfAllow:str=None):
        """return a `dict`"""
        from urllib.parse import  unquote
        if passwordIfAllow == None:
            TXT = read_txt(self.path)
            TXT2 = TXT.split(",")
            DICT = dict()
            for i in TXT2:
                if i != '':

                    i = i.split("=")

                    i2 = i[1].split(":")
                    i[0] = i[0].replace("\n","")
                    if i2[-1] == "hide":
                        pass
                    elif i2[-1] == "int":
                        DICT[unquote(i[0])] = int(unquote(i2[0]))
                    elif i2[-1] == "str":
                        DICT[unquote(i[0])] = str(unquote(i2[0]))
                    elif i2[-1] == "bool":
                        if i2[0] == "True":
                            DICT[unquote(i[0])] = bool(unquote(i2[0]))
                        else:
                            DICT[unquote(i[0])] = False
                    elif i2[-1] == "list":
                        DICT[unquote(i[0])] = literal_eval(unquote(i2[0]))
                    elif i2[-1] == "tuple":
                        DICT[unquote(i[0])] = literal_eval(unquote(i2[0]))
                    else:
                        DICT[unquote(i[0])] = unquote(i2[0])

            return DICT
    
    def close(self):
        """`close` a opened file"""
        self.path = None
    
    def pop(self,key):
        """send `key` to delet"""
        txt = read_txt(self.path)
        txt_l = txt.split(",")
        INDEX = 0
        key = f'\n{key}'
        for i in txt_l:
            i2 = i.split("=")
            
            if i2[0] == key:
                print("wOw")
                print(i2[0])

                txt_l.pop(INDEX)
                break
            else:
                print(i2[0])

            INDEX += 1
        txt_l = ",".join(txt_l)
        write_txt(self.path,txt_l)


def literal_eval(String:str):
    import ast
    List = ast.literal_eval(String)
    return List
    
class temp:
    import tempfile
    Tempdir = tempfile.gettempdir() # change that soon...
    

    def mkdtemp(self):
        gchar = 10
        Folders = get_list_of_namefile_in_dirctory(self.Tempdir)
        tempname = ".temp$" +  generade_character(gchar)
        trys = 0
        while True:
            trys += 1
            if tempname in Folders:
                if trys >= 100:
                    gchar +=1 
                    tempname =".temp$" + generade_character(gchar)
                    trys = 1
                else:
                    tempname =".temp$" + generade_character(gchar)
            else:
                create_folder(self.Tempdir + "\\" + tempname)
                return (self.Tempdir + "\\" + tempname)
    
intervals = (
    ("years", 6622560000),
    ("month", 18144000),
    ('weeks', 604800),  # 60 * 60 * 24 * 7
    ('days', 86400),    # 60 * 60 * 24
    ('hours', 3600),    # 60 * 60
    ('minutes', 60),
    ('seconds', 1),
)

def coverent_time(seconds, granularity=2):
    result = []

    for name, count in intervals:
        value = seconds // count
        if value:
            seconds -= value * count
            if value == 1:
                name = name.rstrip('s')
            result.append("{} {}".format(value, name))
    return ', '.join(result[:granularity])






def stampToAgo(timeStamp):
    TIME = round(time.time()) - int(timeStamp)
    if TIME > 60:
        m = round(TIME / 60)
        if m >= 60:
            h = round(m / 60)
            if (h >= 24):
                d = round(h / 24)
                if d >= 30:
                    m = round(d / 30)
                    if m >= 12:
                        y = round(m / 12)
                        return str(y) + "years ago"
                    else:
                        return str(m) + " month ago"
                else:
                    return str(d) + " day ago"
            else:
                return str(h) + " hours ago"
        else:
            return str(m) + " min ago"
    else:
        return "few secend ago"
    
class static:
    """
        `ImportDirJson` need a json file like:\n
        `all name is coustom!`\n
        {
            "static" : "/project/file/static"
            "database" : "/project/file/database"
        }\n
        get(`"static"`,`"/style/index.css"`)
        return if `exsist` => /project/file/static/style/index.css
    """

    data = "404"
    def ImportDirJson(self , path:str):
        self.data = json_load(path)
    
    def get(self,Folder:str,FileName:str):
        if self.data != "404":
            SubFolder = self.data[Folder]
            PathRequest = SubFolder + "/" + FileName
            if exist_file(PathRequest) == True:
                return PathRequest  
        else:
            return "404"
        


import requests
import ZDbyte
from requests.models import Response
import base64

def base64_encode(text):
    message = text
    message_bytes = message.encode('utf-8')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('utf-8')
    return base64_message

def base64_decode(text):
    base64_message = text
    base64_bytes = base64_message.encode('utf-8')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('utf-8')
    return message


class simpleApi:
    vertion = "1.1"
    api_key = ""
    username = ""
    api_url = "http://database.pythonanywhere.com/api/"
    end_to_end_encryption = False
    encryption_key = ""
    def host_url(self,new_url):
        self.api_url = new_url


    def login(self,api_key,username,end_to_end_encryption=False,encryption_key=""):
        """`end-to-end encryption` is method for risky file"""
        self.end_to_end_encryption = end_to_end_encryption
        self.encryption_key = encryption_key
        self.api_key = api_key
        self.username = username
    def login_cheak(self):
        api_url = self.api_url + "/cheak_permissions"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Username": self.username,
        }

        response = requests.get(api_url, headers=headers)
        return response

    def file_list(self):

        api_url = self.api_url + "/file_list"

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Username": self.username,
        }

        response = requests.get(api_url, headers=headers)
        return response
    
    def create_file(self,fileName,format):

        api_url = self.api_url + "/create_file"

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Username": self.username,
            "filename":fileName,
            "format" : format
        }

        response = requests.get(api_url, headers=headers)
        return response
    
    def write_file(self, fileName, text, use_encryption=False):
        if self.end_to_end_encryption:
            if self.encryption_key:
                if use_encryption:
                    text = ZDbyte.lock_text(self.encryption_key, text)
            else:
                return "encryption_key not set!"

        api_url = self.api_url + "/write_file"

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Username": self.username,
            "filename": fileName
        }

        data = {
            "text":(base64_encode(text))
        }

        response = requests.post(api_url, headers=headers, data=data)
        return response

    def read_file(self,fileName,use_encryption=False):



        api_url = self.api_url + "/read_file"

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Username": self.username,
            "filename":fileName
        }


        response = requests.get(api_url, headers=headers)

        if response.status_code == 200:
            data = base64_decode(eval(response.text)["text"])
            if self.end_to_end_encryption == True:
                if self.encryption_key != "":
                    if use_encryption == True:
                        data = ZDbyte.unlock_text(self.encryption_key,data)
                        response = [response,data]
                        return response
                    else:
                        response = [response,data]
                        return response
                else:
                    return "encryption_key not set!"
            else:
                response = [response,data]
                return response
            
        response = [response,response.status_code]
        return response

    def remove_file(self,fileName):

        api_url = self.api_url + "/rm_file"


        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Username": self.username,
            "filename":fileName
        }


        response = requests.get(api_url, headers=headers)
        return response

def cheakForUpdate():
    print("connecting to server...")
    api = simpleApi()
    api.login("63kj1VN7xLbjXefU78anKzxwRxQrzVekiosORqgyQUEv8wkPvoBumzaw4ITGr6NB","mahdi")
    a = api.login_cheak()
    if a.status_code == 200:
        data = api.read_file("zdbyte.json")
        if data[0].status_code == 200:
            data = eval(data[1])
            Nver = data["VER"]
            Nbuild = data["BUILD"]
            if VER != Nver:
                print(f"new vertion avalivable ({VER}) -> ({Nver})")
            else:
                if BUILD != Nbuild :
                    print(f"new vertion(BUILD) avalivable ({BUILD}) -> ({Nbuild})")
                else:
                    print("lib up to date.")
        else:
            print(f"ERORR {data[0].status_code}")
    else:
        print(f"ERORR {a.status_code}")

class log:
    patch = ""
    mode = ""
    def connectFile(self,patch,mode:str="stamp"):
        """### mode : `stamp` or `human` \n `stamp` :stamptime mode \n`human` : human time mode"""
        self.patch = patch
        self.mode = mode
        
    def log(self,text,log="INFO"):
        txt = read_txt(self.patch)
        mode = self.mode
        if mode == "human":
            TIME = Get_time_now()
            DATE = date_now()

            Flog = f"[{DATE} {TIME}] {log.upper()} {text}"
        else:
            ts = round(datetime.datetime.now().timestamp())
            Flog = f"[{ts}] {log.upper()} {text}"
        if txt == "":
            write_txt(self.patch,Flog)
        else:
            write_txt(self.patch,txt+"\n"+Flog)



def hash_file(filename):
   h = hashlib.sha1()
   with open(filename,'rb') as file:
       chunk = 0
       while chunk != b'':
           chunk = file.read(1024)
           h.update(chunk)
   return h.hexdigest()
