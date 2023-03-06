import os
import json
# import torch
import discord
from discord.ext import commands
from revChatGPT.V1 import Chatbot
# from transformers import pipeline
from dotenv import load_dotenv

# TLDR = 1000

# def summarize(text, max_length=512, min_length=30):
#     summarizer = pipeline("summarization", "jordiclive/flan-t5-11b-summarizer-filtered", torch_dtype=torch.bfloat16)
#     prompt = "Summarize the following article in 10-20 words:"
#     summary = summarizer(
#         f"{prompt} \n\n {text}",
#         num_beams=5,
#         min_length=min_length,
#         no_repeat_ngram_size=3,
#         truncation=True,
#         max_length=max_length,
#     )
#     return summary

# def correct_grammar(text):
#     corrector = pipeline('text2text-generation', 'pszemraj/flan-t5-large-grammar-synthesis')
#     return corrector(text)

load_dotenv()

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

config_file_path = os.path.expanduser('~/.config/revChatGPT/config.json')
with open(config_file_path, 'r') as f:
    config = json.load(f)

def sentencer(text):
    words = text.split()
    sentences = []
    start = 0
    for i, word in enumerate(words):
        if word.endswith((".", "!", "?")):
            sentences.append(" ".join(words[start:i+1]))
            start = i+1
    unique_sentences = set()
    repeated_sentences = []
    for sentence in sentences:
        sentence = sentence.strip()
        if sentence in unique_sentences:
            repeated_sentences.append(sentence)
        else:
            unique_sentences.add(sentence)
    for sentence in repeated_sentences:
        text = text.replace(sentence + '.', '')
    return text

def clean_response(response):
    # if len(response) > 300:
    #     print("grammar correction")
    #     grammarized = str(correct_grammar(response))
    #     grammar_dict = json.loads(grammarized)
    #     response = grammar_dict[0]["generated_text"]
#     if len(response) > TLDR:
#         print("summarizing text")
#         summary = summarize(response)
#         summary_dict = json.loads(summary)
#         response = summary_dict[0]["summary_text"]
    return response

def break_sentences(text, line_length=80):
    words = text.split()
    lines = []
    current_line = ""
    for word in words:
        if len(current_line + word) > line_length:
            lines.append(current_line.rstrip())
            current_line = ""
        current_line += word + " "
    if current_line:
        lines.append(current_line.rstrip())
    return "\n".join(lines)

async def chatbot_response(question: str) -> str:
    chatbot = Chatbot(config=config)
    previous_message = ""
    response = ""
    try:
        for message_data in chatbot.ask(question):
            message = message_data["message"][len(previous_message):]
            response = response + message
            previous_message = message_data["message"]
        response = sentencer(response)
        response = break_sentences(response)
        if response != "":
            return response
    except Exception as e:
        print(f"An error occurred: {e}")
        return "Sorry, I encountered an error and cannot respond at this time."

@bot.event
async def on_ready():
    print(f'{bot.user.name} is connected to Discord!')

@bot.command()
async def ask(ctx, *, question):
    response = await chatbot_response(question)
    await ctx.send(response)

bot.run(os.getenv('DISCORD_TOKEN'))
