from transformers import MBart50TokenizerFast, MBartForConditionalGeneration
import torch

class Translator():
  def __init__(self, source, target, ckpt):
    self.source = f'{source}_XX'
    self.target = f'{target}_XX'
    self.ckpt = ckpt
    self.model = self.get_model()
    self.tokenizer = self.get_tokenizer()

  def get_model(self):
    return MBartForConditionalGeneration.from_pretrained(self.ckpt).to("cuda")

  def get_tokenizer(self):
    tokenizer = MBart50TokenizerFast.from_pretrained(self.ckpt)
    tokenizer.src_lang = self.source
    return tokenizer

  def translate(self, text):
    inputs = self.tokenizer(text, return_tensors='pt')
    input_ids = inputs.input_ids.to('cuda')
    attention_mask = inputs.attention_mask.to('cuda')
    output = self.model.generate(input_ids, attention_mask=attention_mask, forced_bos_token_id=self.tokenizer.lang_code_to_id[self.target])
    result = self.tokenizer.decode(output[0], skip_special_tokens=True)
    result = result.replace("♪", "").strip() # Weird Special Character
    
    print(f'Translation: {self.source.capitalize} -> {self.target.capitalize}: {result}')
    return result