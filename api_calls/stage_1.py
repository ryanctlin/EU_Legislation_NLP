"""This module contains functions to make API calls to the Stage 1 Model of IBM's Watson
NLU, which identifies sections of text containing references to EU Regulations or
Directives"""

from __future__ import print_function
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions


def getEntities_1(text):
    """This function accepts the text to be processed and makes an API call to
    the Stage 1 NLU model. Returns detected entities in JSON format"""

    #Create new client for NLU service
    nlu_stage1 = NaturalLanguageUnderstandingV1(
        version='2018-08-11',
        iam_api_key='m92KNssmXlVm4n8G3fYhlkSE90Yw3xCmSh93XKdiu4oy',
        url='https://gateway-wdc.watsonplatform.net/natural-language-understanding/api')

    #Send text to API and return entities
    response = nlu_stage1.analyze(
        text=text,
        features=Features(entities=EntitiesOptions(model='a0f0773d-d9c0-4b66-9880-be459ac0b3f7', mentions=True)))

    return(response)