# ma'am code


# txt="madhav keshav bhandari"
# x=txt.split()
# new=" "
# for i in range (len(x)-1):
#     txt=x[i]
#     new=new + (txt[0].upper()+'.')
#     new=new + x[-1].title()
#     print(new)


txt = "madhav keshav bhandari"
x = txt.split()
new = ""

# Corrected loop condition and simplified abbreviation process
for i in range(len(x) - 1):  # Only iterate over first and middle names
    new += x[i][0].upper() + '.'

# Add the last name (title-cased) after forming the initials
new += x[-1].title()

print(new)
