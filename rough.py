import requests
a="what is your name"


def chatbot_answer_question(text):
    url = "https://human-impersonator.llama-shubham.workers.dev/"
    params = {
        "text": text
    }
    response = requests.get(url, params=params)
    json= response.json()
    ans = json["response"]
    return ans


d=chatbot_answer_question(a)
print(d)