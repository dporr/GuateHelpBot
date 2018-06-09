#_*_encoding:utf-8_*_
import apiai, json

DIALOGFLOW_ACCESS_TOKEN=""
ES_419 = 'es-419' #Configuracion de idioma ES Latinoamerica

def apiai_infer_intent(sender_id, text):
    ai = apiai.ApiAI(DIALOGFLOW_ACCESS_TOKEN)
    request = ai.text_request()
    request.lang = ES_419
    request.session_id = sender_id
    request.query = text
    response = request.getresponse().read()
    try:
        r_json = json.loads(response.decode('utf-8'))
        intent = r_json.get("result").get('metadata').get("intentName")
        _text = r_json.get("result").get('fulfillment').get("messages")[0].get("speech")
        parameters = r_json.get("result").get('parameters')
        if intent.startswith("SEARCH"):
            #si es search limpiamos el texto original del usuario e ignoramos el texto default de dialoflow
            #_text = clean(text, parameters)
            pass
        return intent, _text, parameters
    except:
        return intent, _text, "None"
