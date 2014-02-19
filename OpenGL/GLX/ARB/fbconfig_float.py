'''OpenGL extension ARB.fbconfig_float

This module customises the behaviour of the 
OpenGL.raw.GLX.ARB.fbconfig_float to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ARB/fbconfig_float.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GLX import _types
from OpenGL.raw.GLX.ARB.fbconfig_float import *
from OpenGL.raw.GLX.ARB.fbconfig_float import _EXTENSION_NAME

def glInitFbconfigFloatARB():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

### END AUTOGENERATED SECTION