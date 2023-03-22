# AI Personal Assistant
Idea of this project was to create a personal assistant who hears what user speaks and answers back using Azure Cognitive Services and Azure ChatGPT.
User can change the personal assistant language and voice by selecting them from these lists: https://learn.microsoft.com/en-us/azure/cognitive-services/speech-service/language-support?tabs=tts
![Alt text](appdata/language-and-voice-selection.png)

## Current State
  * MVP functional by using Azure ChatGPT
  * (Azure OpenAI version works too)
  * Azure Cognitive Services handles voice capture and speech
  * Uses stream deck to initialize communication


## How it works
  * Use Azure Cognitive services to capture user voice through microphone
  * Azure Cognitive Services translates speech to text and sends text data back to application 
  * Application then sends that text data to Azure Azure ChatGPT
  * Azure ChatGPT is using system prompt to create personality to AI who answers back to customer text based answer
  * This text based answer is then send back to Azure Cognitive Services text to speech.
  * Azure Cognitive Services is configured to use specific voice to speak out loud the answer from Azure ChatGPT
    * To get best communication with the application, select matching speech to text language (e.g. en-us) and text to speech voice language (e.g. en-US-AmberNeural)
 
 ## Streamdeck
 * I also added a button to my Streamdeck so that every time I press the button I can talk to Azure ChatGPT
 ![Alt text](appdata/IMG20230322081851.jpg)
 * Configuring Streamdeck is really easy. You can just add System button and point to your local *.py file by using "Python" in front of the file path like: [Python "C:\Temp\foo.py"]
 ![Alt text](appdata/sd-openai.png)
  
## Pre-requisites
* Python (latest is fine)
* VSCode
* Azure Subscription
* Azure OpenAI + Azure ChatGPT
* Azure Cognitive Services

## How to get started
* Clone github repo https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository
