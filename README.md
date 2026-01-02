# Bitty

Bitty is a compact BitTorrent client written for Python 3.5+ that uses
asyncio for non-blocking peer-to-peer communication.

This project is educational rather than production-ready: it purposely
omits many features required by a fully functional client. It was
implemented to learn the BitTorrent protocol and to explore Python's
asyncio primitives.

## Demo

![Bittorrent Client](Bittorrent%20Client.png)

<video controls width="640">
  <source src="Demo.mp4" type="video/mp4">
  Your browser does not support the video tag. Download: [Demo.mp4](Demo.mp4)
</video>

## Getting started

Install dependencies and run tests:

    $ make init
    $ make test

To download a torrent, run:

    $ python bitty.py -v .\tests\data\ubuntu-24.04.3-desktop-amd64.iso.torrent

If the download completes successfully the program exits; press
Ctrl+C to stop the client at any time.

## Design notes

The code prioritizes clarity and simplicity over performance. For
example, pieces are requested sequentially (not using a "rarest-first"
strategy), and all pieces are kept in memory until the torrent finishes
downloading.

File writes are performed synchronously and could be improved in a
future revision.

### Code overview

- `bitty.client.TorrentClient` is the central component. It:
  - connects to the tracker to obtain peers;
  - builds a `Queue` of available peers;
  - decides which pieces to request next;
  - shuts down the client when the download finishes.

- The piece-selection and assembly logic lives in `bitty.client.PieceManager`.

- The BitTorrent protocol implementation is in `bitty.protocol`. The
  `bitty.protocol.PeerConnection` class opens connections to peers and
  manages the message flow between peers.

BitTorrent is a binary protocol, and message decoding is implemented as
an async iterator named `PeerStreamIterator` which reads and parses the
socket stream until the connection closes.

Each protocol message is represented by a class with `encode` and
`decode` methods. Because this client does not currently support
seeding, not all messages are implemented bidirectionally.

## References

The implementation was guided by these resources:

- http://www.kristenwidman.com/blog/33/how-to-write-a-bittorrent-client-part-1/
- https://markuseliasson.se/article/bittorrent-in-python
- https://wiki.theory.org/BitTorrentSpecification

## License

This project is released under the Apache v2 license (see LICENCE).