'''OpenGL extension ATI.meminfo

The official definition of this extension is available here:
http://oss.sgi.com/projects/ogl-sample/registry/ATI/meminfo.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_ATI_meminfo'
_DEPRECATED = False
GL_VBO_FREE_MEMORY_ATI = constant.Constant( 'GL_VBO_FREE_MEMORY_ATI', 0x87FB )
GL_TEXTURE_FREE_MEMORY_ATI = constant.Constant( 'GL_TEXTURE_FREE_MEMORY_ATI', 0x87FC )
GL_RENDERBUFFER_FREE_MEMORY_ATI = constant.Constant( 'GL_RENDERBUFFER_FREE_MEMORY_ATI', 0x87FD )


def glInitMeminfoATI():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )