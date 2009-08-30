'''OpenGL extension SGIS.texture_color_mask

Overview (from the spec)
    
    This extension implements the same functionality for texture
    updates that glColorMask implements for color buffer updates.
    Masks for updating textures with indexed internal formats
    (the analog for glIndexMask) should be supported by a separate extension.
    
    The extension allows an application to update a subset of
    components in an existing texture.	The masks are applied after
    all pixel transfer operations have been performed, immediately
    prior to writing the texel value into texture memory.  They
    apply to all texture updates.

The official definition of this extension is available here:
http://oss.sgi.com/projects/ogl-sample/registry/SGIS/texture_color_mask.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_SGIS_texture_color_mask'
_DEPRECATED = False
GL_TEXTURE_COLOR_WRITEMASK_SGIS = constant.Constant( 'GL_TEXTURE_COLOR_WRITEMASK_SGIS', 0x81EF )
glTextureColorMaskSGIS = platform.createExtensionFunction( 
'glTextureColorMaskSGIS',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLboolean,constants.GLboolean,constants.GLboolean,constants.GLboolean,),
doc='glTextureColorMaskSGIS(GLboolean(red), GLboolean(green), GLboolean(blue), GLboolean(alpha)) -> None',
argNames=('red','green','blue','alpha',),
deprecated=_DEPRECATED,
)


def glInitTextureColorMaskSGIS():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )