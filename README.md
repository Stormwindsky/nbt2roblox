# nbt2roblox (Minecraft to Roblox Converter)

A lightweight Python tool to convert Minecraft `.nbt` structure files into Roblox `.rbxmx` model files.

## Features
- Automatically ignores Air blocks to optimize performance.
- Scales blocks to 4x4x4 studs (standard Roblox scale).
- Anchors all parts by default.

## Quick Start
1. Clone this repo.
2. Run `./setup.sh` to install dependencies.
3. Run `./run.sh your_model.nbt` to generate your Roblox file.
4. Import the resulting `.rbxmx` into Roblox Studio.

## License
Dedicated to the Public Domain (CC0 1.0). See `NOTICE.md` [NOTICE.md]((https://github.com/Stormwindsky/nbt2roblox/blob/main/NOTICE.md) for third-party library details.
