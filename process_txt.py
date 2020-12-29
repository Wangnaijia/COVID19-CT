i=0
with open("data/simpleTest.txt","r",encoding="utf-8") as f:
    lines = f.readlines()
    #print(lines)
with open("data/simpleTest.txt","w",encoding="utf-8") as f_w:
    for line in lines:
        i+=1
        if i%100==0:
            continue
        f_w.write(line)