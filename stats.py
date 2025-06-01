def number_of_words(text):

   return len(text.split())

def number_of_characters(text):
   seen = {}
   characters = list(text.lower())
   for char in characters:
      if char in seen:
         val = seen[char]
         seen[char] = val + 1
      else:
         seen[char] = 1

   return seen

def character_count(dict):
   value = []
   keys = dict.keys()
   for key in keys:
      if key.isalpha():
         value.append({"char": key, "num": dict[key]})
   return sorted(value, key=lambda x: x['num'], reverse=True)


def sort_on(dict):
   return dict["num"]


