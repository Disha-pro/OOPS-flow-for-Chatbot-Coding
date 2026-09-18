#Encapsulation means keeping an object's data and the methods that operate on that data
#together inside a class, while controlling how that data is accessed or changed.

class Chatbot:
    def __init__(self, name):
        self.name = name
        self.history = []

    def ask(self, question):
        self.history.append(question)

    def show_history(self):
        return self.history

  self.name
self.history # are its daata

ask()
show_history() : are its methods
They are encapsulated inside the Chatbot class.
----------------------------------------------------------------------------------------------------
#Python gives us naming conventions such as _ and __ for this.
class Chatbot:
    def __init__(self, name):
        self.name = name
        self._history = []

The _history means:
#This is intended to be an internal attribute. Don't directly mess with it from outside the class."
So instead of:
bot._history.append("hello")

we ideally use:

bot.ask("hello")
and:
bot.show_history()
    def ask(self, question):
        self._history.append(question)

    def show_history(self):
        return self._history
----------------------------------------------------------------------------------------------------------

class AIModel:
  def __init__(self,name,_api_key): #init - that runs automatically when you create an object
    self.name=name #self refers to the current object.
    self._api_key=_api_key #The _ convention indicates that _api_key is intended to be an internal/protected-style attribute.
    self.history=[] #This creates an empty list for the object.

  def show_model(self):
    return self.name #self means model .Hence self.name becomes model.name
  def connect(self):
    return "Connected tp AI model"
model = AIModel("GPT","12345")
print(model.show_model())
print(model.connect())


The key encapsulation idea
Instead of having random variables everywhere:
"""name
api_key
history"""
you keep the model's data and the operations on that data together:
    

AIModel
│
├── DATA
│   ├── name
│   ├── _api_key
│   └── history
│
└── METHODS
    ├── show_model()
    └── connect()

----------------------------------------------------------------------------------------------------

class ChatMemory:
    def __init__(self):
        self._messages = []

    def add_message(self, message): #self - the current object, which will be memory.
        self._messages.append(message) #_messages → an internal-style attribute.

    def show_messages(self):
        return self._messages


memory = ChatMemory()

memory.add_message("What is RAG?")
memory.add_message("What is an embedding?")

print(memory.show_messages())

#The _messages attribute is intended to be used internally by the class. The underscore is a convention in Python, not a strict security restriction.
