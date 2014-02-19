'''OpenGL extension ARB.internalformat_query2

This module customises the behaviour of the 
OpenGL.raw.GL.ARB.internalformat_query2 to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ARB/internalformat_query2.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL import _types
from OpenGL.raw.GL.ARB.internalformat_query2 import *
from OpenGL.raw.GL.ARB.internalformat_query2 import _EXTENSION_NAME

def glInitInternalformatQuery2ARB():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

### END AUTOGENERATED SECTION