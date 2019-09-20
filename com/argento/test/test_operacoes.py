from unittest import TestCase
from com.argento.operacoes import Multi

class TestMulti(TestCase):
        
    def setUp(self):
        self.multiplicacao = Multi()
    
    def test_multiplicacao(self):
        self.assertEqual(self.multiplicacao.multiplicacao([1,1]), 1, "Deveria ser 1!")
        