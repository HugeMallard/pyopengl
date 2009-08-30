'''OpenGL extension EXT.gpu_shader4

The official definition of this extension is available here:
http://oss.sgi.com/projects/ogl-sample/registry/EXT/gpu_shader4.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_EXT_gpu_shader4'
_DEPRECATED = False
GL_SAMPLER_1D_ARRAY_EXT = constant.Constant( 'GL_SAMPLER_1D_ARRAY_EXT', 0x8DC0 )
GL_SAMPLER_2D_ARRAY_EXT = constant.Constant( 'GL_SAMPLER_2D_ARRAY_EXT', 0x8DC1 )
GL_SAMPLER_BUFFER_EXT = constant.Constant( 'GL_SAMPLER_BUFFER_EXT', 0x8DC2 )
GL_SAMPLER_1D_ARRAY_SHADOW_EXT = constant.Constant( 'GL_SAMPLER_1D_ARRAY_SHADOW_EXT', 0x8DC3 )
GL_SAMPLER_2D_ARRAY_SHADOW_EXT = constant.Constant( 'GL_SAMPLER_2D_ARRAY_SHADOW_EXT', 0x8DC4 )
GL_SAMPLER_CUBE_SHADOW_EXT = constant.Constant( 'GL_SAMPLER_CUBE_SHADOW_EXT', 0x8DC5 )
GL_UNSIGNED_INT_VEC2_EXT = constant.Constant( 'GL_UNSIGNED_INT_VEC2_EXT', 0x8DC6 )
GL_UNSIGNED_INT_VEC3_EXT = constant.Constant( 'GL_UNSIGNED_INT_VEC3_EXT', 0x8DC7 )
GL_UNSIGNED_INT_VEC4_EXT = constant.Constant( 'GL_UNSIGNED_INT_VEC4_EXT', 0x8DC8 )
GL_INT_SAMPLER_1D_EXT = constant.Constant( 'GL_INT_SAMPLER_1D_EXT', 0x8DC9 )
GL_INT_SAMPLER_2D_EXT = constant.Constant( 'GL_INT_SAMPLER_2D_EXT', 0x8DCA )
GL_INT_SAMPLER_3D_EXT = constant.Constant( 'GL_INT_SAMPLER_3D_EXT', 0x8DCB )
GL_INT_SAMPLER_CUBE_EXT = constant.Constant( 'GL_INT_SAMPLER_CUBE_EXT', 0x8DCC )
GL_INT_SAMPLER_2D_RECT_EXT = constant.Constant( 'GL_INT_SAMPLER_2D_RECT_EXT', 0x8DCD )
GL_INT_SAMPLER_1D_ARRAY_EXT = constant.Constant( 'GL_INT_SAMPLER_1D_ARRAY_EXT', 0x8DCE )
GL_INT_SAMPLER_2D_ARRAY_EXT = constant.Constant( 'GL_INT_SAMPLER_2D_ARRAY_EXT', 0x8DCF )
GL_INT_SAMPLER_BUFFER_EXT = constant.Constant( 'GL_INT_SAMPLER_BUFFER_EXT', 0x8DD0 )
GL_UNSIGNED_INT_SAMPLER_1D_EXT = constant.Constant( 'GL_UNSIGNED_INT_SAMPLER_1D_EXT', 0x8DD1 )
GL_UNSIGNED_INT_SAMPLER_2D_EXT = constant.Constant( 'GL_UNSIGNED_INT_SAMPLER_2D_EXT', 0x8DD2 )
GL_UNSIGNED_INT_SAMPLER_3D_EXT = constant.Constant( 'GL_UNSIGNED_INT_SAMPLER_3D_EXT', 0x8DD3 )
GL_UNSIGNED_INT_SAMPLER_CUBE_EXT = constant.Constant( 'GL_UNSIGNED_INT_SAMPLER_CUBE_EXT', 0x8DD4 )
GL_UNSIGNED_INT_SAMPLER_2D_RECT_EXT = constant.Constant( 'GL_UNSIGNED_INT_SAMPLER_2D_RECT_EXT', 0x8DD5 )
GL_UNSIGNED_INT_SAMPLER_1D_ARRAY_EXT = constant.Constant( 'GL_UNSIGNED_INT_SAMPLER_1D_ARRAY_EXT', 0x8DD6 )
GL_UNSIGNED_INT_SAMPLER_2D_ARRAY_EXT = constant.Constant( 'GL_UNSIGNED_INT_SAMPLER_2D_ARRAY_EXT', 0x8DD7 )
GL_UNSIGNED_INT_SAMPLER_BUFFER_EXT = constant.Constant( 'GL_UNSIGNED_INT_SAMPLER_BUFFER_EXT', 0x8DD8 )
glGetUniformuivEXT = platform.createExtensionFunction( 
'glGetUniformuivEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLint,arrays.GLuintArray,),
doc='glGetUniformuivEXT(GLuint(program), GLint(location), GLuintArray(params)) -> None',
argNames=('program','location','params',),
deprecated=_DEPRECATED,
)

glBindFragDataLocationEXT = platform.createExtensionFunction( 
'glBindFragDataLocationEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLuint,arrays.GLcharArray,),
doc='glBindFragDataLocationEXT(GLuint(program), GLuint(color), GLcharArray(name)) -> None',
argNames=('program','color','name',),
deprecated=_DEPRECATED,
)

glGetFragDataLocationEXT = platform.createExtensionFunction( 
'glGetFragDataLocationEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=constants.GLint, 
argTypes=(constants.GLuint,arrays.GLcharArray,),
doc='glGetFragDataLocationEXT(GLuint(program), GLcharArray(name)) -> constants.GLint',
argNames=('program','name',),
deprecated=_DEPRECATED,
)

glUniform1uiEXT = platform.createExtensionFunction( 
'glUniform1uiEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLint,constants.GLuint,),
doc='glUniform1uiEXT(GLint(location), GLuint(v0)) -> None',
argNames=('location','v0',),
deprecated=_DEPRECATED,
)

glUniform2uiEXT = platform.createExtensionFunction( 
'glUniform2uiEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLint,constants.GLuint,constants.GLuint,),
doc='glUniform2uiEXT(GLint(location), GLuint(v0), GLuint(v1)) -> None',
argNames=('location','v0','v1',),
deprecated=_DEPRECATED,
)

glUniform3uiEXT = platform.createExtensionFunction( 
'glUniform3uiEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLint,constants.GLuint,constants.GLuint,constants.GLuint,),
doc='glUniform3uiEXT(GLint(location), GLuint(v0), GLuint(v1), GLuint(v2)) -> None',
argNames=('location','v0','v1','v2',),
deprecated=_DEPRECATED,
)

glUniform4uiEXT = platform.createExtensionFunction( 
'glUniform4uiEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLint,constants.GLuint,constants.GLuint,constants.GLuint,constants.GLuint,),
doc='glUniform4uiEXT(GLint(location), GLuint(v0), GLuint(v1), GLuint(v2), GLuint(v3)) -> None',
argNames=('location','v0','v1','v2','v3',),
deprecated=_DEPRECATED,
)

glUniform1uivEXT = platform.createExtensionFunction( 
'glUniform1uivEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLint,constants.GLsizei,arrays.GLuintArray,),
doc='glUniform1uivEXT(GLint(location), GLsizei(count), GLuintArray(value)) -> None',
argNames=('location','count','value',),
deprecated=_DEPRECATED,
)

glUniform2uivEXT = platform.createExtensionFunction( 
'glUniform2uivEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLint,constants.GLsizei,arrays.GLuintArray,),
doc='glUniform2uivEXT(GLint(location), GLsizei(count), GLuintArray(value)) -> None',
argNames=('location','count','value',),
deprecated=_DEPRECATED,
)

glUniform3uivEXT = platform.createExtensionFunction( 
'glUniform3uivEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLint,constants.GLsizei,arrays.GLuintArray,),
doc='glUniform3uivEXT(GLint(location), GLsizei(count), GLuintArray(value)) -> None',
argNames=('location','count','value',),
deprecated=_DEPRECATED,
)

glUniform4uivEXT = platform.createExtensionFunction( 
'glUniform4uivEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLint,constants.GLsizei,arrays.GLuintArray,),
doc='glUniform4uivEXT(GLint(location), GLsizei(count), GLuintArray(value)) -> None',
argNames=('location','count','value',),
deprecated=_DEPRECATED,
)


def glInitGpuShader4EXT():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )