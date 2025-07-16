def get_word_count(text):
  return len(text.split())

def count_characters(text):
  char_dictionary = {}
  for char in text:
    keys = char_dictionary.keys()
    lower_char = char.lower()
    if lower_char in keys:
      char_dictionary[lower_char] += 1
    else:
      char_dictionary[lower_char] = 1
  return char_dictionary

def sort_on(items):
    return items["num"]

def parse_char_counts(dict):
  dict_list = []
  for key, value in dict.items():
    if key.isalpha():
      entry = {'char': key, "num": value}
      dict_list.append(entry)
  dict_list.sort(reverse=True, key=sort_on)
  return dict_list

def create_and_print_message(count, filepath, char_dict_list):
  message = f"""
============ BOOKBOT ============
Analyzing book found at {filepath}...
----------- Word Count ----------
Found {count} total words
--------- Character Count -------
  """
  print(message)
  for item in char_dict_list:
    print(f'{item["char"]}: {item["num"]}')
  print("============= END ===============")

