from hhdata.AnalysisResult import AnalysisResult as AR

AnalysesList = []

#############
# ATLAS Run 2 analyses
#############

#4b
AnalysesList += [
    AR('Resolved ggF $b\\bar{b}b\\bar{b}$', 'ATLAS', 
        126, # fb-1
       'bbbb',
       'ggF',
        13.,  # TeV
        mu95_exp=8.1,
        mu95_exp_err=[5.6,12.0],
        mu95_obs=5.4,
        ref='ATLAS-CONF-HDBS-2022-35',
    ),
    AR('Resolved ggF $b\\bar{b}b\\bar{b}$', 'ATLAS', 
        27.5, # fb-1
       'bbbb',
       'ggF',
        13.,  # TeV
        mu95_exp=20.7,
        mu95_exp_err=[15.0, 28.0],
        mu95_obs=12.9,
        ref='JHEP 01 (2019) 030',
    ),
    # AR('Resolved ggF $b\\bar{b}b\\bar{b}$', 'ATLAS', 
    #     3.2, # fb-1
    #    'bbbb',
    #    'ggF',
    #     13.,  # TeV
    #     mu95_exp=108.,
    #     mu95_obs=108.,
    #     ref='Phys. Rev. D 94 (2016) 052002',
    # ),
]

#bbtautau
AnalysesList += [
    AR('ggF $b\\bar{b}\\tau^+\\tau^-$', 'ATLAS',
        139,  # fb-1
       'bbtt',
       'ggF',
        13.,  # TeV
        mu95_exp=4.7,
        mu95_exp_err=[2.8,5.4],
        mu95_obs=3.9,
        ref='arXiv:2209.10910',
       ),
    AR('ggF $b\\bar{b}\\tau ^+\\tau ^-$', 'ATLAS',
        36,  # fb-1
       'bbtt',
       'ggF',
        13.,  # TeV
        mu95_exp=14.8,
        mu95_exp_err=[10.7,20.6],
        mu95_obs=12.7,
        ref='Phys. Rev. Lett. 121, 191801 (2018)',
       ),
]

#bbyy
AnalysesList += [
    AR('ggF $b\\bar{b}\gamma\gamma$', 'ATLAS',
        139,  # fb-1
       'bbyy',
       'ggF',
        13.,  # TeV
        mu95_exp=5.7,
        mu95_exp_err=[4.1,8.8],
        mu95_obs=4.2,
        ref='Phys. Rev. D 106 (2022) 052001',
       ),
    AR('ggF $b\\bar{b}\gamma\gamma$', 'ATLAS',
        36,  # fb-1
       'bbyy',
       'ggF',
        13.,  # TeV
        mu95_exp=28.0,
        mu95_exp_err=[20.0,40.0],
        mu95_obs=22.0,
        ref='JHEP 11 (2018) 040',
       ),
]

#Combination
AnalysesList += [
    AR('ggF Combination ($b\\bar{b}b\\bar{b},b\\bar{b}\\tau^+\\tau^-,b\\bar{b}\gamma\gamma$)', 'ATLAS',
        139,  # fb-1
       'Comb',
       'ggF',
        13.,  # TeV
        mu95_exp=2.9,
        mu95_exp_err=[2.0, 4.2],
        mu95_obs=2.4,
        ref='Submitted to: Phys. Lett. B.',
       ),
    AR('ggF Combination', 'ATLAS',
        36,  # fb-1
       'Comb',
       'ggF',
        13.,  # TeV
        mu95_exp=10.0,
        mu95_exp_err=[7.3, 15.0],
        mu95_obs=6.9,
        ref='Phys. Lett. B 800 (2020) 135103',
       ),
]


#############
# ATLAS Run 1 analyses
#############

# 4b
AnalysesList += [
    AR('Resolved ggF $b\\bar{b}b\\bar{b}$', 'ATLAS',
        19.5,  # fb-1
       'bbbb',
       'ggF',
        8.,  # TeV
        mu95_exp=56.1,
        mu95_obs=56.1,
        ref='Eur. Phys. J. C (2015) 75:412',
       ),
]

def sel_Run2(Ana):
    return True if Ana.energy==13. else False

def sel_bbbb(Ana):
    return Ana.hh_channel=='bbbb'

def sel_bbtt(Ana):
    return Ana.hh_channel=='bbtt'

def sel_bbyy(Ana):
    return Ana.hh_channel=='bbyy'

def sel_comb(Ana):
    return Ana.hh_channel=='Comb'

def sel_ggF(Ana):
    return Ana.hh_prod=='ggF'

def selectAnalyses(sel_fun, Analyses=AnalysesList):
    ret = []
    for ana in Analyses:
        if sel_fun(ana): ret += [ana]
    return ret
