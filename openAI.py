

get_ipython().system('pip install openai')





import openai





openai.api_key = "write key here"





def Sentiment_analysis(text):
    messages = [
        {"role":"system","content": """"you are trained to analyze and detect the sentiment of given text.
          if you are unsure of an answer, you can say "not sure" and recommend users to review manually"""},
        {"role":"user","content": f"""analyze the following text and determine if the sentiment is: positive or negative.
          return answer in single word as either positive or negative: {text}"""}
    ]





response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=1,
        n=1,
        temperature=0
    )





input=" i am a computer scirnce student"
response = Sentiment_analysis(input)

print(input,':the sentiment is', response)







