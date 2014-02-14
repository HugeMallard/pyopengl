'''OpenGL extension NV.shadow_samplers_cube

This module customises the behaviour of the 
OpenGL.raw.GL.NV.shadow_samplers_cube to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/NV/shadow_samplers_cube.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL import _types
from OpenGL.raw.GL.NV.shadow_samplers_cube import *
from OpenGL.raw.GL.NV.shadow_samplers_cube import _EXTENSION_NAME

def glInitShadowSamplersCubeNV():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

### END AUTOGENERATED SECTION