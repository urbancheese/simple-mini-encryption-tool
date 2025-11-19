import unittest
from test import caesar_cipher, xor_cipher, base64_encode, base64_decode, vigenere_cipher

class TestCryptoTool(unittest.TestCase):
    
    def test_caesar_cipher(self):
        self.assertEqual(caesar_cipher("Hello", 1), "Ifmmp")
        self.assertEqual(caesar_cipher("Ifmmp", 1, decrypt=True), "Hello")
        self.assertEqual(caesar_cipher("abc", 26), "abc")
        self.assertEqual(caesar_cipher("abc", 0), "abc")
        self.assertEqual(caesar_cipher("Zoo", 1), "App")
        self.assertEqual(caesar_cipher("123", 5), "123") # Non-alpha unchanged

    def test_xor_cipher(self):
        key = "secret"
        text = "Hello World"
        encrypted = xor_cipher(text, key)
        decrypted = xor_cipher(encrypted, key)
        self.assertEqual(decrypted, text)
        self.assertNotEqual(encrypted, text)
        
        # Test empty key
        self.assertEqual(xor_cipher("test", ""), "test")

    def test_base64(self):
        text = "Hello World"
        encoded = base64_encode(text)
        decoded = base64_decode(encoded)
        self.assertEqual(decoded, text)
        self.assertEqual(encoded, "SGVsbG8gV29ybGQ=")

    def test_vigenere_cipher(self):
        key = "KEY"
        text = "HELLO"
        # H(7) + K(10) = R(17)
        # E(4) + E(4) = I(8)
        # L(11) + Y(24) = J(9)
        # L(11) + K(10) = V(21)
        # O(14) + E(4) = S(18)
        expected = "RIJVS"
        encrypted = vigenere_cipher(text, key)
        self.assertEqual(encrypted, expected)
        self.assertEqual(vigenere_cipher(expected, key, decrypt=True), text)
        
        # Case sensitivity
        self.assertEqual(vigenere_cipher("Hello", "key"), "Rijvs")

if __name__ == '__main__':
    unittest.main()
