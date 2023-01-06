from enum import Enum

class Experiment(Enum):
    NONE=0
    ATLAS=1
    CMS=2

class AnalysisResult:
    def __init__(self,name,lumi,experiment,mu95=None,mu_obs=None, Z=None) -> None:
        '''__init__ AnalysisResult

        Class describing a certain experiment analysis result

        Parameters
        ----------
        name : str
            Name of the analysis
        lumi : float
            Luminosity in fb-1
        experiment : str or AnalysisResult.Experiment enum
            Experiment that produced this result
        Z : float or None
            Signal statistical significance
        mu95 : float or None
            95% CL upper limit on signal strength
        mu_obs : float or None
            Observed signal strength
        '''
        self._name = name
        self._exp_enum = Experiment[experiment] if isinstance(experiment, str) else experiment
        self._lumi = lumi #Luminosity in fb-1
        self._Z = Z
        self._mu95 = mu95
        self._mu_obs = mu_obs
        pass

    @property
    def name(self):
        return self._name

    @property
    def experiment(self):
        return self._exp_enum.name
    
    @property
    def lumi(self):
        return self._lumi

    @property
    def Z(self):
        return self._Z

    @property
    def mu95(self):
        return self._mu95

    @property
    def mu_obs(self):
        return self._mu_obs