import numpy as np
import matplotlib.pyplot as plt
import sys
import pandas as pd


def plot(x,y,t):  
  # Choose t=1 for plotting time on x axis
  # Choose t=0 for plotting indices on x axis
  plt.figure(1,figsize=(7,70))

  plt.subplot(12, 1, 1)
  plt.plot(x[:,t], x[:,2], 'o-')
  plt.ylabel('img_sim')

  plt.subplot(12, 1, 2)
  plt.plot(x[:,t], x[:,3], 'o-')
  plt.ylabel('or_x')

  plt.subplot(12, 1, 3)
  plt.plot(x[:,t], x[:,4], 'o-')
  plt.ylabel('or_y')

  plt.subplot(12, 1, 4)
  plt.plot(x[:,t], x[:,5], 'o-')
  plt.ylabel('or_z')

  plt.subplot(12, 1, 5)
  plt.plot(x[:,t], x[:,6], 'o-')
  plt.ylabel('or_w')

  plt.subplot(12, 1, 6)
  plt.plot(x[:,t], x[:,7], 'o-')
  plt.ylabel('av_x')

  plt.subplot(12, 1, 7)
  plt.plot(x[:,t], x[:,8], 'o-')
  plt.ylabel('av_y')

  plt.subplot(12, 1, 8)
  plt.plot(x[:,t], x[:,9], 'o-')
  plt.ylabel('av_z')

  plt.subplot(12, 1, 9)
  plt.plot(x[:,t], x[:,10], 'o-')
  plt.ylabel('la_x')

  plt.subplot(12, 1, 10)
  plt.plot(x[:,t], x[:,11], 'o-')
  plt.ylabel('la_y')

  plt.subplot(12, 1, 11)
  plt.plot(x[:,t], x[:,12], 'o-')
  plt.ylabel('la_z')

  plt.subplot(12,1,12)
  plt.plot(y[:,t], y[:,2], 'o-')
  plt.ylabel('armed')

  
  plt.show()

def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx],idx

def main():
    Data_path = sys.argv[1]
    state_path = sys.argv[2]
    output_path = sys.argv[3]
    data = np.loadtxt(Data_path, delimiter=',', skiprows=1)
    state= np.loadtxt(state_path, delimiter=',', skiprows=1) 
    #print(data.shape)
    plot(data,state,1)
    transition_time=float(input("Enter time when abnormality starts upto third decimal place: "))
    nearest_time,idx = find_nearest(data[:,1],transition_time)
    print("nearest_time is",nearest_time)
    print(idx)
    ground_truth= np.concatenate((np.ones(idx+1),np.zeros(data.shape[0]-idx-1)))
    print(ground_truth.shape)
    print(ground_truth)
    combined=np.concatenate((data, np.reshape(ground_truth,(ground_truth.shape[0],1)) ),axis=1)
    print(combined.shape)
    df = pd.DataFrame(combined[:,1:14])
    df.to_csv(output_path, header = ["time", "img_sim", "orientation.x", "orientation.y", "orientation.z", "orientation.w", "angular_velocity.x", "angular_velocity.y", "angular_velocity.z", "linear_acceleration.x", "linear_acceleration.y", "linear_acceleration.z","ground_truth"])


if __name__ == '__main__':
	main()

      
