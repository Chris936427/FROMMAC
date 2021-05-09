cities=['nk','boston','alanta','denver']
outfile=open('cities.txt','w')
for i in cities:
    outfile.write(i+'\n')
outfile.close()