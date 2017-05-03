import pandas as pd
import matplotlib.pyplot as plt

perror = pd.read_csv('pitch_out/perror.csv')
terror = pd.read_csv('time_out/terror.csv')
error2 = pd.read_csv('../20000 epochs/error.csv')
error3 = pd.read_csv('../30000 epochs/error.csv')
error200 = pd.concat([error2, error3])

plt.plot(perror['epoch'], perror[' error'], 'r--', terror['epoch'], terror[' error'], 'bs', error2['epoch'], error2[' error'], 'g^')
plt.show()
