import re

# write a function that returns a boolean
# based on whether a pattern exists in an input string
def identify_match(input_str, pattern):
	match = re.search(pattern, input_str)
	if match == None:
		return False
	else:
		return True

# write an array that scans a text string
# and returns an array of all dates that follow the following format;
# month day, example June 4 or November 11
def identify_dates(input_str):
	date_regex = r"[a-zA-Z]+ \d+"
	matches = re.findall(date_regex, input_str)
	return matches