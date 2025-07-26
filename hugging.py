from transformers import pipeline
import torch

summarizer = pipeline(task = 'summarization', model = 'nyamuda/extractive-summarization', min_new_tokens=10, max_new_tokens=100)

text = "This is a really large text about data science... "

print(summarizer(text))
