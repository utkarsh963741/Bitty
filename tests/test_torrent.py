import unittest

from bitty.torrent import Torrent

class UbuntuTorrentTests(unittest.TestCase):
    def setUp(self):
        self.t = Torrent('tests/data/ubuntu-24.04.3-desktop-amd64.iso.torrent')

    def test_instantiate(self):
        self.assertIsNotNone(self.t)

    def test_is_single_file(self):
        self.assertFalse(self.t.multi_file)

    def test_announce(self):
        self.assertEqual(
            'https://torrent.ubuntu.com/announce', self.t.announce)

    def test_piece_length(self):
        self.assertEqual(
            262144, self.t.piece_length)

    def test_file(self):
        self.assertEqual(1, len(self.t.files))
        self.assertEqual(
            'ubuntu-24.04.3-desktop-amd64.iso', self.t.files[0].name)
        self.assertEqual(6345887744, self.t.files[0].length)

    def test_hash_value(self):
        # hexdigest of the SHA1 '4344503b7e797ebf31582327a5baae35b11bda01',
        self.assertEqual(
            b"\xd1`\xb8\xd8\xea5\xa5\xb4\xe5(7F\x8f\xc8\xf0=U\xce\xf1\xf7",
            self.t.info_hash)

    def test_total_size(self):
        self.assertEqual(6345887744, self.t.total_size)

    def test_pieces(self):
        self.assertEqual(24208, len(self.t.pieces))
