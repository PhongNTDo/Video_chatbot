import torch
from transformers import pipeline

token="token_huggingface"
model_id = "meta-llama/Llama-3.2-3B-Instruct"
pipe = pipeline(
    "text-generation",
    model=model_id,
    torch_dtype=torch.bfloat16,
    device_map="cuda",
    token=token,
)

# context = "Japan[a] is an island country in East Asia. It is located in the Pacific Ocean off the northeast coast of the Asian mainland, and is bordered on the west by the Sea of Japan and extends from the Sea of Okhotsk in the north to the East China Sea in the south. The Japanese archipelago consists of four major islands—Hokkaido, Honshu, Shikoku, and Kyushu—and thousands of smaller islands, covering 377,975 square kilometres (145,937 sq mi). Japan has a population of nearly 124 million as of 2024, and is the eleventh-most populous country. Its capital and largest city is Tokyo; the Greater Tokyo Area is the largest metropolitan area in the world, with more than 38 million inhabitants as of 2016. "
#
# messages = [
#     {"role": "system", "content": "You are a helpful and honest chatbot that always responds concisely and to the point based on the given context. When there is no information in the context, you respond that there is no information!"},
#     {"role": "user", "content": f"You are given a context and a question. You should use information of the context to answer. Please answer: 'No information' if answer is not exists in context.\n"
#                                 f"\nContext: {context}"
#                                 f"\nQuestion: What is the population of Japan?"}
# ]

with open("captions_handled.txt") as f:
    script = f.read()
print("Start answer")
messages = [
    {"role": "system", "content": "You are a helpful and honest chatbot that always responds concisely and to the point based on the given context. When there is no information in the context, you respond that there is no information!"},
    {"role": "user", "content": f"You are given a video script that includes several time slots and what is said in each slot. \n The format is: start time -> end time: what the character says. "
                                f"\nYou are given a question and you have to answer it based on the information in the script. Please answer: 'No information' if answer is not exists in script.\n"
                                f"\nContext: {script}"
                                f"\nQuestion: What is the prize?"}
]

outputs = pipe(
    messages,
    max_new_tokens=256,
)
print(outputs[0]["generated_text"][-1])