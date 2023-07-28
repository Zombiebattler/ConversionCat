from moviepy.editor import VideoFileClip
from colorama import Fore, init
from PIL import Image
import time
import os


#─── Variables ───#

folder = ""                         #the folder to be scanned !!! leave blank for manual entry

create_summary = True               #should a summary be made ?

image = True                        #should the image be converted ?
remove_images = False               #should the old image be deleted after the conversion ?
convert_image = "webp"              #which image type should be changed ?
i_to = "png"                        #what type should it be converted to ?


video = True                        #should the video be converted ?
remove_videos = False                #should the old video be deleted after the conversion ?
convert_video = "mp4"               #which video type should be changed ?
v_to = "gif"                        #what type should it be converted to ?

#─────────────────#


def convert_IMAGE(input_dir, output_dir, filename):
    input_path = os.path.join(input_dir, filename)
    output_filename = os.path.splitext(filename)[0] + f'.{i_to}'
    output_path = os.path.join(output_dir, output_filename)
    img = Image.open(input_path)
    img.save(output_path, f'{i_to}')
    print(YELLOW + f"converted " + RED + f"{filename} " + YELLOW + "to " + GREEN + f"{output_filename}")

def convert_VIDEO(input_dir, output_dir, filename):
    input_path = os.path.join(input_dir, filename)
    output_filename = os.path.splitext(filename)[0] + f'.{v_to}'
    output_path = os.path.join(output_dir, output_filename)

    video_clip = VideoFileClip(input_path)
    video_clip.write_gif(output_path)
    video_clip.close()
    print(YELLOW + f"converted " + RED + f"{filename} " + YELLOW + "to " + GREEN + f"{output_filename}")

def get_files(source):
    global files_found, images_converted, videos_converted, videos_deletet, images_deletet
    print(GREEN + f"Scanning ->" + RED + f" {folder}")
    for file in os.listdir(source):
        files_found += 1
        if file.endswith(f".{convert_image}") and image == True:
            print(WHITE + file + GREEN + f" is a .{convert_image} file !")
            convert_IMAGE(folder, folder, file)
            if remove_images:
                os.remove(source + "\\" + file)
                print(YELLOW + f"removed " + RED + f"{file}")
                images_deletet += 1
            images_converted += 1
        elif file.endswith(f'.{convert_video}') and video == True:
            print(WHITE + file + GREEN + f" is a .{convert_video} file \nconverting ... \n!!! This may take a wile !!!")
            convert_VIDEO(folder, folder, file)
            if remove_videos:
                os.remove(source + "\\" + file)
                print(YELLOW + f"removed " + RED + f"{file}")
                videos_deletet += 1
            videos_converted += 1
        else:
            print(WHITE + file + YELLOW + " Skipped")

def summary(length):
    print(f"\n ")
    print(YELLOW + "┌─────────summary")
    print(f"│")
    print(f"├─── files total -> " + GREEN + f"{files_found}" + YELLOW)
    print(f"│")
    print(f"├─── {convert_image} Converted -> " + GREEN + f"{images_converted}" + YELLOW)
    print(f"├─── {convert_image} Deletet -> " + GREEN + f"{images_deletet}" + YELLOW)
    print(f"│")
    print(f"├─── {convert_video} converted -> " + GREEN + f"{videos_converted}" + YELLOW)
    print(f"├─── {convert_video} Deletet -> " + GREEN + f"{videos_deletet}" + YELLOW)
    print(f"│")
    print(f"└─── Time Elapsed -> " + GREEN + f"{length} Seconds" + YELLOW + "\n")

def start():
    print(Fore.LIGHTGREEN_EX + """
   _____                              _              _____      _   
  / ____|                            (_)            / ____|    | |  
 | |     ___  _ ____   _____ _ __ ___ _  ___  _ __ | |     __ _| |_ 
 | |    / _ \| '_ \ \ / / _ \ '__/ __| |/ _ \| '_ \| |    / _` | __|
 | |___| (_) | | | \ V /  __/ |  \__ \ | (_) | | | | |___| (_| | |_ 
  \_____\___/|_| |_|\_/ \___|_|  |___/_|\___/|_| |_|\_____\__,_|\__|
                                                                    
                                                                    
                       Made by Zombiebattler

                                                     """)
    print(f" \n \n")


init()
start()

if folder == "":
    folder = input("folder: ")

RED = Fore.LIGHTRED_EX
GREEN = Fore.LIGHTGREEN_EX
YELLOW = Fore.LIGHTYELLOW_EX
WHITE = Fore.WHITE

files_found = 0
videos_converted = 0
videos_deletet = 0
images_converted = 0
images_deletet = 0

startzeit = time.time()
get_files(folder)
endzeit = time.time()
length = round(endzeit - startzeit, 3)
if create_summary:
    summary(length)

print(" ")
print(GREEN + "ConversionCat v1.1 \nMade by Zombiebattler \nhttps://github.com/Zombiebattler \n")
