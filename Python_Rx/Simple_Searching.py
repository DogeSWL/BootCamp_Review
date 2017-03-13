import re

def get_matching_words(regex):
 words = ["aimlessness", "assassin", "baby", "beekeeper", "belladonna", "cannonball", "crybaby", "denver", "embraceable", "facetious", "flashbulb", "gaslight", "hobgoblin", "iconoclast", "issue", "kebab", "kilo", "laundered", "mattress", "millennia", "natural", "obsessive", "paranoia", "queen", "rabble", "reabsorb", "sacrilegious", "schoolroom", "tabby", "tabloid", "unbearable", "union", "videotape", "bible", "b0b12", "baswz0b", "1321"]

 matches = []

 for word in words:
 	if re.search(regex,word):
 		matches.append(word)

 return matches

contain_v = 'v+'
# print get_matching_words(contain_v)

contain_ss = 'ss+'
# print get_matching_words(contain_ss)

end_e = 'e$'
# print get_matching_words(end_e)

contain_b_any_b = 'b[a-z]b'
# print get_matching_words(contain_b_any_b)

contain_b_one_b = 'bib'
# print get_matching_words(contain_b_one_b)

contain_b_anyChar0_b = 'b[a-z0]+b'
# print get_matching_words(contain_b_anyChar0_b)

# contain_all_vowels = 'a\e'
# print get_matching_words(contain_all_vowels)

# contain_letr_reg = '(\D)'
# print get_matching_words(contain_letr_reg)

contain_double_L = r'(\w)\1'        # with 'r' backslash characters are treated literally
print get_matching_words(contain_double_L)
