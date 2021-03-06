# Animal-Mashing

![startmenu](https://user-images.githubusercontent.com/10473118/49051851-649df380-f19e-11e8-8830-da4395e9cf53.png)

<img width="730" alt="gamescreenshot" src="https://user-images.githubusercontent.com/10473118/49052014-fe65a080-f19e-11e8-9039-7df37cc2a59d.png">

This is a python game made with pygame for HackHighSchool, a high school program for students. As a mentor, I made a simple game for showcase. The point of the game is to mash buttons and see who is the fastest. There are two players. The left player uses the left shift key, and the right player uses the right shift key for control. Escape is used to exit the game screen during game intro or you can quit right away by clicking the top left corner 'x' for window exit. Enter is used to start the countdown timer for when the game starts!

Big thanks to Xuan Zhu (xlz447) for helping with debugging, photoshop skills, and working hard to make an executable version! Also big thanks to kenney.nl for the free assets used in the game and free intro music used from:
https://opengameart.org/content/frozen-jam-seamless-loop

Run the commands to compile the game in the terminal. Make sure you have python and pygame.  
```
python Animal-Mashing.py
```
If you don't have pygame use the following code to install it
```
pip install --user pygame
```
To make the executable, we use pyinstaller. Make sure you have it installed as well.
First run the following code to make the spec file
```
pyi-makespec --onefile Animal-Mashing.py
```
Next, add this code into the spec file after the 'a'. This is to add the resources to the executable library.
```
a.datas += [
            ('graphics/bgimage.png', './graphics/bgimage.png', 'graphics'),
            ('graphics/chick.png', './graphics/chick.png', 'graphics'),
            ('graphics/duck.png', './graphics/duck.png', 'graphics'),
            ('graphics/elephant.png', './graphics/elephant.png', 'graphics'),
            ('graphics/hippo.png', './graphics/hippo.png', 'graphics'),
            ('graphics/hourse.png', './graphics/horse.png', 'graphics'),
            ('graphics/p1win.png', './graphics/p1win.png', 'graphics'),
            ('graphics/p2win.png', './graphics/p2win.png', 'graphics'),
            ('graphics/parrot.png', './graphics/parrot.png', 'graphics'),
            ('graphics/penguin.png', './graphics/penguin.png', 'graphics'),
            ('graphics/pig.png', './graphics/pig.png', 'graphics'),
            ('graphics/startmenu.png', './graphics/startmenu.png', 'graphics'),
            ('graphics/whale.png', './graphics/whale.png', 'graphics'),
            ('sounds/1.ogg', './sounds/1.ogg', 'sounds'),
            ('sounds/2.ogg', './sounds/2.ogg', 'sounds'),
            ('sounds/3.ogg', './sounds/3.ogg', 'sounds'),
            ('sounds/begin.ogg', './sounds/begin.ogg', 'sounds'),
            ('sounds/flawless_victory.ogg', './sounds/flawless_victory.ogg', 'sounds'),
            ('sounds/FrozenJam.ogg', './sounds/FrozenJam.ogg', 'sounds'),
            ('sounds/jingle1.ogg', './sounds/jingle1.ogg', 'sounds'),
            ('sounds/jingle2.ogg', './sounds/jingle2.ogg', 'sounds'),
            ('sounds/player_1.ogg', './sounds/player_1.ogg', 'sounds'),
            ('sounds/player_2.ogg', './sounds/player_2.ogg', 'sounds'),
            ('sounds/prepare_yourself.ogg', './sounds/prepare_yourself.ogg', 'sounds')
           ]
```
Lastly, run the following code.
```
pyinstaller --onefile Animal-Mashing.spec
```
The executable will come out in the dist folder. It should work by itself. 

---
MIT License

Copyright (c) 2018 Luigi Zheng

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
