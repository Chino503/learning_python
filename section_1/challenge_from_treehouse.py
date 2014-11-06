def add_list(list_1):
  sum = 0
  for item in list_1:
    sum = sum + item
  return sum

def summarize(list_1):
  sentence = "The sum of X is Y"
  word_list = sentence.split()

  word_list[3] = str(list_1)
  word_list[5] = str(add_list(list_1))

  sentence = ' '.join(word_list)
  return sentence+'.'