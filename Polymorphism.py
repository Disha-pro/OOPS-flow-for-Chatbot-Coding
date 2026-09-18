Poly = many
Morph = forms
The same method/interface can behave differently depending on the object using it.

class LLM:
    def generate(self):
        return "Generating normal response"


class RAGLLM(LLM):
    def generate(self):
        return "Retrieving documents and generating response"


class VisionLLM(LLM):
    def generate(self):
        return "Analyzing image and generating response"

We called the same method three times:
.generate()

But we got different behavior.
That's polymorphism.

                 generate()
                    │
        ┌───────────┼───────────┐
        ↓           ↓           ↓
      LLM          RAG         Vision
        ↓           ↓           ↓
    Text answer   Retrieve    Analyze
                  + answer     image
The outside code doesn't need to know the internal implementation.
It can simply say:

model.generate()
The object determines which behavior happens.
---------------------------------------------------------------------------

Method overriding

The child changes the parent's method:

class RAGLLM(LLM):
    def generate(self):
        ...

  ------------
Polymorphism
We can then use different objects through the same interface:

llm.generate()
rag.generate()
vision.generate()

Same call:

.generate()
Different behavior.

-------------------------------------------------------------------------------

#Different Behaviour 
class Chatbot:
    def respond(self):
        return "Basic chatbot response"


class RAGChatbot(Chatbot):
    def respond(self):
        return "RAG chatbot response with retrieval context"


class AgentChatbot(Chatbot):
    def respond(self):
        return "Agent chatbot response using tools"


bots = [Chatbot(), RAGChatbot(), AgentChatbot()]

for bot in bots:
    print(bot.respond())

#OUTPUT:
Basic chatbot response
RAG chatbot response with retrieval context
Agent chatbot response using tools

#Different behavior:
Chatbot      → Basic response
RAGChatbot   → Retrieval + response
AgentChatbot → Tools + response

That is polymorphism. ✅
