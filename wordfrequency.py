import wordcloud
from wordcloud import WordCloud
print("||_||// (()) /"". /))  '.'.',.',")
path=input("Enter the path to your text(like .../path/)")
pather=input("Enter  where to store the image:'""")
lim=int(input("enter the maximum string limit"))
file = open(path, 'r')
content = file.read()
d = dict() 
words=[word for word in content.split() if word.isalpha() ]
for word in words :
    if len(word)>lim:
        if word in d : 
            d[word] = d[word] + 1
        else: 
            d[word] = 1
data_sorted = {k: v for k, v in sorted(d.items(), key=lambda x: x[1])}
print(data_sorted)
cloud = WordCloud()
cloud.generate_from_frequencies(data_sorted)
cloud.to_file(pather)
