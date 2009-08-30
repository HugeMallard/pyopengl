'''OpenGL extension SGIX.shadow

Overview (from the spec)
    
    This extension defines two new operations to be performed on texture
    values before they are passed on to the filtering subsystem.  These
    operations perform either a <= or >= test on the value from texture
    memory and the iterated R value, and return 1.0 or 0.0 if the test
    passes or fails, respectively.

The official definition of this extension is available here:
http://oss.sgi.com/projects/ogl-sample/registry/SGIX/shadow.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_SGIX_shadow'
_DEPRECATED = False
GL_TEXTURE_COMPARE_SGIX = constant.Constant( 'GL_TEXTURE_COMPARE_SGIX', 0x819A )
GL_TEXTURE_COMPARE_OPERATOR_SGIX = constant.Constant( 'GL_TEXTURE_COMPARE_OPERATOR_SGIX', 0x819B )
GL_TEXTURE_LEQUAL_R_SGIX = constant.Constant( 'GL_TEXTURE_LEQUAL_R_SGIX', 0x819C )
GL_TEXTURE_GEQUAL_R_SGIX = constant.Constant( 'GL_TEXTURE_GEQUAL_R_SGIX', 0x819D )


def glInitShadowSGIX():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )