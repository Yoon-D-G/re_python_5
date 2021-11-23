import re

test_string = """Give thy thoughts no tongue, 
Nor any unproportioned thought his act. 60 
Be thou familiar, but by no means vulgar. 
Those friends thou hast, and their adoption tried, 
Grapple them to thy soul with hoops of steel; 
But do not dull thy palm with entertainment 
Of each new-hatch’d, unfledged comrade. Beware 65 
Of entrance to a quarrel, but being in, 
Bear’t that the opposed may beware of thee. 
Give every man thy ear, but few thy voice; 
Take each man’s censure, but reserve thy judgment. 
Costly thy habit as thy purse can buy, 70 
But not express’d in fancy; rich, not gaudy; 
For the apparel oft proclaims the man, 
And they in France of the best rank and station 
Are of a most select and generous chief in that. 
Neither a borrower nor a lender be; 75 
For loan oft loses both itself and friend, 
And borrowing dulls the edge of husbandry. 
This above all: to thine ownself be true, 
And it must follow, as the night the day, 
Thou canst not then be false to any man.. """

pattern = re.compile(r'_?\d')
matches = pattern.finditer(test_string)
for match in matches:
        print(match)
