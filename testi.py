import os
import azure.cognitiveservices.speech as speechsdk

import openai
import re
import requests
import sys
from num2words import num2words
import os
import pandas as pd
import numpy as np

openai.api_type = "azure"
openai.api_key = os.getenv('OPENAI_API_KEY') 
openai.api_base = os.getenv("OPENAI_API_ENDPOINT")
openai.api_version = "2022-12-01"

COMPLETIONS_MODEL = "text-davinci-003"

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
    elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized: {}".format(speech_recognition_result.no_match_details))
    elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_recognition_result.cancellation_details
        print("Speech Recognition canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))
            print("Did you set the speech resource key and region values?")

recognize_from_microphone()

prompt = "{}".format(speech_recognition_result.text)
openai.Completion.create(
    prompt=prompt,
    temperature=0,
    max_tokens=1000,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    engine=COMPLETIONS_MODEL
)["choices"][0]["text"].strip(" \n")