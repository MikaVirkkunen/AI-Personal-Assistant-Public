# AI Personal Assistant
Idea of this project is to create personal assistant who hears what user speaks and answers back using Azure Cognitive Services and Azure ChatGPT.
User can change the personal assistant language and voice by selecting them from these lists: https://learn.microsoft.com/en-us/azure/cognitive-services/speech-service/language-support?tabs=tts
![Alt text](appdata/language-and-voice-selection.png)

## Current State
  * MVP functional by using Azure ChatGPT
  * Azure OpenAI version works too
  * Azure Cognitive Services handles voice capture and speech
  * Uses stream deck to initialize communication
  * No continuous discussion yet
  * Jupyter notebook versions work too

## How it works
  * Use Azure Cognitive services to capture user voice through microphone
  * Azure Cognitive Services translates speech to text and sends text data back to application 
  * Application then sends that text data to Azure Azure ChatGPT
  * Azure ChatGPT is using system prompt to create personality to AI who answers back to customer text based answer
  * This text based answer is then send back to Azure Cognitive Services text to speech.
  * Azure Cognitive Services is configured to use specific voice to speak out loud the answer from Azure ChatGPT
    * To get best communication with the application, select matching speech to text language (e.g. en-us) and text to speech voice language (e.g. en-US-AmberNeural)
  
## Azure OpenAI version
  * Uses Azure OpenAI to handle user discussions
 
## Azure ChatGPT version
  * Uses Azure ChatGPT to handle user discussions
  * 

### Next Steps
  * Continuous discussion
    * Use tiktoken to calculate discussion tokens
    * inform user when tokens are running low

### v2
  * Create easy way to change ChatGPT persona
  * Use other voices like real Ned Flanders or Homer Simpson voice
