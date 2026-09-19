#Abstraction means hiding the complicated implementation and exposing only what the user needs to use.
generate()
   gem↓
tokenization
   ↓
model processing
   ↓
attention layers
   ↓
probability calculation
   ↓
token generation
   ↓
response
Above is hidden 
You just use:

model.generate()

That is the basic idea of abstraction.
-----------------------------------------------------
Python provides ABC and abstractmethod for creating abstract classes.

from abc import ABC, abstractmethod
class AIModel(ABC): #creates an abstract base class.

    @abstractmethod #Any concrete child class must provide its own generate() implementation.
    def generate(self):
        pass
Here AIModel defines what every AI model must provide, but doesn't define exactly how generate() works.
---------------------------------------------------------------------
Think about an AI framework

Imagine we design:

AIModel
   │
   ├── ChatModel
   ├── VisionModel
   ├── RAGModel
   └── AgentModel

The parent says:

"Every model must have generate()."

"""But each child decides how it generates.

AIModel
  │
  └── generate()  ← required interface
       │
       ├── ChatModel → text generation
       ├── VisionModel → image understanding
       ├── RAGModel → retrieval + generation
       └── AgentModel → tools + reasoning

That's abstraction."""
----------------------------------------------------------------

from abc import ABC,abstractmethod
class AIModel(ABC): #"I define the structure that an AI model should follow."
  @abstractmethod#"Every actual AI model must have generate()."
  def generate(self):
    pass
class ChatModel(AIModel):
  def generate(self):
    return "Generating text"
class VisionModel(AIModel):
  def generate(self):
    return "Analyzing image"
models =[ChatModel(),VisionModel()] #This is an list so list will be implememted by the follwoing way only
for model in models :
  print(model.generate())

AIModel
   │
   └── generate() ← required
          │
          ├── ChatModel
          │      └── "Generating text"
          │
          └── VisionModel
                 └── "Analyzing image"             #This is abstraction.
------------------------------------------------------------------------------------------------------

Encapsulation	 = Bundle data + methods and control access	✅
Inheritance     =	Child gets functionality from parent	✅
Polymorphism	 = Same interface, different behavior	✅
Abstraction	Hide = implementation and define required interface	
