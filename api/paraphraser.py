from gcp_translator import Translator
from parrot import Parrot

class Paraphraser():
  def __init__(self, ckpt_en_pt="Narrativa/mbart-large-50-finetuned-opus-en-pt-translation", ckpt_pt_en="Narrativa/mbart-large-50-finetuned-opus-pt-en-translation"):
    self.translator = Translator()
    self.parrot = Parrot(model_tag="prithivida/parrot_paraphraser_on_T5", use_gpu=False)

  def paraphraseia(self, my_input):
    
    print(f"Input Original: {my_input}")

    my_input = self.translator.translate_to_english(my_input)

    print(f"Input Translated: {my_input}")

    paraphrases = []
    param = 1

    while not paraphrases or len(paraphrases) <= 3:

        param -= 0.1

        try:
            paraphrases.extend(self.parrot.augment(input_phrase=my_input, adequacy_threshold=param, fluency_threshold=param, max_return_phrases=5))

            if paraphrases.indexof(my_input) != -1:
                paraphrases.remove(my_input)
        except:
            pass
        
        print("Model return is either None or doesn't have enough paraphrases. Trying again with lower thresholds...\n")

    filtered_paraphrases = [paraphrase[0] for paraphrase in paraphrases[:3]]

    print(f"Paraphrases Original: {filtered_paraphrases}")

    if not "en" in self.translator.recent_source: 
      filtered_paraphrases = [self.translator.translate_back(paraphrase) for paraphrase in filtered_paraphrases]

    print(f"Paraphrases Translated: {filtered_paraphrases}")

    return filtered_paraphrases