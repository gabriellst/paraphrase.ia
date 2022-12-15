<h1 align=center>✏️ How to quickly paraphrase texts using A.I. ✏️</h1>

<p align=center><strong><em>paraphrase.ia</em></strong> is a Chrome extension that let's you make paraphrases of a highlighted text in your browser.</p>
<p align=center><strong>Many languages are supported!</strong></p>

<p align=center>
    <img style="margin-inline: auto" src="https://raw.githubusercontent.com/gabriellst/paraphrase.ia/master/readme_assets/main_page.png" style="height: 500px;">
</p>

## What does it do? 📝

It's an app that harnesses the power of pre-trained transformers and their natural language processing capabilities to create a few paraphrases from any given text you have highlighted in your browser.

Why only highlighted texts? Well, we thought it would be a better UX than just throwing an input box :)

## How to use it:
1. **Highlight** any text inside your browser.
2. **Click** the extension icon.
3. Click ***paraphrase now*** and wait a few seconds.

* ### Showcase:

![](https://raw.githubusercontent.com/gabriellst/paraphrase.ia/master/readme_assets/how_to_border.gif)

### You're done!! 🎉🎉
You'll receive a list with a few paraphrases that you may use to enhance your writting experience.
Clicking any result paraphrase will copy it's text so you can paste it anywhere you want.

## Installation

1. Download any of the **extension_XX** folders based on your desired UI language. (Either **portuguese** or **english** at the moment).
2. Go to your chrome extensions settings and then **activate developer mode.**
3. Then click **load unpack** and select the whole **extension_XX** folder in your downloads.

![](https://github.com/gabriellst/paraphrase.ia/blob/master/readme_assets/installation_guide.gif?raw=true)

### **Done!** 

Now you'll be able to access ***paraphrase.ia*** by clicking it's icon on the top right corner of your browser.

> **Note**: This process assumes our server is still running and you haven't hosted your own.

## Architecture

Our application uses a transformers language **model** and a **translation api**.
- Paraphrasing model.
  - [<ins>**Parrot**</ins>](https://huggingface.co/prithivida/parrot_paraphraser_on_T5) 
- Translation API.
  - [<ins>**Google Cloud Translation**</ins>](https://cloud.google.com/translate) 
 
At the time of writting this readme, the model is being hosted by a flask web server running in a Google Cloud VM with 4 cores and 16 GiB RAM. It's service costs around **$170** monthly not counting for the translation costs, we're currently affording it, but it won't be up for long. **You may host it for yourself!**

### If you wan't to host it for yourself:

1. **Create a folder** for our web server.
2. **Download the API folder** of this repository.
3. Make sure to have a Google Cloud Translate API **key**.
4. Place the **Translate API key JSON** in the API folder.
5. Install **required libraries** and Parrot.
```html
pip install flask flask-cors pandas google-cloud-translate git+https://github.com/PrithivirajDamodaran/Parrot_Paraphraser.git
```
6. Run ```main.py``` and your server should be running.

**Finally**, inside the ```popup.js``` file, **replace** the ```api_url``` variable with your Flask server ip address and now all ***paraphrase.ia*** requests should be headed there.

### Known Limitations
- Selection feature doesn't work within applications where it's text is written inside a canvas tag.
- Bigger phrases aren't being paraphrased correctly.
- Sometimes paraphrases come duplicated.
- Depending of which text you chose, it may not be able to paraphrase.

## Authors
<div>
    <div align=center>
        <a href="https://github.com/gabriellst"><h3>Gabriel Araújo</h3></a>
        <img src="https://avatars.githubusercontent.com/u/80013362?v=4" height="100px">
    </div>
    <div align=center>
        <a href="https://github.com/davirpp"><h3>Davi Ribeiro</h3></a>
        <img src="https://avatars.githubusercontent.com/u/62841854?v=4" height="100px">
    </div>
    <div align=center>
        <a href="https://github.com/tazc0de"><h3>Lucas Dantas</h3></a>
        <img src="https://avatars.githubusercontent.com/u/53546156?v=4" height="100px">
    </div>
</div>
