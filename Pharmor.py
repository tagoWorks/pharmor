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
        numimages = len(imagefiles)
        imagesdone = 0
        for image_file in os.listdir('images'):
            title()
            try:
                printcenter('Extracting text from images...' + ' | ' + str(imagesdone) + ' / ' + str(numimages))
                time.sleep(1)
                if image_file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                    image_path = os.path.join('images', image_file)
                    img = Image.open(image_path)
                    extracted_text = pytesseract.image_to_string(img)
                    title()
                    printcenter('Converting text to audio...' + ' | ' + str(imagesdone) + ' / ' + str(numimages))
                    try:
                        tts = gTTS(text=extracted_text, lang='en')
                        audio_filename = os.path.splitext(image_file)[0] + '.mp3'
                        tts.save('images/' + audio_filename)
                        imagesdone += 1
                    except Exception as e:
                        title()
                        printcenter('Error converting text to audio\n\n')
                        print(e)
                        time.sleep(2)
                        exit()
            except Exception as e:
                title()
                printcenter('Error extracting text from image')
                time.sleep(2)
                exit()
        title()
        printcenter('Overlaying images...')
        image_files = [file for file in os.listdir('images') if file.lower().endswith(('.jpg', '.jpeg', '.png'))]
        mp3_files = [file for file in os.listdir('images') if file.lower().endswith('.mp3')]
        time_position = 0
        master_video = VideoFileClip(randomid + '.mp4')
        for image_file, audio_file in zip(image_files, mp3_files):
            image = ImageClip(os.path.join('images', image_file))
            audio = AudioFileClip(os.path.join('images', audio_file))
            audio_duration = audio.duration
            image_with_audio = image.set_duration(audio_duration).set_audio(audio)
            video_width, video_height = master_video.size
            image_width, image_height = image_with_audio.size
            scale_factor = min(video_width / image_width, video_height / image_height)
            image_with_audio = image_with_audio.resize(width=image_width * scale_factor, height=image_height * scale_factor)
            x_center = (video_width - image_with_audio.w) / 2
            y_center = (video_height - image_with_audio.h) / 2
            image_with_audio = image_with_audio.set_position((x_center, y_center))
            master_video = CompositeVideoClip([master_video, image_with_audio.set_start(time_position)])
            time_position += audio_duration
        master_video.write_videofile(randomid + '-FINAL.mp4', codec='libx264', audio_codec='aac')
        oldid = randomid
        randomid = str(random.randint(1111, 9999))
        clip.close()
        os.remove(oldid + '.mp4')
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
    colorama.init()
    clear = lambda: os.system('cls')
    def printcenter(s):
        print(s.center(shutil.get_terminal_size().columns))
    with open(('header.txt'), 'r') as f:
        header = f.read()
    def begin():
        global videoinput
        global randomid
        imagefiles = []
        for f in os.listdir('images'):
            if f.lower().endswith(('.png', '.jpg', '.jpeg')):
                imagefiles.append(f)
        if len(imagefiles) == 0:
            clear()
            printcenter(Fore.LIGHTYELLOW_EX + header + "\n\n\n\n")
            printcenter(Fore.WHITE + 'Folder is empty or does not contain enough image files!')
            time.sleep(2)
            exit()
        clear()
        printcenter(Fore.LIGHTYELLOW_EX + header + "\n\n\n\n")
        printcenter(Fore.WHITE + 'Downloading youtube video: ' + videoinput)
        yt = YouTube(videoinput)
        video_stream = yt.streams.get_highest_resolution()
        video_stream.download((''), filename=randomid + '.mp4')
        lengthlimit = 65
        if yt.length > lengthlimit:
            clear()
            printcenter(Fore.LIGHTYELLOW_EX + header + "\n\n\n\n")
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
        clear()
        printcenter(Fore.LIGHTYELLOW_EX + header + "\n\n\n\n")
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
        numimages = len(imagefiles)
        imagesdone = 0
        for image_file in os.listdir('images'):
            clear()
            printcenter(Fore.LIGHTYELLOW_EX + header + "\n\n\n\n")
            try:
                printcenter(Fore.WHITE + 'Extracting text from images...' + ' | ' + str(imagesdone) + ' / ' + str(numimages))
                time.sleep(1)
                if image_file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                    image_path = os.path.join('images', image_file)
                    img = Image.open(image_path)
                    extracted_text = pytesseract.image_to_string(img)
                    clear()
                    printcenter(Fore.LIGHTYELLOW_EX + header + "\n\n\n\n")
                    printcenter(Fore.WHITE + 'Converting text to audio...' + ' | ' + str(imagesdone) + ' / ' + str(numimages))
                    try:
                        tts = gTTS(text=extracted_text, lang='en')
                        audio_filename = os.path.splitext(image_file)[0] + '.mp3'
                        tts.save('images/' + audio_filename)
                        imagesdone += 1
                    except Exception as e:
                        clear()
                        printcenter(Fore.LIGHTYELLOW_EX + header + "\n\n\n\n")
                        printcenter(Fore.WHITE + 'Error converting text to audio')
                        print(Back.RED + '    ' * 30 + Back.RESET + '\n')
                        print(e)
                        time.sleep(2)
                        exit()
            except Exception as e:
                clear()
                printcenter(Fore.LIGHTYELLOW_EX + header + "\n\n\n\n")
                printcenter(Fore.WHITE + 'Error extracting text from image')
                time.sleep(2)
                exit()
        clear()
        printcenter(Fore.LIGHTYELLOW_EX + header + "\n\n\n\n")
        printcenter(Fore.WHITE + 'Overlaying images...')
        image_files = [file for file in os.listdir('images') if file.lower().endswith(('.jpg', '.jpeg', '.png'))]
        mp3_files = [file for file in os.listdir('images') if file.lower().endswith('.mp3')]
        time_position = 0
        master_video = VideoFileClip(randomid + '.mp4')
        for image_file, audio_file in zip(image_files, mp3_files):
            image = ImageClip(os.path.join('images', image_file))
            audio = AudioFileClip(os.path.join('images', audio_file))
            audio_duration = audio.duration
            image_with_audio = image.set_duration(audio_duration).set_audio(audio)
            video_width, video_height = master_video.size
            image_width, image_height = image_with_audio.size
            scale_factor = min(video_width / image_width, video_height / image_height)
            image_with_audio = image_with_audio.resize(width=image_width * scale_factor, height=image_height * scale_factor)
            x_center = (video_width - image_with_audio.w) / 2
            y_center = (video_height - image_with_audio.h) / 2
            image_with_audio = image_with_audio.set_position((x_center, y_center))
            master_video = CompositeVideoClip([master_video, image_with_audio.set_start(time_position)])
            time_position += audio_duration
        master_video.write_videofile(randomid + '-FINAL.mp4', codec='libx264', audio_codec='aac')
        oldid = randomid
        randomid = str(random.randint(1111, 9999))
        clip.close()
        os.remove(oldid + '.mp4')
        clear()
        printcenter(Fore.LIGHTYELLOW_EX + header + "\n\n\n\n")
        printcenter(Fore.WHITE + 'Done!')
        time.sleep(2)
        exit()
    def downloadfunc():
        global videoinput
        clear()
        printcenter(Fore.LIGHTYELLOW_EX + header + "\n\n\n\n")
        printcenter(Fore.WHITE + 'Enter YouTube video URL (rec 1920x1080):')
        videoinput = input("")
        if "https://www.youtube.com/watch?v=" in videoinput: 
            if not os.path.exists('images'):
                os.mkdir('images')
                clear()
                printcenter(Fore.LIGHTYELLOW_EX + header + "\n\n\n\n")
                printcenter(Fore.WHITE + 'Please put your image files in the "images" folder.\nFor more information visit https://github.com/t-a-go/Pharmor')
                time.sleep(2)
            else:
                begin()
        else:
            clear()
            printcenter(Fore.LIGHTYELLOW_EX + header + "\n\n\n\n")
            printcenter(Fore.WHITE + 'Invalid URL, please try again')
            time.sleep(2)
            downloadfunc()
    downloadfunc()