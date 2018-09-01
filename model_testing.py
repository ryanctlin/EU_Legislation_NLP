from __future__ import print_function
import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions


# natural_language_understanding = NaturalLanguageUnderstandingV1(
#     version='2017-02-27',
#     username='0d5f76e9-3f7b-4597-a54c-26728f57649b',
#     password='Zsm2II4BPurY')

natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2018-08-11',
    iam_api_key='2rwmGRHIqfyUnmVKoOfsJX4XjABZx33g_7hKNlKh9NDi',
    url='https://gateway-wdc.watsonplatform.net/natural-language-understanding/api')

test_string = 'Those thresholds should be set at a level that is proportionate to the aim of Directive (EU) 2015/849 to facilitate supervision by competent authorities of such establishments compliance, on behalf of their appointing institution'

response = natural_language_understanding.analyze(
    text=test_string,
    features=Features(entities=EntitiesOptions(model='c29ac388-a625-4cb4-89e7-f4661383ffff', mentions=True), keywords=KeywordsOptions()))

print(json.dumps(response, indent=2))