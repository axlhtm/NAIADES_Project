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
FS = 0.125 
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
    # SET LEAK DATAFRAME
    global L26May, Step
    L26May    = pd.DataFrame(columns = [leak_node])
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
        L26May_Pres_Temp = results.node['pressure'].loc[[3*3600],[leak_node]]
        L26May           = L26May.append(L26May_Pres_Temp, ignore_index=False)
    # MERGE PRESSURE AND LEAK STEP AS A DATAFRAME
    L26May['Leak Step'] = np.resize(Step,len(L26May))

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
    # SET LEAK DATAFRAME
    global L10Jun, Step
    L10Jun    = pd.DataFrame(columns = [leak_node])
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
        L10Jun_Pres_Temp = results.node['pressure'].loc[[3*3600],[leak_node]]
        L10Jun           = L10Jun.append(L10Jun_Pres_Temp, ignore_index=False)
    # MERGE PRESSURE AND LEAK STEP AS A DATAFRAME
    L10Jun['Leak Step'] = np.resize(Step,len(L10Jun))
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
    # SET LEAK DATAFRAME
    global L29Jun, Step
    L29Jun    = pd.DataFrame(columns = [leak_node])
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
        L29Jun_Pres_Temp = results.node['pressure'].loc[[3*3600],[leak_node]]
        L29Jun           = L29Jun.append(L29Jun_Pres_Temp, ignore_index=False)
    # MERGE PRESSURE AND LEAK STEP AS A DATAFRAME
    L29Jun['Leak Step'] = np.resize(Step,len(L29Jun))

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
    # SET LEAK DATAFRAME
    global L4Jul, Step
    L4Jul    = pd.DataFrame(columns = [leak_node])
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
        L4Jul_Pres_Temp = results.node['pressure'].loc[[3*3600],[leak_node]]
        L4Jul           = L4Jul.append(L4Jul_Pres_Temp, ignore_index=False)
    # MERGE PRESSURE AND LEAK STEP AS A DATAFRAME
    L4Jul['Leak Step'] = np.resize(Step,len(L4Jul))
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
    # SET LEAK DATAFRAME
    global L7Jul_A, L7Jul_B, Step
    L7Jul_A   = pd.DataFrame(columns = [leak_node_a])
    L7Jul_B   = pd.DataFrame(columns = [leak_node_b])
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
        L7Jul_A_Pres_Temp = results.node['pressure'].loc[[3*3600],[leak_node_a]]
        L7Jul_A           = L7Jul_A.append(L7Jul_A_Pres_Temp, ignore_index=False)
        L7Jul_B_Pres_Temp = results.node['pressure'].loc[[3*3600],[leak_node_b]]
        L7Jul_B           = L7Jul_B.append(L7Jul_B_Pres_Temp, ignore_index=False)
    # MERGE PRESSURE AND LEAK STEP AS A DATAFRAME
    L7Jul_A['Leak Step'] = np.resize(Step,len(L7Jul_A))
    L7Jul_B['Leak Step'] = np.resize(Step,len(L7Jul_B))
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
    # SET LEAK DATAFRAME
    global L12Jul_A, L12Jul_B, L12Jul_D, Step
    L12Jul_A   = pd.DataFrame(columns = [leak_node_a])
    L12Jul_B   = pd.DataFrame(columns = [leak_node_b])
    L12Jul_D   = pd.DataFrame(columns = [leak_node_d])
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
        L12Jul_A_Pres_Temp = results.node['pressure'].loc[[3*3600],[leak_node_a]]
        L12Jul_A           = L12Jul_A.append(L12Jul_A_Pres_Temp, ignore_index=False)
        L12Jul_B_Pres_Temp = results.node['pressure'].loc[[3*3600],[leak_node_b]]
        L12Jul_B           = L12Jul_B.append(L12Jul_B_Pres_Temp, ignore_index=False)
        L12Jul_D_Pres_Temp = results.node['pressure'].loc[[3*3600],[leak_node_d]]
        L12Jul_D           = L12Jul_D.append(L12Jul_D_Pres_Temp, ignore_index=False)
    # MERGE PRESSURE AND LEAK STEP AS A DATAFRAME
    L12Jul_A['Leak Step'] = np.resize(Step,len(L12Jul_A))
    L12Jul_B['Leak Step'] = np.resize(Step,len(L12Jul_B))
    L12Jul_D['Leak Step'] = np.resize(Step,len(L12Jul_D))
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
    # SET LEAK DATAFRAME
    global L21Jul_A, L21Jul_B, Step
    L21Jul_A   = pd.DataFrame(columns = [leak_node_a])
    L21Jul_B   = pd.DataFrame(columns = [leak_node_b])
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
        L21Jul_A_Pres_Temp = results.node['pressure'].loc[[3*3600],[leak_node_a]]
        L21Jul_A           = L21Jul_A.append(L21Jul_A_Pres_Temp, ignore_index=False)
        L21Jul_B_Pres_Temp = results.node['pressure'].loc[[3*3600],[leak_node_b]]
        L21Jul_B           = L21Jul_B.append(L21Jul_B_Pres_Temp, ignore_index=False)
    # MERGE PRESSURE AND LEAK STEP AS A DATAFRAME
    L21Jul_A['Leak Step'] = np.resize(Step,len(L21Jul_A))
    L21Jul_B['Leak Step'] = np.resize(Step,len(L21Jul_B))
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
    # SET LEAK DATAFRAME
    global L26Jul, Step
    L26Jul    = pd.DataFrame(columns = [leak_node])
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
        L26Jul_Pres_Temp = results.node['pressure'].loc[[3*3600],[leak_node]]
        L26Jul           = L26Jul.append(L26Jul_Pres_Temp, ignore_index=False)
    # MERGE PRESSURE AND LEAK STEP AS A DATAFRAME
    L26Jul['Leak Step'] = np.resize(Step,len(L26Jul))
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
    # SET LEAK DATAFRAME
    global L28Jul_A, L28Jul_B, Step
    L28Jul_A   = pd.DataFrame(columns = [leak_node_a])
    L28Jul_B   = pd.DataFrame(columns = [leak_node_b])
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
        L28Jul_A_Pres_Temp = results.node['pressure'].loc[[3*3600],[leak_node_a]]
        L28Jul_A           = L28Jul_A.append(L28Jul_A_Pres_Temp, ignore_index=False)
        L28Jul_B_Pres_Temp = results.node['pressure'].loc[[3*3600],[leak_node_b]]
        L28Jul_B           = L28Jul_B.append(L28Jul_B_Pres_Temp, ignore_index=False)
    # MERGE PRESSURE AND LEAK STEP AS A DATAFRAME
    L28Jul_A['Leak Step'] = np.resize(Step,len(L28Jul_A))
    L28Jul_B['Leak Step'] = np.resize(Step,len(L28Jul_B))

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
    # SET LEAK DATAFRAME
    global L19Aug, Step
    L19Aug    = pd.DataFrame(columns = [leak_node])
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
        L19Aug_Pres_Temp = results.node['pressure'].loc[[3*3600],[leak_node]]
        L19Aug           = L19Aug.append(L19Aug_Pres_Temp, ignore_index=False)
    # MERGE PRESSURE AND LEAK STEP AS A DATAFRAME
    L19Aug['Leak Step'] = np.resize(Step,len(L19Aug))
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
    # SET LEAK DATAFRAME
    global L22Aug, Step
    L22Aug    = pd.DataFrame(columns = [leak_node])
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
        L22Aug_Pres_Temp = results.node['pressure'].loc[[3*3600],[leak_node]]
        L22Aug           = L22Aug.append(L22Aug_Pres_Temp, ignore_index=False)
    # MERGE PRESSURE AND LEAK STEP AS A DATAFRAME
    L22Aug['Leak Step'] = np.resize(Step,len(L22Aug))
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
    # SET LEAK DATAFRAME
    global L23Aug_A, L23Aug_B, Step
    L23Aug_A   = pd.DataFrame(columns = [leak_node_a])
    L23Aug_B   = pd.DataFrame(columns = [leak_node_b])
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
        L23Aug_A_Pres_Temp = results.node['pressure'].loc[[3*3600],[leak_node_a]]
        L23Aug_A           = L23Aug_A.append(L23Aug_A_Pres_Temp, ignore_index=False)
        L23Aug_B_Pres_Temp = results.node['pressure'].loc[[3*3600],[leak_node_b]]
        L23Aug_B           = L23Aug_B.append(L23Aug_B_Pres_Temp, ignore_index=False)
    # MERGE PRESSURE AND LEAK STEP AS A DATAFRAME
    L23Aug_A['Leak Step'] = np.resize(Step,len(L23Aug_A))
    L23Aug_B['Leak Step'] = np.resize(Step,len(L23Aug_B))
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
    # SET LEAK DATAFRAME
    global L26Aug, Step
    L26Aug    = pd.DataFrame(columns = [leak_node])
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
        L26Aug_Pres_Temp = results.node['pressure'].loc[[3*3600],[leak_node]]
        L26Aug           = L26Aug.append(L26Aug_Pres_Temp, ignore_index=False)
    # MERGE PRESSURE AND LEAK STEP AS A DATAFRAME
    L26Aug['Leak Step'] = np.resize(Step,len(L26Aug))
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
    # SET LEAK DATAFRAME
    global L30Aug_A, L30Aug_B, Step
    L30Aug_A   = pd.DataFrame(columns = [leak_node_a])
    L30Aug_B   = pd.DataFrame(columns = [leak_node_b])
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
        L30Aug_A_Pres_Temp = results.node['pressure'].loc[[3*3600],[leak_node_a]]
        L30Aug_A           = L30Aug_A.append(L30Aug_A_Pres_Temp, ignore_index=False)
        L30Aug_B_Pres_Temp = results.node['pressure'].loc[[3*3600],[leak_node_b]]
        L30Aug_B           = L30Aug_B.append(L30Aug_B_Pres_Temp, ignore_index=False)
    # MERGE PRESSURE AND LEAK STEP AS A DATAFRAME
    L30Aug_A['Leak Step'] = np.resize(Step,len(L30Aug_A))
    L30Aug_B['Leak Step'] = np.resize(Step,len(L30Aug_B))

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
    # SET LEAK DATAFRAME
    global L5Sep_A, L5Sep_B, Step
    L5Sep_A   = pd.DataFrame(columns = [leak_node_a])
    L5Sep_B   = pd.DataFrame(columns = [leak_node_b])
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
        L5Sep_A_Pres_Temp = results.node['pressure'].loc[[3*3600],[leak_node_a]]
        L5Sep_A           = L5Sep_A.append(L5Sep_A_Pres_Temp, ignore_index=False)
        L5Sep_B_Pres_Temp = results.node['pressure'].loc[[3*3600],[leak_node_b]]
        L5Sep_B           = L5Sep_B.append(L5Sep_B_Pres_Temp, ignore_index=False)
    # MERGE PRESSURE AND LEAK STEP AS A DATAFRAME
    L5Sep_A['Leak Step'] = np.resize(Step,len(L5Sep_A))
    L5Sep_B['Leak Step'] = np.resize(Step,len(L5Sep_B))
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
    # SET LEAK DATAFRAME
    global L8Sep, Step
    L8Sep     = pd.DataFrame(columns = [leak_node])
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
        L8Sep_Pres_Temp = results.node['pressure'].loc[[3*3600],[leak_node]]
        L8Sep           = L8Sep.append(L8Sep_Pres_Temp, ignore_index=False)
    # MERGE PRESSURE AND LEAK STEP AS A DATAFRAME
    L8Sep['Leak Step'] = np.resize(Step,len(L8Sep))
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
    # SET LEAK DATAFRAME
    global L12Sep, Step
    L12Sep    = pd.DataFrame(columns = [leak_node])
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
        L12Sep_Pres_Temp = results.node['pressure'].loc[[3*3600],[leak_node]]
        L12Sep           = L12Sep.append(L12Sep_Pres_Temp, ignore_index=False)
    # MERGE PRESSURE AND LEAK STEP AS A DATAFRAME
    L12Sep['Leak Step'] = np.resize(Step,len(L12Sep))
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
    # SET LEAK DATAFRAME
    global L15Sep, Step
    L15Sep    = pd.DataFrame(columns = [leak_node])
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
        L15Sep_Pres_Temp = results.node['pressure'].loc[[3*3600],[leak_node]]
        L15Sep           = L15Sep.append(L15Sep_Pres_Temp, ignore_index=False)
    # MERGE PRESSURE AND LEAK STEP AS A DATAFRAME
    L15Sep['Leak Step'] = np.resize(Step,len(L15Sep))
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
    junction  = wn.get_node(leak_node)
    # SET LEAK DATAFRAME
    global L21Sep, Step
    L21Sep    = pd.DataFrame(columns = [leak_node])
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
        L21Sep_Pres_Temp = results.node['pressure'].loc[[3*3600],[leak_node]]
        L21Sep           = L21Sep.append(L21Sep_Pres_Temp, ignore_index=False)
    # MERGE PRESSURE AND LEAK STEP AS A DATAFRAME
    L21Sep['Leak Step'] = np.resize(Step,len(L21Sep))
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
    # SET LEAK DATAFRAME
    global L28Sep_A, L28Sep_B, Step
    L28Sep_A  = pd.DataFrame(columns = [leak_node_a])
    L28Sep_B  = pd.DataFrame(columns = [leak_node_b])
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
        L28Sep_A_Pres_Temp = results.node['pressure'].loc[[3*3600],[leak_node_a]]
        L28Sep_A           = L28Sep_A.append(L28Sep_A_Pres_Temp, ignore_index=False)
        L28Sep_B_Pres_Temp = results.node['pressure'].loc[[3*3600],[leak_node_b]]
        L28Sep_B           = L28Sep_B.append(L28Sep_B_Pres_Temp, ignore_index=False)
    # MERGE PRESSURE AND LEAK STEP AS A DATAFRAME
    L28Sep_A['Leak Step'] = np.resize(Step,len(L28Sep_A))
    L28Sep_B['Leak Step'] = np.resize(Step,len(L28Sep_B))
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
    junction_a  = wn.get_node(leak_node_a)
    junction_b  = wn.get_node(leak_node_b)
    # SET LEAK DATAFRAME
    global L30Sep_A, L30Sep_B, Step
    L30Sep_A  = pd.DataFrame(columns = [leak_node_a])
    L30Sep_B  = pd.DataFrame(columns = [leak_node_b])
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
        L30Sep_A_Pres_Temp = results.node['pressure'].loc[[3*3600],[leak_node_a]]
        L30Sep_A           = L30Sep_A.append(L30Sep_A_Pres_Temp, ignore_index=False)
        L30Sep_B_Pres_Temp = results.node['pressure'].loc[[3*3600],[leak_node_b]]
        L30Sep_B           = L30Sep_B.append(L30Sep_B_Pres_Temp, ignore_index=False)
    # MERGE PRESSURE AND LEAK STEP AS A DATAFRAME
    L30Sep_A['Leak Step'] = np.resize(Step,len(L30Sep_A))
    L30Sep_B['Leak Step'] = np.resize(Step,len(L30Sep_B))

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
    # SET LEAK DATAFRAME
    global L27Oct, Step
    L27Oct    = pd.DataFrame(columns = [leak_node])
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
        L27Oct_Pres_Temp = results.node['pressure'].loc[[3*3600],[leak_node]]
        L27Oct           = L27Oct.append(L27Oct_Pres_Temp, ignore_index=False)
    # MERGE PRESSURE AND LEAK STEP AS A DATAFRAME
    L27Oct['Leak Step'] = np.resize(Step,len(L27Oct))

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
    # SET LEAK DATAFRAME
    global L4Nov, Step
    L4Nov     = pd.DataFrame(columns = [leak_node])
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
        L4Nov_Pres_Temp = results.node['pressure'].loc[[3*3600],[leak_node]]
        L4Nov           = L4Nov.append(L4Nov_Pres_Temp, ignore_index=False)
    # MERGE PRESSURE AND LEAK STEP AS A DATAFRAME
    L4Nov['Leak Step'] = np.resize(Step,len(L4Nov))
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
    # SET LEAK DATAFRAME
    global L8Nov, Step
    L8Nov     = pd.DataFrame(columns = [leak_node])
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
        L8Nov_Pres_Temp = results.node['pressure'].loc[[3*3600],[leak_node]]
        L8Nov           = L8Nov.append(L8Nov_Pres_Temp, ignore_index=False)
    # MERGE PRESSURE AND LEAK STEP AS A DATAFRAME
    L8Nov['Leak Step'] = np.resize(Step,len(L8Nov))

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
    global HM_df, HM_Transposed
    HM_List = [L26May, L10Jun, L29Jun, L4Jul, L7Jul_A, L7Jul_B, L12Jul_A, L12Jul_B, L12Jul_D, 
               L21Jul_A, L21Jul_B, L26Jul, L28Jul_A, L28Jul_B, L19Aug, L22Aug, L23Aug_A, L23Aug_B,
               L26Aug, L30Aug_A, L30Aug_B, L5Sep_A, L5Sep_B, L8Sep, L12Sep, L15Sep, L21Sep,L28Sep_A, L28Sep_B, 
               L30Sep_A, L30Sep_B, L27Oct, L4Nov, L8Nov]
    HM_df   = reduce(lambda  left,right: pd.merge(left,right,on=['Leak Step'],how='outer'),HM_List)
    #  REORDER MERGED DATAFRAMES
    LeakStep_Val = HM_df['Leak Step']
    HM_df = HM_df.drop(columns=['Leak Step'])
    HM_df.insert(loc=0, column='Leak Step', value=LeakStep_Val)
    HM_Transposed = HM_df.T

run_hydraulic_model() 

# SAVE NEW DATAFRAME TO CSV
HM_Transposed.to_csv('Hydraulic Model using WNTR.csv')