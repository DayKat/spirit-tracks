# The Legend of Zelda: Spirit Tracks AP Setup Guide

## Required Software

* [Archipelago 0.6.1+](https://archipelago.gg/tutorial/Archipelago/setup/en)
* [Bizhawk 2.10+](https://github.com/TASEmulators/BizHawk)
* Legally acquired Spirit Tracks EU rom *(Not revision 1)*. Apparently it only works in English
* [Latest tloz_st.apworld](https://github.com/DayKat/spirit-tracks/releases)

## Recommended Software

* [Universal Tracker](https://github.com/FarisTheAncient/Archipelago/releases)

## Setup

1. Find your Archipelago directory, and put tloz_st.apworld in the 'custom_worlds' folder
2. Create a yaml settings file, and put it in the Archipelago directories 'players' folder. You can generate a template yaml with the archipelago launcher.
3. Generate your game
4. Host the game, either locally or via the archipelago web hosting service
5. Open the 'generic bizhawk client' in Archipelago, and connect to the server
6. Launch the vanilla game in bizhawk, and open the lua console. Add the 'connector_bizhawk_generic.lua' script that can be found in 'Archipelago\data\lua'. 
7. You are now ready to play! Start a new savefile and go!

## FAQ
### I can't leave Outset/Aboda
You need to get two locations, `Outset Clear Rocks` and `Outset Bee Item` and reload the room before Zelda will spawn to let you on the train, and you need the `Forest Glyph` and `Cannon` to use the train.

### My train is slow
You can adjust the train speed with `/train` in your bizhawk client

### Is there a map tracker?
Yes! Get [Universal Tracker](https://github.com/FarisTheAncient/Archipelago/releases) and it will create a simple map page!
