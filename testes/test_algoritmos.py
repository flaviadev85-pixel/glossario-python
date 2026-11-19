import random
import unittest

from algoritmos import bubble_sort, selection_sort, sort_nativo


class TesteAlgoritmos(unittest.TestCase):
    def test_algoritmos_ordenam_numeros(self):
        valores = [8, 3, 1, 9, 3, -2, 7]
        esperado = sorted(valores)
        for algoritmo in (bubble_sort, selection_sort, sort_nativo):
            with self.subTest(algoritmo=algoritmo.__name__):
                self.assertEqual(algoritmo(valores), esperado)

    def test_algoritmos_ordenam_palavras(self):
        palavras = ["sentença", "ação", "contrato", "direito"]
        esperado = sorted(palavras)
        for algoritmo in (bubble_sort, selection_sort, sort_nativo):
            with self.subTest(algoritmo=algoritmo.__name__):
                self.assertEqual(algoritmo(palavras), esperado)

    def test_algoritmos_nao_alteram_lista_original(self):
        original = [3, 2, 1]
        for algoritmo in (bubble_sort, selection_sort, sort_nativo):
            algoritmo(original)
            self.assertEqual(original, [3, 2, 1])

    def test_resultado_aleatorio_igual_ao_sorted(self):
        gerador = random.Random(2819)
        valores = [gerador.randint(-100, 100) for _ in range(40)]
        self.assertEqual(bubble_sort(valores), sorted(valores))
        self.assertEqual(selection_sort(valores), sorted(valores))


if __name__ == "__main__":
    unittest.main()

