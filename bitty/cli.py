
from bitty.bencoding import Decoder
from bitty.torrent import Torrent

def main():
    print("Bitty CLI is running")
    with open('tests/data/ubuntu-16.04-desktop-amd64.iso.torrent', 'rb') as f:
        meta_info = f.read()
        torrent = Decoder(meta_info).decode()
        for key, value in list(torrent.items())[:-1]:
            print(key, value)
    
    file = Torrent('tests/data/ubuntu-16.04-desktop-amd64.iso.torrent')
    print("Announce URL:", file.announce)