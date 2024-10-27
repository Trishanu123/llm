import ollama

stream = ollama.chat(
    model='llama3.1',
    messages=[{'role': 'user', 'content': 'tell me more about thermodinamics and expalain it to me as if i am a 5 year old. also give me a corss question realted to it for understanding it better. Also, mention some tips on how i can learn this topic.'}],
    stream=True,
)

for chunk in stream:
  print(chunk['message']['content'], end='', flush=True)