import sys

from stats import get_word_count
from stats import count_characters
from stats import parse_char_counts
from stats import create_and_print_message

def get_book_text(filepath):
  with open(filepath, "r") as f:
    content = f.read()
    return content

def main():
  if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  filepath = sys.argv[1]
  text = get_book_text(filepath)
  count = get_word_count(text)
  char_dictionary = count_characters(text)
  dict_list = parse_char_counts(char_dictionary)
  create_and_print_message(count, filepath, dict_list)

main()