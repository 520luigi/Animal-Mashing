# -*- mode: python -*-

block_cipher = None


a = Analysis(['Animal-Mashing.py'],
             pathex=['/Users/xx/Animal-Mashing'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

a.datas += [
            ('graphics/bgimage.png', '/Users/xx/Animal-Mashing/graphics/bgimage.png', 'graphics'),
            ('graphics/chick.png', '/Users/xx/Animal-Mashing/graphics/chick.png', 'graphics'),
            ('graphics/duck.png', '/Users/xx/Animal-Mashing/graphics/duck.png', 'graphics'),
            ('graphics/elephant.png', '/Users/xx/Animal-Mashing/graphics/elephant.png', 'graphics'),
            ('graphics/hippo.png', '/Users/xx/Animal-Mashing/graphics/hippo.png', 'graphics'),
            ('graphics/horse.png', '/Users/xx/Animal-Mashing/graphics/horse.png', 'graphics'),
            ('graphics/p1win.png', '/Users/xx/Animal-Mashing/graphics/p1win.png', 'graphics'),
            ('graphics/p2win.png', '/Users/xx/Animal-Mashing/graphics/p2win.png', 'graphics'),
            ('graphics/parrot.png', '/Users/xx/Animal-Mashing/graphics/parrot.png', 'graphics'),
            ('graphics/penguin.png', '/Users/xx/Animal-Mashing/graphics/penguin.png', 'graphics'),
            ('graphics/pig.png', '/Users/xx/Animal-Mashing/graphics/pig.png', 'graphics'),
            ('graphics/startmenu.png', '/Users/xx/Animal-Mashing/graphics/startmenu.png', 'graphics'),
            ('graphics/whale.png', '/Users/xx/Animal-Mashing/graphics/whale.png', 'graphics'),
            ('sounds/1.ogg', '/Users/xx/Animal-Mashing/sounds/1.ogg', 'sounds'),
            ('sounds/2.ogg', '/Users/xx/Animal-Mashing/sounds/2.ogg', 'sounds'),
            ('sounds/3.ogg', '/Users/xx/Animal-Mashing/sounds/3.ogg', 'sounds'),
            ('sounds/begin.ogg', '/Users/xx/Animal-Mashing/sounds/begin.ogg', 'sounds'),
            ('sounds/flawless_victory.ogg', '/Users/xx/Animal-Mashing/sounds/flawless_victory.ogg', 'sounds'),
            ('sounds/FrozenJam.ogg', '/Users/xx/Animal-Mashing/sounds/FrozenJam.ogg', 'sounds'),
            ('sounds/jingle1.ogg', '/Users/xx/Animal-Mashing/sounds/jingle1.ogg', 'sounds'),
            ('sounds/jingle2.ogg', '/Users/xx/Animal-Mashing/sounds/jingle2.ogg', 'sounds'),
            ('sounds/player_1.ogg', '/Users/xx/Animal-Mashing/sounds/player_1.ogg', 'sounds'),
            ('sounds/player_2.ogg', '/Users/xx/Animal-Mashing/sounds/player_2.ogg', 'sounds'),
            ('sounds/prepare_yourself.ogg', '/Users/xx/Animal-Mashing/sounds/prepare_yourself.ogg', 'sounds')
           ]

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='Animal-Mashing',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
