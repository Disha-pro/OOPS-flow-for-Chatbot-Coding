# Class → Object → self → Attributes → Methods → Object State
class AIAssistant:
    def __init__(self, name, model):
        self.name = name
        self.model = model
        self.history = []

    def ask(self, question):
        self.history.append(question)
        return f"Question Received : {question}"

    def show_history(self):
        return self.history
      
# What you demonstrated
Concept	Your code
Class	 - class AIAssistant:
Object -	assistant = AIAssistant(...)
Attributes -	self.name, self.model, self.history
self - 	Refers to the assistant object
Method	- ask() and show_history()
Object state	- self.history
Modifying state - 	self.history.append(question)
Reading state -	return self.history
