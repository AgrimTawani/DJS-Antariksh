import pandas as pd
import matplotlib.pyplot as plt  

diamond_data = pd.read_csv('Diamond.csv')

def cost_function(m_now, c_now, data, L):
    m_gradient, c_gradient = 0, 0
    n = len(data)

    for i in range(n):
        x = data.iloc[i].carat
        y = data.iloc[i].price 

        m_gradient += -(2/n) * x * (y - (m_now * x + c_now))
        c_gradient += -(2/n) * (y - (m_now * x + c_now))

    m = m_now - m_gradient * L
    c = c_now - c_gradient * L

    return m, c

m=0
c=0
L = 0.0001
epochs = 300

for i in range(epochs):
    m, c = cost_function(m, c, diamond_data, L)

x = diamond_data.carat
y = diamond_data.price
Y = m*x + c

plt.scatter(x, y, color="black")
plt.plot(x, Y, color="red")
plt.show()


