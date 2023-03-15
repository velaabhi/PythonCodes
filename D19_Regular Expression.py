
#1. Extract each charac by \.
import re
result = re.findall(r'.','AV is largest Analytics community of India')
print(result)       #findall returns res in list

#2. Extract each charac by \w
import re
result = re.findall(r'\w','AV is largest Analytics community of India')
print(result)       #findall returns res in list, but space is not taken cz of \w

#3. Extract each charac by \w*
import re
result = re.findall(r'\w*','AV is largest Analytics community of India')
print(result)       #findall returns res in list, returns words also spaces cz of \w*

#4. Extract each charac by \w+
import re
result = re.findall(r'\w+','AV is largest Analytics community of India')
print(result)       #findall returns res in list, returns words w/o spaces cz of \w+

#5. Not Extract each charac only 1st word extract ^\w+
import re
result = re.findall(r'^\w+','AV is largest Analytics community of India')
print(result)       #findall returns only 1st word cz of ^\w+

#6. Not Extract each charac only last word extract \w+$
import re
result = re.findall(r'\w+$','AV is largest Analytics community of India')
print(result)       #findall returns only last word cz of \w+$

#7. Extracting pair of 2 charac  \w\w
import re
result = re.findall(r'\w\w','AV is largest Analytics community of India.')
print(result)       #findall returns only last word cz of \w\w

#8. Extracting pair of first 2 charac of each word  \b\w. -boundary
import re
result = re.findall(r'\b\w.','AV is largest Analytics community of India.')
print(result)       #findall returns 1st 2 chars of each word \b\w.

#9. Extracting pair of first charac of each word and spaces  \b. -boundary
import re
result = re.findall(r'\b.','AV is largest Analytics community of India.')
print(result)       #findall returns 1st chars plus spaces of each word \b.

#10. Extracting domain type by @\w+
import re
result = re.findall(r'@\w+','ab@gmail.com, mt@test.com, rv@yahoo.co.in')
print(result)       #findall returns word after @ symbol cz of @\w+
result = re.findall(r'@\w+.','ab@gmail.com, mt@test.com, rv@yahoo.co.in')
print(result)       #findall returns word after @ symbol till . cz of @\w+.
result = re.findall(r'@\w+.\w+','ab@gmail.com, mt@test.com, rv@yahoo.co.in')
print(result)       #findall returns word after @ symbol till . and next word till next .  cz of @\w+.\w+
result = re.findall(r'@\w+.+','ab@gmail.com, mt@test.com, rv@yahoo.co.in')
print(result)       #findall returns word after @ symbol till end cz of @\w+.+

#11. Extracting only domain  by ()
import re
result = re.findall(r'@\w+.(\w+)','ab@gmail.com, mt@test.com, rv@yahoo.co.in')
print(result)       #findall returns word after @ and dot symbol

#12. Extracting date by \d{}
import re
result = re.findall(r'\d{2}-\d{2}-\d{4}','Amit 34-3456 12-05-2007, xyz 56-3234 11-11-2011, sje 98-3413 12-12-2034')
print(result)       #findall returns dates cz of pattern 2digits-2digits-4digits

#12. Extracting year only from date by (\d{})
import re
result = re.findall(r'\d{2}-\d{2}-(\d{4})','Amit 34-3456 12-05-2007, xyz 56-3234 11-11-2011, sje 98-3413 12-12-2034')
print(result)       #findall returns year only cz pattern 2digits-2digits-(4digits) - () are added


result = re.findall(r'\d{2}-(\d{2})-(\d{4})','Amit 34-3456 12-05-2007, xyz 56-3234 11-11-2011, sje 98-3413 12-12-2034')
print(result)       #findall returns month and year only cz pattern 2digits-(2digits)-(4digits) - () are added


#13. Extracting strings that start with a vowel []\w
import re
result = re.findall(r'[aeiouAEIOU]\w+','AV is largest Analytics community of India.')
print(result)       #findall returns str that starts with vowels by spliting existing words


#14. Extracting words that start with a vowel \b[]\w
import re
result = re.findall(r'\b[aeiouAEIOU]\w+','AV is largest Analytics community of India.')
print(result)       #findall returns words that starts with vowels

#15. Extracting words that start with a consonent \b[^]\w
import re
result = re.findall(r'\b[^aeiouAEIOU]\w+','AV is largest Analytics community of India.')
print(result)       #findall returns words that starts with consonent and space is included

#16. Extracting words that start with a consonent w/o space by - b[^space]\w
import re
result = re.findall(r'\b[^aeiouAEIOU ]\w+','AV is largest Analytics community of India.')
print(result)       #findall returns words that starts with consonent but space is excluded

#17. Validating  Phone number
import re
li = ['9921041282','932648','8949979971']
for x in li:
    if re.match(r'[8-9]{1}[0-9]{9}',x) and len(x)==10:
        print("yes")
    else:
        print("no")

#18. split with multiple delimiters
import re
line = 'wecdsfre;cmkmdm,dpkfe,adojfr;frfsd ded'
res = re.split(r'[;,\s]',line)
print(res)  #\s is for space delimiter
res = re.sub(r'[;,\s]',' ',line)
print(res)  #\s is for space delimiter





























