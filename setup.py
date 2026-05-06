# -*- coding: utf-8 -*-
import cx_Freeze
addtional_mods = ['numpy.core._methods', 'numpy.lib.format']
executables=[cx_Freeze.Executable("PLAY.py")]

cx_Freeze.setup(
    name="Brawlers Arena",
    version="0.9.5",
    description="Game",
    options = {'build_exe': {'includes': addtional_mods}},
    executables=executables,
    )