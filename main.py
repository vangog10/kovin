from functools import wraps
from datetime import datetime


def perfomance_log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'{datetime.now().strftime("[%d.%m.%Y %H-%M-%S]")} Обновлён параметр {args[1]} на значение {args[2]}')
        return result

    return wrapper


class ComputerExtended:
    __slots__ = ['_cpu', '_ram', '_storage', '_gpu', '_vram', 'id']
    computer_count = 0

    def __init__(self, cpu, ram, storage, gpu, vram):
        self._cpu = cpu
        self._ram = ram
        self._storage = storage
        self._gpu = gpu
        self._vram = vram
        ComputerExtended.computer_count += 1
        self.id = f"PC_{ComputerExtended.computer_count}"

    def __str__(self):
        return f"Computer {self.id}: CPU: {self.cpu}, RAM: {self.ram}GB, Storage: {self.storage}GB, GPU: {self.gpu}"

    def __eq__(self, other):
        return self._cpu == other._cpu and \
            self._ram == other._ram and \
            self._storage == other._storage and \
            self._gpu == other._gpu and self._vram == other._vram

    @property
    def cpu(self):
        return self._cpu

    @cpu.setter
    def cpu(self, value):
        if not isinstance(value, str):
            raise ValueError("CPU должен быть строкой")
        self._cpu = value

    @property
    def ram(self):
        return self._ram

    @ram.setter
    def ram(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("RAM должен быть положительным целым числом")
        self._ram = value

    @property
    def storage(self):
        return self._storage

    @storage.setter
    def storage(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Объем хранилища должен быть положительным целым числом")
        self._storage = value

    @property
    def gpu(self):
        return self._gpu

    @gpu.setter
    def gpu(self, value):
        if not isinstance(value, str):
            raise ValueError("GPU должен быть строкой")
        self._gpu = value

    @property
    def vram(self):
        return self._vram

    @vram.setter
    def vram(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("VRAM должен быть целым положителным числом")

    def total_memory(self):
        return self._ram + self._vram

    @perfomance_log
    def upgrade_component(self, component, new_value):
        if f'_{component}' not in ComputerExtended.__slots__:
            raise ValueError("Попытка обновить несуществующий сопонент")
        setattr(self, f'_{component}', new_value)

    @staticmethod
    def is_hight_perfomance(computer):
        return computer._ram > 32 and \
            computer._storage > 1024 and \
            computer._vram > 8


a = ComputerExtended(1, 2, 3, 4, 5)

assert a.total_memory() == 7
assert a == ComputerExtended(1, 2, 3, 4, 5)
a.upgrade_component('cpu', 10)
assert a == ComputerExtended(10, 2, 3, 4, 5)
assert a.is_hight_perfomance(a) == False
