import seaborn as sns
import numpy as np
import pandas as pd
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV, StratifiedShuffleSplit, LeaveOneOut
from sklearn.neighbors import KernelDensity

#######################################
########## Training KDE classifier 
#######################################

df = pd.read_csv(r'') # Import KDE_train.csv 
A_diagram = df[df['diagram'] == 'A'].iloc[:,1:].values.reshape((2000,1))
B_diagram = df[df['diagram'] == 'B'].iloc[:,1:].values.reshape((2000,1))
C_diagram = df[df['diagram'] == 'C'].iloc[:,1:].values.reshape((2000,1))
D_diagram = df[df['diagram'] == 'D'].iloc[:,1:].values.reshape((2000,1))
E_diagram = df[df['diagram'] == 'E'].iloc[:,1:].values.reshape((2000,1))
F_diagram = df[df['diagram'] == 'F'].iloc[:,1:].values.reshape((2000,1))
G_diagram = df[df['diagram'] == 'G'].iloc[:,1:].values.reshape((2000,1))
diagram = [A_diagram,B_diagram,C_diagram,D_diagram,E_diagram,F_diagram,G_diagram]
diagram_name = ['A','B','C','D','E','F','G']

SB = np.concatenate((A_diagram,B_diagram),axis=0) # single-component structures 
MB = np.concatenate((C_diagram,D_diagram,E_diagram),axis=0) # mixed-component structures
CB = np.concatenate((F_diagram,G_diagram),axis=0) # confounded structures
structure = [SB,MB,CB]
structure_name = ['SB','MB','CB']

params = {"bandwidth": np.arange(0.0001,0.1,0.0001)}
loocv = LeaveOneOut()
grid = GridSearchCV(KernelDensity(kernel="gaussian"), params,n_jobs=-2)
kde_estimator = {}

for i in range(3):
    grid.fit(structure[i])
    kde_estimator[structure_name[i]] = grid.best_estimator_

label = ['Single-component band','Mixed-component band','Confounded band']
from matplotlib import cm
# Create points for plotting the KDE curve
x_plot = np.linspace(-0.2, 0.2, 1000).reshape(-1, 1)
colors = cm.viridis(np.linspace(0, 1, 3))
fig,ax = plt.subplots(figsize=(12, 7))

for i in range(3):
    log_density_plot = kde_estimator[structure_name[i]].score_samples(x_plot)

    # Plot the KDE curve
    ax.plot(x_plot, np.exp(log_density_plot), color=colors[i], lw=2, label=label[i])
    ax.tick_params(axis='x', which='major', labelsize=30)
    ax.tick_params(axis='y', which='major', labelsize=20)
    plt.rcParams['axes.labelsize'] = 40
    plt.legend(fontsize = 30)
    ax.plot(structure[i], [0.5*(i)]*len(structure[i]), '|', color=colors[i])
    plt.show()
    

#################################
########## Import test data 
#################################
test_data = 
n_bands = # number of tested bands
loglh_test_mean = np.zeros(len(n_bands),3) # storing avg. loglikelihood of all causal types 
loglh_test_std = np.zeros(len(n_bands),3) # storing std. loglikelihood of all causal types

for i in range(3):
    for j in range(len(n_bands)):
        samples = kde_estimator[structure_name[i]].score_samples(test_data[j])
        loglh_test_mean[j, i] = samples.mean()
        loglh_test_std[j, i]  = samples.std()
        