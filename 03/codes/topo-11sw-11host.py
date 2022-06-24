from asyncio import protocols

from mininet.topo import Topo


class MyTopo(Topo):

    def __init__(self):

        Topo.__init__(self)

        Host1 = self.addHost('h1')

        Host2 = self.addHost('h2')

        Host3 = self.addHost('h3')

        Host4 = self.addHost('h4')

        Host5 = self.addHost('h5')

        Host6 = self.addHost('h6')

        Host7 = self.addHost('h7')

        Host8 = self.addHost('h8')

        Host9 = self.addHost('h9')

        Host10 = self.addHost('h10')

        Host11 = self.addHost('h11')

        Switch1 = self.addSwitch('s1', protocols='OpenFlow13')

        Switch2 = self.addSwitch('s2', protocols='OpenFlow13')

        Switch3 = self.addSwitch('s3', protocols='OpenFlow13')

        Switch4 = self.addSwitch('s4', protocols='OpenFlow13')

        Switch5 = self.addSwitch('s5', protocols='OpenFlow13')

        Switch6 = self.addSwitch('s6', protocols='OpenFlow13')

        Switch7 = self.addSwitch('s7', protocols='OpenFlow13')

        Switch8 = self.addSwitch('s8', protocols='OpenFlow13')

        Switch9 = self.addSwitch('s9', protocols='OpenFlow13')

        Switch10 = self.addSwitch('s10', protocols='OpenFlow13')

        Switch11 = self.addSwitch('s11', protocols='OpenFlow13')

        self.addLink(Switch1, Switch5)

        self.addLink(Switch1, Switch3)

        self.addLink(Switch1, Switch6)

        self.addLink(Switch2, Switch5)

        self.addLink(Switch3, Switch8)

        self.addLink(Switch4, Switch5)

        self.addLink(Switch3, Switch6)

        self.addLink(Switch2, Switch4)

        self.addLink(Switch4, Switch6)

        self.addLink(Switch5, Switch4)

        self.addLink(Switch6, Switch7)

        self.addLink(Switch7, Switch9)

        self.addLink(Switch8, Switch7)

        self.addLink(Switch9, Switch10)

        self.addLink(Switch10, Switch1)

        self.addLink(Switch10, Switch11)

        self.addLink(Switch11, Switch1)

        self.addLink(Host1, Switch1)

        self.addLink(Host2, Switch2)

        self.addLink(Host3, Switch3)

        self.addLink(Host4, Switch4)

        self.addLink(Host5, Switch5)

        self.addLink(Host6, Switch6)

        self.addLink(Host7, Switch7)

        self.addLink(Host8, Switch8)

        self.addLink(Host9, Switch9)

        self.addLink(Host10, Switch10)

        self.addLink(Host11, Switch11)


topos = {'mytopo': (lambda: MyTopo())}
