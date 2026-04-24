from cpu import CPU
from memory import Memory
from display import Display
from input import Input
import time

ROM_PATH = "roms/test.gb"  # put ROM here

def main():
    memory = Memory(ROM_PATH)
    cpu = CPU(memory)
    display = Display()
    inp = Input()

    while cpu.running:
        if not inp.handle():
            break

        cpu.step()

        display.clear()
        display.update()

        time.sleep(0.001)

if __name__ == "__main__":
    main()
