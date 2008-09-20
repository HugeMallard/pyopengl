'''OpenGL extension SGIX.FfdMask

This module customises the behaviour of the 
OpenGL.raw.GL.SGIX.FfdMask to provide a more 
Python-friendly API
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.SGIX.FfdMask import *
### END AUTOGENERATED SECTION