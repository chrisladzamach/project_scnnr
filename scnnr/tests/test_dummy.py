import unittest
from scnnr import file_scanner, comment_parser

class TestScanner(unittest.TestCase):
  def test_contar_archivos(self):
    data = file_scanner.contar_archivos_por_extension(".")
    self.assertIsInstance(data, dict)

  def test_detectar_comentarios(self):
    comentarios = comment_parser.detectar_comentarios_en_archivo("tests/test_dummy.py")
    self.assertIsInstance(comentarios, list)

if __name__ == '__main__':
  unittest.main()
