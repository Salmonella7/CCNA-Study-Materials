## What is the OSI Model?

The open systems interconnection (OSI) model is a conceptual model created by the International Organization for Standardization which enables diverse communication systems to communicate using standard [protocols](https://www.cloudflare.com/learning/network-layer/what-is-a-protocol/). In plain English, the OSI provides a standard for different computer systems to be able to communicate with each other.

The OSI Model can be seen as a universal language for computer networking. It is based on the concept of splitting up a communication system into seven abstract layers, each one stacked upon the last.

Application Layer
- sdsdsd

Presentation Layer
- data in the application layer is in 'application format'
- needs to be translated to a different format to be sent over the network
- presentation layer's job is to 'translate' between application and network format
- an example is encryption of data as it is being sent and decryption of data as is being received

Session Later
- controls dialogues 'sessions' between communicating hosts
- establishes, manages and terminates sessions between 'web browser' and the remote application

Note: Network engineers don't usually handle these three layers as they are commonly handled by web devs.

Transport Layer
- provides host-to-host communication or 'end-to-end communication'
- segments and reassembles data for communication between hosts
- breaks larger data to smaller segmented versions to be easily sent over the network
- less likely to cause transmission errors
- UDP/ TCP

Segment
- layer 4 (transport layer)

Network Layer
- provides connectivity between hosts on different networks (i.e. outside the LAN)
- provides logical addressing (IP addresses)
- path selection between source and destination
- routers operate at layer 3

Packet
- layer 3 (network layer)

Data Link Layer
- provides node-to-node connectivity and data transfer (PC to switch, router to router, switch to router)
- defines how data is formatted for transmission over a physical medium (e.g. copper UTP cables)
- detects and (possibly) corrects physical layer errors
- similar to layer 3, Data Link layer also uses addressing system (separate and different from  layer 3  addressing)
- switches operate at layer 2
- MAC address
- switches look at the destination layer 2 address to determine where to send the data

Frame
- contains the following (L2 Trailer, Data, L4 header, L3 Header, L2 Header)

Physical Layer
- defines the physical characteristics of the medium used to transfer data between devices
- an example, voltage levels, maximum transmission distances, physical connectors, cable specifications and others
-  digital bits are converted into electrical (for wired) or radio (for wireless) signals
- sdsd

**Protocol Data Units**
- Data
- Segment
- Packet Frame
- Bit (layer 1)

OSI Layer Acronyms
P lease
D o
N ot 
T each 
S tudents
P ointless
A cronyms


Next is the [[TCP IP Suite]]