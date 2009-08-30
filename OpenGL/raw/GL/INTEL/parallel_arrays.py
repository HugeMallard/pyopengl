'''OpenGL extension INTEL.parallel_arrays

Overview (from the spec)
    
    This extension adds the ability to format vertex arrays in a way that's 

The official definition of this extension is available here:
http://oss.sgi.com/projects/ogl-sample/registry/INTEL/parallel_arrays.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_INTEL_parallel_arrays'
_DEPRECATED = False
GL_PARALLEL_ARRAYS_INTEL = constant.Constant( 'GL_PARALLEL_ARRAYS_INTEL', 0x83F4 )
glget.addGLGetConstant( GL_PARALLEL_ARRAYS_INTEL, (1,) )
GL_VERTEX_ARRAY_PARALLEL_POINTERS_INTEL = constant.Constant( 'GL_VERTEX_ARRAY_PARALLEL_POINTERS_INTEL', 0x83F5 )
GL_NORMAL_ARRAY_PARALLEL_POINTERS_INTEL = constant.Constant( 'GL_NORMAL_ARRAY_PARALLEL_POINTERS_INTEL', 0x83F6 )
GL_COLOR_ARRAY_PARALLEL_POINTERS_INTEL = constant.Constant( 'GL_COLOR_ARRAY_PARALLEL_POINTERS_INTEL', 0x83F7 )
GL_TEXTURE_COORD_ARRAY_PARALLEL_POINTERS_INTEL = constant.Constant( 'GL_TEXTURE_COORD_ARRAY_PARALLEL_POINTERS_INTEL', 0x83F8 )
glVertexPointervINTEL = platform.createExtensionFunction( 
'glVertexPointervINTEL',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLint,constants.GLenum,ctypes.POINTER(ctypes.c_void_p),),
doc='glVertexPointervINTEL(GLint(size), GLenum(type), POINTER(ctypes.c_void_p)(pointer)) -> None',
argNames=('size','type','pointer',),
deprecated=_DEPRECATED,
)

glNormalPointervINTEL = platform.createExtensionFunction( 
'glNormalPointervINTEL',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,ctypes.POINTER(ctypes.c_void_p),),
doc='glNormalPointervINTEL(GLenum(type), POINTER(ctypes.c_void_p)(pointer)) -> None',
argNames=('type','pointer',),
deprecated=_DEPRECATED,
)

glColorPointervINTEL = platform.createExtensionFunction( 
'glColorPointervINTEL',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLint,constants.GLenum,ctypes.POINTER(ctypes.c_void_p),),
doc='glColorPointervINTEL(GLint(size), GLenum(type), POINTER(ctypes.c_void_p)(pointer)) -> None',
argNames=('size','type','pointer',),
deprecated=_DEPRECATED,
)

glTexCoordPointervINTEL = platform.createExtensionFunction( 
'glTexCoordPointervINTEL',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLint,constants.GLenum,ctypes.POINTER(ctypes.c_void_p),),
doc='glTexCoordPointervINTEL(GLint(size), GLenum(type), POINTER(ctypes.c_void_p)(pointer)) -> None',
argNames=('size','type','pointer',),
deprecated=_DEPRECATED,
)


def glInitParallelArraysINTEL():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )