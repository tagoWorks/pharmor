import random, time, os, pytesseract, platform
import moviepy.editor as mpy
from pytube import YouTube
from PIL import Image
from moviepy.editor import *
from moviepy.video.fx.all import crop
from gtts import gTTS

global randomid
randomid = str(random.randint(1111, 9999))


#                                        $$$$$$\   $$$$$$\  
#                                       $$  __$$\ $$  __$$\ 
#     $$$$$$\$$$$\   $$$$$$\   $$$$$$$\ $$ /  $$ |$$ /  \__|
#     $$  _$$  _$$\  \____$$\ $$  _____|$$ |  $$ |\$$$$$$\  
#     $$ / $$ / $$ | $$$$$$$ |$$ /      $$ |  $$ | \____$$\ 
#     $$ | $$ | $$ |$$  __$$ |$$ |      $$ |  $$ |$$\   $$ |
#     $$ | $$ | $$ |\$$$$$$$ |\$$$$$$$\  $$$$$$  |\$$$$$$  |
#     \__| \__| \__| \_______| \_______| \______/  \______/ 

if platform.system() == 'Darwin':
    clear = lambda: os.system('clear')
    def printcenter(s):
        cols, _ = os.get_terminal_size(0)
        print((s.center(cols)))
    with open(('header.txt'), 'r') as f:
        header = f.read()
    def title():
        clear()
        printcenter(header + "\n\n\n\n")
    def begin():
        global videoinput
        global randomid
        imagefiles = []
        for f in os.listdir('images'):
            if f.lower().endswith(('.png', '.jpg', '.jpeg')):
                imagefiles.append(f)
        if len(imagefiles) == 0:
            title()
            printcenter('Folder is empty or does not contain enough image files!')
            time.sleep(2)
            exit()
        title()
        printcenter('Downloading youtube video: ' + videoinput)
        yt = YouTube(videoinput)
        video_stream = yt.streams.get_highest_resolution()
        video_stream.download((''), filename=randomid + '.mp4')
        lengthlimit = 65
        if yt.length > lengthlimit:
            title()
            printcenter(f'Video is longer than {str(lengthlimit)} seconds! Cutting it...')
            clip = mpy.VideoFileClip(randomid + '.mp4').subclip(0, 65)            
            oldid = randomid
            time.sleep(1)
            randomid = str(random.randint(1111, 9999))
            clip.write_videofile(randomid + '.mp4')
            clip.close()
            os.remove(oldid + '.mp4')
        else:
            clip = mpy.VideoFileClip(randomid + '.mp4')
        time.sleep(1)
        title()
        printcenter('Cropping video for mobile devices...')
        clip = mpy.VideoFileClip(randomid + '.mp4')
        (w, h) = clip.size
        crop_width = h * 9/16
        x1, x2 = (w - crop_width)//2, (w+crop_width)//2
        y1, y2 = 0, h
        cropped_clip = crop(clip, x1=x1, y1=y1, x2=x2, y2=y2)
        oldid = randomid
        time.sleep(1)
        randomid = str(random.randint(1111, 9999))
        cropped_clip.write_videofile(randomid + '.mp4')
        clip.close()
        os.remove(oldid + '.mp4')

        # fix the code

        title()
        printcenter('Done!')
        time.sleep(2)
        exit()
    def downloadfunc():
        global videoinput
        title()
        printcenter('Enter YouTube video URL (rec 1920x1080):')
        videoinput = input("")
        if "https://www.youtube.com/watch?v=" or "https://youtu.be/" in videoinput:
            if not os.path.exists('images'):
                os.mkdir('images')
                title()
                printcenter('Please put your image files in the "images" folder.\nFor more information visit https://github.com/t-a-go/Pharmor')
                time.sleep(2)
            else:
                begin()
        else:
            title()
            printcenter('Invalid URL, please try again')
            time.sleep(2)
            downloadfunc()
    downloadfunc()

#     $$\      $$\ $$\                 $$\                                   
#     $$ | $\  $$ |\__|                $$ |                                  
#     $$ |$$$\ $$ |$$\ $$$$$$$\   $$$$$$$ | $$$$$$\  $$\  $$\  $$\  $$$$$$$\ 
#     $$ $$ $$\$$ |$$ |$$  __$$\ $$  __$$ |$$  __$$\ $$ | $$ | $$ |$$  _____|
#     $$$$  _$$$$ |$$ |$$ |  $$ |$$ /  $$ |$$ /  $$ |$$ | $$ | $$ |\$$$$$$\  
#     $$$  / \$$$ |$$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ | $$ | $$ | \____$$\ 
#     $$  /   \$$ |$$ |$$ |  $$ |\$$$$$$$ |\$$$$$$  |\$$$$$\$$$$  |$$$$$$$  |
#     \__/     \__|\__|\__|  \__| \_______| \______/  \_____\____/ \_______/                                                                       

elif platform.system() == 'Windows':
    import colorama, shutil
    from colorama import Fore, Back
    from PIL import Image, ImageDraw, ImageFont

    colorama.init()
    clear = lambda: os.system('cls')
    def printcenter(s):
        print(s.center(shutil.get_terminal_size().columns))
    with open(('header.txt'), 'r') as f:
        header = f.read()
    def title():
        clear()
        printcenter(Fore.LIGHTYELLOW_EX + header + "\n\n\n\n")
    def begin():
        global videoinput
        global randomid
        global filechosen
        global titlechosen
        global storychosen
        imagefiles = []
        for f in os.listdir('frames'):
            if f.lower().endswith(('.png', '.jpg', '.jpeg')):
                imagefiles.append(f)
        if len(imagefiles) == 0:
            title()
            printcenter(Fore.WHITE + 'Folder is empty or does not contain enough image files!')
            time.sleep(2)
            exit()
        title()
        printcenter(Fore.WHITE + 'Downloading youtube video: ' + videoinput)
        yt = YouTube(videoinput)
        video_stream = yt.streams.get_highest_resolution()
        video_stream.download((''), filename=randomid + '.mp4')
        lengthlimit = 65
        if yt.length > lengthlimit:
            title()
            printcenter(Fore.WHITE + f'Video is longer than {str(lengthlimit)} seconds! Cutting it...')
            clip = mpy.VideoFileClip(randomid + '.mp4').subclip(0, 65)            
            oldid = randomid
            time.sleep(1)
            randomid = str(random.randint(1111, 9999))
            clip.write_videofile(randomid + '.mp4')
            clip.close()
            os.remove(oldid + '.mp4')
        else:
            clip = mpy.VideoFileClip(randomid + '.mp4')
        time.sleep(1)
        title()
        printcenter(Fore.WHITE + 'Cropping video for mobile devices...')
        clip = mpy.VideoFileClip(randomid + '.mp4')
        (w, h) = clip.size
        crop_width = h * 9/16
        x1, x2 = (w - crop_width)//2, (w+crop_width)//2
        y1, y2 = 0, h
        cropped_clip = crop(clip, x1=x1, y1=y1, x2=x2, y2=y2)
        oldid = randomid
        time.sleep(1)
        randomid = str(random.randint(1111, 9999))
        cropped_clip.write_videofile(randomid + '.mp4')
        clip.close()
        os.remove(oldid + '.mp4')
        image = Image.open('frames/' + filechosen)
        draw = ImageDraw.Draw(image)
        font_path = "arial.ttf"
        font_size = 36
        font = ImageFont.load_default()
        text_width, text_height = draw.textsize(titlechosen, font)
        image_width, image_height = image.size
        text_x = (image_width - text_width) // 2
        text_y = (image_height - text_height) // 2
        draw.text((text_x, text_y), titlechosen, font=font, fill="white")
        name, extension = os.path.splitext('frames/' + filechosen)
        saveas = f"{str(random.randint(1111, 9999))}_with_text{extension}" 
        image.save(saveas)
        title()
        printcenter(Fore.WHITE + 'Done!')
        time.sleep(2)
        exit()
    def downloadfunc():
        global videoinput
        title()
        videoinput = input(Fore.WHITE + 'Enter YouTube video URL (rec 1920x1080): ')
        if "https://www.youtube.com/watch?v=" in videoinput: 
                chooseheader()
        else:
            if "test" in videoinput:
                chooseheader()
            else:
                title()
                printcenter(Fore.WHITE + 'Invalid URL, please try again')
                time.sleep(2)
                downloadfunc()
    def chooseheader():
        title()
        global filechosen
        files = os.listdir('frames')
        for i, file in enumerate(files):
            print(Fore.YELLOW + f"[{i+1}] {file}")
        while True:
            choice = input(Fore.WHITE + "\nWhich frame header are you using (Enter the corresponding number): ")
            try:
                choice = int(choice)
                if 1 <= choice <= len(files):
                    filechosen = files[choice - 1]
                    print('You choose the file ' + filechosen)
                    time.sleep(1)
                    inputtitletext()
                else:
                    title()
                    printcenter(Fore.WHITE + "Invalid choice. Please enter a number within the range.")
                    time.sleep(2)
                    chooseheader()
            except ValueError:
                title()
                printcenter(Fore.WHITE + "Invalid input. Please enter a number.")
                time.sleep(2)
                chooseheader()
    def inputtitletext():
        title()
        global titlechosen
        titlechosen = input(Fore.WHITE + "\nWhat is the story title?: ")
        inputstorytext()
    
    def inputstorytext():
        title()
        global storychosen
        storychosen = input(Fore.WHITE + "\nPaste or type the contents of the story:\n")
        begin()

    downloadfunc()