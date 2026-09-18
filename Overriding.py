#A child class can define a method with the same name as the parent method, but give it different behavior.
@Inheritance = child gets the parent's method.
@Method overriding = child changes the behavior of that method.

class LLM:
  def generate(self):
    return "Generating response"
class RAGLLM(LLM):
  def generate(self):
     return "Retrivieng context and gnerating response"

model = RAGLLM()
print(model.generate())

#Notice something important:
Both classes have a method called:

"respond()"
But the child has its own version.
This is method overriding.
bot → RAGChatbot
          ↓
       respond()
So it uses the child's respond(), not the parent's.

             Chatbot
                │
          respond()
                │
     "I am a basic chatbot"
                │
                ↓
          RAGChatbot
                │
       respond() ← OVERRIDDEN
                │
                ↓
"I retrieve documents before answering"

---------------------------------------------
The Key idea:

Parent:
LLM
└── generate() → "Generating response"

        ↓ inherited

Child:
RAGLLM
└── generate() → "Retrieving context and generating response"
                 ↑
             OVERRIDES


