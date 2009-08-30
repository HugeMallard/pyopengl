'''OpenGL extension EXT.texture_env_add

Overview (from the spec)
    
    New texture environment function ADD is supported with the following 
    equation: 
                        Cv = Cf + Ct
    
    New function may be specified by calling TexEnv with ADD token.
    

The official definition of this extension is available here:
http://oss.sgi.com/projects/ogl-sample/registry/EXT/texture_env_add.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_EXT_texture_env_add'
_DEPRECATED = False



def glInitTextureEnvAddEXT():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )