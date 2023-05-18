st='ping me when you have the bandwidth'
st=st.split()
v='aeiou'
resultlist= []
for i in st:
    if i[0].lower() not in v and i[-1].lower() in v:
        resultlist.append(i)
print(resultlist)        
