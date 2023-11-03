import OMPython
import unittest
import tempfile, shutil, os

class testFMIRegression(unittest.TestCase):
  def __init__(self, *args, **kwargs):
    super(testFMIRegression, self).__init__(*args, **kwargs)
    self.tmp = ""

  def __del__(self):
    shutil.rmtree(self.tmp, ignore_errors=True)

  def test_Modelica_Blocks_Examples_Filter(self):
      print("Modelica.Blocks.Examples.Filter")
      mod = OMPython.ModelicaSystem(modelName="Modelica.Blocks.Examples.Filter")
      self.tmp = mod.getWorkDirectory()

      fmu = mod.convertMo2Fmu(fileNamePrefix="Filter")
      self.assertEqual(True, os.path.exists(fmu))


if __name__ == '__main__':
    unittest.main()