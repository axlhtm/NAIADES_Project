#  ============================================================================
#  THESIS RESEARCH - REMOTE EPANET HYDRAULIC MODEL USING WNTR
#  ============================================================================

#  IMPORT PYTHON LIBRARIES 
import os
import wntr 
import numpy as np
import pandas as pd 

from functools import reduce

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

#  PYTHON CODE FOR LEAKAGE MODEL IN EACH DATE
#  LEAK ON MAY 2022
def Leak26May() :
    '''
    In this function, we are trying to execute and record the stress on a 
    designated note based on some request values. The request value used refers
    to the First Step (FS), Last Step (LS), and Increment Step (IS) ranges.
    '''
    # LOAD HYDRAULIC MODEL FROM EPANET
    inp_file  = 'Hydraulic Model/May 2022/Leak - 26 Mey 2022.inp'
    wn        = wntr.network.WaterNetworkModel(inp_file)
    # SET NODE OF INTEREST 
    leak_node = 'L26/5/22'
    junction  = wn.get_node(leak_node)
    pipe_1_node_US = 'Conducta-1278(A)'
    pipe_1_node_DS = 'Conducta-1278(B)'
    # SET LEAK DATAFRAME
    global P26May, V26May_pipe_1, Step
    P26May    = pd.DataFrame(columns = [leak_node])
    V26May_pipe_1_US    = pd.DataFrame()
    V26May_pipe_1_DS    = pd.DataFrame()
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
        P26May_Pres_Temp = results.node['pressure'].loc[[3*3600],[leak_node]]
        P26May           = P26May.append(P26May_Pres_Temp, ignore_index=False)
        'Store the velocity on leak pipe on data frame'
        V26May_pipe_1_VelUS_Temp = results.link['velocity'].loc[[3*3600],[pipe_1_node_US]]
        V26May_pipe_1_VelDS_Temp = results.link['velocity'].loc[[3*3600],[pipe_1_node_DS]]
        V26May_pipe_1_US         = V26May_pipe_1_US.append(V26May_pipe_1_VelUS_Temp, ignore_index=False)
        V26May_pipe_1_DS         = V26May_pipe_1_DS.append(V26May_pipe_1_VelDS_Temp, ignore_index=False)
    # MERGE PRESSURE, VELOCITY, AND LEAK STEP AS A DATAFRAME
    P26May['Leak Step'] = np.resize(Step,len(P26May))
    V26May_pipe_1_US['Leak Step'] = np.resize(Step,len(V26May_pipe_1_US))
    V26May_pipe_1_DS['Leak Step'] = np.resize(Step,len(V26May_pipe_1_DS))
    V26May_pipe_1 = pd.merge(V26May_pipe_1_US, V26May_pipe_1_DS, how='inner')
    V26May_pipe_1 = V26May_pipe_1[[pipe_1_node_US, pipe_1_node_DS, 'Leak Step']]
Leak26May() # SUCESSFULY CROSS-CHECKED WITH EPANET RESULT

#  LEAK ON JUNE 2022 
def Leak10June() :
    '''
    In this function, we are trying to execute and record the stress on a 
    designated note based on some request values. The request value used refers
    to the First Step (FS), Last Step (LS), and Increment Step (IS) ranges.
    '''
    # LOAD HYDRAULIC MODEL FROM EPANET
    inp_file  = 'Hydraulic Model/June 2022/Leak - 10 June 2022.inp'
    wn        = wntr.network.WaterNetworkModel(inp_file)
    # SET NODE OF INTEREST 
    leak_node = 'L10/6/22'
    junction  = wn.get_node(leak_node)
    pipe_1_node_US = 'Conducta-2988(A)'
    pipe_1_node_DS = 'Conducta-2988(B)'
    # SET LEAK DATAFRAME
    global P10Jun, V10Jun_pipe_1, Step
    P10Jun    = pd.DataFrame(columns = [leak_node])
    V10Jun_pipe_1_US    = pd.DataFrame()
    V10Jun_pipe_1_DS    = pd.DataFrame()
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
        P10Jun_Pres_Temp = results.node['pressure'].loc[[3*3600],[leak_node]]
        P10Jun           = P10Jun.append(P10Jun_Pres_Temp, ignore_index=False)
        'Store the velocity on leak pipe on data frame'
        V10Jun_pipe_1_US_Temp = results.link['velocity'].loc[[3*3600],[pipe_1_node_US]]
        V10Jun_pipe_1_DS_Temp = results.link['velocity'].loc[[3*3600],[pipe_1_node_DS]]
        V10Jun_pipe_1_US      = V10Jun_pipe_1_US.append(V10Jun_pipe_1_US_Temp, ignore_index=False)
        V10Jun_pipe_1_DS      = V10Jun_pipe_1_DS.append(V10Jun_pipe_1_DS_Temp, ignore_index=False)
    # MERGE PRESSURE, VELOCITY, AND LEAK STEP AS A DATAFRAME
    P10Jun['Leak Step'] = np.resize(Step,len(P10Jun))
    V10Jun_pipe_1_US['Leak Step'] = np.resize(Step,len(V10Jun_pipe_1_US))
    V10Jun_pipe_1_DS['Leak Step'] = np.resize(Step,len(V10Jun_pipe_1_DS))
    V10Jun_pipe_1 = pd.merge(V10Jun_pipe_1_US, V10Jun_pipe_1_DS, how='inner')
    V10Jun_pipe_1 = V10Jun_pipe_1[[pipe_1_node_US, pipe_1_node_DS, 'Leak Step']]
Leak10June() # SUCESSFULY CROSS-CHECKED WITH EPANET RESULT

def Leak29June() : 
    '''
    In this function, we are trying to execute and record the stress on a 
    designated note based on some request values. The request value used refers
    to the First Step (FS), Last Step (LS), and Increment Step (IS) ranges.
    '''
    # LOAD HYDRAULIC MODEL FROM EPANET
    inp_file  = 'Hydraulic Model/June 2022/Leak - 29 June 2022.inp'
    wn        = wntr.network.WaterNetworkModel(inp_file)
    # SET NODE OF INTEREST 
    leak_node = 'L29/6/22'
    junction  = wn.get_node(leak_node)
    pipe_1_node_US = 'Conducta-1282(A)'
    pipe_1_node_DS = 'Conducta-1282(B)'
    # SET LEAK DATAFRAME
    global P29Jun, V29Jun_pipe_1, Step
    P29Jun    = pd.DataFrame(columns = [leak_node])
    V29Jun_pipe_1_US    = pd.DataFrame()
    V29Jun_pipe_1_DS    = pd.DataFrame()
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
        P29Jun_Pres_Temp = results.node['pressure'].loc[[3*3600],[leak_node]]
        P29Jun           = P29Jun.append(P29Jun_Pres_Temp, ignore_index=False)
        'Store the velocity on leak pipe on data frame'
        V29Jun_pipe_1_US_Temp = results.link['velocity'].loc[[3*3600],[pipe_1_node_US]]
        V29Jun_pipe_1_DS_Temp = results.link['velocity'].loc[[3*3600],[pipe_1_node_DS]]
        V29Jun_pipe_1_US      = V29Jun_pipe_1_US.append(V29Jun_pipe_1_US_Temp, ignore_index=False)
        V29Jun_pipe_1_DS      = V29Jun_pipe_1_DS.append(V29Jun_pipe_1_DS_Temp, ignore_index=False)
    # MERGE PRESSURE AND LEAK STEP AS A DATAFRAME
    P29Jun['Leak Step'] = np.resize(Step,len(P29Jun))
    V29Jun_pipe_1_US['Leak Step'] = np.resize(Step,len(V29Jun_pipe_1_US))
    V29Jun_pipe_1_DS['Leak Step'] = np.resize(Step,len(V29Jun_pipe_1_DS))
    V29Jun_pipe_1 = pd.merge(V29Jun_pipe_1_US, V29Jun_pipe_1_DS, how='inner')
    V29Jun_pipe_1 = V29Jun_pipe_1[[pipe_1_node_US, pipe_1_node_DS, 'Leak Step']]
Leak29June() # SUCESSFULY CROSS-CHECKED WITH EPANET RESULT

#  LEAK ON JULY 2022
def Leak4July() : 
    '''
    In this function, we are trying to execute and record the stress on a 
    designated note based on some request values. The request value used refers
    to the First Step (FS), Last Step (LS), and Increment Step (IS) ranges.
    '''
    # LOAD HYDRAULIC MODEL FROM EPANET
    inp_file  = 'Hydraulic Model/July 2022/Leak - 4 July 2022.inp'
    wn        = wntr.network.WaterNetworkModel(inp_file)
    # SET NODE OF INTEREST 
    leak_node = 'L4/7/22(A)'
    junction  = wn.get_node(leak_node)
    pipe_1_node_US = 'Conducta-1071(A)'
    pipe_1_node_DS = 'Conducta-1071(B)'
    # SET LEAK DATAFRAME
    global P4Jul, V4Jul_pipe_1, Step
    P4Jul    = pd.DataFrame(columns = [leak_node])
    V4Jul_pipe_1_US    = pd.DataFrame()
    V4Jul_pipe_1_DS    = pd.DataFrame()
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
        P4Jul_Pres_Temp = results.node['pressure'].loc[[3*3600],[leak_node]]
        P4Jul           = P4Jul.append(P4Jul_Pres_Temp, ignore_index=False)
        'Store the velocity on leak pipe on data frame'
        V4Jul_pipe_1_US_Temp = results.link['velocity'].loc[[3*3600],[pipe_1_node_US]]
        V4Jul_pipe_1_DS_Temp = results.link['velocity'].loc[[3*3600],[pipe_1_node_DS]]
        V4Jul_pipe_1_US      = V4Jul_pipe_1_US.append(V4Jul_pipe_1_US_Temp, ignore_index=False)
        V4Jul_pipe_1_DS      = V4Jul_pipe_1_DS.append(V4Jul_pipe_1_DS_Temp, ignore_index=False)
    # MERGE PRESSURE AND LEAK STEP AS A DATAFRAME
    P4Jul['Leak Step'] = np.resize(Step,len(P4Jul))
    V4Jul_pipe_1_US['Leak Step'] = np.resize(Step,len(V4Jul_pipe_1_US))
    V4Jul_pipe_1_DS['Leak Step'] = np.resize(Step,len(V4Jul_pipe_1_DS))
    V4Jul_pipe_1 = pd.merge(V4Jul_pipe_1_US, V4Jul_pipe_1_DS, how='inner')
    V4Jul_pipe_1 = V4Jul_pipe_1[[pipe_1_node_US, pipe_1_node_DS, 'Leak Step']]
Leak4July() # SUCESSFULY CROSS-CHECKED WITH EPANET RESULT

def Leak7July() :
    '''
    In this function, we are trying to execute and record the stress on a 
    designated note based on some request values. The request value used refers
    to the First Step (FS), Last Step (LS), and Increment Step (IS) ranges.
    '''
    # LOAD HYDRAULIC MODEL FROM EPANET
    inp_file  = 'Hydraulic Model/July 2022/Leak - 7 July 2022.inp'
    wn        = wntr.network.WaterNetworkModel(inp_file)
    # SET NODE OF INTEREST 
    leak_node_a = 'L7/7/22'
    leak_node_b = 'L7/7/22(B)'
    junction_a  = wn.get_node(leak_node_a)
    junction_b  = wn.get_node(leak_node_b)
    pipe_1_node_US = 'Conducta-699(2)(1)(A)'
    pipe_1_node_DS = 'Conducta-699(2)(1)(B)'
    pipe_2_node_US = 'Conduct-956(1)(A)'
    pipe_2_node_DS = 'Conducta-956(1)(B)'
    # SET LEAK DATAFRAME
    global P7Jul_A, P7Jul_B, V7Jul_pipe_1, V7Jul_pipe_2, Step
    P7Jul_A   = pd.DataFrame(columns = [leak_node_a])
    P7Jul_B   = pd.DataFrame(columns = [leak_node_b])
    V7Jul_pipe_1_US    = pd.DataFrame()
    V7Jul_pipe_1_DS    = pd.DataFrame()
    V7Jul_pipe_2_US    = pd.DataFrame()
    V7Jul_pipe_2_DS    = pd.DataFrame()
    Step      = pd.DataFrame(columns = ['Leak Step'])
    Step_list = []
    # RUN HYDRAULIC MODEL USING WNTR
    for i in np.arange (FS , LS , IS) : 
        'Delete the existing existing demand (leak) on the node'
        del junction_a.demand_timeseries_list[0]
        del junction_b.demand_timeseries_list[0]
        'Add new demand (leak) on the node based on the incremental step'
        junction_a.add_demand(base= i * 0.001, pattern_name='LeakPattern')
        junction_b.add_demand(base= i * 0.001, pattern_name='LeakPattern')
        'Simulate hydraulic model'
        sim = wntr.sim.EpanetSimulator(wn)
        results = sim.run_sim()
        'Store the leak step on data frame'
        Step_list.append(i)
        Step = pd.DataFrame(Step_list, columns=['Leak Step'])
        'Store the pressure on leak node on data frame'
        P7Jul_A_Pres_Temp = results.node['pressure'].loc[[3*3600],[leak_node_a]]
        P7Jul_A           = P7Jul_A.append(P7Jul_A_Pres_Temp, ignore_index=False)
        P7Jul_B_Pres_Temp = results.node['pressure'].loc[[3*3600],[leak_node_b]]
        P7Jul_B           = P7Jul_B.append(P7Jul_B_Pres_Temp, ignore_index=False)
        'Store the velocity on leak pipe on data frame'
        V7Jul_pipe_1_US_Temp = results.link['velocity'].loc[[3*3600],[pipe_1_node_US]]
        V7Jul_pipe_1_DS_Temp = results.link['velocity'].loc[[3*3600],[pipe_1_node_DS]]
        V7Jul_pipe_1_US      = V7Jul_pipe_1_US.append(V7Jul_pipe_1_US_Temp, ignore_index=False)
        V7Jul_pipe_1_DS      = V7Jul_pipe_1_DS.append(V7Jul_pipe_1_DS_Temp, ignore_index=False)
        
        V7Jul_pipe_2_US_Temp = results.link['velocity'].loc[[3*3600],[pipe_2_node_US]]
        V7Jul_pipe_2_DS_Temp = results.link['velocity'].loc[[3*3600],[pipe_2_node_DS]]
        V7Jul_pipe_2_US      = V7Jul_pipe_2_US.append(V7Jul_pipe_2_US_Temp, ignore_index=False)
        V7Jul_pipe_2_DS      = V7Jul_pipe_2_DS.append(V7Jul_pipe_2_DS_Temp, ignore_index=False)
    # MERGE PRESSURE AND LEAK STEP AS A DATAFRAME
    P7Jul_A['Leak Step'] = np.resize(Step,len(P7Jul_A))
    P7Jul_B['Leak Step'] = np.resize(Step,len(P7Jul_B))
    
    V7Jul_pipe_1_US['Leak Step'] = np.resize(Step,len(V7Jul_pipe_1_US))
    V7Jul_pipe_1_DS['Leak Step'] = np.resize(Step,len(V7Jul_pipe_1_DS))
    V7Jul_pipe_1 = pd.merge(V7Jul_pipe_1_US, V7Jul_pipe_1_DS, how='inner')
    V7Jul_pipe_1 = V7Jul_pipe_1[[pipe_1_node_US, pipe_1_node_DS, 'Leak Step']]
    
    V7Jul_pipe_2_US['Leak Step'] = np.resize(Step,len(V7Jul_pipe_2_US))
    V7Jul_pipe_2_DS['Leak Step'] = np.resize(Step,len(V7Jul_pipe_2_DS))
    V7Jul_pipe_2 = pd.merge(V7Jul_pipe_2_US, V7Jul_pipe_2_DS, how='inner')
    V7Jul_pipe_2 = V7Jul_pipe_2[[pipe_2_node_US, pipe_2_node_DS, 'Leak Step']]
Leak7July() # SUCESSFULY CROSS-CHECKED WITH EPANET RESULT

def Leak12July() : 
    '''
    In this function, we are trying to execute and record the stress on a 
    designated note based on some request values. The request value used refers
    to the First Step (FS), Last Step (LS), and Increment Step (IS) ranges.
    '''
    # LOAD HYDRAULIC MODEL FROM EPANET
    inp_file  = 'Hydraulic Model/July 2022/Leak - 12 July 2022.inp'
    wn        = wntr.network.WaterNetworkModel(inp_file)
    # SET NODE OF INTEREST 
    leak_node_a = 'L12/7/2022(A)'
    leak_node_b = 'L12/7/2022(B)'
    leak_node_d = 'L12/7/2022(D)'
    junction_a  = wn.get_node(leak_node_a)
    junction_b  = wn.get_node(leak_node_b)
    junction_d  = wn.get_node(leak_node_d)
    pipe_1_node_US = 'Conducta-2722(A)'
    pipe_1_node_DS = 'Conducta-2722(B)'
    pipe_2_node_US = 'Conducta-957(2)(A)'
    pipe_2_node_DS = 'Conducta-957(2)(B)'
    pipe_3_node_US = 'Conducta-1270(A)'
    pipe_3_node_DS = 'Conducta-1270(B)'
    # SET LEAK DATAFRAME
    global P12Jul_A, P12Jul_B, P12Jul_D, V12Jul_pipe_1, V12Jul_pipe_2, V12Jul_pipe_3, Step
    P12Jul_A   = pd.DataFrame(columns = [leak_node_a])
    P12Jul_B   = pd.DataFrame(columns = [leak_node_b])
    P12Jul_D   = pd.DataFrame(columns = [leak_node_d])
    V12Jul_pipe_1_US    = pd.DataFrame()
    V12Jul_pipe_1_DS    = pd.DataFrame()
    V12Jul_pipe_2_US    = pd.DataFrame()
    V12Jul_pipe_2_DS    = pd.DataFrame()
    V12Jul_pipe_3_US    = pd.DataFrame()
    V12Jul_pipe_3_DS    = pd.DataFrame()
    Step      = pd.DataFrame(columns = ['Leak Step'])
    Step_list = []
    # RUN HYDRAULIC MODEL USING WNTR
    for i in np.arange (FS , LS , IS) : 
        'Delete the existing existing demand (leak) on the node'
        del junction_a.demand_timeseries_list[0]
        del junction_b.demand_timeseries_list[0]
        del junction_d.demand_timeseries_list[0]
        'Add new demand (leak) on the node based on the incremental step'
        junction_a.add_demand(base= i * 0.001, pattern_name='LeakPattern')
        junction_b.add_demand(base= i * 0.001, pattern_name='LeakPattern')
        junction_d.add_demand(base= i * 0.001, pattern_name='LeakPattern')
        'Simulate hydraulic model'
        sim = wntr.sim.EpanetSimulator(wn)
        results = sim.run_sim()
        'Store the leak step on data frame'
        Step_list.append(i)
        Step = pd.DataFrame(Step_list, columns=['Leak Step'])
        'Store the pressure on leak node on data frame'
        P12Jul_A_Pres_Temp = results.node['pressure'].loc[[3*3600],[leak_node_a]]
        P12Jul_A           = P12Jul_A.append(P12Jul_A_Pres_Temp, ignore_index=False)
        P12Jul_B_Pres_Temp = results.node['pressure'].loc[[3*3600],[leak_node_b]]
        P12Jul_B           = P12Jul_B.append(P12Jul_B_Pres_Temp, ignore_index=False)
        P12Jul_D_Pres_Temp = results.node['pressure'].loc[[3*3600],[leak_node_d]]
        P12Jul_D           = P12Jul_D.append(P12Jul_D_Pres_Temp, ignore_index=False)
        'Store the velocity on leak pipe on data frame'
        V12Jul_pipe_1_US_Temp = results.link['velocity'].loc[[3*3600],[pipe_1_node_US]]
        V12Jul_pipe_1_DS_Temp = results.link['velocity'].loc[[3*3600],[pipe_1_node_DS]]
        V12Jul_pipe_1_US      = V12Jul_pipe_1_US.append(V12Jul_pipe_1_US_Temp, ignore_index=False)
        V12Jul_pipe_1_DS      = V12Jul_pipe_1_DS.append(V12Jul_pipe_1_DS_Temp, ignore_index=False)
        
        V12Jul_pipe_2_US_Temp = results.link['velocity'].loc[[3*3600],[pipe_2_node_US]]
        V12Jul_pipe_2_DS_Temp = results.link['velocity'].loc[[3*3600],[pipe_2_node_DS]]
        V12Jul_pipe_2_US      = V12Jul_pipe_2_US.append(V12Jul_pipe_2_US_Temp, ignore_index=False)
        V12Jul_pipe_2_DS      = V12Jul_pipe_2_DS.append(V12Jul_pipe_2_DS_Temp, ignore_index=False)
        
        V12Jul_pipe_3_US_Temp = results.link['velocity'].loc[[3*3600],[pipe_3_node_US]]
        V12Jul_pipe_3_DS_Temp = results.link['velocity'].loc[[3*3600],[pipe_3_node_DS]]
        V12Jul_pipe_3_US      = V12Jul_pipe_3_US.append(V12Jul_pipe_3_US_Temp, ignore_index=False)
        V12Jul_pipe_3_DS      = V12Jul_pipe_3_DS.append(V12Jul_pipe_3_DS_Temp, ignore_index=False)
    # MERGE PRESSURE AND LEAK STEP AS A DATAFRAME
    P12Jul_A['Leak Step'] = np.resize(Step,len(P12Jul_A))
    P12Jul_B['Leak Step'] = np.resize(Step,len(P12Jul_B))
    P12Jul_D['Leak Step'] = np.resize(Step,len(P12Jul_D))
    
    V12Jul_pipe_1_US['Leak Step'] = np.resize(Step,len(V12Jul_pipe_1_US))
    V12Jul_pipe_1_DS['Leak Step'] = np.resize(Step,len(V12Jul_pipe_1_DS))
    V12Jul_pipe_1 = pd.merge(V12Jul_pipe_1_US, V12Jul_pipe_1_DS, how='inner')
    V12Jul_pipe_1 = V12Jul_pipe_1[[pipe_1_node_US, pipe_1_node_DS, 'Leak Step']]
    
    V12Jul_pipe_2_US['Leak Step'] = np.resize(Step,len(V12Jul_pipe_2_US))
    V12Jul_pipe_2_DS['Leak Step'] = np.resize(Step,len(V12Jul_pipe_2_DS))
    V12Jul_pipe_2 = pd.merge(V12Jul_pipe_2_US, V12Jul_pipe_2_DS, how='inner')
    V12Jul_pipe_2 = V12Jul_pipe_2[[pipe_2_node_US, pipe_2_node_DS, 'Leak Step']]
    
    V12Jul_pipe_3_US['Leak Step'] = np.resize(Step,len(V12Jul_pipe_3_US))
    V12Jul_pipe_3_DS['Leak Step'] = np.resize(Step,len(V12Jul_pipe_3_DS))
    V12Jul_pipe_3 = pd.merge(V12Jul_pipe_3_US, V12Jul_pipe_3_DS, how='inner')
    V12Jul_pipe_3 = V12Jul_pipe_3[[pipe_3_node_US, pipe_3_node_DS, 'Leak Step']]
Leak12July() # SUCESSFULY CROSS-CHECKED WITH EPANET RESULT

def Leak21July() :
    '''
    In this function, we are trying to execute and record the stress on a 
    designated note based on some request values. The request value used refers
    to the First Step (FS), Last Step (LS), and Increment Step (IS) ranges.
    '''
    # LOAD HYDRAULIC MODEL FROM EPANET
    inp_file  = 'Hydraulic Model/July 2022/Leak - 21 July 2022.inp'
    wn        = wntr.network.WaterNetworkModel(inp_file)
    # SET NODE OF INTEREST 
    leak_node_a = 'L21/7/22(A)'
    leak_node_b = 'L21/7/22(B)'
    junction_a  = wn.get_node(leak_node_a)
    junction_b  = wn.get_node(leak_node_b)
    pipe_1_node_US = 'Conducta-705(A)'
    pipe_1_node_DS = 'Conducta-705(B)'
    pipe_2_node_US = 'Conducta-1275(A)'
    pipe_2_node_DS = 'Conducta-1275(B)'
    # SET LEAK DATAFRAME
    global P21Jul_A, P21Jul_B, V21Jul_pipe_1, V21Jul_pipe_2, Step
    P21Jul_A   = pd.DataFrame(columns = [leak_node_a])
    P21Jul_B   = pd.DataFrame(columns = [leak_node_b])
    V21Jul_pipe_1_US    = pd.DataFrame()
    V21Jul_pipe_1_DS    = pd.DataFrame()
    V21Jul_pipe_2_US    = pd.DataFrame()
    V21Jul_pipe_2_DS    = pd.DataFrame()
    Step      = pd.DataFrame(columns = ['Leak Step'])
    Step_list = []
    # RUN HYDRAULIC MODEL USING WNTR
    for i in np.arange (FS , LS , IS) : 
        'Delete the existing existing demand (leak) on the node'
        del junction_a.demand_timeseries_list[0]
        del junction_b.demand_timeseries_list[0]
        'Add new demand (leak) on the node based on the incremental step'
        junction_a.add_demand(base= i * 0.001, pattern_name='LeakPattern')
        junction_b.add_demand(base= i * 0.001, pattern_name='LeakPattern')
        'Simulate hydraulic model'
        sim = wntr.sim.EpanetSimulator(wn)
        results = sim.run_sim()
        'Store the leak step on data frame'
        Step_list.append(i)
        Step = pd.DataFrame(Step_list, columns=['Leak Step'])
        'Store the pressure on leak node on data frame'
        P21Jul_A_Pres_Temp = results.node['pressure'].loc[[3*3600],[leak_node_a]]
        P21Jul_A           = P21Jul_A.append(P21Jul_A_Pres_Temp, ignore_index=False)
        P21Jul_B_Pres_Temp = results.node['pressure'].loc[[3*3600],[leak_node_b]]
        P21Jul_B           = P21Jul_B.append(P21Jul_B_Pres_Temp, ignore_index=False)
        'Store the velocity on leak pipe on data frame'
        V21Jul_pipe_1_US_Temp = results.link['velocity'].loc[[3*3600],[pipe_1_node_US]]
        V21Jul_pipe_1_DS_Temp = results.link['velocity'].loc[[3*3600],[pipe_1_node_DS]]
        V21Jul_pipe_1_US      = V21Jul_pipe_1_US.append(V21Jul_pipe_1_US_Temp, ignore_index=False)
        V21Jul_pipe_1_DS      = V21Jul_pipe_1_DS.append(V21Jul_pipe_1_DS_Temp, ignore_index=False)
        
        V21Jul_pipe_2_US_Temp = results.link['velocity'].loc[[3*3600],[pipe_2_node_US]]
        V21Jul_pipe_2_DS_Temp = results.link['velocity'].loc[[3*3600],[pipe_2_node_DS]]
        V21Jul_pipe_2_US      = V21Jul_pipe_2_US.append(V21Jul_pipe_2_US_Temp, ignore_index=False)
        V21Jul_pipe_2_DS      = V21Jul_pipe_2_DS.append(V21Jul_pipe_2_DS_Temp, ignore_index=False)
    # MERGE PRESSURE AND LEAK STEP AS A DATAFRAME
    P21Jul_A['Leak Step'] = np.resize(Step,len(P21Jul_A))
    P21Jul_B['Leak Step'] = np.resize(Step,len(P21Jul_B))
    V21Jul_pipe_1_US['Leak Step'] = np.resize(Step,len(V21Jul_pipe_1_US))
    V21Jul_pipe_1_DS['Leak Step'] = np.resize(Step,len(V21Jul_pipe_1_DS))
    V21Jul_pipe_1 = pd.merge(V21Jul_pipe_1_US, V21Jul_pipe_1_DS, how='inner')
    V21Jul_pipe_1 = V21Jul_pipe_1[[pipe_1_node_US, pipe_1_node_DS, 'Leak Step']]
    
    V21Jul_pipe_2_US['Leak Step'] = np.resize(Step,len(V21Jul_pipe_2_US))
    V21Jul_pipe_2_DS['Leak Step'] = np.resize(Step,len(V21Jul_pipe_2_DS))
    V21Jul_pipe_2 = pd.merge(V21Jul_pipe_2_US, V21Jul_pipe_2_DS, how='inner')
    V21Jul_pipe_2 = V21Jul_pipe_2[[pipe_2_node_US, pipe_2_node_DS, 'Leak Step']]
Leak21July() # SUCESSFULY CROSS-CHECKED WITH EPANET RESULT

def Leak26July() : 
    '''
    In this function, we are trying to execute and record the stress on a 
    designated note based on some request values. The request value used refers
    to the First Step (FS), Last Step (LS), and Increment Step (IS) ranges.
    '''
    # LOAD HYDRAULIC MODEL FROM EPANET
    inp_file  = 'Hydraulic Model/July 2022/Leak - 26 July 2022.inp'
    wn        = wntr.network.WaterNetworkModel(inp_file)
    # SET NODE OF INTEREST 
    leak_node = 'L26/7/22'
    junction  = wn.get_node(leak_node)
    pipe_1_node_US = 'Conducta-3578(A)'
    pipe_1_node_DS = 'Conducta-3578(B)'
    # SET LEAK DATAFRAME
    global P26Jul, V26Jul_pipe_1, Step
    P26Jul    = pd.DataFrame(columns = [leak_node])
    Step      = pd.DataFrame(columns = ['Leak Step'])
    V26Jul_pipe_1_US    = pd.DataFrame()
    V26Jul_pipe_1_DS    = pd.DataFrame()
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
        P26Jul_Pres_Temp = results.node['pressure'].loc[[3*3600],[leak_node]]
        P26Jul           = P26Jul.append(P26Jul_Pres_Temp, ignore_index=False)
        'Store the velocity on leak pipe on data frame'
        V26Jul_pipe_1_VelUS_Temp = results.link['velocity'].loc[[3*3600],[pipe_1_node_US]]
        V26Jul_pipe_1_VelDS_Temp = results.link['velocity'].loc[[3*3600],[pipe_1_node_DS]]
        V26Jul_pipe_1_US         = V26Jul_pipe_1_US.append(V26Jul_pipe_1_VelUS_Temp, ignore_index=False)
        V26Jul_pipe_1_DS         = V26Jul_pipe_1_DS.append(V26Jul_pipe_1_VelDS_Temp, ignore_index=False)
    # MERGE PRESSURE AND LEAK STEP AS A DATAFRAME
    P26Jul['Leak Step'] = np.resize(Step,len(P26Jul))
    V26Jul_pipe_1_US['Leak Step'] = np.resize(Step,len(V26Jul_pipe_1_US))
    V26Jul_pipe_1_DS['Leak Step'] = np.resize(Step,len(V26Jul_pipe_1_DS))
    V26Jul_pipe_1 = pd.merge(V26Jul_pipe_1_US, V26Jul_pipe_1_DS, how='inner')
    V26Jul_pipe_1 = V26Jul_pipe_1[[pipe_1_node_US, pipe_1_node_DS, 'Leak Step']]
Leak26July() # SUCESSFULY CROSS-CHECKED WITH EPANET RESULT

def Leak28July() :
    '''
    In this function, we are trying to execute and record the stress on a 
    designated note based on some request values. The request value used refers
    to the First Step (FS), Last Step (LS), and Increment Step (IS) ranges.
    '''
    # LOAD HYDRAULIC MODEL FROM EPANET
    inp_file  = 'Hydraulic Model/July 2022/Leak - 28 July 2022.inp'
    wn        = wntr.network.WaterNetworkModel(inp_file)
    # SET NODE OF INTEREST 
    leak_node_a = 'L28/7/22(A)'
    leak_node_b = 'L28/7/22(B)'
    junction_a  = wn.get_node(leak_node_a)
    junction_b  = wn.get_node(leak_node_b)
    pipe_1_node_US = 'Conducta-705(A)'
    pipe_1_node_DS = 'Conducta-705(B)'
    pipe_2_node_US = 'Conducta-1947(A)'
    pipe_2_node_DS = 'Conducta-1947(B)'
    # SET LEAK DATAFRAME
    global P28Jul_A, P28Jul_B, P7Jul_B, V28Jul_pipe_1, V28Jul_pipe_2, Step
    P28Jul_A   = pd.DataFrame(columns = [leak_node_a])
    P28Jul_B   = pd.DataFrame(columns = [leak_node_b])
    V28Jul_pipe_1_US    = pd.DataFrame()
    V28Jul_pipe_1_DS    = pd.DataFrame()
    V28Jul_pipe_2_US    = pd.DataFrame()
    V28Jul_pipe_2_DS    = pd.DataFrame()
    Step      = pd.DataFrame(columns = ['Leak Step'])
    Step_list = []
    # RUN HYDRAULIC MODEL USING WNTR
    for i in np.arange (FS , LS , IS) : 
        'Delete the existing existing demand (leak) on the node'
        del junction_a.demand_timeseries_list[0]
        del junction_b.demand_timeseries_list[0]
        'Add new demand (leak) on the node based on the incremental step'
        junction_a.add_demand(base= i * 0.001, pattern_name='LeakPattern')
        junction_b.add_demand(base= i * 0.001, pattern_name='LeakPattern')
        'Simulate hydraulic model'
        sim = wntr.sim.EpanetSimulator(wn)
        results = sim.run_sim()
        'Store the leak step on data frame'
        Step_list.append(i)
        Step = pd.DataFrame(Step_list, columns=['Leak Step'])
        'Store the pressure on leak node on data frame'
        P28Jul_A_Pres_Temp = results.node['pressure'].loc[[3*3600],[leak_node_a]]
        P28Jul_A           = P28Jul_A.append(P28Jul_A_Pres_Temp, ignore_index=False)
        P28Jul_B_Pres_Temp = results.node['pressure'].loc[[3*3600],[leak_node_b]]
        P28Jul_B           = P28Jul_B.append(P28Jul_B_Pres_Temp, ignore_index=False)
        'Store the velocity on leak pipe on data frame'
        V28Jul_pipe_1_US_Temp = results.link['velocity'].loc[[3*3600],[pipe_1_node_US]]
        V28Jul_pipe_1_DS_Temp = results.link['velocity'].loc[[3*3600],[pipe_1_node_DS]]
        V28Jul_pipe_1_US      = V28Jul_pipe_1_US.append(V28Jul_pipe_1_US_Temp, ignore_index=False)
        V28Jul_pipe_1_DS      = V28Jul_pipe_1_DS.append(V28Jul_pipe_1_DS_Temp, ignore_index=False)
        
        V28Jul_pipe_2_US_Temp = results.link['velocity'].loc[[3*3600],[pipe_2_node_US]]
        V28Jul_pipe_2_DS_Temp = results.link['velocity'].loc[[3*3600],[pipe_2_node_DS]]
        V28Jul_pipe_2_US      = V28Jul_pipe_2_US.append(V28Jul_pipe_2_US_Temp, ignore_index=False)
        V28Jul_pipe_2_DS      = V28Jul_pipe_2_DS.append(V28Jul_pipe_2_DS_Temp, ignore_index=False)
    # MERGE PRESSURE AND LEAK STEP AS A DATAFRAME
    P28Jul_A['Leak Step'] = np.resize(Step,len(P28Jul_A))
    P28Jul_B['Leak Step'] = np.resize(Step,len(P28Jul_B))
    V28Jul_pipe_1_US['Leak Step'] = np.resize(Step,len(V28Jul_pipe_1_US))
    V28Jul_pipe_1_DS['Leak Step'] = np.resize(Step,len(V28Jul_pipe_1_DS))
    V28Jul_pipe_1 = pd.merge(V28Jul_pipe_1_US, V28Jul_pipe_1_DS, how='inner')
    V28Jul_pipe_1 = V28Jul_pipe_1[[pipe_1_node_US, pipe_1_node_DS, 'Leak Step']]
    
    V28Jul_pipe_2_US['Leak Step'] = np.resize(Step,len(V28Jul_pipe_2_US))
    V28Jul_pipe_2_DS['Leak Step'] = np.resize(Step,len(V28Jul_pipe_2_DS))
    V28Jul_pipe_2 = pd.merge(V28Jul_pipe_2_US, V28Jul_pipe_2_DS, how='inner')
    V28Jul_pipe_2 = V28Jul_pipe_2[[pipe_2_node_US, pipe_2_node_DS, 'Leak Step']]
Leak28July() # SUCESSFULY CROSS-CHECKED WITH EPANET RESULT

# LEAK ON AUGUST 2022 
def Leak19August() : 
    '''
    In this function, we are trying to execute and record the stress on a 
    designated note based on some request values. The request value used refers
    to the First Step (FS), Last Step (LS), and Increment Step (IS) ranges.
    '''
    # LOAD HYDRAULIC MODEL FROM EPANET
    inp_file  = 'Hydraulic Model/August 2022/Leak - 19 August 2022.inp'
    wn        = wntr.network.WaterNetworkModel(inp_file)
    # SET NODE OF INTEREST 
    leak_node = 'L19/8/22'
    junction  = wn.get_node(leak_node)
    pipe_1_node_US = 'Conducta-1947(A)'
    pipe_1_node_DS = 'Conducta-1947(B)'
    # SET LEAK DATAFRAME
    global P19Aug,V19Aug_pipe_1, Step
    P19Aug    = pd.DataFrame(columns = [leak_node])
    V19Aug_pipe_1_US    = pd.DataFrame()
    V19Aug_pipe_1_DS    = pd.DataFrame()
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
        P19Aug_Pres_Temp = results.node['pressure'].loc[[3*3600],[leak_node]]
        P19Aug           = P19Aug.append(P19Aug_Pres_Temp, ignore_index=False)
        'Store the velocity on leak pipe on data frame'
        V19Aug_pipe_1_VelUS_Temp = results.link['velocity'].loc[[3*3600],[pipe_1_node_US]]
        V19Aug_pipe_1_VelDS_Temp = results.link['velocity'].loc[[3*3600],[pipe_1_node_DS]]
        V19Aug_pipe_1_US         = V19Aug_pipe_1_US.append(V19Aug_pipe_1_VelUS_Temp, ignore_index=False)
        V19Aug_pipe_1_DS         = V19Aug_pipe_1_DS.append(V19Aug_pipe_1_VelDS_Temp, ignore_index=False)
    # MERGE PRESSURE AND LEAK STEP AS A DATAFRAME
    P19Aug['Leak Step'] = np.resize(Step,len(P19Aug))
    V19Aug_pipe_1_US['Leak Step'] = np.resize(Step,len(V19Aug_pipe_1_US))
    V19Aug_pipe_1_DS['Leak Step'] = np.resize(Step,len(V19Aug_pipe_1_DS))
    V19Aug_pipe_1 = pd.merge(V19Aug_pipe_1_US, V19Aug_pipe_1_DS, how='inner')
    V19Aug_pipe_1 = V19Aug_pipe_1[[pipe_1_node_US, pipe_1_node_DS, 'Leak Step']]
Leak19August() # SUCESSFULY CROSS-CHECKED WITH EPANET RESULT

def Leak22August() : 
    '''
    In this function, we are trying to execute and record the stress on a 
    designated note based on some request values. The request value used refers
    to the First Step (FS), Last Step (LS), and Increment Step (IS) ranges.
    '''
    # LOAD HYDRAULIC MODEL FROM EPANET
    inp_file  = 'Hydraulic Model/August 2022/Leak - 22 August 2022.inp'
    wn        = wntr.network.WaterNetworkModel(inp_file)
    # SET NODE OF INTEREST 
    leak_node = 'L22/8/22'
    junction  = wn.get_node(leak_node)
    pipe_1_node_US = 'Conducta-1284(A)'
    pipe_1_node_DS = 'Conduta-1284(B)'
    # SET LEAK DATAFRAME
    global P22Aug, V22Aug_pipe_1, Step
    P22Aug    = pd.DataFrame(columns = [leak_node])
    V22Aug_pipe_1_US    = pd.DataFrame()
    V22Aug_pipe_1_DS    = pd.DataFrame()
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
        P22Aug_Pres_Temp = results.node['pressure'].loc[[3*3600],[leak_node]]
        P22Aug           = P22Aug.append(P22Aug_Pres_Temp, ignore_index=False)
        'Store the velocity on leak pipe on data frame'
        V22Aug_pipe_1_VelUS_Temp = results.link['velocity'].loc[[3*3600],[pipe_1_node_US]]
        V22Aug_pipe_1_VelDS_Temp = results.link['velocity'].loc[[3*3600],[pipe_1_node_DS]]
        V22Aug_pipe_1_US         = V22Aug_pipe_1_US.append(V22Aug_pipe_1_VelUS_Temp, ignore_index=False)
        V22Aug_pipe_1_DS         = V22Aug_pipe_1_DS.append(V22Aug_pipe_1_VelDS_Temp, ignore_index=False)
    # MERGE PRESSURE AND LEAK STEP AS A DATAFRAME
    P22Aug['Leak Step'] = np.resize(Step,len(P22Aug))
    V22Aug_pipe_1_US['Leak Step'] = np.resize(Step,len(V22Aug_pipe_1_US))
    V22Aug_pipe_1_DS['Leak Step'] = np.resize(Step,len(V22Aug_pipe_1_DS))
    V22Aug_pipe_1 = pd.merge(V22Aug_pipe_1_US, V22Aug_pipe_1_DS, how='inner')
    V22Aug_pipe_1 = V22Aug_pipe_1[[pipe_1_node_US, pipe_1_node_DS, 'Leak Step']]
Leak22August() # SUCESSFULY CROSS-CHECKED WITH EPANET RESULT

def Leak23August() :
    '''
    In this function, we are trying to execute and record the stress on a 
    designated note based on some request values. The request value used refers
    to the First Step (FS), Last Step (LS), and Increment Step (IS) ranges.
    '''
    # LOAD HYDRAULIC MODEL FROM EPANET
    inp_file  = 'Hydraulic Model/August 2022/Leak - 23 August 2022.inp'
    wn        = wntr.network.WaterNetworkModel(inp_file)
    # SET NODE OF INTEREST 
    leak_node_a = 'L23/7/22(A)'
    leak_node_b = 'L23/7/22(B)'
    junction_a  = wn.get_node(leak_node_a)
    junction_b  = wn.get_node(leak_node_b)
    pipe_1_node_US = 'Conducta-1974(A)'
    pipe_1_node_DS = 'Conducta-1974(B)'
    pipe_2_node_US = 'Conducta-1916(2)(A)'
    pipe_2_node_DS = 'Conducta-1916(2)(B)'
    # SET LEAK DATAFRAME
    global P23Aug_A, P23Aug_B, V23Aug_pipe_1, V23Aug_pipe_2, Step
    P23Aug_A   = pd.DataFrame(columns = [leak_node_a])
    P23Aug_B   = pd.DataFrame(columns = [leak_node_b])
    V23Aug_pipe_1_US    = pd.DataFrame()
    V23Aug_pipe_1_DS    = pd.DataFrame()
    V23Aug_pipe_2_US    = pd.DataFrame()
    V23Aug_pipe_2_DS    = pd.DataFrame()
    Step      = pd.DataFrame(columns = ['Leak Step'])
    Step_list = []
    # RUN HYDRAULIC MODEL USING WNTR
    for i in np.arange (FS , LS , IS) : 
        'Delete the existing existing demand (leak) on the node'
        del junction_a.demand_timeseries_list[0]
        del junction_b.demand_timeseries_list[0]
        'Add new demand (leak) on the node based on the incremental step'
        junction_a.add_demand(base= i * 0.001, pattern_name='LeakPattern')
        junction_b.add_demand(base= i * 0.001, pattern_name='LeakPattern')
        'Simulate hydraulic model'
        sim = wntr.sim.EpanetSimulator(wn)
        results = sim.run_sim()
        'Store the leak step on data frame'
        Step_list.append(i)
        Step = pd.DataFrame(Step_list, columns=['Leak Step'])
        'Store the pressure on leak node on data frame'
        P23Aug_A_Pres_Temp = results.node['pressure'].loc[[3*3600],[leak_node_a]]
        P23Aug_A           = P23Aug_A.append(P23Aug_A_Pres_Temp, ignore_index=False)
        P23Aug_B_Pres_Temp = results.node['pressure'].loc[[3*3600],[leak_node_b]]
        P23Aug_B           = P23Aug_B.append(P23Aug_B_Pres_Temp, ignore_index=False)
        'Store the velocity on leak pipe on data frame'
        V23Aug_pipe_1_US_Temp = results.link['velocity'].loc[[3*3600],[pipe_1_node_US]]
        V23Aug_pipe_1_DS_Temp = results.link['velocity'].loc[[3*3600],[pipe_1_node_DS]]
        V23Aug_pipe_1_US      = V23Aug_pipe_1_US.append(V23Aug_pipe_1_US_Temp, ignore_index=False)
        V23Aug_pipe_1_DS      = V23Aug_pipe_1_DS.append(V23Aug_pipe_1_DS_Temp, ignore_index=False)
        
        V23Aug_pipe_2_US_Temp = results.link['velocity'].loc[[3*3600],[pipe_2_node_US]]
        V23Aug_pipe_2_DS_Temp = results.link['velocity'].loc[[3*3600],[pipe_2_node_DS]]
        V23Aug_pipe_2_US      = V23Aug_pipe_2_US.append(V23Aug_pipe_2_US_Temp, ignore_index=False)
        V23Aug_pipe_2_DS      = V23Aug_pipe_2_DS.append(V23Aug_pipe_2_DS_Temp, ignore_index=False)
    # MERGE PRESSURE AND LEAK STEP AS A DATAFRAME
    P23Aug_A['Leak Step'] = np.resize(Step,len(P23Aug_A))
    P23Aug_B['Leak Step'] = np.resize(Step,len(P23Aug_B))
    V23Aug_pipe_1_US['Leak Step'] = np.resize(Step,len(V23Aug_pipe_1_US))
    V23Aug_pipe_1_DS['Leak Step'] = np.resize(Step,len(V23Aug_pipe_1_DS))
    V23Aug_pipe_1 = pd.merge(V23Aug_pipe_1_US, V23Aug_pipe_1_DS, how='inner')
    V23Aug_pipe_1 = V23Aug_pipe_1[[pipe_1_node_US, pipe_1_node_DS, 'Leak Step']]
    
    V23Aug_pipe_2_US['Leak Step'] = np.resize(Step,len(V23Aug_pipe_2_US))
    V23Aug_pipe_2_DS['Leak Step'] = np.resize(Step,len(V23Aug_pipe_2_DS))
    V23Aug_pipe_2 = pd.merge(V23Aug_pipe_2_US, V23Aug_pipe_2_DS, how='inner')
    V23Aug_pipe_2 = V23Aug_pipe_2[[pipe_2_node_US, pipe_2_node_DS, 'Leak Step']]
Leak23August() # SUCESSFULY CROSS-CHECKED WITH EPANET RESULT

def Leak26August() : 
    '''
    In this function, we are trying to execute and record the stress on a 
    designated note based on some request values. The request value used refers
    to the First Step (FS), Last Step (LS), and Increment Step (IS) ranges.
    '''
    # LOAD HYDRAULIC MODEL FROM EPANET
    inp_file  = 'Hydraulic Model/August 2022/Leak - 26 August 2022.inp'
    wn        = wntr.network.WaterNetworkModel(inp_file)
    # SET NODE OF INTEREST 
    leak_node = 'L26/7/22(A)'
    junction  = wn.get_node(leak_node)
    pipe_1_node_US = 'Conducta-1916(2)(A)'
    pipe_1_node_DS = 'Conducta-1916(2)(B)'
    # SET LEAK DATAFRAME
    global P26Aug, V26Aug_pipe_1, Step
    P26Aug    = pd.DataFrame(columns = [leak_node])
    Step      = pd.DataFrame(columns = ['Leak Step'])
    V26Aug_pipe_1_US    = pd.DataFrame()
    V26Aug_pipe_1_DS    = pd.DataFrame()
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
        P26Aug_Pres_Temp = results.node['pressure'].loc[[3*3600],[leak_node]]
        P26Aug           = P26Aug.append(P26Aug_Pres_Temp, ignore_index=False)
        'Store the velocity on leak pipe on data frame'
        V26Aug_pipe_1_VelUS_Temp = results.link['velocity'].loc[[3*3600],[pipe_1_node_US]]
        V26Aug_pipe_1_VelDS_Temp = results.link['velocity'].loc[[3*3600],[pipe_1_node_DS]]
        V26Aug_pipe_1_US         = V26Aug_pipe_1_US.append(V26Aug_pipe_1_VelUS_Temp, ignore_index=False)
        V26Aug_pipe_1_DS         = V26Aug_pipe_1_DS.append(V26Aug_pipe_1_VelDS_Temp, ignore_index=False)
    # MERGE PRESSURE AND LEAK STEP AS A DATAFRAME
    P26Aug['Leak Step'] = np.resize(Step,len(P26Aug))
    V26Aug_pipe_1_US['Leak Step'] = np.resize(Step,len(V26Aug_pipe_1_US))
    V26Aug_pipe_1_DS['Leak Step'] = np.resize(Step,len(V26Aug_pipe_1_DS))
    V26Aug_pipe_1 = pd.merge(V26Aug_pipe_1_US, V26Aug_pipe_1_DS, how='inner')
    V26Aug_pipe_1 = V26Aug_pipe_1[[pipe_1_node_US, pipe_1_node_DS, 'Leak Step']]
Leak26August() # SUCESSFULY CROSS-CHECKED WITH EPANET RESULT
    
def Leak30August() :
    '''
    In this function, we are trying to execute and record the stress on a 
    designated note based on some request values. The request value used refers
    to the First Step (FS), Last Step (LS), and Increment Step (IS) ranges.
    '''
    # LOAD HYDRAULIC MODEL FROM EPANET
    inp_file  = 'Hydraulic Model/August 2022/Leak - 30 August 2022.inp'
    wn        = wntr.network.WaterNetworkModel(inp_file)
    # SET NODE OF INTEREST 
    leak_node_a = 'L30/8/22(A)'
    leak_node_b = 'L30/8/22(B)'
    junction_a  = wn.get_node(leak_node_a)
    junction_b  = wn.get_node(leak_node_b)
    pipe_1_node_US = 'Conducta-2955(A)'
    pipe_1_node_DS = 'Conducta-2955(B)'
    pipe_2_node_US = 'Conducta-2208(A)'
    pipe_2_node_DS = 'Conducta-2208(B)'
    # SET LEAK DATAFRAME
    global P30Aug_A, P30Aug_B, V30Aug_pipe_1, V30Aug_pipe_2, Step
    P30Aug_A   = pd.DataFrame(columns = [leak_node_a])
    P30Aug_B   = pd.DataFrame(columns = [leak_node_b])
    V30Aug_pipe_1_US    = pd.DataFrame()
    V30Aug_pipe_1_DS    = pd.DataFrame()
    V30Aug_pipe_2_US    = pd.DataFrame()
    V30Aug_pipe_2_DS    = pd.DataFrame()
    Step      = pd.DataFrame(columns = ['Leak Step'])
    Step_list = []
    # RUN HYDRAULIC MODEL USING WNTR
    for i in np.arange (FS , LS , IS) : 
        'Delete the existing existing demand (leak) on the node'
        del junction_a.demand_timeseries_list[0]
        del junction_b.demand_timeseries_list[0]
        'Add new demand (leak) on the node based on the incremental step'
        junction_a.add_demand(base= i * 0.001, pattern_name='LeakPattern')
        junction_b.add_demand(base= i * 0.001, pattern_name='LeakPattern')
        'Simulate hydraulic model'
        sim = wntr.sim.EpanetSimulator(wn)
        results = sim.run_sim()
        'Store the leak step on data frame'
        Step_list.append(i)
        Step = pd.DataFrame(Step_list, columns=['Leak Step'])
        'Store the pressure on leak node on data frame'
        P30Aug_A_Pres_Temp = results.node['pressure'].loc[[3*3600],[leak_node_a]]
        P30Aug_A           = P30Aug_A.append(P30Aug_A_Pres_Temp, ignore_index=False)
        P30Aug_B_Pres_Temp = results.node['pressure'].loc[[3*3600],[leak_node_b]]
        P30Aug_B           = P30Aug_B.append(P30Aug_B_Pres_Temp, ignore_index=False)
        'Store the velocity on leak pipe on data frame'
        V30Aug_pipe_1_US_Temp = results.link['velocity'].loc[[3*3600],[pipe_1_node_US]]
        V30Aug_pipe_1_DS_Temp = results.link['velocity'].loc[[3*3600],[pipe_1_node_DS]]
        V30Aug_pipe_1_US      = V30Aug_pipe_1_US.append(V30Aug_pipe_1_US_Temp, ignore_index=False)
        V30Aug_pipe_1_DS      = V30Aug_pipe_1_DS.append(V30Aug_pipe_1_DS_Temp, ignore_index=False)
        
        V30Aug_pipe_2_US_Temp = results.link['velocity'].loc[[3*3600],[pipe_2_node_US]]
        V30Aug_pipe_2_DS_Temp = results.link['velocity'].loc[[3*3600],[pipe_2_node_DS]]
        V30Aug_pipe_2_US      = V30Aug_pipe_2_US.append(V30Aug_pipe_2_US_Temp, ignore_index=False)
        V30Aug_pipe_2_DS      = V30Aug_pipe_2_DS.append(V30Aug_pipe_2_DS_Temp, ignore_index=False)
    # MERGE PRESSURE AND LEAK STEP AS A DATAFRAME
    P30Aug_A['Leak Step'] = np.resize(Step,len(P30Aug_A))
    P30Aug_B['Leak Step'] = np.resize(Step,len(P30Aug_B))
    V30Aug_pipe_1_US['Leak Step'] = np.resize(Step,len(V30Aug_pipe_1_US))
    V30Aug_pipe_1_DS['Leak Step'] = np.resize(Step,len(V30Aug_pipe_1_DS))
    V30Aug_pipe_1 = pd.merge(V30Aug_pipe_1_US, V30Aug_pipe_1_DS, how='inner')
    V30Aug_pipe_1 = V30Aug_pipe_1[[pipe_1_node_US, pipe_1_node_DS, 'Leak Step']]
    
    V30Aug_pipe_2_US['Leak Step'] = np.resize(Step,len(V30Aug_pipe_2_US))
    V30Aug_pipe_2_DS['Leak Step'] = np.resize(Step,len(V30Aug_pipe_2_DS))
    V30Aug_pipe_2 = pd.merge(V30Aug_pipe_2_US, V30Aug_pipe_2_DS, how='inner')
    V30Aug_pipe_2 = V30Aug_pipe_2[[pipe_2_node_US, pipe_2_node_DS, 'Leak Step']]
Leak30August() # SUCESSFULY CROSS-CHECKED WITH EPANET RESULT

# LEAK ON SEPTEMBER 2022
def Leak5September() :
    '''
    In this function, we are trying to execute and record the stress on a 
    designated note based on some request values. The request value used refers
    to the First Step (FS), Last Step (LS), and Increment Step (IS) ranges.
    '''
    # LOAD HYDRAULIC MODEL FROM EPANET
    inp_file  = 'Hydraulic Model/September 2022/Leak - 5 September 2022.inp'
    wn        = wntr.network.WaterNetworkModel(inp_file)
    # SET NODE OF INTEREST 
    leak_node_a = 'L5/9/22(A)'
    leak_node_b = 'L5/9/22(B)'
    junction_a  = wn.get_node(leak_node_a)
    junction_b  = wn.get_node(leak_node_b)
    pipe_1_node_US = 'Conducta_1285(A)'
    pipe_1_node_DS = 'Conducta_1285(B)'
    pipe_2_node_US = 'Conducta_582(A)'
    pipe_2_node_DS = 'Conducta_582(B)'
    # SET LEAK DATAFRAME
    global P5Sep_A, P5Sep_B, V5Sep_pipe_1, V5Sep_pipe_2, Step
    P5Sep_A   = pd.DataFrame(columns = [leak_node_a])
    P5Sep_B   = pd.DataFrame(columns = [leak_node_b])
    V5Sep_pipe_1_US    = pd.DataFrame()
    V5Sep_pipe_1_DS    = pd.DataFrame()
    V5Sep_pipe_2_US    = pd.DataFrame()
    V5Sep_pipe_2_DS    = pd.DataFrame()
    Step      = pd.DataFrame(columns = ['Leak Step'])
    Step_list = []
    # RUN HYDRAULIC MODEL USING WNTR
    for i in np.arange (FS , LS , IS) : 
        'Delete the existing existing demand (leak) on the node'
        del junction_a.demand_timeseries_list[0]
        del junction_b.demand_timeseries_list[0]
        'Add new demand (leak) on the node based on the incremental step'
        junction_a.add_demand(base= i * 0.001, pattern_name='LeakPattern')
        junction_b.add_demand(base= i * 0.001, pattern_name='LeakPattern')
        'Simulate hydraulic model'
        sim = wntr.sim.EpanetSimulator(wn)
        results = sim.run_sim()
        'Store the leak step on data frame'
        Step_list.append(i)
        Step = pd.DataFrame(Step_list, columns=['Leak Step'])
        'Store the pressure on leak node on data frame'
        P5Sep_A_Pres_Temp = results.node['pressure'].loc[[3*3600],[leak_node_a]]
        P5Sep_A           = P5Sep_A.append(P5Sep_A_Pres_Temp, ignore_index=False)
        P5Sep_B_Pres_Temp = results.node['pressure'].loc[[3*3600],[leak_node_b]]
        P5Sep_B           = P5Sep_B.append(P5Sep_B_Pres_Temp, ignore_index=False)
        'Store the velocity on leak pipe on data frame'
        V5Sep_pipe_1_US_Temp = results.link['velocity'].loc[[3*3600],[pipe_1_node_US]]
        V5Sep_pipe_1_DS_Temp = results.link['velocity'].loc[[3*3600],[pipe_1_node_DS]]
        V5Sep_pipe_1_US      = V5Sep_pipe_1_US.append(V5Sep_pipe_1_US_Temp, ignore_index=False)
        V5Sep_pipe_1_DS      = V5Sep_pipe_1_DS.append(V5Sep_pipe_1_DS_Temp, ignore_index=False)
        
        V5Sep_pipe_2_US_Temp = results.link['velocity'].loc[[3*3600],[pipe_2_node_US]]
        V5Sep_pipe_2_DS_Temp = results.link['velocity'].loc[[3*3600],[pipe_2_node_DS]]
        V5Sep_pipe_2_US      = V5Sep_pipe_2_US.append(V5Sep_pipe_2_US_Temp, ignore_index=False)
        V5Sep_pipe_2_DS      = V5Sep_pipe_2_DS.append(V5Sep_pipe_2_DS_Temp, ignore_index=False)
    # MERGE PRESSURE AND LEAK STEP AS A DATAFRAME
    P5Sep_A['Leak Step'] = np.resize(Step,len(P5Sep_A))
    P5Sep_B['Leak Step'] = np.resize(Step,len(P5Sep_B))
    V5Sep_pipe_1_US['Leak Step'] = np.resize(Step,len(V5Sep_pipe_1_US))
    V5Sep_pipe_1_DS['Leak Step'] = np.resize(Step,len(V5Sep_pipe_1_DS))
    V5Sep_pipe_1 = pd.merge(V5Sep_pipe_1_US, V5Sep_pipe_1_DS, how='inner')
    V5Sep_pipe_1 = V5Sep_pipe_1[[pipe_1_node_US, pipe_1_node_DS, 'Leak Step']]
    
    V5Sep_pipe_2_US['Leak Step'] = np.resize(Step,len(V5Sep_pipe_2_US))
    V5Sep_pipe_2_DS['Leak Step'] = np.resize(Step,len(V5Sep_pipe_2_DS))
    V5Sep_pipe_2 = pd.merge(V5Sep_pipe_2_US, V5Sep_pipe_2_DS, how='inner')
    V5Sep_pipe_2 = V5Sep_pipe_2[[pipe_2_node_US, pipe_2_node_DS, 'Leak Step']]
Leak5September() # SUCESSFULY CROSS-CHECKED WITH EPANET RESULT
    
def Leak8September() : 
    '''
    In this function, we are trying to execute and record the stress on a 
    designated note based on some request values. The request value used refers
    to the First Step (FS), Last Step (LS), and Increment Step (IS) ranges.
    '''
    # LOAD HYDRAULIC MODEL FROM EPANET
    inp_file  = 'Hydraulic Model/September 2022/Leak - 8 September 2022.inp'
    wn        = wntr.network.WaterNetworkModel(inp_file)
    # SET NODE OF INTEREST 
    leak_node = 'L8/9/22'
    junction  = wn.get_node(leak_node)
    pipe_1_node_US = 'Conducta_1285(A)'
    pipe_1_node_DS = 'Conducta_1285(B)'
    # SET LEAK DATAFRAME
    global P8Sep, V8Sep_pipe_1, Step
    P8Sep     = pd.DataFrame(columns = [leak_node])
    V8Sep_pipe_1_US    = pd.DataFrame()
    V8Sep_pipe_1_DS    = pd.DataFrame()
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
        P8Sep_Pres_Temp = results.node['pressure'].loc[[3*3600],[leak_node]]
        P8Sep           = P8Sep.append(P8Sep_Pres_Temp, ignore_index=False)
        'Store the velocity on leak pipe on data frame'
        V8Sep_pipe_1_VelUS_Temp = results.link['velocity'].loc[[3*3600],[pipe_1_node_US]]
        V8Sep_pipe_1_VelDS_Temp = results.link['velocity'].loc[[3*3600],[pipe_1_node_DS]]
        V8Sep_pipe_1_US         = V8Sep_pipe_1_US.append(V8Sep_pipe_1_VelUS_Temp, ignore_index=False)
        V8Sep_pipe_1_DS         = V8Sep_pipe_1_DS.append(V8Sep_pipe_1_VelDS_Temp, ignore_index=False)
    # MERGE PRESSURE AND LEAK STEP AS A DATAFRAME
    P8Sep['Leak Step'] = np.resize(Step,len(P8Sep))
    V8Sep_pipe_1_US['Leak Step'] = np.resize(Step,len(V8Sep_pipe_1_US))
    V8Sep_pipe_1_DS['Leak Step'] = np.resize(Step,len(V8Sep_pipe_1_DS))
    V8Sep_pipe_1 = pd.merge(V8Sep_pipe_1_US, V8Sep_pipe_1_DS, how='inner')
    V8Sep_pipe_1 = V8Sep_pipe_1[[pipe_1_node_US, pipe_1_node_DS, 'Leak Step']]
Leak8September() # SUCESSFULY CROSS-CHECKED WITH EPANET RESULT
    
def Leak12September() : 
    '''
    In this function, we are trying to execute and record the stress on a 
    designated note based on some request values. The request value used refers
    to the First Step (FS), Last Step (LS), and Increment Step (IS) ranges.
    '''
    # LOAD HYDRAULIC MODEL FROM EPANET
    inp_file  = 'Hydraulic Model/September 2022/Leak - 12 September 2022.inp'
    wn        = wntr.network.WaterNetworkModel(inp_file)
    # SET NODE OF INTEREST 
    leak_node = 'L12/9/2022(A)'
    junction  = wn.get_node(leak_node)
    pipe_1_node_US = 'Conducta-1974(A)'
    pipe_1_node_DS = 'Conducta-1974(B)'
    # SET LEAK DATAFRAME
    global P12Sep,V12Sep_pipe_1, Step
    V12Sep_pipe_1_US    = pd.DataFrame()
    V12Sep_pipe_1_DS    = pd.DataFrame()
    P12Sep    = pd.DataFrame(columns = [leak_node])
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
        P12Sep_Pres_Temp = results.node['pressure'].loc[[3*3600],[leak_node]]
        P12Sep           = P12Sep.append(P12Sep_Pres_Temp, ignore_index=False)
        'Store the velocity on leak pipe on data frame'
        V12Sep_pipe_1_VelUS_Temp = results.link['velocity'].loc[[3*3600],[pipe_1_node_US]]
        V12Sep_pipe_1_VelDS_Temp = results.link['velocity'].loc[[3*3600],[pipe_1_node_DS]]
        V12Sep_pipe_1_US         = V12Sep_pipe_1_US.append(V12Sep_pipe_1_VelUS_Temp, ignore_index=False)
        V12Sep_pipe_1_DS         = V12Sep_pipe_1_DS.append(V12Sep_pipe_1_VelDS_Temp, ignore_index=False)
    # MERGE PRESSURE AND LEAK STEP AS A DATAFRAME
    P12Sep['Leak Step'] = np.resize(Step,len(P12Sep))
    V12Sep_pipe_1_US['Leak Step'] = np.resize(Step,len(V12Sep_pipe_1_US))
    V12Sep_pipe_1_DS['Leak Step'] = np.resize(Step,len(V12Sep_pipe_1_DS))
    V12Sep_pipe_1 = pd.merge(V12Sep_pipe_1_US, V12Sep_pipe_1_DS, how='inner')
    V12Sep_pipe_1 = V12Sep_pipe_1[[pipe_1_node_US, pipe_1_node_DS, 'Leak Step']]
Leak12September() # SUCESSFULY CROSS-CHECKED WITH EPANET RESULT

def Leak15September() : 
    '''
    In this function, we are trying to execute and record the stress on a 
    designated note based on some request values. The request value used refers
    to the First Step (FS), Last Step (LS), and Increment Step (IS) ranges.
    '''
    # LOAD HYDRAULIC MODEL FROM EPANET
    inp_file  = 'Hydraulic Model/September 2022/Leak - 15 September 2022.inp'
    wn        = wntr.network.WaterNetworkModel(inp_file)
    # SET NODE OF INTEREST 
    leak_node = 'L15/9/22(A)'
    junction  = wn.get_node(leak_node)
    pipe_1_node_US = 'Pipe-5(A)'
    pipe_1_node_DS = 'Pipe-5(B)'
    # SET LEAK DATAFRAME
    global P15Sep, V15Sep_pipe_1, Step
    P15Sep    = pd.DataFrame(columns = [leak_node])
    V15Sep_pipe_1_US    = pd.DataFrame()
    V15Sep_pipe_1_DS    = pd.DataFrame()
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
        P15Sep_Pres_Temp = results.node['pressure'].loc[[3*3600],[leak_node]]
        P15Sep           = P15Sep.append(P15Sep_Pres_Temp, ignore_index=False)
        'Store the velocity on leak pipe on data frame'
        V15Sep_pipe_1_VelUS_Temp = results.link['velocity'].loc[[3*3600],[pipe_1_node_US]]
        V15Sep_pipe_1_VelDS_Temp = results.link['velocity'].loc[[3*3600],[pipe_1_node_DS]]
        V15Sep_pipe_1_US         = V15Sep_pipe_1_US.append(V15Sep_pipe_1_VelUS_Temp, ignore_index=False)
        V15Sep_pipe_1_DS         = V15Sep_pipe_1_DS.append(V15Sep_pipe_1_VelDS_Temp, ignore_index=False)
    # MERGE PRESSURE AND LEAK STEP AS A DATAFRAME
    P15Sep['Leak Step'] = np.resize(Step,len(P15Sep))
    V15Sep_pipe_1_US['Leak Step'] = np.resize(Step,len(V15Sep_pipe_1_US))
    V15Sep_pipe_1_DS['Leak Step'] = np.resize(Step,len(V15Sep_pipe_1_DS))
    V15Sep_pipe_1 = pd.merge(V15Sep_pipe_1_US, V15Sep_pipe_1_DS, how='inner')
    V15Sep_pipe_1 = V15Sep_pipe_1[[pipe_1_node_US, pipe_1_node_DS, 'Leak Step']]
Leak15September() # SUCESSFULY CROSS-CHECKED WITH EPANET RESULT
    
def Leak21September() : 
    '''
    In this function, we are trying to execute and record the stress on a 
    designated note based on some request values. The request value used refers
    to the First Step (FS), Last Step (LS), and Increment Step (IS) ranges.
    '''
    # LOAD HYDRAULIC MODEL FROM EPANET
    inp_file  = 'Hydraulic Model/September 2022/Leak - 21 September 2022.inp'
    wn        = wntr.network.WaterNetworkModel(inp_file)
    # SET NODE OF INTEREST 
    leak_node = 'L21/9/22(A)'
    pipe_1_node_US = 'Conducta-2956(1)(2)(A)'
    pipe_1_node_DS = 'Conducta-2956(1)(2)(B)'
    junction  = wn.get_node(leak_node)
    # SET LEAK DATAFRAME
    global P21Sep, V21Sep_pipe_1, Step
    P21Sep    = pd.DataFrame(columns = [leak_node])
    V21Sep_pipe_1_US    = pd.DataFrame()
    V21Sep_pipe_1_DS    = pd.DataFrame()
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
        P21Sep_Pres_Temp = results.node['pressure'].loc[[3*3600],[leak_node]]
        P21Sep           = P21Sep.append(P21Sep_Pres_Temp, ignore_index=False)
        'Store the velocity on leak pipe on data frame'
        V21Sep_pipe_1_VelUS_Temp = results.link['velocity'].loc[[3*3600],[pipe_1_node_US]]
        V21Sep_pipe_1_VelDS_Temp = results.link['velocity'].loc[[3*3600],[pipe_1_node_DS]]
        V21Sep_pipe_1_US         = V21Sep_pipe_1_US.append(V21Sep_pipe_1_VelUS_Temp, ignore_index=False)
        V21Sep_pipe_1_DS         = V21Sep_pipe_1_DS.append(V21Sep_pipe_1_VelDS_Temp, ignore_index=False)
    # MERGE PRESSURE AND LEAK STEP AS A DATAFRAME
    P21Sep['Leak Step'] = np.resize(Step,len(P21Sep))
    V21Sep_pipe_1_US['Leak Step'] = np.resize(Step,len(V21Sep_pipe_1_US))
    V21Sep_pipe_1_DS['Leak Step'] = np.resize(Step,len(V21Sep_pipe_1_DS))
    V21Sep_pipe_1 = pd.merge(V21Sep_pipe_1_US, V21Sep_pipe_1_DS, how='inner')
    V21Sep_pipe_1 = V21Sep_pipe_1[[pipe_1_node_US, pipe_1_node_DS, 'Leak Step']]
Leak21September() # SUCESSFULY CROSS-CHECKED WITH EPANET RESULT

def Leak28September() :
    '''
    In this function, we are trying to execute and record the stress on a 
    designated note based on some request values. The request value used refers
    to the First Step (FS), Last Step (LS), and Increment Step (IS) ranges.
    '''
    # LOAD HYDRAULIC MODEL FROM EPANET
    inp_file  = 'Hydraulic Model/September 2022/Leak - 28 September 2022.inp'
    wn        = wntr.network.WaterNetworkModel(inp_file)
    # SET NODE OF INTEREST 
    leak_node_a = 'L28/9/22(A)'
    leak_node_b = 'L28/9/22(B)'
    junction_a  = wn.get_node(leak_node_a)
    junction_b  = wn.get_node(leak_node_b)
    pipe_1_node_US = 'Conducta-1298(A)'
    pipe_1_node_DS = 'Conducta-1298(B)'
    pipe_2_node_US = 'Conducta-837(A)'
    pipe_2_node_DS = 'Conducta-837(B)'
    # SET LEAK DATAFRAME
    global P28Sep_A, P28Sep_B, V28Sep_pipe_1, V28Sep_pipe_2, Step
    P28Sep_A  = pd.DataFrame(columns = [leak_node_a])
    P28Sep_B  = pd.DataFrame(columns = [leak_node_b])
    V28Sep_pipe_1_US    = pd.DataFrame()
    V28Sep_pipe_1_DS    = pd.DataFrame()
    V28Sep_pipe_2_US    = pd.DataFrame()
    V28Sep_pipe_2_DS    = pd.DataFrame()
    Step      = pd.DataFrame(columns = ['Leak Step'])
    Step_list = []
    # RUN HYDRAULIC MODEL USING WNTR
    for i in np.arange (FS , LS , IS) : 
        'Delete the existing existing demand (leak) on the node'
        del junction_a.demand_timeseries_list[0]
        del junction_b.demand_timeseries_list[0]
        'Add new demand (leak) on the node based on the incremental step'
        junction_a.add_demand(base= i * 0.001, pattern_name='LeakPattern')
        junction_b.add_demand(base= i * 0.001, pattern_name='LeakPattern')
        'Simulate hydraulic model'
        sim = wntr.sim.EpanetSimulator(wn)
        results = sim.run_sim()
        'Store the leak step on data frame'
        Step_list.append(i)
        Step = pd.DataFrame(Step_list, columns=['Leak Step'])
        'Store the pressure on leak node on data frame'
        P28Sep_A_Pres_Temp = results.node['pressure'].loc[[3*3600],[leak_node_a]]
        P28Sep_A           = P28Sep_A.append(P28Sep_A_Pres_Temp, ignore_index=False)
        P28Sep_B_Pres_Temp = results.node['pressure'].loc[[3*3600],[leak_node_b]]
        P28Sep_B           = P28Sep_B.append(P28Sep_B_Pres_Temp, ignore_index=False)
        'Store the velocity on leak pipe on data frame'
        V28Sep_pipe_1_US_Temp = results.link['velocity'].loc[[3*3600],[pipe_1_node_US]]
        V28Sep_pipe_1_DS_Temp = results.link['velocity'].loc[[3*3600],[pipe_1_node_DS]]
        V28Sep_pipe_1_US      = V28Sep_pipe_1_US.append(V28Sep_pipe_1_US_Temp, ignore_index=False)
        V28Sep_pipe_1_DS      = V28Sep_pipe_1_DS.append(V28Sep_pipe_1_DS_Temp, ignore_index=False)
        
        V28Sep_pipe_2_US_Temp = results.link['velocity'].loc[[3*3600],[pipe_2_node_US]]
        V28Sep_pipe_2_DS_Temp = results.link['velocity'].loc[[3*3600],[pipe_2_node_DS]]
        V28Sep_pipe_2_US      = V28Sep_pipe_2_US.append(V28Sep_pipe_2_US_Temp, ignore_index=False)
        V28Sep_pipe_2_DS      = V28Sep_pipe_2_DS.append(V28Sep_pipe_2_DS_Temp, ignore_index=False)
    # MERGE PRESSURE AND LEAK STEP AS A DATAFRAME
    P28Sep_A['Leak Step'] = np.resize(Step,len(P28Sep_A))
    P28Sep_B['Leak Step'] = np.resize(Step,len(P28Sep_B))
    V28Sep_pipe_1_US['Leak Step'] = np.resize(Step,len(V28Sep_pipe_1_US))
    V28Sep_pipe_1_DS['Leak Step'] = np.resize(Step,len(V28Sep_pipe_1_DS))
    V28Sep_pipe_1 = pd.merge(V28Sep_pipe_1_US, V28Sep_pipe_1_DS, how='inner')
    V28Sep_pipe_1 = V28Sep_pipe_1[[pipe_1_node_US, pipe_1_node_DS, 'Leak Step']]
    
    V28Sep_pipe_2_US['Leak Step'] = np.resize(Step,len(V28Sep_pipe_2_US))
    V28Sep_pipe_2_DS['Leak Step'] = np.resize(Step,len(V28Sep_pipe_2_DS))
    V28Sep_pipe_2 = pd.merge(V28Sep_pipe_2_US, V28Sep_pipe_2_DS, how='inner')
    V28Sep_pipe_2 = V28Sep_pipe_2[[pipe_2_node_US, pipe_2_node_DS, 'Leak Step']]
Leak28September() # SUCESSFULY CROSS-CHECKED WITH EPANET RESULT
    
def Leak30September() :
    '''
    In this function, we are trying to execute and record the stress on a 
    designated note based on some request values. The request value used refers
    to the First Step (FS), Last Step (LS), and Increment Step (IS) ranges.
    '''
    # LOAD HYDRAULIC MODEL FROM EPANET
    inp_file  = 'Hydraulic Model/September 2022/Leak - 30 September 2022.inp'
    wn        = wntr.network.WaterNetworkModel(inp_file)
    # SET NODE OF INTEREST 
    leak_node_a = 'L30/9/22(A)'
    leak_node_b = 'L30/9/22(B)'
    pipe_1_node_US = 'Conducta-1298(A)'
    pipe_1_node_DS = 'Conducta-1298(B)'
    pipe_2_node_US = 'Conducta-11947(A)'
    pipe_2_node_DS = 'Conducta-11947(B)'
    junction_a  = wn.get_node(leak_node_a)
    junction_b  = wn.get_node(leak_node_b)
    # SET LEAK DATAFRAME
    global P30Sep_A, P30Sep_B, V30Sep_pipe_1, V30Sep_pipe_2, Step
    P30Sep_A  = pd.DataFrame(columns = [leak_node_a])
    P30Sep_B  = pd.DataFrame(columns = [leak_node_b])
    V30Sep_pipe_1_US    = pd.DataFrame()
    V30Sep_pipe_1_DS    = pd.DataFrame()
    V30Sep_pipe_2_US    = pd.DataFrame()
    V30Sep_pipe_2_DS    = pd.DataFrame()
    Step      = pd.DataFrame(columns = ['Leak Step'])
    Step_list = []
    # RUN HYDRAULIC MODEL USING WNTR
    for i in np.arange (FS , LS , IS) : 
        'Delete the existing existing demand (leak) on the node'
        del junction_a.demand_timeseries_list[0]
        del junction_b.demand_timeseries_list[0]
        'Add new demand (leak) on the node based on the incremental step'
        junction_a.add_demand(base= i * 0.001, pattern_name='LeakPattern')
        junction_b.add_demand(base= i * 0.001, pattern_name='LeakPattern')
        'Simulate hydraulic model'
        sim = wntr.sim.EpanetSimulator(wn)
        results = sim.run_sim()
        'Store the leak step on data frame'
        Step_list.append(i)
        Step = pd.DataFrame(Step_list, columns=['Leak Step'])
        'Store the pressure on leak node on data frame'
        P30Sep_A_Pres_Temp = results.node['pressure'].loc[[3*3600],[leak_node_a]]
        P30Sep_A           = P30Sep_A.append(P30Sep_A_Pres_Temp, ignore_index=False)
        P30Sep_B_Pres_Temp = results.node['pressure'].loc[[3*3600],[leak_node_b]]
        P30Sep_B           = P30Sep_B.append(P30Sep_B_Pres_Temp, ignore_index=False)
        'Store the velocity on leak pipe on data frame'
        V30Sep_pipe_1_US_Temp = results.link['velocity'].loc[[3*3600],[pipe_1_node_US]]
        V30Sep_pipe_1_DS_Temp = results.link['velocity'].loc[[3*3600],[pipe_1_node_DS]]
        V30Sep_pipe_1_US      = V30Sep_pipe_1_US.append(V30Sep_pipe_1_US_Temp, ignore_index=False)
        V30Sep_pipe_1_DS      = V30Sep_pipe_1_DS.append(V30Sep_pipe_1_DS_Temp, ignore_index=False)
        
        V30Sep_pipe_2_US_Temp = results.link['velocity'].loc[[3*3600],[pipe_2_node_US]]
        V30Sep_pipe_2_DS_Temp = results.link['velocity'].loc[[3*3600],[pipe_2_node_DS]]
        V30Sep_pipe_2_US      = V30Sep_pipe_2_US.append(V30Sep_pipe_2_US_Temp, ignore_index=False)
        V30Sep_pipe_2_DS      = V30Sep_pipe_2_DS.append(V30Sep_pipe_2_DS_Temp, ignore_index=False)
    # MERGE PRESSURE AND LEAK STEP AS A DATAFRAME
    P30Sep_A['Leak Step'] = np.resize(Step,len(P30Sep_A))
    P30Sep_B['Leak Step'] = np.resize(Step,len(P30Sep_B))
    V30Sep_pipe_1_US['Leak Step'] = np.resize(Step,len(V30Sep_pipe_1_US))
    V30Sep_pipe_1_DS['Leak Step'] = np.resize(Step,len(V30Sep_pipe_1_DS))
    V30Sep_pipe_1 = pd.merge(V30Sep_pipe_1_US, V30Sep_pipe_1_DS, how='inner')
    V30Sep_pipe_1 = V30Sep_pipe_1[[pipe_1_node_US, pipe_1_node_DS, 'Leak Step']]
    
    V30Sep_pipe_2_US['Leak Step'] = np.resize(Step,len(V30Sep_pipe_2_US))
    V30Sep_pipe_2_DS['Leak Step'] = np.resize(Step,len(V30Sep_pipe_2_DS))
    V30Sep_pipe_2 = pd.merge(V30Sep_pipe_2_US, V30Sep_pipe_2_DS, how='inner')
    V30Sep_pipe_2 = V30Sep_pipe_2[[pipe_2_node_US, pipe_2_node_DS, 'Leak Step']]
Leak30September() # SUCESSFULY CROSS-CHECKED WITH EPANET RESULT

# LEAK ON OCTOBER 2022
def Leak27October() : 
    '''
    In this function, we are trying to execute and record the stress on a 
    designated note based on some request values. The request value used refers
    to the First Step (FS), Last Step (LS), and Increment Step (IS) ranges.
    '''
    # LOAD HYDRAULIC MODEL FROM EPANET
    inp_file  = 'Hydraulic Model/October 2022/Leak - 27 October 2022.inp'
    wn        = wntr.network.WaterNetworkModel(inp_file)
    # SET NODE OF INTEREST 
    leak_node = 'L27/10/22'
    junction  = wn.get_node(leak_node)
    pipe_1_node_US = 'Conducta-1294(A)'
    pipe_1_node_DS = 'Conducta-1294(B)'
    # SET LEAK DATAFRAME
    global P27Oct, V27Oct_pipe_1, Step
    P27Oct    = pd.DataFrame(columns = [leak_node])
    V27Oct_pipe_1_US    = pd.DataFrame()
    V27Oct_pipe_1_DS    = pd.DataFrame()
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
        P27Oct_Pres_Temp = results.node['pressure'].loc[[3*3600],[leak_node]]
        P27Oct           = P27Oct.append(P27Oct_Pres_Temp, ignore_index=False)
        'Store the velocity on leak pipe on data frame'
        V27Oct_pipe_1_VelUS_Temp = results.link['velocity'].loc[[3*3600],[pipe_1_node_US]]
        V27Oct_pipe_1_VelDS_Temp = results.link['velocity'].loc[[3*3600],[pipe_1_node_DS]]
        V27Oct_pipe_1_US         = V27Oct_pipe_1_US.append(V27Oct_pipe_1_VelUS_Temp, ignore_index=False)
        V27Oct_pipe_1_DS         = V27Oct_pipe_1_DS.append(V27Oct_pipe_1_VelDS_Temp, ignore_index=False)
    # MERGE PRESSURE AND LEAK STEP AS A DATAFRAME
    P27Oct['Leak Step'] = np.resize(Step,len(P27Oct))
    V27Oct_pipe_1_US['Leak Step'] = np.resize(Step,len(V27Oct_pipe_1_US))
    V27Oct_pipe_1_DS['Leak Step'] = np.resize(Step,len(V27Oct_pipe_1_DS))
    V27Oct_pipe_1 = pd.merge(V27Oct_pipe_1_US, V27Oct_pipe_1_DS, how='inner')
    V27Oct_pipe_1 = V27Oct_pipe_1[[pipe_1_node_US, pipe_1_node_DS, 'Leak Step']]
Leak27October() # SUCESSFULY CROSS-CHECKED WITH EPANET RESULT

#  LEAK ON NOVERMBER 2022
def Leak4November() : 
    '''
    In this function, we are trying to execute and record the stress on a 
    designated note based on some request values. The request value used refers
    to the First Step (FS), Last Step (LS), and Increment Step (IS) ranges.
    '''
    # LOAD HYDRAULIC MODEL FROM EPANET
    inp_file  = 'Hydraulic Model/November 2022/Leak - 4 November 2022.inp'
    wn        = wntr.network.WaterNetworkModel(inp_file)
    # SET NODE OF INTEREST 
    leak_node = 'L4/11/22'
    junction  = wn.get_node(leak_node)
    pipe_1_node_US = 'Conducta-2955(A)'
    pipe_1_node_DS = 'Conducta-2955(B)'
    # SET LEAK DATAFRAME
    global P4Nov, V4Nov_pipe_1, Step
    V4Nov_pipe_1_US    = pd.DataFrame()
    V4Nov_pipe_1_DS    = pd.DataFrame()
    P4Nov     = pd.DataFrame(columns = [leak_node])
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
        P4Nov_Pres_Temp = results.node['pressure'].loc[[3*3600],[leak_node]]
        P4Nov           = P4Nov.append(P4Nov_Pres_Temp, ignore_index=False)
        'Store the velocity on leak pipe on data frame'
        V4Nov_pipe_1_VelUS_Temp = results.link['velocity'].loc[[3*3600],[pipe_1_node_US]]
        V4Nov_pipe_1_VelDS_Temp = results.link['velocity'].loc[[3*3600],[pipe_1_node_DS]]
        V4Nov_pipe_1_US         = V4Nov_pipe_1_US.append(V4Nov_pipe_1_VelUS_Temp, ignore_index=False)
        V4Nov_pipe_1_DS         = V4Nov_pipe_1_DS.append(V4Nov_pipe_1_VelDS_Temp, ignore_index=False)
    # MERGE PRESSURE AND LEAK STEP AS A DATAFRAME
    P4Nov['Leak Step'] = np.resize(Step,len(P4Nov))
    V4Nov_pipe_1_US['Leak Step'] = np.resize(Step,len(V4Nov_pipe_1_US))
    V4Nov_pipe_1_DS['Leak Step'] = np.resize(Step,len(V4Nov_pipe_1_DS))
    V4Nov_pipe_1 = pd.merge(V4Nov_pipe_1_US, V4Nov_pipe_1_DS, how='inner')
    V4Nov_pipe_1 = V4Nov_pipe_1[[pipe_1_node_US, pipe_1_node_DS, 'Leak Step']]
Leak4November() # SUCESSFULY CROSS-CHECKED WITH EPANET RESULT

def Leak8November() : 
    '''
    In this function, we are trying to execute and record the stress on a 
    designated note based on some request values. The request value used refers
    to the First Step (FS), Last Step (LS), and Increment Step (IS) ranges.
    '''
    # LOAD HYDRAULIC MODEL FROM EPANET
    inp_file  = 'Hydraulic Model/November 2022/Leak - 8 November 2022.inp'
    wn        = wntr.network.WaterNetworkModel(inp_file)
    # SET NODE OF INTEREST 
    leak_node = 'L8/11/22'
    junction  = wn.get_node(leak_node)
    pipe_1_node_US = 'Pipe-1296(A)'
    pipe_1_node_DS = 'Conducta-1296(B)'
    # SET LEAK DATAFRAME
    global P8Nov, V8Nov_pipe_1, Step
    P8Nov     = pd.DataFrame(columns = [leak_node])
    V8Nov_pipe_1_US    = pd.DataFrame()
    V8Nov_pipe_1_DS    = pd.DataFrame()
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
        P8Nov_Pres_Temp = results.node['pressure'].loc[[3*3600],[leak_node]]
        P8Nov           = P8Nov.append(P8Nov_Pres_Temp, ignore_index=False)
        'Store the velocity on leak pipe on data frame'
        V8Nov_pipe_1_VelUS_Temp = results.link['velocity'].loc[[3*3600],[pipe_1_node_US]]
        V8Nov_pipe_1_VelDS_Temp = results.link['velocity'].loc[[3*3600],[pipe_1_node_DS]]
        V8Nov_pipe_1_US         = V8Nov_pipe_1_US.append(V8Nov_pipe_1_VelUS_Temp, ignore_index=False)
        V8Nov_pipe_1_DS         = V8Nov_pipe_1_DS.append(V8Nov_pipe_1_VelDS_Temp, ignore_index=False)
    # MERGE PRESSURE AND LEAK STEP AS A DATAFRAME
    P8Nov['Leak Step'] = np.resize(Step,len(P8Nov))
    V8Nov_pipe_1_US['Leak Step'] = np.resize(Step,len(V8Nov_pipe_1_US))
    V8Nov_pipe_1_DS['Leak Step'] = np.resize(Step,len(V8Nov_pipe_1_DS))
    V8Nov_pipe_1 = pd.merge(V8Nov_pipe_1_US, V8Nov_pipe_1_DS, how='inner')
    V8Nov_pipe_1 = V8Nov_pipe_1[[pipe_1_node_US, pipe_1_node_DS, 'Leak Step']]
Leak8November() # SUCESSFULY CROSS-CHECKED WITH EPANET RESULT

#  RUN MODEL
def run_hydraulic_model() : 
    Leak26May()
    Leak10June()
    Leak29June()
    Leak4July()
    Leak7July()
    Leak12July()
    Leak21July()
    Leak26July() 
    Leak28July()
    Leak19August()
    Leak22August()
    Leak23August()
    Leak26August() 
    Leak30August()
    Leak5September()
    Leak8September()
    Leak12September()
    Leak15September()
    Leak21September()
    Leak28September()
    Leak30September()
    Leak27October()
    Leak4November()
    Leak8November()
    #  MERGE ALL DATAFRAMES TO ONE DATAFRAME
    global HM_P_df, HM_P_Transposed
    HM_P_List = [P26May, P10Jun, P29Jun, P4Jul, P7Jul_A, P7Jul_B, P12Jul_A, P12Jul_B, P12Jul_D, 
               P21Jul_A, P21Jul_B, P26Jul, P28Jul_A, P28Jul_B, P19Aug, P22Aug, P23Aug_A, P23Aug_B,
               P26Aug, P30Aug_A, P30Aug_B, P5Sep_A, P5Sep_B, P8Sep, P12Sep, P15Sep, P21Sep,P28Sep_A, P28Sep_B, 
               P30Sep_A, P30Sep_B, P27Oct, P4Nov, P8Nov]
    HM_P_df   = reduce(lambda  left,right: pd.merge(left,right,on=['Leak Step'],how='outer'),HM_P_List)
    #  REORDER MERGED DATAFRAMES
    LeakStep_Val = HM_P_df['Leak Step']
    HM_P_df = HM_P_df.drop(columns=['Leak Step'])
    HM_P_df.insert(loc=0, column='Leak Step', value=LeakStep_Val)
    HM_P_Transposed = HM_P_df.T
    
    global HM_V_df, HM_V_Transposed
    HM_V_List = [V26May_pipe_1, V10Jun_pipe_1, V29Jun_pipe_1, V4Jul_pipe_1, V7Jul_pipe_1, V7Jul_pipe_2, 
                 V12Jul_pipe_1, V12Jul_pipe_2, V12Jul_pipe_3, V21Jul_pipe_1, V21Jul_pipe_2, V26Jul_pipe_1, 
                 V28Jul_pipe_1, V28Jul_pipe_2, V19Aug_pipe_1, V22Aug_pipe_1, V23Aug_pipe_1, V23Aug_pipe_2, 
                 V26Aug_pipe_1, V30Aug_pipe_1, V30Aug_pipe_2, V5Sep_pipe_1, V5Sep_pipe_2, V8Sep_pipe_1, 
                 V12Sep_pipe_1, V15Sep_pipe_1, V21Sep_pipe_1, V28Sep_pipe_1, V28Sep_pipe_2, V30Sep_pipe_1, 
                 V30Sep_pipe_2, V27Oct_pipe_1, V4Nov_pipe_1, V8Nov_pipe_1]
    HM_V_df   = reduce(lambda  left,right: pd.merge(left,right,on=['Leak Step'],how='outer'),HM_V_List)
    #  REORDER MERGED DATAFRAMES
    LeakStep_Val = HM_V_df['Leak Step']
    HM_V_df = HM_V_df.drop(columns=['Leak Step'])
    HM_V_df.insert(loc=0, column='Leak Step', value=LeakStep_Val)
    HM_V_Transposed = HM_V_df.T

run_hydraulic_model() 

# SAVE NEW DATAFRAME TO CSV
HM_P_Transposed.to_csv('Leak Pressure on Node Record.csv')
HM_V_Transposed.to_csv('Leak Velocity on Pipe Record.csv')