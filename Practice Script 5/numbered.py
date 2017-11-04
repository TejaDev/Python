f = open('Numbered.txt', 'r')

f_out = open('New1.txt', 'w')

count = 1
for i in f:
    print (i)
    f_out.write(str(count) + '. ' + i)
    count += 1

f.close()
f_out.close()