class Memory:
    def __init__(self, rom_path):
        self.ram = [0] * 65536  # 64KB

        with open(rom_path, "rb") as f:
            rom_data = f.read()

        for i in range(len(rom_data)):
            self.ram[i] = rom_data[i]

    def read(self, addr):
        return self.ram[addr]

    def write(self, addr, value):
        self.ram[addr] = value & 0xFF
