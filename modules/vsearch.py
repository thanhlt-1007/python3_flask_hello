def search4vowels(phrase: str) -> set:
  """
  Returns any vowels found in a supplied phrase.
  """
  vowels = set("aeiou")
  return vowels.intersection(set(phrase))

def search4leters(phrase: str, letters: str = "aeiou") -> set:
  """
  Return a set of the letters found in phrase.
  """
  return set(letters).intersection(set(phrase))
