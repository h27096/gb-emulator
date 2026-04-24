class CPU:
    def __init__(self, memory):
        self.mem = memory
        self.pc = 0x0100  # Game Boy entry point
        self.running = True

    def step(self):
        opcode = self.mem.read(self.pc)
        self.pc += 1

        # Minimal opcode handling
        if opcode == 0x00:  # NOP
            pass

        elif opcode == 0xC3:  # JP addr
            low = self.mem.read(self.pc)
            high = self.mem.read(self.pc + 1)
            self.pc = (high << 8) | low

        else:
            print(f"Unknown opcode: {hex(opcode)}")
            self.running = False
