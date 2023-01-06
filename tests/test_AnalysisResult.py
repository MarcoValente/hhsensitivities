import unittest
from hhdata.AnalysisResult import Experiment,AnalysisResult

class TestAnalysisResults(unittest.TestCase):

    def test_Experiment(self):
        self.assertEqual(Experiment.ATLAS.name,'ATLAS') 
        self.assertEqual(Experiment.CMS.name,'CMS') 

    def test_AnalysisResult(self):
        res = AnalysisResult('AAA','ATLAS',100,'bbbb')
        self.assertEqual(res.lumi,100)
        self.assertEqual(res.name,'AAA')
        self.assertEqual(res.experiment,'ATLAS')
        
if __name__ == '__main__':
    unittest.main() #This will run all the tests when you execute python test_Models.py