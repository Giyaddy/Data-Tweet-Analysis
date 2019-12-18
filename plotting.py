import plotly.graph_objects as go

f = open("hasil_akhir.txt", 'r')
baris = f.readlines()

minggu = []
positive = []
negative = []
neutral = []
average =[]

bawah = 0
atas = 7
for i in range(1, 11):

    pos = 0
    neg = 0
    neu = 0
    total_data = 0
    minggu.append("Minggu ke-"+str(i))

    for j in range(bawah, atas):
        barisTemp = baris[j].split(",")

        pos+=int(barisTemp[1])
        neg+=int(barisTemp[2])
        neu+=int(barisTemp[3])
        total_data+=float(barisTemp[4])
    
    avg = total_data/(pos+neg+neu)

    positive.append(pos)
    negative.append(neg)
    neutral.append(neu)
    average.append(avg)

    bawah = atas
    atas+=7

fig = go.Figure(data=[go.Bar(name="Positive", x=minggu, y=positive), go.Bar(name="Negative", x=minggu, y=negative), go.Bar(name="Neutral", x=minggu, y=neutral)])
fig.show()

line_graph = go.Figure(data=go.Scatter(x=minggu, y=average))
line_graph.show()