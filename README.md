A Tiny Japanese English Dictionary (TJED) API and Webapp utilizing Django.


Access UI at: https://tjedictionary.herokuapp.com/ui

Access API at: https://tjedictionary.herokuapp.com/api

API Documentation

<pre>
| URL Extension                        | Method | Expected Results                                      |
| /api/kanji/{kanji_character}/        | GET    | Metadata associated with the Kanji character          |
| /api/vocab/japanese/{japanese_word}/ | GET    | Data of the Japanese word and it's English equivalent |
| /api/vocab/english/{english_word}/   | GET    | Data of the Japanese word from the English equivalent |
</pre>

Basic Usage (listed respective to the API documentation above)

Via Web Browser

To use the API in your web browser:
<pre>
 - (Parent URL)/api/kanji/{Kanji you will search for}/
 - (Parent URL)/api/vocab/japanese/{The Japanese word in question}/
 - (Parent URL)/api/vocab/english/{The English word in question}/
</pre>

Via Curl
<pre>
 - curl (Parent URL)/api/kanji/{Kanji you will search for}/
 - curl (Parent URL)/api/vocab/japanese/{The Japanese word in question}/
 - curl (Parent URL)/api/vocab/english/{The English word in question}/
</pre>

Via Python (using requests library)
<pre>
 - requests.get("(Parent URL)/api/kanji/{Kanji you will search for}")
 - requests.get("(Parent URL)/api/vocab/japanese/{The Japanese word in question}/")
 - requests.get("(Parent URL)/api/vocab/english/{The English word in question}/")
</pre>
 Note that following retrieving results, you will most likely need to decode the response to utf-8
 
   ex. 
<pre>
  import requests
  resp = requests.get("http://127.0.0.1:8000/api/vocab/japanese/にち/")
  resp.content.decode("utf-8") # prints {"japanese_word": "日", "furigana": "にち", "english_word": "Sun"}
</pre>

Via Javascript
 Note: All examples presume the user has defined xhr as an XMLHttpRequest object.
 (It seems this object type is available in all browsers.)
<pre>
 - xhr.open("GET", "(Parent URL)/api/vocab/japanese/{Kanji you will search for}/", false)
 - xhr.open("GET", "(Parent URL)/api/vocab/japanese/{The Japanese word in question}/", false)
 - xhr.open("GET", "(Parent URL)/api/vocab/japanese/{The English word in question}/", false)
</pre>
