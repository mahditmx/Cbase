import requests
import json
import argparse
import os 
from ZDbyte import Zjson
from tqdm import tqdm
import sys 
from requests_toolbelt import MultipartEncoder, MultipartEncoderMonitor
from progress_bar import *



URL = "http://127.0.0.1:5000/api"







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



def file_info(username , password,file_name,mode= "single"):
    url = URL+"/info"

    data = {"username": username, 'password' : password, "file_name" : file_name , "mode" : mode}
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




def upload(username,password,path): 
    print(f"\nUploading {path}...")
    url = URL+"/upload"

    data = {"username": username, 'password' : password}
    file_path = path

    set_defualt()
    hide_cursor()

    file_size = get_file_size(file_path) 
    if file_size == 0:
        print("file was 0 can't upload")
        show_cursor()

        return
    e = MultipartEncoder(
        fields={'username': 'mahdi', 'password': '123',
                'file': (file_path, open(file_path, 'rb'), 'text/plain')} # in file_path first need replace whit file_name ! *IMPORTANT BUG 
        )
    m = MultipartEncoderMonitor(e, lambda monitor: progressbar(monitor.bytes_read, file_size,f"upload"))

    r = requests.post(url, data=m,
                    headers={'Content-Type': m.content_type})
    print(r.json()["message"])

    # print(r.json())
    show_cursor()


def download(username, password, path):
    url = URL + "/download"
    data = {"username": username, 'password': password, "filename": path}

    print(f"\ngeting {color.magenta}{path}{color.reset} info...")


    info = file_info(username,password,path)
    if info == False:
        q = input(f"Failed to get file info countine to download [Y/n] ? ")
        if q.strip().lower() not in ['y',"Y","yes","yup"]:
            print(f'{color.red}download cancel by user.{color.reset}')
            return
    else:
        if info['data']['exsist'] == False:
            print(f"{color.yellow}404{color.reset} {path}{color.red} not exsist{color.reset}.")
            return
        q = input(f"are you shure to download {path} ({format_size(info['data']['size'])}) [Y/n] ? ")
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


        with open(path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
                    bytes_downloaded += len(chunk)
                    progressbar(bytes_downloaded,total_size,"download",mode="down")

    

        print(f"file save successfully as {path}")

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







def main():
    if not os.path.exists('config'):
        os.mkdir("config")
        with open('config/usr.json' , "w+") as f:
            f.write("{}")

    parser = argparse.ArgumentParser(description='Uploader CLI app')

    parser.add_argument('command', help='upload | download | create account | login')
    parser.add_argument('option', help='option of command', nargs='?', default=None)

    args = parser.parse_args()

    command = args.command
    option = args.option

    json_usr = Zjson()
    json_usr.connectFile('config/usr.json')


    if command == "login":
        usr = input('username : ')
        password = input('password : ')
        r = login(usr,password)
        if r['success'] == True:
            json_usr.append({"username" : usr , "password" : password})


    if command == "signup":
        usr = input('username : ')
        password = input('password : ')
        r = create_account(usr,password)
        if r['success'] == True:
            json_usr.append({"username" : usr , "password" : password})

    if command == "upload":

        usr_data  = json_usr.read()
        if "username" not in usr_data:
            print("please login/signup")
        usr = usr_data['username']
        password = usr_data['password']

        if option == None:
            print("usage:")
            return
        r = upload(usr,password,option)



    if command == "download":

        usr_data  = json_usr.read()
        if "username" not in usr_data:
            print("please login/signup")
        usr = usr_data['username']
        password = usr_data['password']

        if option == None:
            print("usage:")
            return
        r = download(usr,password,option)

    if command in ["info",'ls']:

        usr_data  = json_usr.read()
        if "username" not in usr_data:
            print("please login/signup")
        usr = usr_data['username']
        password = usr_data['password']

        if option == None:
            info = file_info(usr,password,'','all')



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


                    print(f"{color.green}*{color.reset} {white_space_name} {color.yellow}{white_space_time}   {color.cyan}{format_size(i[1])}{color.reset}")
            else:
                print(f"{color.red}ERROR{color.reset} Fail to get files info.")



            return
        
        info = file_info(usr,password,option)
        try:
            if info['success'] == True:
                if info['data']['exsist'] == False:
                    print(f"{color.yellow}*{color.reset} {option}{color.red} not exsist{color.reset}")
                else:
                    print(f"{color.green}*{color.reset} {option} {color.cyan}{format_size(info['data']['size'])}{color.reset}")
            else:
                print(f"{color.red}ERROR{color.reset} Fail to get {option} info.")

        except:
            print(info)










if __name__ == '__main__':
    main()



    show_cursor()


