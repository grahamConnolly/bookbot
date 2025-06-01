from stats import number_of_words
from stats import number_of_characters
from stats import character_count
import sys
def get_book_text(filepath):
  with open(filepath) as f:
    file_contents = f.read()

    return file_contents

def main():
  print(f"arg {len(sys.argv)}")
  if len(sys.argv) != 2:
     print("Usage: python3 main.py <path_to_book>")
     sys.exit(1)
  path = sys.argv[1]
  text = get_book_text(path)
  num_words = number_of_words(text)
  seen = number_of_characters(text)

  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {path}...")
  print("----------- Word Count ----------")
  print(f"Found {num_words} total words")
  print("--------- Character Count -------")
  values = character_count(seen)
  print(f"Type {type(values)}")
  for item in values:
      print(f"{item["char"]}: {item["num"]}")
  print("============= END ===============")

if __name__=="__main__":
    main()