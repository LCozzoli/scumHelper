# SCUM Game Helper

This python code/scripts allows players to have better experience in SCUM by automatising some unfriendly tasks. If devs decide to add those features in the game directly I'll be pleased to close this project.

**Despite the fact that it don't read the game memory at all, I'm still waiting for the SCUM devs reply. I don't take any responsibility so use at your own risks.**

## Keybinds

- **[CTRL+0]** Disable
- **[CTRL+1]** Chop planks
- **[CTRL+2]** Chop sticks
- **[CTRL+3]** Unbox bolts or nails and stack them by 10 in inventory
- **[CTRL+4]** Craft bundles of lockpicks from bobby pins boxes
- **[CTRL+5]** Autoclicker
- **[CTRL+6]** Autoloot for metal and stuff (in car wreck)
- **[F1]** Buy bulk at shop (15 elements)
- **[F2]** Double click on all padlocks from general store depot
- **[r]** Move red selected items to opened container

Every binds are customizable in the **config.json**, if you use something else than **F** to use, change the use key or the autoloot will not work.

## Python Installation

Install Python3 and PIP

https://www.python.org/downloads/

Then run the following in a terminal

```bash
py -m ensurepip --upgrade
```

## Requirements

After downloading or cloning the repository, run the following

```bash
pip install -r requirements.txt
```

If you have issues with missing OpenCV, install it there

https://opencv.org/releases/

## Usage

#### Compiling the code

```bash
./build.bat
```

Or execute the build.bat directly.

#### Running the script

```bash
python .
```
