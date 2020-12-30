from unittest import TestCase
from OO.Carro import Direcao
from OO.Carro import Motor
from OO.Carro import Carro

class CarroTestCase(TestCase):
    def test_diracao_valor(self):
        direcao = Direcao()

        # Asserção de valor
        # Conferir o valor
        # assertEqual(valor esperado, valor que vai receber)
        self.assertEqual('Norte', direcao.valor)

    def test_motor_velocidade(self):
        motor = Motor()
        self.assertEqual(0, motor.velocidade)

        motor.acelerar()
        self.assertEqual(1, motor.velocidade)

    def test_carro(self):
        carro = Carro(direcao=Direcao(), motor=Motor())

        self.assertEqual(0, carro.calcular_velocidade())
        self.assertEqual('Norte', carro.calcular_direcao())
        carro.girar_a_direita()
        self.assertEqual('Leste', carro.calcular_direcao())
