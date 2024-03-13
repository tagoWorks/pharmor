<br />
<div align="center">
  <a href="https://github.com/t-a-g-o/pharmor">
    <img src="logo.png" alt="Logo" width="245" height="245">
  </a>
<h3 align="center">Pharmor</h3>
  <p align="center">
    An easy to use short video creator to farm TikTok stories.
    <br />
    <br />
    <a href="https://github.com/t-a-g-o/pharmor/releases">Download</a>
    -
    <a href="https://tago.works">tagoWorks Site</a>
    -
    <a href="https://tago.works/discord">Discord</a>
  </p>
</div>
<h2 align="center">What is Pharmor?</h2>

 ![Pharmor](https://github.com/t-a-g-o/pharmor/blob/ba93865ed3764a81b0bbfb1bb32de45c4303acda/showcase.png)

Pharmor is a tool that I (tago) developed to try and automate the process of making TikTok story videos as much as I can. You know the videos with Minecraft parkour and a random reddit story being
presented, yeah this will basically automate all of that from the image overlaying, cutting the video down, and text to speech!
This is just releasing so I do plan on heavily working to improve on it and make it the best I can, and also see if it's possible to make money with the Creator Funds.

Pharmor right now does not work as well as I plan for it to. I just want this code out there to see if there are any contributers willing to check out the project and put it tweak it to their own liking.
If you want to work with me in this project or future projects please contact me at santiagobuisnessmail@gmail.com

## Getting started with Pharmor on Windows (recommended)

### Download Pharmor
1. Clone the repo
   ```sh
   git clone https://github.com/t-a-g-o/pharmor
   ```
### Get prerequisites
1. Download Tesseract OCR
   * To use Pharmor's image text to speech you need a Optical Character Recognition software. Download Tesseract OCR from https://github.com/UB-Mannheim/tesseract/wiki
   * Make sure Tesseract is in your PATH
   * If you're stuck and need more help check out this very helpful video by JayMartMedia https://www.youtube.com/watch?v=2kWvk4C1pMo
2. Download required modules
   ```sh
   pip install -r requirements.txt

## Using Pharmor on macOS
Pharmor on macOS is in heavy development and may not work as intended.
### Download Pharmor
1. Clone the repo
   ```sh
   git clone https://github.com/t-a-g-o/pharmor
   ```
### Get prerequisites

1. Download required modules
   ```sh
   pip install -r requirements.txt
   ```
2. Download packages via homerew
   ```sh
   brew install ffmpeg
   ```
      ```sh
   brew install tesseract
   ```

## Using Pharmor to make a Video
* Copy the link of the YouTube video you want to use as a background for the story video. Usually vidoes like Minecraft parkour or slime making.
    If the YouTube is over 65 seconds (by default) it will be cut down. To change this edit the "lengthlimit" variable in Pharmor.py
* Put the images of the story sectioned off, in the order you want them shown ascending from 1
    Pharmor will automatically extact the text, and only show the image for however long the TTS is.
* Wait for your video to be done. The output result will be "0000-FINAL.mp4" where 0000 is a random string

## Extras
Please report any major problems in the discord so I can continue to improve on this project. 
If you want to check out my project Spotium, look below!

<h2 align="center">Spotium for Spotify</h2>

![Spotium for Spotify](https://github.com/t-a-g-o/pharmor/blob/3854279a7f8563ac7cb0ea11c5c3bb589320ff9b/spotium.png)

\nStart enjoying your music. With Spotium you get a straightforward appealing way to enjoy your music without ads. In about one second your listening experience will be smoother and more enjoyable.
For VirusTotal links, and download links visit https://spotium.dev/!

