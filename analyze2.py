class Data:

    def __init__(self, number):
        self.negative = 0
        self.positive = 0
        self.neutral = 0
        self.total = number
    
f = open("sentiments_data.csv", 'r')
r = open("hasil_data.txt ", 'w+')

lines = f.readlines()
dailyFreq = {}

for i in range(1, len(lines)):
    line1 = lines[i].split(",")
    monthDay = line1[0]

    if monthDay not in dailyFreq.keys():
        dat = Data(float(line1[3]))
        dailyFreq[monthDay]=dat

        if float(line1[3]) > 0.0:
            dailyFreq[monthDay].positive+=1
        
        elif float(line1[3]) < 0.0:
            dailyFreq[monthDay].negative+=1
        
        else:
            dailyFreq[monthDay].neutral+=1
    
    else:
        dailyFreq[monthDay].total+=float(line1[3])
        
        if float(line1[3]) > 0.0:
            dailyFreq[monthDay].positive+=1
        
        elif float(line1[3]) < 0.0:
            dailyFreq[monthDay].negative+=1
        
        else:
            dailyFreq[monthDay].neutral+=1

r.write("date,positive,negative,neutral,total_pol\n")
for key in sorted(dailyFreq.keys()):
    r.write(key+","+str(dailyFreq[key].positive)+","+str(dailyFreq[key].negative)+","+str(dailyFreq[key].neutral)+","+str(dailyFreq[key].total)+"\n")

f.close()
r.close()