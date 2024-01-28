from matplotlib import pyplot as plt 
def DDA(x0,y0,x1,y1):

    #cari beda absolut
    dx = abs(x0-x1)
    dy = abs(y0-y1)

    #cari beda maximum
    steps = max(dx,dy)

    #menghitung
    #  inkrementasi di x dan y
    yInc = dy/steps
    xInc = dx/steps
    x =float(x0)
    y = float(y0)

    koordinatX = []
    koordinatY = []



    for  i in range(steps):
        koordinatX.append(x)
        koordinatY.append(y)

        x = x+xInc
        y = y + yInc
    plt.plot(koordinatX,koordinatY,marker = "o",markersize=1,markerfacecolor="green")
    plt.show()

if __name__ == "__main__":
    DDA(20,20,60,1000)
    