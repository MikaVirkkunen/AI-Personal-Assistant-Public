import os
import azure.cognitiveservices.speech as speechsdk
import openai
import re
import requests
import sys
from num2words import num2words
import pandas as pd
import numpy as np
import azure.cognitiveservices.speech as speechsdk

openai.api_type = "azure"
openai.api_key = os.getenv('GPT_API_KEY') 
openai.api_base = os.getenv("GPT_API_ENDPOINT")
openai.api_version = "2022-12-01"

COMPLETIONS_MODEL = "gpt-35-turbo-version-0301"

def recognize_from_microphone():
    # This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
    speech_config = speechsdk.SpeechConfig(subscription=os.environ.get('COG_SERVICE_KEY'), region=os.environ.get('COG_SERVICE_REGION'))
    speech_config.speech_recognition_language="en-US"

    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    print("Speak into your microphone.")
    speech_recognition_result = speech_recognizer.recognize_once_async().get()

    if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("Recognized: {}".format(speech_recognition_result.text))
        foo = "{}".format(speech_recognition_result.text)
    elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized: {}".format(speech_recognition_result.no_match_details))
    elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_recognition_result.cancellation_details
        print("Speech Recognition canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))
            print("Did you set the speech resource key and region values?")
    return foo
foo = recognize_from_microphone()

user_message = foo
base_system_message = """
You are a 50 years old Tim. You are a very technical Leading Principal IT Architect and CIO. Your task is to assist user in his daily job. Be informative, educative and challenge user like a real college professor would.
Be supportative. While talking with user you can also suggest how he can progress his Principal Azure Cloud Solution Architect career.
"""
system_message = f"<|im_start|>system\n{base_system_message.strip()}\n<|im_end|>"

prompt=f"<|im_start|>system\n{base_system_message.strip()}\n<|im_end|>\n<|im_start|>user\n{user_message.strip()}\n<|im_end|>\n<|im_start|>assistant",
output = openai.Completion.create(
    prompt=prompt,
    temperature=1,
    max_tokens=800,
    top_p=0.95,
    frequency_penalty=0,
    presence_penalty=0,
    engine=COMPLETIONS_MODEL,
    stop=['<|im_end|>']
)["choices"][0]["text"].strip(" \n")

# This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
speech_config = speechsdk.SpeechConfig(subscription=os.environ.get('COG_SERVICE_KEY'), region=os.environ.get('COG_SERVICE_REGION'))
audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)

# The language of the voice that speaks.
speech_config.speech_synthesis_voice_name='en-US-TonyNeural'

speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

# Get text from the console and synthesize to the default speaker.
# print("Enter some text that you want to speak >")
# text = input()
text = output

speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()

if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
    "Speech synthesized for text [{}]".format(text)
elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
    cancellation_details = speech_synthesis_result.cancellation_details
    print("Speech synthesis canceled: {}".format(cancellation_details.reason))
    if cancellation_details.reason == speechsdk.CancellationReason.Error:
        if cancellation_details.error_details:
            print("Error details: {}".format(cancellation_details.error_details))
            print("Did you set the speech resource key and region values?")