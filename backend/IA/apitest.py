import openai

#openai.api_key = "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"

completion = openai.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

print(completion.choices[0].message)