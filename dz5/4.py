import requests

URL = "https://translate.yandex.net/api/v1.5/tr.json/translate"
KEY = "trnsl.1.1.20200429T073126Z.2b4b31adbe9493f8.ca0adad5ce878f72d1429ce3b421dddebb8683e0" #Это ваш API ключ


def translate_me(mytext):

    params = dict(key=KEY, text=mytext, lang='en-ru')
    response = requests.get(URL, params=params)
    return response.json()


with open("text_4.txt", 'r', encoding='utf-8') as text:
    content = text.readlines()
    for i in content:
        print(i)
        result = translate_me(i)
        print(str(result['text'][0]))
        with open("new_txt.txt", 'a', encoding='utf-8') as f:
            f.write(str(result['text'][0]))
