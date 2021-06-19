text = 'X-DSPM-Confidence: 0.8475'
start = text.find(':')
value = text[start+2:]
value = float(value)
print(value)
