# -*- mode: python -*-

block_cipher = None


a = Analysis(['core\\聊天软件的实现_v1.1\\reg_Tkinter.py'],
             pathex=['E:\\hyx'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='reg_Tkinter',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
