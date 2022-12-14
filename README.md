<h1 align=center> paraphrase.ia ✏️ How to quickly paraphrase texts using A.I. </h1>

<p align=center><strong>paraphrase.ia</strong> is a Chrome extension that let's you make paraphrases of a highlighted text in your browser.</p>

<p align=center>
    <img style="margin-inline: auto" src="https://raw.githubusercontent.com/gabriellst/paraphrase.ia/master/readme_assets/main_page.png" style="height: 500px;">
</p>

## What does it do? 📝

It's an app that harnesses the power of pre-trained transformers and their natural language processing capabilities to create portuguese paraphrases from any given text you have highlighted in your browser.

> **Note**: English support will be shipped in the next update.

Why only highlighted texts? Well, we thought it would be a better UX than just throwing an input box :)

## How to use it:
1. Highlight any text inside your browser.
2. Click on the extension icon.
3. Click the "paraphrase" button and wait a few seconds.

### You're done!! 🎉🎉
You'll receive a list with a few paraphrases that you may use to enhance your writting experience.
Clicking on any result paraphrase will copy it's text so you can paste it anywhere you want.

> **Note**: This process assumes you already have a web server running the model, if you don't, check the installation process down below.

## Architecture

Our application uses 3 different transformers language **models**.
- 1 for paraphrasing.
  - [<ins>**Parrot**</ins>](https://huggingface.co/prithivida/parrot_paraphraser_on_T5) 
- 2 for translation.
  - [<ins>**Narrativa mBART EN to PT**</ins>](https://huggingface.co/Narrativa/mbart-large-50-finetuned-opus-en-pt-translation) 
  - [<ins>**Narrativa mBART PT to EN**</ins>](https://huggingface.co/Narrativa/mbart-large-50-finetuned-opus-pt-en-translation)
 
At the time of writting this readme, the model is being hosted by a flask web server running in a Google Cloud VM with an NVIDIA T4 GPU. It's service costs around **$400** so it won't be up for long.
**Unfortunately we can't host it for everyone**, for now, affording a GPU focused server is not a priority.
