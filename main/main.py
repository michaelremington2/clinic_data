import file_load as p 
import matplotlib.pylab as plt
import math as m 


f = p.file_load(12)
clinic_data = f.total_data
rows, col  = clinic_data.shape
mean_health_per_day = dict(enumerate(clinic_data.mean(axis = 0)))
graph_data = mean_health_per_day.items()
error = clinic_data.std(axis = 0)/m.sqrt(rows)
x,y = zip(*graph_data)

def plot(x,y, error):
    plt.plot(x, y,color='blue', linestyle='dashed')
    plt.errorbar(x,y,yerr=error)
    plt.title('Mean Number of Inflamation Bouts Per Day Of Trial')
    plt.ylabel('Mean Number of Innflamation Bouts Reported Per Patient')
    plt.xlabel('Days in Trial')
    plt.grid(color='k', linestyle='--', linewidth=0.1)
    plt.show()
plot(x,y, error)

##print(clinic_data.shape)
####blah blah
