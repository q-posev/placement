#! /usr/bin/env python
# -*- coding: utf-8 -*-

from utilities import *
from hardware import *
from architecture import *
import unittest

#@unittest.skip("it works, not tested")
class TestScatterExclusive(unittest.TestCase):
    def setUp(self):
        self.hardware = Bullx_dlc()

        # Architecture = 4 tâches/4 threads
        self.exclu_ok1   = Exclusive(self.hardware,2,4,4,False)

        # Architecture = 4 tâches/8 threads hyperthreading
        self.exclu_ok2   = Exclusive(self.hardware,2,8,4,True)

    def test_getCore2Socket(self):
        self.assertEqual(self.exclu_ok1.getCore2Socket(0),0)
        self.assertEqual(self.exclu_ok1.getCore2Socket(6),0)
        self.assertEqual(self.exclu_ok1.getCore2Socket(9),0)
        self.assertEqual(self.exclu_ok1.getCore2Socket(10),1)
        self.assertEqual(self.exclu_ok1.getCore2Socket(16),1)
        self.assertEqual(self.exclu_ok1.getCore2Socket(19),1)
        self.assertEqual(self.exclu_ok1.getCore2Socket(20),0)
        self.assertEqual(self.exclu_ok1.getCore2Socket(26),0)
        self.assertEqual(self.exclu_ok1.getCore2Socket(29),0)
        self.assertEqual(self.exclu_ok1.getCore2Socket(30),1)
        self.assertEqual(self.exclu_ok1.getCore2Socket(36),1)
        self.assertEqual(self.exclu_ok1.getCore2Socket(39),1)

    def test_getCore2Core(self):
        self.assertEqual(self.exclu_ok1.getCore2Core(0),0)
        self.assertEqual(self.exclu_ok1.getCore2Core(6),6)
        self.assertEqual(self.exclu_ok1.getCore2Core(9),9)
        self.assertEqual(self.exclu_ok1.getCore2Core(10),0)
        self.assertEqual(self.exclu_ok1.getCore2Core(16),6)
        self.assertEqual(self.exclu_ok1.getCore2Core(19),9)
        self.assertEqual(self.exclu_ok1.getCore2Core(20),0)
        self.assertEqual(self.exclu_ok1.getCore2Core(26),6)
        self.assertEqual(self.exclu_ok1.getCore2Core(29),9)
        self.assertEqual(self.exclu_ok1.getCore2Core(30),0)
        self.assertEqual(self.exclu_ok1.getCore2Core(36),6)
        self.assertEqual(self.exclu_ok1.getCore2Core(39),9)

    def test_getCore2PhysCore(self):
        self.assertEqual(self.exclu_ok1.getCore2PhysCore(0),0)
        self.assertEqual(self.exclu_ok1.getCore2PhysCore(6),6)
        self.assertEqual(self.exclu_ok1.getCore2PhysCore(9),9)
        self.assertEqual(self.exclu_ok1.getCore2PhysCore(10),10)
        self.assertEqual(self.exclu_ok1.getCore2PhysCore(16),16)
        self.assertEqual(self.exclu_ok1.getCore2PhysCore(19),19)
        self.assertEqual(self.exclu_ok1.getCore2PhysCore(20),0)
        self.assertEqual(self.exclu_ok1.getCore2PhysCore(26),6)
        self.assertEqual(self.exclu_ok1.getCore2PhysCore(29),9)
        self.assertEqual(self.exclu_ok1.getCore2PhysCore(30),10)
        self.assertEqual(self.exclu_ok1.getCore2PhysCore(36),16)
        self.assertEqual(self.exclu_ok1.getCore2PhysCore(39),19)

# bien qu'on teste ici une architecture Shared, on considère qu'elle est Exclusive
class TestScatterSharedMesca(unittest.TestCase):
    def setUp(self):
        self.hardware = Mesca2()

        # Architecture = 8 sockets/4 tâches/4 threads
        self.shared_ok1   = Shared(self.hardware,8,4,4,False)

#    @unittest.skip("it works, not tested")
    def test_getCore2Socket(self):
        self.assertEqual(self.shared_ok1.getCore2Socket(0),0)
        self.assertEqual(self.shared_ok1.getCore2Socket(5),0)
        self.assertEqual(self.shared_ok1.getCore2Socket(15),0)
        self.assertEqual(self.shared_ok1.getCore2Socket(16),1)
        self.assertEqual(self.shared_ok1.getCore2Socket(20),1)
        self.assertEqual(self.shared_ok1.getCore2Socket(31),1)
        self.assertEqual(self.shared_ok1.getCore2Socket(32),2)
        self.assertEqual(self.shared_ok1.getCore2Socket(34),2)
        self.assertEqual(self.shared_ok1.getCore2Socket(47),2)
        self.assertEqual(self.shared_ok1.getCore2Socket(48),3)
        self.assertEqual(self.shared_ok1.getCore2Socket(52),3)
        self.assertEqual(self.shared_ok1.getCore2Socket(63),3)
        self.assertEqual(self.shared_ok1.getCore2Socket(64),4)
        self.assertEqual(self.shared_ok1.getCore2Socket(66),4)
        self.assertEqual(self.shared_ok1.getCore2Socket(79),4)
        self.assertEqual(self.shared_ok1.getCore2Socket(80),5)
        self.assertEqual(self.shared_ok1.getCore2Socket(86),5)
        self.assertEqual(self.shared_ok1.getCore2Socket(95),5)
        self.assertEqual(self.shared_ok1.getCore2Socket(96),6)
        self.assertEqual(self.shared_ok1.getCore2Socket(100),6)
        self.assertEqual(self.shared_ok1.getCore2Socket(111),6)
        self.assertEqual(self.shared_ok1.getCore2Socket(112),7)
        self.assertEqual(self.shared_ok1.getCore2Socket(118),7)
        self.assertEqual(self.shared_ok1.getCore2Socket(127),7)

#    @unittest.skip("it works, not tested")
    def test_getCore2Core(self):
        self.assertEqual(self.shared_ok1.getCore2Core(0),0)
        self.assertEqual(self.shared_ok1.getCore2Core(5),5)
        self.assertEqual(self.shared_ok1.getCore2Core(15),15)
        self.assertEqual(self.shared_ok1.getCore2Core(16),0)
        self.assertEqual(self.shared_ok1.getCore2Core(20),4)
        self.assertEqual(self.shared_ok1.getCore2Core(31),15)
        self.assertEqual(self.shared_ok1.getCore2Core(32),0)
        self.assertEqual(self.shared_ok1.getCore2Core(34),2)
        self.assertEqual(self.shared_ok1.getCore2Core(47),15)
        self.assertEqual(self.shared_ok1.getCore2Core(48),0)
        self.assertEqual(self.shared_ok1.getCore2Core(52),4)
        self.assertEqual(self.shared_ok1.getCore2Core(63),15)
        self.assertEqual(self.shared_ok1.getCore2Core(64),0)
        self.assertEqual(self.shared_ok1.getCore2Core(66),2)
        self.assertEqual(self.shared_ok1.getCore2Core(79),15)
        self.assertEqual(self.shared_ok1.getCore2Core(80),0)
        self.assertEqual(self.shared_ok1.getCore2Core(86),6)
        self.assertEqual(self.shared_ok1.getCore2Core(95),15)
        self.assertEqual(self.shared_ok1.getCore2Core(96),0)
        self.assertEqual(self.shared_ok1.getCore2Core(100),4)
        self.assertEqual(self.shared_ok1.getCore2Core(111),15)
        self.assertEqual(self.shared_ok1.getCore2Core(112),0)
        self.assertEqual(self.shared_ok1.getCore2Core(118),6)
        self.assertEqual(self.shared_ok1.getCore2Core(127),15)

#    @unittest.skip("it works, not tested")
    def test_getCore2PhysCore(self):
        self.assertEqual(self.shared_ok1.getCore2PhysCore(0),0)
        self.assertEqual(self.shared_ok1.getCore2PhysCore(5),5)
        self.assertEqual(self.shared_ok1.getCore2PhysCore(15),15)
        self.assertEqual(self.shared_ok1.getCore2PhysCore(16),16)
        self.assertEqual(self.shared_ok1.getCore2PhysCore(20),20)
        self.assertEqual(self.shared_ok1.getCore2PhysCore(31),31)
        self.assertEqual(self.shared_ok1.getCore2PhysCore(32),32)
        self.assertEqual(self.shared_ok1.getCore2PhysCore(34),34)
        self.assertEqual(self.shared_ok1.getCore2PhysCore(47),47)
        self.assertEqual(self.shared_ok1.getCore2PhysCore(48),48)
        self.assertEqual(self.shared_ok1.getCore2PhysCore(52),52)
        self.assertEqual(self.shared_ok1.getCore2PhysCore(63),63)
        self.assertEqual(self.shared_ok1.getCore2PhysCore(64),64)
        self.assertEqual(self.shared_ok1.getCore2PhysCore(66),66)
        self.assertEqual(self.shared_ok1.getCore2PhysCore(79),79)
        self.assertEqual(self.shared_ok1.getCore2PhysCore(80),80)
        self.assertEqual(self.shared_ok1.getCore2PhysCore(86),86)
        self.assertEqual(self.shared_ok1.getCore2PhysCore(95),95)
        self.assertEqual(self.shared_ok1.getCore2PhysCore(96),96)
        self.assertEqual(self.shared_ok1.getCore2PhysCore(100),100)
        self.assertEqual(self.shared_ok1.getCore2PhysCore(111),111)
        self.assertEqual(self.shared_ok1.getCore2PhysCore(112),112)
        self.assertEqual(self.shared_ok1.getCore2PhysCore(118),118)
        self.assertEqual(self.shared_ok1.getCore2PhysCore(127),127)

if __name__ == '__main__':
    unittest.main()
