import re

test_string = """I wandered lonely as a cloud
That floats on high o'er vales and hills,
When all at once I saw a crowd,
A host, of golden daffodils;
Beside the lake, beneath the trees,
Fluttering and dancing in the breeze. """

pattern = re.compile(r'_?\d')
matches = pattern.finditer(test_string)
for match in matches:
        print(match)
