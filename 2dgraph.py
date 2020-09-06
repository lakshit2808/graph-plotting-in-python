
#To run this program first install matplotlib to your system 
# for that simple open your command prompt and type this command pip install matplotlib
import matplotlib.pyplot as plt 

x =[]
y = []

for i in range(1,11):
    x.append(i)

for i in range(1 , 11):
    y.append(pow(2 , i))

print(x)
print(y)

plt.title('Graph : Power of 2')
plt.xlabel('x : 1 to 10')
plt.ylabel('Power of 2 for corresponding x ')

plt.plot(x,y)
plt.show()
