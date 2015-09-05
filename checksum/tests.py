
from GenerateChecksum import generate_checksum
import unittest


class ChecksumTests(unittest.TestCase):
    def test_sums_equal(self):
        checksum = generate_checksum("a", "E:\TV\kali-linux-2.0-amd64\kali-linux-2.0-amd64.iso")
        self.assertEqual(checksum, "aaeb89a78f155377282f81a785aa1b38ee5f8ba0")

    def test_file_exists(self):
        checksum = generate_checksum("a", "b")
        self.assertTrue(checksum)

if __name__ == '__main__':
    unittest.main()
