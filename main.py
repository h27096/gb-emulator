from js import fetch
import asyncio

async def load_rom():
    try:
        print("Fetching ROM file...")
        response = await fetch("roms/test.gb")

        if not response.ok:
            print("ERROR: ROM not found!")
            return None

        buffer = await response.arrayBuffer()
        data = buffer.to_py()

        print("ROM loaded successfully!")
        return data

    except Exception as e:
        print("ERROR loading ROM:", e)
        return None


async def main():
    print("Starting emulator...")

    rom = await load_rom()

    if rom is None:
        print("No ROM loaded. Stopping.")
        return

    print("ROM size:", len(rom))

    print("\nFirst 16 bytes:")
    for i in range(min(16, len(rom))):
        print(hex(rom[i]))

    print("\nExecuting...")

    pc = 0x100

    for _ in range(20):
        opcode = rom[pc]
        print(f"PC {hex(pc)} → {hex(opcode)}")
        pc += 1


asyncio.run(main())
