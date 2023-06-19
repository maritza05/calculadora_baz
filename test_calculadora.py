#!/usr/bin/env python3

import unittest
from calculadora import Calculadora


class TestCalculadora(unittest.TestCase):

    def test_sumar_2_y_2_regresa_4(self):
        calcu = Calculadora()
        resultado = calcu.sumar(2, 2)

        self.assertEqual(resultado, 4)

    def test_sumar_3_y_5_regresa_8(self):
        calcu = Calculadora()
        resultado = calcu.sumar(3, 5)

        self.assertEqual(resultado, 8)


    def test_restar_8_y_2_regresa_6(self):
        calcu = Calculadora()
        resultado = calcu.restar(8, 2)

        self.assertEqual(resultado, 6)


    def test_restar_5_y_5_regresa_0(self):
        calcu = Calculadora()
        resultado = calcu.restar(5, 5)

        self.assertEqual(resultado, 0)
