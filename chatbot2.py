from random import choice


def get_animal_bot_response(user_response):

  bot_response_duck = ["duck"]
  bot_response_dog = ["dog"]
  bot_response_cat = ["cat"]

  if user_response ==  "woof":
    return choice(bot_response_dog)
  elif user_response == "meow" :
    return choice(bot_response_cat)
  elif user_response == "quack" :
    return choice(bot_response_duck)
  else:
    return "I don't recognize that animal sound"




print(" Animal guess")
print(" Type in one of the following animal sounds 'woof','quack', or 'meow' and I will guess the animal. ")

user_response = ""

while True:
  user_response = input(" What is the sound?: ")
  
  
  if user_response == 'done':
    break

  
  bot_response = get_animal_bot_response(user_response)
  print(bot_response)