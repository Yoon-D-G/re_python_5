import re

test_string = """My heart aches, and a drowsy numbness pains
         My sense, as though of hemlock I had drunk,
Or emptied some dull opiate to the drains
         One minute past, and Lethe-wards had sunk:
'Tis not through envy of thy happy lot,
         But being too happy in thine happiness,—
                That thou, light-winged Dryad of the trees
                        In some melodious plot
         Of beechen green, and shadows numberless,
                Singest of summer in full-throated ease. """

pattern = re.compile(r'_?\d')
matches = pattern.finditer(test_string)
for match in matches:
        print(match)
