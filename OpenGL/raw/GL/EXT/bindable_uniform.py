'''OpenGL extension EXT.bindable_uniform

The official definition of this extension is available here:
http://oss.sgi.com/projects/ogl-sample/registry/EXT/bindable_uniform.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_EXT_bindable_uniform'
_DEPRECATED = False
GL_MAX_VERTEX_BINDABLE_UNIFORMS_EXT = constant.Constant( 'GL_MAX_VERTEX_BINDABLE_UNIFORMS_EXT', 0x8DE2 )
GL_MAX_FRAGMENT_BINDABLE_UNIFORMS_EXT = constant.Constant( 'GL_MAX_FRAGMENT_BINDABLE_UNIFORMS_EXT', 0x8DE3 )
GL_MAX_GEOMETRY_BINDABLE_UNIFORMS_EXT = constant.Constant( 'GL_MAX_GEOMETRY_BINDABLE_UNIFORMS_EXT', 0x8DE4 )
GL_MAX_BINDABLE_UNIFORM_SIZE_EXT = constant.Constant( 'GL_MAX_BINDABLE_UNIFORM_SIZE_EXT', 0x8DED )
GL_UNIFORM_BUFFER_EXT = constant.Constant( 'GL_UNIFORM_BUFFER_EXT', 0x8DEE )
GL_UNIFORM_BUFFER_BINDING_EXT = constant.Constant( 'GL_UNIFORM_BUFFER_BINDING_EXT', 0x8DEF )
glUniformBufferEXT = platform.createExtensionFunction( 
'glUniformBufferEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLint,constants.GLuint,),
doc='glUniformBufferEXT(GLuint(program), GLint(location), GLuint(buffer)) -> None',
argNames=('program','location','buffer',),
deprecated=_DEPRECATED,
)

glGetUniformBufferSizeEXT = platform.createExtensionFunction( 
'glGetUniformBufferSizeEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=constants.GLint, 
argTypes=(constants.GLuint,constants.GLint,),
doc='glGetUniformBufferSizeEXT(GLuint(program), GLint(location)) -> constants.GLint',
argNames=('program','location',),
deprecated=_DEPRECATED,
)

glGetUniformOffsetEXT = platform.createExtensionFunction( 
'glGetUniformOffsetEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=constants.GLintptr, 
argTypes=(constants.GLuint,constants.GLint,),
doc='glGetUniformOffsetEXT(GLuint(program), GLint(location)) -> constants.GLintptr',
argNames=('program','location',),
deprecated=_DEPRECATED,
)


def glInitBindableUniformEXT():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )