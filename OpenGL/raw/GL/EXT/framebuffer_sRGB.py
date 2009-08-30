'''OpenGL extension EXT.framebuffer_sRGB

The official definition of this extension is available here:
http://oss.sgi.com/projects/ogl-sample/registry/EXT/framebuffer_sRGB.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_EXT_framebuffer_sRGB'
_DEPRECATED = False
GL_FRAMEBUFFER_SRGB_EXT = constant.Constant( 'GL_FRAMEBUFFER_SRGB_EXT', 0x8DB9 )
GL_FRAMEBUFFER_SRGB_CAPABLE_EXT = constant.Constant( 'GL_FRAMEBUFFER_SRGB_CAPABLE_EXT', 0x8DBA )


def glInitFramebufferSrgbEXT():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )