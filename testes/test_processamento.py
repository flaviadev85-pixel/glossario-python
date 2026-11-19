import tempfile
import unittest
from pathlib import Path

from kdd import criar_glossario
from processamento import ler_palavras, normalizar_palavra, remover_repeticoes


class TesteProcessamento(unittest.TestCase):
    def test_normalizacao(self):
        self.assertEqual(normalizar_palavra("Justiça,"), "justiça")
        self.assertEqual(normalizar_palavra("CONTRATO."), "contrato")

    def test_leitura_linha_a_linha(self):
        with tempfile.TemporaryDirectory() as pasta:
            arquivo = Path(pasta, "entrada.txt")
            arquivo.write_text("Direito e justiça.\nDireito civil.", encoding="utf-8")
            self.assertEqual(
                ler_palavras(arquivo),
                ["direito", "e", "justiça", "direito", "civil"],
            )

    def test_remove_repeticoes_preservando_ordem(self):
        self.assertEqual(remover_repeticoes(["b", "a", "b"]), ["b", "a"])

    def test_criacao_do_glossario(self):
        with tempfile.TemporaryDirectory() as pasta:
            origem = Path(pasta, "entrada.txt")
            destino = Path(pasta, "saida.txt")
            origem.write_text("Contrato direito contrato ação.", encoding="utf-8")
            palavras, duracao = criar_glossario(origem, destino)
            self.assertEqual(palavras, ["ação", "contrato", "direito"])
            self.assertEqual(destino.read_text(encoding="utf-8"), "ação\ncontrato\ndireito\n")
            self.assertGreaterEqual(duracao, 0)


if __name__ == "__main__":
    unittest.main()

