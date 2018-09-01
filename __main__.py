from EU_Legislation_NLP.api_calls.stage_1 import getEntities_1
from EU_Legislation_NLP.api_calls.stage_2 import getEntities_2
from EU_Legislation_NLP.data.file_operations import write_json, read_json
import json

def main():
    #test_string = 'Directive (EU) 2015/849 to facilitate supervision by competent authorities. As defined in Regulation (EC) No 1049/2001 of the European Parliament and of the Council'
    test_string = '‘household customer’ means household customer as defined in point 25 of Article 2 of Directive 2009/73/EC; 2.   Products listed in Annex I which are admitted free of import duties pursuant to Council Regulation (EC) No 1186/2009 (9) shall not be subject to the additional import duty. Article 8. Regulation (EC) No 673/2005 is repealed.'


    #--------------Stage 1 Model---------------------------------------------------
    #Call getEntities_1 with text to obtain sections containing the Directives/Regulations referenced in it
    # response_1_raw = getEntities_1(test_string)
    # print(json.dumps(response_1_raw, indent=3))

    #Export and reload JSON data to 'data/stage1_data.txt' for offline processing
    # write_json(response_1_raw, 'data/stage1_data.txt')
    # response_1_raw = read_json('data/stage1_data.txt')



    #--------------Stage 2 Preprocessing---------------------------------------------------
    #Extract text sections containing references to be analysed in Stage 2
    # response_1_extract = [] #List to store dicts containing each reference text and type
    #
    # for item in response_1_raw['entities']: #Iterate through detected entities
    #     text = item['text'].replace('/', " / ") #Extract text and add spaces between the forward slash
    #     text = text.replace('(', " (")
    #     type = item['type'] #Extract reference type
    #     response_1_extract.append({'text': text, 'type': type})
    # response_1_extract = {'reference': response_1_extract}

    #Export and reload dictionary with references to 'data/stage1_extract.txt' for offline processing
    # write_json(response_1_extract, 'data/stage1_extract')
    response_1_extract = read_json('data/stage1_extract')
    # print(json.dumps(response_1_extract, indent=3))



    #--------------Stage 2 Model---------------------------------------------------
    #Call getEntities_2 with each reference to obtain breakdown of its components
    # response_2_raw = []
    # for counter, item in enumerate(response_1_extract['reference']):
    #     response_2_raw.append(getEntities_2(item['text']))

    #Export and reload dictionary to 'data/stage2_data.txt'
    # write_json(response_2_raw, 'data/stage2_data.txt')
    # response_2_raw = read_json('data/stage2_data.txt')
    #print(json.dumps(response_2_raw[1]['entities'], indent=3))


    #--------------Results Processing---------------------------------------------------
    # response_2_extract = [] #List to store dicts containing each component of reference
    # for item in response_2_raw:
    #     response_2_component_dict = {}
    #     for component in item['entities']:
    #         type = component['type']
    #         text = component['text']
    #         response_2_component_dict[type] = text
    #     response_2_extract.append(response_2_component_dict)
    # response_2_extract = {'result': response_2_extract}

    # Export and reload dictionary with results to 'data/stage2_extract.txt' for offline processing
    # write_json(response_2_extract, 'data/stage2_extract')
    response_2_extract = read_json('data/stage2_extract')
    print(json.dumps(response_2_extract, indent=3))





#-----------------Execute program-------------------------------------------
if __name__ == '__main__':
    main()