A Tiny Japanese English Dictionary (TJED) API and Webapp utilizing Django.


API Documentation

URL Extension                        | Method | Expected Results   
/api/kanji/{kanji_character}/        | GET    | Metadata associated with the Kanji character       
/api/vocab/japanese/{japanese_word}/ | GET    | Data of the Japanese word and it's English equivalent 
/api/vocab/english/{english_word}/   | GET    | Data of the Japanese word from the English equivalent 
---------------------------------------------------------------------------------------------------------

Basic Usage
Via Web Browser
To use the API in your web browser:
 - (Parent URL)/api/kanji/{Kanji you will search for}/
 - (Parent URL)/api/vocab/japanese/{The Japanese word in question}/
 - (Parent URL)/api/vocab/english/{The English word in question}/

Via Curl
 - curl (Parent URL)/api/kanji/{Kanji you will search for}/
 - curl (Parent URL)/api/vocab/japanese/{The Japanese word in question}/
 - curl (Parent URL)/api/vocab/english/{The English word in question}/

Via Python (using requests library)
 - requests.get("(Parent URL)/api/kanji/{Kanji you will search for}")
 - requests.get("(Parent URL)/api/vocab/japanese/{The Japanese word in question}/")
 - requests.get("(Parent URL)/api/vocab/english/{The English word in question}/")
 Note that following retrieving results, you will most likely need to decode the response to utf-8
   ex. 
     import requests
     resp = requests.get("http://127.0.0.1:8000/api/vocab/japanese/にち/")
     resp.content.decode("utf-8") # prints {"japanese_word": "日", "furigana": "にち", "english_word": "Sun"}

Via Javascript
 Note: All examples presume the user has defined xhr as an XMLHttpRequest object.
 (I'm more of a backend dev but it seems this object type is available in all browsers.)
 - xhr.open("GET", "(Parent URL)/api/vocab/japanese/{Kanji you will search for}/", false)
 - xhr.open("GET", "(Parent URL)/api/vocab/japanese/{The Japanese word in question}/", false)
 - xhr.open("GET", "(Parent URL)/api/vocab/japanese/{The English word in question}/", false)
