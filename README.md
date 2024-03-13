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
    ·
    <a href="https://github.com/t-a-g-o/pharmor/issues">Report Bug</a>
    ·
    <a href="https://tago.works/discord">Join Discord</a>
  </p>
</div>

<h2 align="center">What is Pharmor?</h2>

 ![Pharmor](https://github.com/t-a-g-o/pharmor/blob/ba93865ed3764a81b0bbfb1bb32de45c4303acda/showcase.png)

Pharmor is a tool that I (tago) developed to try and automate the process of making TikTok story videos as much as I can. You know the videos with Minecraft parkour and a random reddit story being
presented, yeah this will basically automate all of that from the image overlaying, cutting the video down, and text to speech!
This is just releasing so I do plan on heavily working to improve on it and make it the best I can, and also see if it's possible to make money with the Creator Funds

## Getting started with Pharmor
This is the quickest way to get setup with Pharmor
### Downloading Pharmor
Download the latest Pharmor compile from the releases tab and run the file.
This should automatically download any required libraries automatically for you.
### Using Pharmor
* Provide a YouTube URL, I recommend this video to be at least 1920x1080 since Pharmor crops to the middle
* Put all your images asending from 1 in the created "images" folder. (PNG, JPG, JPEG)
* Press enter

## Compile Pharmor yourself

### Get prerequisites
1. Clone the repo
   ```sh
   git clone https://github.com/t-a-g-o/pharmor
   ```
2. Download Tesseract OCR
   * To use Pharmor's image text to speech you need a Optical Character Recognition software. Download Tesseract OCR from https://github.com/UB-Mannheim/tesseract/wiki
   * Make sure Tesseract is in your PATH
   * If you're stuck and need more help check out this very helpful video by JayMartMedia https://www.youtube.com/watch?v=2kWvk4C1pMo
3. Download required modules
   ```sh
   pip install -r requirements.txt
   ```
4. Run Pharmor.puy

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

