# -*- mode: python -*-

__testname__ = 'test_multiprocess_onefile'

a = Analysis([__testname__ + '.py'],
             pathex=[])
a = Analysis([__testname__ + '.py'],
             pathex=[],
             hookspath=None)
pyz = PYZ(a.pure)
exe = EXE( pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name=os.path.join('dist', __testname__ + '.exe'),
          debug=True,
          strip=None,
          upx=True,
          console=True )
