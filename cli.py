#!/usr/bin/python3


import requests
import argparse
import os 
from ZDbyte import Zjson , simpleApi , log
from requests_toolbelt import MultipartEncoder, MultipartEncoderMonitor
from progress_bar import *
import hashlib
import magic
import tempfile
import zipfile
from url_downloads import *
import signal

# URL = "http://127.0.0.1:5000/api"
URL = "https://cliserver.pythonanywhere.com/api"





BUILD = 25
VERSION = "0.0.4"
import requests


def create_account(username , password):
    url = URL+"/crAcc"

    data = {"username": username, 'password' : password}
    headers = {'Content-Type': 'application/json'}

    r = requests.post(url , json=data, headers=headers)
    print(r)
    try:
        print(r.text)
    except:
        print(r.status_code+" ERROR CREATE ACCOUNT")
    return r.json()


def login(username , password):
    url = URL+"/login"

    data = {"username": username, 'password' : password}
    headers = {'Content-Type': 'application/json'}

    r = requests.post(url , json=data, headers=headers)
    print(r)
    try:
        print(r.text)
    except:
        print(r.status_code+" ERROR CREATE ACCOUNT")
    return r.json()



def file_info(username , token,file_name,mode= "single",opt=[]):
    url = URL+"/info"

    data = {"username": username, 'token' : token, "file_name" : file_name , "mode" : mode}
    headers = {'Content-Type': 'application/json'}

    r = requests.post(url , json=data, headers=headers)


    try:
        r = r.json()

        if r['success'] == True:
            return r
        else:
            print(r)
            return False
    except:
        return False




def get_file_hash(file_path):
    # Initialize the hash object
    file_hash = hashlib.sha256()

    # Open the file in binary mode and calculate the hash
    with open(file_path, "rb") as f:
        while True:
            # Read the file in chunks
            chunk = f.read(4096)
            if not chunk:
                break
            # Update the hash object with each chunk of data
            file_hash.update(chunk)

    # Retrieve the hexadecimal digest of the hash
    file_hash_hexdigest = file_hash.hexdigest()
    
    return file_hash_hexdigest

def check_file_extension(file_path):
    allowed_extensions = {'zip', 'rar', 'gz'}
    _, extension = os.path.splitext(file_path)
    extension = extension.lower()[1:]  # Remove the leading dot
    if extension in allowed_extensions:
        return True
    return False

def check_media_file_content(file_path):
    allowed_media_types = {'video/', 'audio/', 'image/'}
    with open(file_path, 'rb') as file:
        file_type = magic.Magic(mime=True).from_buffer(file.read(1024))
        if any(file_type.startswith(media_type) for media_type in allowed_media_types):
            return True
    return False
def zip_file(file_path, output_path):
    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(file_path, arcname=os.path.basename(file_path))



def upload(username,token,path): 
    print(f"Uploading {path}...")
    url = URL+"/upload"

    file_path = path

    if os.path.exists(file_path) == False:
        print(f"{file_path} not {color.red}exists{color.reset} to upload")
        return

    tmp = False
    filename = os.path.basename(file_path)
    file_name = os.path.basename(file_path)
    org_hash = get_file_hash(file_path)


    if not check_file_extension(file_path):
        if not check_media_file_content(file_path):
            tmp = True
            print(f"Ziping {file_path}...")
            temp_dir = tempfile.mkdtemp()
            
            dot_index = file_name.rfind('.')
            if dot_index != -1:
                output =  file_name[:dot_index] + '.zip'
            else:
                output = file_name + '.zip'

            out_path = os.path.join(temp_dir,output)
            zip_file(file_path,out_path)
            if os.path.exists(out_path):
                file_path = out_path
                file_name = output
            else:
                print(f"{color.red}fail to zip file{color.reset}")





    set_defualt()
    hide_cursor()


    local_file_hash = get_file_hash(file_path)
    file_size = get_file_size(file_path) 
    if file_size == 0:
        print("file was 0 can't upload")
        show_cursor()

        return
    e = MultipartEncoder(
        fields={'username': username, 'token': token, 'zip' : str(tmp) , "filename" : filename, "org-hash" : org_hash,
                'file': (file_name, open(file_path, 'rb'), 'text/plain')} 
        )
    m = MultipartEncoderMonitor(e, lambda monitor: progressbar(monitor.bytes_read, file_size,f"\t"))

    r = requests.post(url, data=m,
                    headers={'Content-Type': m.content_type})
    
    try:
        r = r.json()
    except:
        print(f"{color.red}{r.status_code} ERROR{color.reset}")

    if r['success'] == True:
        print("file uploaded.")
        print(f"{color.yellow}Verifying the file hash match{color.reset}")
        file_hash = r['data']['hash']

        hash_print_info = ""
        if tmp:
            hash_print_info = f"{color.yellow}Ziped hash{color.reset}"
        print(f"server file hash : {color.blue} {file_hash}{color.reset} {hash_print_info}")
        print(f"local file hash  : {color.cyan} {local_file_hash}{color.reset} {hash_print_info}")

        if local_file_hash == file_hash:
            print(f'\tFile hash match successfully {color.green}verified{color.reset}.')
        else:
            print(f"\t{color.red}WARNING{color.reset} File hash verification {color.red}failed{color.reset}.")
    else:
        print(r['message'])

    if tmp:
        os.remove(file_path)


    # print(r.json())
    show_cursor()


def download(username, token, path):
    url = URL + "/download"
    data = {"username": username, 'token': token, "filename": path}

    print(f"geting {color.magenta}{path}{color.reset} info...")

    file_hash = None
    info = file_info(username,token,path)
    if info == False:
        q = input(f"Failed to get file info countine to download [Y/n] ? ")
        if q.strip().lower() not in ['y',"Y","yes","yup"]:
            print(f'{color.red}download cancel by user.{color.reset}')
            return
    else:
        if info['data']['exsist'] == False:
            print(f"[{color.red}404{color.reset}] {color.magenta}{path}{color.reset} not exsist on your cloud.")
            return
        ziped = info['data']['ziped']
        ziped_info = ""
        if ziped :
            ziped_info = f"[{color.yellow}ZIP{color.reset}] File ziped on the server"
        print(ziped_info)
        file_hash = info['data']['hash']
        print(f"{color.cyan}{path}{color.reset} hash : {file_hash}")
        if info['data']['exsist'] == False:
            print(f"{color.yellow}404{color.reset} {path}{color.red} not exsist{color.reset}.")
            return
        q = input(f"are you shure to download {color.cyan}{path} {color.magenta}({format_size(info['data']['size'])}){color.reset} ? [Y/n] ")
        if q.strip().lower() not in ['y',"Y","yes","yup"]:
            print(f'{color.red}download cancel by user.{color.reset}')
            return


    print(f"downloading {color.magenta}{path}{color.reset}...")


    response = requests.get(url,data=data ,stream=True)
    set_defualt()
    hide_cursor()
    if response.status_code == 200:
        total_size = int(response.headers.get('content-length', 0))
        bytes_downloaded = 0
        if ziped:
            temp_dir = tempfile.mkdtemp()
            org_path = path
            path = os.path.join(temp_dir, path)

        with open(path, 'wb') as f: # TODO check if tmp = true (ziped by our) unzip and next get hash and save First in temp file next unzip and save in regular path
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
                    bytes_downloaded += len(chunk)
                    progressbar(bytes_downloaded,total_size,"\t",mode="down")

        if ziped:
            print(f"[{color.cyan}INFO{color.reset}] extracting zip...")
            with zipfile.ZipFile(path, 'r') as zip_ref:
                zip_ref.extractall('.')
            path = org_path


        print(f"[{color.cyan}INFO{color.reset}] file save  as {path}")
        print(f"[{color.cyan}INFO{color.reset}]{color.yellow} Verifying the file hash match{color.reset}")
        save_file_hash = get_file_hash(path)
        if file_hash == None:
            print(f"[{color.yellow}WARNING{color.reset}] Fail to get hash file from server")
            return

        print(f"server file hash : {color.blue} {file_hash}{color.reset}")
        print(f"local file hash  : {color.cyan} {save_file_hash}{color.reset}")

        if save_file_hash == file_hash:
            print(f'\tFile hash match successfully {color.green}verified{color.reset}.')
        else:
            print(f"\t{color.red}WARNING{color.reset} File hash verification {color.red}failed{color.reset}.")






    else:
        print(color.yellow + "Failed to download the file" + color.reset)
        try:
            try:
                print(color.red+response.json()['message']+color.reset)
            except:
                print(response.json())
        except:
            print(response)
    show_cursor()





def get_(path,save_as='.'):
    url = URL + "/get"
    data = {"filename": path,"pwd":False}

    print(f"geting {color.magenta}{path}{color.reset} info...")

    file_hash = None
    info = file_info("","",path,mode='get')

    if info == False:
        q = input(f"Failed to get file info countine to download [Y/n] ? ")
        if q.strip().lower() not in ['y',"Y","yes","yup"]:
            print(f'{color.red}download cancel by user.{color.reset}')
            return
    else:
        if info != True:
            if info['data']['exsist'] == False:
                print(f"[{color.red}404{color.reset}] {color.magenta}{path}{color.reset} not exsist on the server.")
                return
            ziped = info['data']['ziped']
            ziped_info = ""
            if ziped :
                ziped_info = f"[{color.yellow}ZIP{color.reset}] File ziped on the server"
            if info['data']['exsist'] == False:
                print(f"{color.yellow}404{color.reset} {path}{color.red} not exsist{color.reset}.")
                return
            print(ziped_info)
            
            file_hash = info['data']['hash']
            print(f"{color.cyan}{info['data']['info'][0]}{color.reset} hash : {file_hash}")
            q = input(f"\tare you shure to download {color.cyan}{info['data']['info'][0]} {color.magenta}({format_size(info['data']['info'][1])}){color.reset} published by {color.bold_yellow}{info['data']['info'][3]}{color.reset} [Y/n] ? ")
            if q.strip().lower() not in ['y',"Y","yes","yup"]:
                print(f'{color.red}download cancel by user.{color.reset}')
                return
            path = info['data']['info'][0]
        else:
            q = input(f"Failed to get file info countine to download [Y/n] ? ")
            if q.strip().lower() not in ['y',"Y","yes","yup"]:
                print(f'{color.red}download cancel by user.{color.reset}')
                return

    lock = info['data']['lock']

    if lock == True:
        print("this file protected by password")
        pwd = input("file password: ")
        data['pwd'] = pwd
    print(f"downloading {color.magenta}{path}{color.reset}...")

    response = requests.get(url,data=data ,stream=True)
    set_defualt()
    hide_cursor()

    if response.status_code == 403:
        print("password is uncorrect.")
        return

    if response.status_code == 200:
        total_size = int(response.headers.get('content-length', 0))
        bytes_downloaded = 0



        if ziped:
            temp_dir = tempfile.mkdtemp()
            org_path = path
            path = os.path.join(temp_dir, path)


        with open(path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
                    bytes_downloaded += len(chunk)
                    progressbar(bytes_downloaded,total_size,"\t",mode="down")

        if ziped:
            print(f"[{color.cyan}INFO{color.reset}] extracting zip...")
            with zipfile.ZipFile(path, 'r') as zip_ref:
                zip_ref.extractall(save_as)
            path = org_path


            

        print(f"[{color.cyan}INFO{color.reset}] file save as {path}")
        print(f"[{color.cyan}INFO{color.reset}] {color.yellow}Verifying the file hash match{color.reset}")
        save_file_hash = get_file_hash(path)
        if file_hash == None:
            print(f"{color.yellow}WARNING{color.reset} Fail to get hash file from server")
            return
        
        print(f"server file hash : {color.blue} {file_hash}{color.reset}")
        print(f"local file hash  : {color.cyan} {file_hash}{color.reset}")

        if save_file_hash == file_hash:
            print(f'\t[{color.cyan}INFO{color.reset}] File hash match successfully {color.green}verified{color.reset}.')
        else:
            print(f"\t[{color.red}WARNING{color.reset}] File hash verification {color.red}failed{color.reset}.")






    else:
        print(color.yellow + "Failed to download the file" + color.reset)
        try:
            try:
                print(color.red+response.json()['message']+color.reset)
            except:
                print(response.json())
        except:
            print(response)
    show_cursor()




def index(username , token,path,f_name,force,pwd):
    url = URL+"/pub"

    data = {"username": username, 'token' : token , "file_name" : path , "f_name" : f_name , "force" : force,"pwd":pwd}
    headers = {'Content-Type': 'application/json'}

    r = requests.post(url , json=data, headers=headers)
    try:
        r.json()
    except:
        print(r.status_code+" ERROR CREATE ACCOUNT")
    return r.json()



def rm_file(username , token,path):
    url = URL+"/rm_file"

    data = {"username": username, 'token' : token , "file_name" : path }
    headers = {'Content-Type': 'application/json'}

    r = requests.post(url , json=data, headers=headers)
    try:
        r.json()
    except:
        print(r.status_code+" ERROR RM FILE")
    return r.json()






def check_for_update(startup = False):
    api = simpleApi()
    api.login('qQYN9t4uinbbVrMozztDr2NMOMDCaUPpbRnbflIbHvODeEsoPq2NOVeTt3n9UWl4','mahdi')
    data = api.read_file('sync/info.json')
    data = eval(data[1])
    update_des = data['info']
    get_id = data['get']
    if data['build'] > BUILD:
        print(f"{color.bold_cyan}A new update avalivable{color.reset}")
        print(f"{color.yellow}update description{color.reset} : {update_des}")
        print(f"get new update by running : {color.magenta}cbase get {get_id}{color.reset} and {color.cyan}install{color.reset} the downloaded file")
        print(f"or download manual from {color.red}http://cliserver.pythonanywhere.com/downloads{color.reset}")
        return data['important']

    else:
        if startup == False:
            print("already up to date.")
        else:
            print()



def auto_check_update(mode='normal'):
    

    home_directory = os.path.expanduser("~")

    config_directory = os.path.join(home_directory, '.config', 'cbase')
    json_file_path = os.path.join(config_directory, 'usr.json')
    if not os.path.exists(config_directory):
        os.mkdir(config_directory)
        with open(json_file_path , "w+") as f:
            f.write("{}")



    json_usr = Zjson()
    json_usr.connectFile(json_file_path)


    conf_usr_data = json_usr.read()
    if "lst_run" not in conf_usr_data:
        conf_usr_data['lst_run'] = time.time()
    
        json_usr.append(conf_usr_data)

        return
    
    lst_run = conf_usr_data['lst_run'] 
    if time.time() - lst_run > 7200:
        if mode == 'thetime':
            return True
        
        print(f'[{color.green}UPDATE{color.reset}] checking for update...')
        conf_usr_data['lst_run'] = time.time()
        json_usr.append(conf_usr_data)

        important = check_for_update()
        return important
    elif mode == 'thetime':
        return False
    
    
def is_admin():

    if os.geteuid() == 0:
        return True
    elif os.name == 'nt':
        import ctypes
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except AttributeError:
            return False
    else:
        return False


def install_cbase():
    if not is_admin():
        print(f"Are you root ? try use {color.green}sudo{color.reset}") 
        exit()
    get_('cbase_linux_exe',save_as='/usr/bin/')


def download_command(option , json_usr):
    usr_data  = json_usr.read()
    if "username" not in usr_data:
        print("please login/signup")
    usr = usr_data['username']
    token = usr_data['token']

    if option == None:
        print("usage:")
        return
    
    if not Dis_Url(option):
        r = download(usr,token,option)
        return


    print(f"geting {color.magenta}Url file{color.reset} info...")

    info_file = Dget_file_info(option)
    if info_file['content_length'] == None:
        q = input(f"[{color.yellow}INFO{color.reset}] Fail to get file size, countine download ? [Y/n] ")
        if q.strip().lower() not in ['y',"Y","yes","yup"]:
            print(f'{color.red}remove cancel by user.{color.reset}')
            return
        size = "None"
    else:
        size = format_size(int(info_file['content_length']))


    if info_file['file_name'] == None:
        print(f"[{color.yellow}INFO{color.reset}] Fail to get file name")
        name = input(f'Save file as: ')
    else:
        name = info_file['file_name']


    q = input(f"are you shure to download {color.cyan}{name}{color.reset} ({size}) ? [Y/n] ")
    if q.strip().lower() not in ['y',"Y","yes","yup"]:
        print(f'{color.red}remove cancel by user.{color.reset}')
        return

    print(f"[{color.cyan}INFO{color.reset}] Downloading {color.magenta}{name}{color.reset}...")
    Ddownload_file(option,name,progress_callback)







def main():

    home_directory = os.path.expanduser("~")

    config_directory = os.path.join(home_directory, '.config', 'cbase')
    json_file_path = os.path.join(config_directory, 'usr.json')

    parser = argparse.ArgumentParser(description='Uploader CLI app')

    parser.add_argument('command', help='upload | download | signup | login',nargs='?')
    parser.add_argument('option', help='option of command [path]', nargs='?', default=None)
    parser.add_argument('-f', action='store_true', help='Force command')
    parser.add_argument('-i', action='store_true', help='show more info')
    parser.add_argument('-v', action='store_true', help='show version and build')
    parser.add_argument('--get', action='store_true', help='Description of the --get flag')

    

    args = parser.parse_args()

    command = args.command
    option = args.option

    json_usr = Zjson()
    json_usr.connectFile(json_file_path)

    if command == None and not args.v:
        parser.print_help()
        return


    if command == "login":
        usr = input('username : ')
        password = input('password : ')
        r = login(usr,password)
        if r['success'] == True:
            json_usr.append({"username" : usr , "token" : r['data']['token']})
        return

    if command == "signup":
        usr = input('username : ')
        password = input('password : ')
        r = create_account(usr,password)
        if r['success'] == True:
            json_usr.append({"username" : usr , "token" : r['data']['token']})
        return

    if command == "upload":

        usr_data  = json_usr.read()
        if "username" not in usr_data:
            print("please login/signup")
            return
        usr = usr_data['username']
        token = usr_data['token']

        if option == None:
            print("usage:")
            return

        if args.f == False:

            if os.path.exists(option) == False:
                print(f"{option} not {color.red}exists{color.reset} to upload")
                return


            file_hash = get_file_hash(option)
            x = file_info(usr,token,file_hash,mode='hash')
            if x['success'] == False:
                q = input(f"{color.red}Fail{color.reset} to get file exsist info from server [Y/n] ? ")
                if q.strip().lower() not in ['y',"Y","yes","yup"]:
                    print(f'{color.red}upload cancel by user.{color.reset}')
                    return

                # return
            if len(x['data']['ls']) != 0:
                q = input(f"{color.red}{len(x['data']['ls'])}{color.reset} same file {color.yellow}exsist{color.reset} on your space in the server are you want to upload one more ? [Y/n] ")
                if q.strip().lower() not in ['y',"Y","yes","yup"]:
                    print(f'{color.red}upload cancel by user.{color.reset}')
                    return




        r = file_info(usr,token,option)

        if r['success'] == True:
            if r['data']['exsist'] == True:
                if args.f == False:
                    print(f"this file-name allready exsist. use {color.cyan}-f{color.reset} to replace")
                    print(f"{color.red}Upload cancel becuse file-name exsist on the server{color.reset}")
                    print(f'\t{color.yellow}INFO{color.reset}')
                    print(f'\tThis error can be happend becuse')
                    print(f"\t{color.cyan}None-media{color.reset} files will send when {color.yellow}ziped{color.reset} and save on server as a zip file \n\tthats mean same {color.magenta}file-name{color.reset} whit diffrent extension cant be save on server whitout replace\n\tPlease change file-name to {color.green}save{color.reset} it on server whitout replace whit old-one.")
                    return
                
        else:
            print("Failed to get info from server")
            print("uploading cancel")
            return	

        r = upload(usr,token,option)
        return


    if command == "download":
        if args.get:
            get_(option)
            return
        download_command(option, json_usr)
        return




    if command in ["info",'ls']:

        usr_data  = json_usr.read()
        if "username" not in usr_data:
            print("please login/signup")
            return
        usr = usr_data['username']
        token = usr_data['token']


        if option == None:
            if args.get: # --get was mean | INFO : get all public indexed things in cbase server  
                print(f"List of all {color.bold_magenta}public{color.reset} indexed file")
                info = file_info(usr,token,'','get_ls')
                

                largest_get_name = 5
                largest_get_file_name = 5
                largest_get_file_size = 5

                for i in info['data']:
                    if info['data'][i] == 404:
                        continue
                    leght = len(i)
                    leght_filename = len(info['data'][i]['info'][3])
                    leght_size = len(format_size(info['data'][i]['info'][1]))


                    if leght > largest_get_name:
                        largest_get_name = leght
                    if leght_filename > largest_get_file_name:
                        largest_get_file_name = leght_filename

                    if leght_size > largest_get_file_size:
                        largest_get_file_size = leght_size


                for i in info['data']:
                    if info['data'][i] == 404:
                        # print("404") # TODO : Name {color.red}info not found{color.red}
                        continue
                    

                    # print(info['data'][i])
                    hash_info = ""
                    if args.i:
                        hash_info = info['data'][i]['hash']

                    req_get_name_space = ' ' * (largest_get_name - len(i) + 3) 
                    req_get_file_name_space = ' ' * (largest_get_file_name - len(info['data'][i]['info'][3]) + 3)
                    req_get_file_size_space = ' ' * (largest_get_file_size - len(format_size(info['data'][i]['info'][1])) + 3)

                    Line = f"""{color.green}#{color.reset} {i}{req_get_name_space}{color.bold_yellow}{info['data'][i]['info'][3]}{color.reset}{req_get_file_name_space}{color.magenta}{format_size(info['data'][i]['info'][1])}{req_get_file_size_space}{color.cyan}{format_time(info['data'][i]['info'][2])}{color.reset}  {color.yellow}{hash_info}{color.reset}                           """

                    print(Line)




                return










            else:
                info = file_info(usr,token,'','all')
                if info['success'] == True:
                    files_list = info['data']['ls']

                    biggest_len_name = 0
                    biggest_len_time = 0

                    for i in files_list:
                        if len(i[0]) > biggest_len_name:
                            biggest_len_name = len(i[0])

                    

                    for i in files_list:
                        file_name_space = biggest_len_name+5 - len(i[0])
                        white_space_name = i[0] + (" "*file_name_space)
                        
                        dt_utc = datetime.fromtimestamp(i[2])
                        formatted_dt = dt_utc.strftime('%b %d %H:%M')

                        white_space_time = ((formatted_dt))

                        start_color = color.green
                        hash_color = color.yellow

                        if i[1] == 0:
                            start_color = color.yellow
                        if i[4] != None:
                            start_color = color.magenta
                            hash_color = color.magenta




                        file_hash = ""
                        if args.i:
                            file_hash = i[3] + "   "

                        print(f"{start_color}*{color.reset} {white_space_name} {color.yellow}{white_space_time}  {hash_color}{file_hash}{color.reset}{color.cyan}{format_size(i[1])}{color.reset} ")
                else:
                    print(f"{color.red}ERROR{color.reset} Fail to get files info.")
                return



        info = file_info(usr,token,option)
        file_hash = info['data']['hash']
        if args.i == False:
            file_hash = ""
        try:
            if info['success'] == True:
                if info['data']['exsist'] == False:
                    print(f"{color.yellow}*{color.reset} {option}{color.red} not exsist{color.reset}")
                else:
                    print(f"{color.green}*{color.reset} {option} {color.cyan}{format_size(info['data']['size'])}{color.reset} {color.yellow}{file_hash}{color.reset}")
            else:
                print(f"{color.red}ERROR{color.reset} Fail to get {option} info.")

        except:
            print(info)

    if command == "get" :
        if option == None:
            print("usage:")
            return 
        get_(option)
        return


    if command in ['publish','index','public'] :
        if option == None:
            print("usage:")
            return 
        
        usr_data  = json_usr.read()
        if "username" not in usr_data:
            print("please login/signup")
            return
        usr = usr_data['username']
        token = usr_data['token']


        f_name = input("friendly name : ")
        f_pwd = input("password (option) - leave blank for public : ")
        if f_pwd.rstrip() == "":
            f_pwd  = False
        force = False
        if args.f :
            force = True
        print(f_pwd)
        r = index(usr,token,option,f_name,force,f_pwd)
        print(f"{color.yellow}server replay {color.reset}: {r['message']}")
        if r['success'] == False:
            if r['data']['per'] :
                print(f"{color.cyan}HINT{color.reset}: use {color.magenta}-f{color.reset} to replace")
                return
            else:
                print(f"{color.red}WARNING{color.reset}: you dont have permission to replace")
                return
        return
    
    if command in ["update" , 'check-for-update']:
        i = auto_check_update(mode='thetime')
        if not i :
            check_for_update() 
        return

    if command in ['exsist']:

        if option == None:
            print("usage:")
            return 
        
        usr_data  = json_usr.read()
        if "username" not in usr_data:
            print("please login/signup")
            return
        usr = usr_data['username']
        token = usr_data['token']

        if os.path.exists(option) == False: 
            print(f"{color.red}{option}{color.reset} was not exsist.")

        option = get_file_hash(option)


        info = file_info(usr,token,option,mode='hash')
        if info['success'] == True:
            files_list = info['data']['ls']

            biggest_len_name = 0
            for i in files_list:
                if len(i[0]) > biggest_len_name:
                    biggest_len_name = len(i[0])

            
            first = True
            for i in files_list:
                file_name_space = biggest_len_name+5 - len(i[0])
                white_space_name = i[0] + (" "*file_name_space)
                
                dt_utc = datetime.fromtimestamp(i[2])
                formatted_dt = dt_utc.strftime('%b %d %H:%M')

                white_space_time = ((formatted_dt))

                start_color = color.green
                if i[1] == 0:
                    start_color = color.yellow
                file_hash = ""
                if args.i:
                    file_hash = i[3] + "   "

                if first:
                    size = format_size(i[1])
                    first = False
                else:
                    size = "**"

                print(f"{start_color}*{color.reset} {white_space_name} {color.yellow}{white_space_time}  {color.yellow}{file_hash}{color.reset}{color.cyan}{size}{color.reset} ")
        else:
            print(f"{color.red}ERROR{color.reset} Fail to get files info.")

    if command in ['logout']:
        data = json_usr.read()
        data['token'] = None
        data['username'] = None

        json_usr.append(data)
        print(f"you logout {color.red}only{color.reset} from this device \nuse {color.magenta}logout-all{color.reset} (when logined) for logout from all device")

    if command in ['rm']:

        if option == None:
            print("usage:")
            return 
        
        usr_data  = json_usr.read()
        if "username" not in usr_data:
            print("please login/signup")
            return
        usr = usr_data['username']
        token = usr_data['token']

        if not args.f: 
            q = input(f"are you shure to delete {color.cyan}{option}{color.reset} ? [Y/n] ")
            if q.strip().lower() not in ['y',"Y","yes","yup"]:
                print(f'{color.red}remove cancel by user.{color.reset}')
                return

        r = rm_file(usr,token,option)
        if 'success' in r:
            print(r['message'])
        else:
            print(r)
        return

            
    if command in ['cat']:
        download_command(option,json_usr)
        return



    if args.v:
        print(f"Cbase {VERSION}:{BUILD}")
        return


    print(f"{command} was not found. Use {color.cyan}-h{color.reset} or run \n{color.green}${color.reset} {color.reset}cbase{color.reset} get help\nto get help")






def signal_handler(sig, frame):
    # Define the signal handler function
    print("\nCtrl+C detected. Are you sure you want to exit? (y/n)")
    response = input().strip().lower()
    if response == 'y':
        print("Exiting...")
        exit(0)
    else:
        print("Resuming...")

# Set the signal handler for SIGINT (Ctrl+C)
signal.signal(signal.SIGINT, signal_handler)


if __name__ == '__main__':
    important = auto_check_update()
    if important : 
        exit()
    

    try:
        main()

    except KeyboardInterrupt:
        print('\nCtrl+C detected. Are you shure want to exit? [y/n]')
        q = input().strip().lower()
        if q in ['y','yes','yup']:
            print('Exiting...')
            exit(0)
        else:
            print('Resuming...')

    show_cursor()
    # install_cbase()

