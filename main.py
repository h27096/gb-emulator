from js import fetch
import asyncio

async def load_rom():
    response = await fetch("roms/test.gb")
    buffer = await response.arrayBuffer()
    return buffer.to_py()

async def main():
    print("Loading ROM...")

    rom = await load_rom()
    print("ROM size:", len(rom), "bytes")

    print("First 16 bytes:")
    for i in range(16):
        print(hex(rom[i]))

    print("\nStarting execution...\n")

    pc = 0x100  # Game Boy entry point

    for _ in range(20):
        opcode = rom[pc]
        print(f"PC: {hex(pc)} | Opcode: {hex(opcode)}")
        pc += 1

asyncio.run(main())
