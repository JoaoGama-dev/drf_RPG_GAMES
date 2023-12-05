from django.test import TestCase
from core.models import Cliente

class ClientesTestCase(TestCase):

    def setUp(self):
        Cliente.objects.create(nome= 'Gama', idade = 25, jogo_favorito ='Diablo4')


    def test_clientes_cadastrado(self):
        cliente = Cliente.objects.get(nome = 'Gama')
        self.assertEqual(cliente.nome,'Gama')