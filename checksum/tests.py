
from GenerateChecksum import generate_checksum, get_file, check_equal
import unittest
import Errors


class ChecksumTests(unittest.TestCase):

    def test_sums_equal(self):
        checksum = generate_checksum("sha1", "C:/Users/deanw/Downloads/kali-linux-2.0-amd64/kali-linux-2.0-amd64.iso")
        self.assertEqual(checksum, "aaeb89a78f155377282f81a785aa1b38ee5f8ba0")

    def test_file_exists(self):
        checksum = generate_checksum("sha1", "b")
        self.assertEqual(checksum, "File non-existent")

    def test_hash_exists(self):
        self.assertRaises(Errors.HashError, generate_checksum, "wrong",
                          "C:/Users/deanw/Downloads/kali-linux-2.0-amd64/kali-linux-2.0-amd64.iso")

    def test_file_retrieval(self):
        test_file = get_file()
        self.assertEqual(test_file, "C:/Users/deanw/Downloads/kali-linux-2.0-amd64/kali-linux-2.0-amd64.iso")

    def test_equality_check(self):
        test_equal = check_equal("aaeb89a78f155377282f81a785aa1b38ee5f8ba0", "aaeb89a78f155377282f81a785aa1b38ee5f8ba0")
        self.assertTrue(test_equal)
        test_equal = check_equal("aaeb89a78f155377282f81a785aa1b38ee5f8ba0", "nope")
        self.assertFalse(test_equal)

if __name__ == '__main__':
    unittest.main()
