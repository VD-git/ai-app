import os
from mistralai import Mistral

class ChatbotMistral:
    def __init__(self):
        self.api_key = os.environ["MISTRAL_API_KEY"]
        self.client = Mistral(api_key=self.api_key)
        self.model = "mistral-small-latest"
        self.system_message = [{"role": "system", "content": "Você é um solucionador de dúvidas que só responde em português"}]
        self.assistant_examples = [
            {"role": "user", "content": "What is the division between 20 and 2?"},
            {"role": "assistant", "content": "É resposta é 10"},
            {"role": "user", "content": "Divide 50 for 4"},
            {"role": "assistant", "content": "Aqui é 12.5"}
        ]
        self.history_messages = []

    def make_question(self, question:str):
        if len(self.history_messages) > 0:
            messages = self.system_message + self.assistant_examples + self.history_messages + [{"role": "user", "content": question}]
            response = client.chat.complete(model = self.model, messages = messages).choices[0].message.content
            self.history_messages += [{"role": "user", "content": question}, {"role": "assistant", "content": response}]
            return response
        else:
            messages = self.system_message + self.assistant_examples + [{"role": "user", "content": question}]
            response = client.chat.complete(model = self.model, messages = messages).choices[0].message.content
            self.history_messages = [{"role": "user", "content": question}, {"role": "assistant", "content": response}]
            return response