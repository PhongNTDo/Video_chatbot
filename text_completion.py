import os
os.environ["CUDA_DEVICE_ORDER"]="PCI_BUS_ID"   # see issue #152
os.environ["CUDA_VISIBLE_DEVICES"]="1"

import torch
from transformers import pipeline


class LLM():
    def __init__(self, script_file):
        token="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"
        model_id = "meta-llama/Llama-3.2-3B-Instruct"
        self.pipe = pipeline(
            "text-generation",
            model=model_id,
            torch_dtype=torch.bfloat16,
            device_map="cuda",
            token=token)
        
        
        with open(script_file) as f:
            script = f.read()
        self.script = script

    def get_answer(self, question):
        messages = [
            {"role": "system", "content": "You are a helpful and honest chatbot that always responds concisely and to the point based on the given context. When there is no information in the context, you respond that there is no information!"},
            {"role": "user", "content": f"You are given a video script that includes several time slots and what is said in each slot. \n The format is: start time -> end time: what the character says. "
                                        f"\nYou are given a question and you have to answer it based on the information in the script. Only answer with the content in script. Please answer: 'No information' if answer is not exists in script.\n"
                                        f"\Script: {self.script}"
                                        f"\nQuestion: {question}"}
        ]
        outputs = self.pipe(
            messages,
            max_new_tokens=256,
        )
        return outputs[0]["generated_text"][-1]