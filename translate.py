# -*- coding: utf-8 -*-
from google.cloud import translate_v2 as translate

def translate_text(text, target):
    translate_client = translate.Client()
    result = translate_client.translate(text, target_language=target)

    #print('Text: ', result['input'])
    #print('Translation', result['translatedText'])
    #print('Detected source lang: ', result['detectedSourceLanguage'])
    return result['translatedText']

#example_text = 'como estas'
#print (translate_text(example_text, 'en'))
