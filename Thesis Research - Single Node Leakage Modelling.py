#  ============================================================================
#  THESIS RESEARCH - SINGLE NODE LEAKAGE MODELLING 
#  ============================================================================

#  I. IMPORT PYTHON LIBRARIES 
from matplotlib import pyplot as plt
import wntr

#  II. LOAD EPANET INPUT FILE 
file  = 'G:/My Drive/Work Data/PT. Hutomo Bangun Perkasa/Hydroinformatics/Thesis Research/Leakage Modelling/Cal_A_RN1_RN2.inp'
epnt  = wntr.network.WaterNetworkModel(file)

#  III. RUN HYDRAULIC SIMULATION 
sim   = wntr.sim.EpanetSimulator(epnt)
res   = sim.run_sim() 

# GRAPH WATER DISTRIBUTION NETWORKS (WDN)
wntr.graphics.plot_network(epnt, title = 'Water Distribution Networks') 

# EXAMINING THE HEADING RESULT AS IN PANDAS DATA FRAME 
link_keys = results.link.keys()
print(link_keys)

# MAXIMUM FLOW IN PIPE 10 BY CALLING THE HEADING 
flow_p10 = results.link["flowrate"].loc[:,'10']
flow_p10.max()