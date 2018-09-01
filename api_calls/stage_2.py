"""This module contains functions to make API calls to the Stage 2 Model of IBM's Watson
NLU, which identifies the individual components of EU Regulations or Directives references"""

from __future__ import print_function
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions


def getEntities_2(reference):
    """This function accepts the text to be processed and makes an API call to
    the Stage 2 NLU model. Returns detected entities in JSON format"""

    #Create new client for NLU service
    nlu_stage1 = NaturalLanguageUnderstandingV1(
        version='2018-08-11',
        iam_api_key='2rwmGRHIqfyUnmVKoOfsJX4XjABZx33g_7hKNlKh9NDi',
        url='https://gateway-wdc.watsonplatform.net/natural-language-understanding/api')

    #Send text to API and return entities
    response = nlu_stage1.analyze(
        text=reference,
        features=Features(entities=EntitiesOptions(model='7e0e13ae-1d62-4820-9564-46cd4c9a7f9e', mentions=True)))

    return(response)