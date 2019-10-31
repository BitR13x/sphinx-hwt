from hwt.synthesizer.unit import Unit
from hwt.interfaces.std import VectSignal
from hwt.synthesizer.param import Param


def example_constructor():
    u = ExampleCls0()
    u.WIDTH = 32
    return u


def example_constructor2():
    u = ExampleCls0()
    u.WIDTH = 64
    return u


class ExampleCls0(Unit):
    """
    
    Without parameter
    
    .. hwt-schematic::

    example_constructor:
    
    .. hwt-schematic:: example_constructor

    example_constructor2
    
    .. hwt-schematic:: example_constructor2
    """

    def _config(self):
        self.WIDTH = Param(1)

    def _declr(self):
        self.din0 = VectSignal(self.WIDTH)
        self.dout0 = VectSignal(self.WIDTH)._m()

        if self.WIDTH >= 3:
            self.din1 = VectSignal(self.WIDTH)
            self.dout1 = VectSignal(self.WIDTH)._m()

    def _impl(self):
        self.dout0(self.din0)

        if self.WIDTH >= 3:
            self.dout1(self.din1)
