import pandas 
import numpy
df=pandas.read_csv('file.csv')
a=df["death"]
c=df["state"]
data=a.head(50).to_numpy()
country=c.head(50).to_numpy()

def partition(data,country,low,high): 
    i = ( low-1 )         # index of smaller element 
    pivot = data[high]     # pivot 
  
    for j in range(low , high): 
        if   data[j] < pivot: 
          
            # increment index of smaller element 
            i = i+1 
            data[i],data[j] = data[j],data[i] 
            country[i],country[j] =country[j],country[i]
  
    data[i+1],data[high] = data[high],data[i+1]
    country[i+1],country[high] = country[high],country[i+1]
     
    return ( i+1 ) 
  

# Function to do Quick sort 
def quickSort(data,country,low,high): 
    if low < high: 
  
        # pi is partitioning index, data[p] is now 
        # at right place 
        pi = partition(data,country,low,high) 
  
        # Separately sort elements before 
        # partition and after partition 
        quickSort(data,country, low, pi-1) 
        quickSort(data,country, pi+1, high) 
    


n = len(data) 
print("unsorted Data")
for i in range(n):    
    print(country[i],":",data[i])
print("____________________________________________")
quickSort(data,country,0,n-1) 
print ("Sorted data ") 

for i in range(n):    
    print(country[i],":",data[i])
    
    