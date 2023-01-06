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
        mu95_obs=5.4,
        ref='ATLAS-CONF-HDBS-2022-35',
    ),
    AR('Resolved ggF $b\\bar{b}b\\bar{b}$', 'ATLAS', 
        24, # fb-1
       'bbbb',
       'ggF',
        13.,  # TeV
        mu95_exp=20.7,
        mu95_obs=12.9,
        ref='JHEP 01 (2019) 030',
    ),
    AR('Resolved ggF $b\\bar{b}b\\bar{b}$', 'ATLAS', 
        3.2, # fb-1
       'bbbb',
       'ggF',
        13.,  # TeV
        mu95_exp=108.,
        mu95_obs=108.,
        ref='Phys. Rev. D 94 (2016) 052002',
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

def sel_ggF(Ana):
    return Ana.hh_prod=='ggF'

def selectAnalyses(sel_fun, Analyses=AnalysesList):
    ret = []
    for ana in Analyses:
        if sel_fun(ana): ret += [ana]
    return ret
