from enum import Enum

class Experiment(Enum):
    NONE=0
    ATLAS=1
    CMS=2

class HHChannel(Enum):
    Comb=0
    bbbb=1
    bbtt=2
    bbyy=3

class HHProd(Enum):
    ggF=0
    VBF=1
class AnalysisResult:
    def __init__(self, name, experiment, lumi, hh_channel, hh_prod, energy, mu95_obs=None, mu95_exp=None, mu_obs=None, Z=None, ref=None) -> None:
        '''__init__ AnalysisResult

        Class describing a certain experiment analysis result

        Parameters
        ----------
        name : str
            Name of the analysis
        experiment : str or AnalysisResult.Experiment
            Experiment that produced this result
        lumi : float
            Luminosity in fb-1
        hh_channel: str or AnalysisResult.HHChannel 
            HH channel corresponding to result
        hh_prod: str or AnalysisResult.HHProd
            HH production mode
        energy: float
            COM energy in TeV
        Z : float or None
            Signal statistical significance
        mu95_obs : float or None
            95% CL observed upper limit on signal strength
        mu95_exp : float or None
            95% CL expected upper limit on signal strength
        mu_obs : float or None
            Observed signal strength
        ref : str
            Reference to result (arxiv entry, etc.)
        '''
        self._name = name
        self._exp_enum = Experiment[experiment] if isinstance(experiment, str) else experiment
        self._lumi = lumi #Luminosity in fb-1
        self._hh_chan = HHChannel[hh_channel] if isinstance(hh_channel, str) else hh_channel
        self._hh_prod = HHProd[hh_prod] if isinstance(hh_prod, str) else hh_prod
        self._energy = energy
        self._Z = Z
        self._mu95_obs = mu95_obs
        self._mu95_exp = mu95_exp
        self._mu_obs = mu_obs
        self._ref = ref
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
    def hh_channel(self):
        return self._hh_chan.name

    @property
    def hh_prod(self):
        return self._hh_prod.name

    @property
    def energy(self):
        return self._energy

    @property
    def Z(self):
        return self._Z

    @property
    def mu95_obs(self):
        return self._mu95_obs

    @property
    def mu95_exp(self):
        return self._mu95_exp

    @property
    def mu_obs(self):
        return self._mu_obs
    
    @property
    def ref(self):
        return self._ref