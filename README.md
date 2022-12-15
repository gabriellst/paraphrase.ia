<h1 align=center>✏️ How to quickly paraphrase texts using A.I. ✏️</h1>

<p align=center><strong>paraphrase.ia</strong> is a Chrome extension that let's you make paraphrases of a highlighted text in your browser.</p>
<p align=center><strong>Many languages are supported!</strong></p>

<p align=center>
    <img style="margin-inline: auto" src="https://raw.githubusercontent.com/gabriellst/paraphrase.ia/master/readme_assets/main_page.png" style="height: 500px;">
</p>

## 🟢 What does it do? 📝

It's an app that harnesses the power of pre-trained transformers and their natural language processing capabilities to create a few paraphrases from any given text you have highlighted in your browser.

Why only highlighted texts? Well, we thought it would be a better UX than just throwing an input box :)

## 🟢 How to use it:
1. **Highlight** any text inside your browser.
2. **Click** on the extension icon.
3. Click the **"paraphrase now"** button and wait a few seconds.

### ⚫ Showcase:

![](https://raw.githubusercontent.com/gabriellst/paraphrase.ia/master/readme_assets/how_to_border.gif)

### You're done!! 🎉🎉
You'll receive a list with a few paraphrases that you may use to enhance your writting experience.
Clicking on any result paraphrase will copy it's text so you can paste it anywhere you want.

## 🟢 Installation

> **Note**: This process assumes our server is still running and you haven't hosted your own

1. Download any of the **extension_XX** folders based on your desired UI language. (Either **portuguese** or **english** at the moment).
2. Go to your chrome extensions settings and then **activate developer mode.**
3. Then click on the **load unpack** button and select the whole **extension_XX** folder in your downloads.

### **Done!** 

Now you'll be able to access paraphrase.ia by clicking it's icon on the top right corner of your browser.

## 🟢 Architecture

Our application uses a transformers language **model** and a **translation api**.
- Paraphrasing model. English To English.
  - [<ins>**Parrot**</ins>](https://huggingface.co/prithivida/parrot_paraphraser_on_T5) 
- Translation API.
  - [<ins>**Google Cloud Translation**</ins>](https://cloud.google.com/translate) 
 
At the time of writting this readme, the model is being hosted by a flask web server running in a Google Cloud VM with 4 cores and 16 GiB RAM. It's service costs around **$170** monthly not counting for the translation costs, i'm currently affording it, but it won't be up for long. **You may host it for yourself!**

### If you wan't to host for yourself:

1. **Create a folder** for our web server.
2. **Download the API folder** of this repository.
3. Make sure to have a Google Cloud Translate API **key**.
4. Place the **Translate API key JSON** in the API folder.
5. Install **required libraries** and Parrot.
```html
pip install flask flask-cors pandas google-cloud-translate git+https://github.com/PrithivirajDamodaran/Parrot_Paraphraser.git
```
6. Run the ```main.py``` file and your server should be running.

**Finally**, inside the ```popup.js``` file, **replace** the ```api_url``` variable with your Flask server ip address and now all paraphrase.ia requests should be headed there.

