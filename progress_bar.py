
import requests
import sys , os , time
from datetime import datetime

class colors:
    # Reset
    reset = "\033[0m"
    
    # Regular colors
    black = "\033[30m"
    red = "\033[31m"
    green = "\033[32m"
    yellow = "\033[33m"
    blue = "\033[34m"
    magenta = "\033[35m"
    cyan = "\033[36m"
    white = "\033[37m"
    
    # Bold colors
    bold_black = "\033[1;30m"
    bold_red = "\033[1;31m"
    bold_green = "\033[1;32m"
    bold_yellow = "\033[1;33m"
    bold_blue = "\033[1;34m"
    bold_magenta = "\033[1;35m"
    bold_cyan = "\033[1;36m"
    bold_white = "\033[1;37m"
    
    # Background colors
    bg_black = "\033[40m"
    bg_red = "\033[41m"
    bg_green = "\033[42m"
    bg_yellow = "\033[43m"
    bg_blue = "\033[44m"
    bg_magenta = "\033[45m"
    bg_cyan = "\033[46m"
    bg_white = "\033[47m"

color = colors()


def hide_cursor():
    sys.stdout.write("\033[?25l")  # ANSI escape code to hide cursor
    sys.stdout.flush()
def show_cursor():
    sys.stdout.write("\033[?25h")  # ANSI escape code to show cursor
    sys.stdout.flush()
def get_file_size(file_path):
    try:
        # Get the size of the file in bytes
        size = os.path.getsize(file_path)
        return size
    except OSError:
        # Handle any potential errors, such as the file not existing
        print("Error: Unable to get file size.")
        return None
def format_time(stamptime):
    timestamp = datetime.fromtimestamp(1710748888.0903776)
    formatted_timestamp = timestamp.strftime("%b %d %H:%M")
    return formatted_timestamp


def format_size(size_bytes,show_unit=True):
    """
    Convert bytes to the appropriate unit (KB, MB, GB, etc.).
    
    Args:
        size_bytes (int): Number of bytes.
    
    Returns:
        str: Formatted size string with the appropriate unit.
    """
    units = ['bytes', 'KB', 'MB', 'GB', 'TB']
    index = 0
    while size_bytes >= 1024 and index < len(units) - 1:
        size_bytes /= 1024.0
        index += 1
    if show_unit:
        return f"{size_bytes:.2f} {units[index]}"
    return f"{size_bytes:.2f}"




# file_size = get_file_size("NEW.png")


def set_defualt():
    global finisht , lst_time , prev_bytes_read , prev_time

    finisht = False
    lst_time = 0
    prev_bytes_read = 0
    prev_time = time.time()




def progressbar(byte, file_size, des,mode='up'):
    global finisht
    global prev_bytes_read
    global prev_time

    if finisht:
        return
    
    end = "\r"
    persent = round((byte / file_size) * 100, 2)
    if mode == 'up':
        if persent > 100:
            persent = 100
            end = "\n"
            finisht = True
    else:
        if persent >= 100:
            persent = 100
            end = "\n"
            finisht = True


    progressbar_color = color.red
    if persent > 25 :
        progressbar_color = color.yellow
    if persent > 65:
        progressbar_color = color.green


    # Calculate download speed
    current_time = time.time()
    time_elapsed = current_time - prev_time
    bytes_diff = byte - prev_bytes_read
    download_speed = bytes_diff / time_elapsed if time_elapsed > 0 else 0  # Avoid division by zero
    
    # Update previous values for the next iteration
    prev_bytes_read = byte
    prev_time = current_time

    # Your callback function
    v_progress_bar = "-" * int(persent/2) + " " * (int(100/2) - int(persent/2))

    display_persent = "{:.2f}".format(persent)
    print(f"\r{des}: {progressbar_color}{display_persent}{color.reset}{color.cyan} %{color.reset} |{progressbar_color}{v_progress_bar}{color.reset}| {color.blue}{format_size(byte, False)}{color.cyan}/{color.magenta}{format_size(file_size)}{color.reset} [{color.cyan}Speed{color.reset}: {format_size(download_speed / 1000)}/s]       ", end=end) 



