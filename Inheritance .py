# Class → Object → self → Attributes → Methods → Object State
Class
 ↓
Object
 ↓
self
 ↓
Attributes
 ↓
Methods
 ↓
State

#Inheritance
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

                  AIAssistant(Parent Class)
                       │
          ┌────────────┼────────────┐
          ↓            ↓            ↓
      RAGAssistant  VisionBot   AgentAssistant(Child class inherited by Parent Class)
          │            │            │
       retrieval     images       tools
       documents     vision       planning
-----------------------------------------------------------------------------------------
Chatbot
   │
   │ inherits
   ↓
RAGChatbot
   │
   ├── inherited ask()
   └── own retrieve()
#code
class Chatbot: #parent class
  def __init__(self,name):
    self.name=name
    self.history=[]
  def ask(self,question):
    self.history.append(question)
class RAGChatbot(Chatbot): #child class
  def retrive(self):
    return f"Retriving relevant documents"
bot = RAGChatbot("Disha-RAG") #object
bot.ask("what is rag?")
print(bot.retrive())
print(bot.history)

@Inheritance = creating a specialized class that reuses functionality from an existing class.
---------------------------------------------------------------------------------------------

********************SUPER()*******************************************
super().__init__(name)
Run the parent's __init__() method.

    Chatbot
   │
   ├── name
   ├── history
   └── ask()
        ↑
        │ inherited
        │
RAGChatbot
   │
   ├── name
   ├── history
   └── vector_db

#code
class Chatbot: #parent
  def __init__(self,name):
    self.name=name
    self.history=[] #history was created in the parent's __init___
  def ask(self,question):
    self.history.append(question)

class RAGChatbot(Chatbot): #class child inherits from chatbot

  def __init__(self,name,vector_db):
    super().__init__(name) #This calls the parent init method
    self.vector_db=vector_db #then child attribute gets add.
  
bot = RAGChatbot("Disha","Pinecone") #object(instance) - bot is an object (instance) of the RAGChatbot class.
bot.ask("What is vector db and how it is stored") #comes form parent class
bot.ask("what are compoents of AGentic AI?")
print(bot.history)
print(bot.vector_db)
print(bot.name)

bot
│
├── name → "Disha"
├── history → [
│     "What is vector db and how it is stored",
│     "what are compoents of AGentic AI?"
│   ]
│
└── vector_db → "Pinecone"
             Chatbot
          (Parent Class)
               │
        ┌──────┴──────┐
        │             │
      name          history
        │             │
        └──────┬──────┘
               │
         RAGChatbot
          (Child Class)
               │
          retrive()
               │
               ↓
             bot
          (Object)
               │
        ┌──────┼─────────────┐
        ↓      ↓             ↓
      name   history      retrive()
   Disha-RAG ["what is rag?"] 
#Class = blueprint, object = actual thing created from the blueprint, and bot is the actual RAGChatbot object.
----------------------------------------------------------------------------------------------------
