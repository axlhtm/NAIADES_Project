#  ============================================================================
#  THESIS RESEARCH - REMOTE EPANET HYDRAULIC MODEL USING WNTR
#  ============================================================================

#  IMPORT PYTHON LIBRARIES 
import os
import wntr 
import numpy as np
import pandas as pd 

#  CHANGE THE FILE DIRECTORY 
os.chdir('G:/My Drive/College Data/S2 - M.Sc. - Hydroinformatics - UN-IHE Delft/Thesis Research/Result/')
os.getcwd()

#  SET THE INCREMENTAL STEP FOR LEAKAGE DEMAND 
'''
In this section we will set the First Step (FS), Last Step (LS), and Increment Step (IS) 
for leakage demand in our hydraulic model.
'''
FS = 0 
LS = 5.125
IS = 0.125

def Leak23Aug() :
    '''
    In this function, we are trying to execute and record the stress on a 
    designated note based on some request values. The request value used refers
    to the First Step (FS), Last Step (LS), and Increment Step (IS) ranges.
    '''
    # LOAD HYDRAULIC MODEL FROM EPANET
    inp_file  = 'Hydraulic Model/August 2022/Leak - 23 August 2022.inp'
    wn        = wntr.network.WaterNetworkModel(inp_file)
    # SET NODE OF INTEREST 
    leak_node = 'L23/7/22(A)'
    junction  = wn.get_node(leak_node)
    pipe_1_node_US = 'Conducta-1974(A)'
    pipe_1_node_DS = 'Conducta-1974(B)'
    # SET LEAK DATAFRAME
    global P23Aug, V23Aug_pipe_1, Step
    P23Aug    = pd.DataFrame(columns = [leak_node])
    V23Aug_pipe_1_US    = pd.DataFrame()
    V23Aug_pipe_1_DS    = pd.DataFrame()
    Step      = pd.DataFrame(columns = ['Leak Step'])
    Step_list = []
    # RUN HYDRAULIC MODEL USING WNTR
    for i in np.arange (FS , LS , IS) : 
        'Delete the existing existing demand (leak) on the node'
        del junction.demand_timeseries_list[0]
        'Add new demand (leak) on the node based on the incremental step'
        junction.add_demand(base= i * 0.001, pattern_name='LeakPattern')
        'Simulate hydraulic model'
        sim = wntr.sim.EpanetSimulator(wn)
        results = sim.run_sim()
        'Store the leak step on data frame'
        Step_list.append(i)
        Step = pd.DataFrame(Step_list, columns=['Leak Step'])
        'Store the pressure on leak node on data frame'
        P23Aug_Pres_Temp = results.node['pressure'].loc[[3*3600],[leak_node]]
        P23Aug           = P23Aug.append(P23Aug_Pres_Temp, ignore_index=False)
        'Store the velocity on leak pipe on data frame'
        V23Aug_pipe_1_VelUS_Temp = results.link['velocity'].loc[[3*3600],[pipe_1_node_US]]
        V23Aug_pipe_1_VelDS_Temp = results.link['velocity'].loc[[3*3600],[pipe_1_node_DS]]
        V23Aug_pipe_1_US         = V23Aug_pipe_1_US.append(V23Aug_pipe_1_VelUS_Temp, ignore_index=False)
        V23Aug_pipe_1_DS         = V23Aug_pipe_1_DS.append(V23Aug_pipe_1_VelDS_Temp, ignore_index=False)
    # MERGE PRESSURE, VELOCITY, AND LEAK STEP AS A DATAFRAME
    P23Aug['Leak Step'] = np.resize(Step,len(P23Aug))
    V23Aug_pipe_1_US['Leak Step'] = np.resize(Step,len(V23Aug_pipe_1_US))
    V23Aug_pipe_1_DS['Leak Step'] = np.resize(Step,len(V23Aug_pipe_1_DS))
    V23Aug_pipe_1 = pd.merge(V23Aug_pipe_1_US, V23Aug_pipe_1_DS, how='inner')
    V23Aug_pipe_1 = V23Aug_pipe_1[[pipe_1_node_US, pipe_1_node_DS, 'Leak Step']]
Leak23Aug() # SUCESSFULY CROSS-CHECKED WITH EPANET RESULT