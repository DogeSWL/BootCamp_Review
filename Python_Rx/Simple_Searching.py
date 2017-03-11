import re

def get_matching_words(regex):
 words = ["aimlessness", "assassin", "baby", "beekeeper", "belladonna", "cannonball", "crybaby", "denver", "embraceable", "facetious", "flashbulb", "gaslight", "hobgoblin", "iconoclast", "issue", "kebab", "kilo", "laundered", "mattress", "millennia", "natural", "obsessive", "paranoia", "queen", "rabble", "reabsorb", "sacrilegious", "schoolroom", "tabby", "tabloid", "unbearable", "union", "videotape"]

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

contain_any_b = 'b\w{1}b'
print get_matching_words(contain_any_b)
