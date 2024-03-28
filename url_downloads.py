import requests
import os 
from ZDbyte import Zjson , simpleApi , log
from requests_toolbelt import MultipartEncoder, MultipartEncoderMonitor
from progress_bar import *
import re
import cgi





# url = 'https://dl.discordapp.net/apps/linux/0.0.47/discord-0.0.47.deb'




def Dis_Url(url):
    # Regular expression pattern to match URLs
    url_pattern = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https:// or ftp://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    return re.match(url_pattern, url) is not None


def Ddownload_file(url, save_path, progress_callback=None):
    with requests.get(url, stream=True) as response:
        response.raise_for_status()
        total_size = int(response.headers.get('content-length', 0))
        bytes_so_far = 0
        with open(save_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
                    bytes_so_far += len(chunk)
                    if progress_callback:
                        progress_callback(bytes_so_far, total_size)

def Dget_file_info(url):
    response = requests.head(url, allow_redirects=True)
    content_length = response.headers.get('content-length')
    file_name = None

    # Extract filename from content disposition if available
    content_disposition = response.headers.get('content-disposition')
    if content_disposition:
        _, params = cgi.parse_header(content_disposition)
        file_name = params.get('filename')

    return {
        'file_name': file_name,
        'content_length': content_length
    }


try:
    hide_cursor()
    set_defualt()
    def progress_callback(bytes_so_far, total_size):
        progressbar(bytes_so_far,total_size,'\t',mode='down')
    show_cursor()
except:
    print("ERROR IN SHOW DOWNLOAD PROGRESS")
finally:
    show_cursor


# file_info = get_file_info(url)
# if file_info['file_name']:
#     print("File Name:", file_info['file_name'])
# else:
#     print("File Name: Not available")

# print("Content Length:", file_info['content_length'])

# save_path = os.path.join(os.getcwd(), "deb.deb")
# download_file(url, save_path, progress_callback)
# print("File downloaded to:", save_path)