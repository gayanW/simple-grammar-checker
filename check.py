import language_check

tool = language_check.LanguageTool('en-US')
text = u'A sentence with a error in the Hitchhiker’s Guide tot he Galaxy'
matches = tool.check(text)

print("################# SENTENCE #################")
print(text)
print("#############################################\n")

print(str(len(matches)) + " matches found")

for match in matches:
    print(match)


# uncomment this to automatically apply suggestions to the text:
# result = language_check.correct(text, matches)
# print(result)
