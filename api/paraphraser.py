import translator
from parrot import Parrot

class Paraphraser():
  def __init__(self, ckpt_en_pt="Narrativa/mbart-large-50-finetuned-opus-en-pt-translation", ckpt_pt_en="Narrativa/mbart-large-50-finetuned-opus-pt-en-translation"):
    self.pt_en_translator = translator.Translator("pt", "en", ckpt_pt_en)
    self.en_pt_translator = translator.Translator("en", "pt", ckpt_en_pt)
    self.parrot = Parrot(model_tag="prithivida/parrot_paraphraser_on_T5", use_gpu=True)

  def paraphraseia(self, my_input,  translate=True):
    if translate: 
      my_input = self.pt_en_translator.translate(my_input)

    paraphrases = []
    param = 1

    while not paraphrases or len(paraphrases) <= 3:

        param -= 0.1
        try:
            paraphrases.extend(self.parrot.augment(input_phrase=my_input, adequacy_threshold=param, fluency_threshold=param, max_return_phrases=5))
        except:
            pass
        
        print("Model return is either None or doesn't have enough paraphrases. Trying again with lower thresholds...\n")

    filtered_paraphrases = [paraphrase[0] for paraphrase in paraphrases[:3]]
    if translate: 
      filtered_paraphrases = [self.en_pt_translator.translate(paraphrase) for paraphrase in filtered_paraphrases]

    return filtered_paraphrases