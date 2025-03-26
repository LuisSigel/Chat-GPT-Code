#This code will allow to define GPT persona and make follow up questions. Previous promts are saved and taken into account for follow up questions.
from openai import OpenAI
from dotenv import load_dotenv
import os

# loads .env into environment with the API key
load_dotenv()
api_key = os.getenv("open_api_key")

# Initialize the OpenAI client with the API key
client = OpenAI(api_key=api_key)

#For GPT to know the previous conversations we need to store the conversation history in a list
conversation_history = []

#Define GPT persona for this conversation
persona_input = input("What persona do you want me enbody: ")
conversation_history.append({"role": "system", "content": persona_input}) #User input is stored in the conversation history list. "System" Defines persona

#Loop trough a text conversation until user writes "Quit"
while True:
    
    user_input = input("User Input: ").strip() #User input is taken at beginning of each loop (remove leading/trailing spaces)

     #The loop continues until the user types "Quit"
    if user_input.lower() in {"quit", "exit", "bye", "stop"}:
        print("Ciao, Kakao")
        break
    
    conversation_history.append({"role": "user", "content": user_input}) #User input is stored in the conversation history list. "User" defines user input

    # Call AI model
    AI_response = client.chat.completions.create(
        model="gpt-4o", #Model to be used
        messages = conversation_history, #Conversation history is passed to the model
        temperature = 0.6, #Adjusts temperature of model. Higher temperature means more randomness.
        max_tokens = 50 # Defines max output. 
        #addfunctions = Here, add additional functions apart from model and messages. E.g.  presence penalty, repsonse format, store(only then requests are stored)..See documentation
    )
    ai_output = AI_response.choices[0].message.content #choices[] defines which answer to take (by default you only get one); message.content means only the content is the output.
    print("AI Answer:",ai_output) 
   
    conversation_history.append({"role": "assistant", "content": ai_output})  #AI output is stored in the conversation history list. "assistant" defines AI output
