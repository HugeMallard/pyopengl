'''OpenGL extension SGIX.texture_lod_bias

Overview (from the spec)
    
    This extension modifies the calculation of texture level of detail 
    parameter LOD, which is represented by the Greek character lambda
    in the GL Specification. The LOD equation assumes that a 2^n x 2^m x 2^l
    texture is band limited at 2^(n-1), 2^(m-1), 2^(l-1).  Often a texture is 
    oversampled or filtered such that the texture is band limited at lower
    frequencies in one or more dimensions.  The result is that texture-mapped 
    primitives appear excessively blurry.  This extension provides biases 
    for n, m, and l in the LOD calculation to to compensate for under or over 
    sampled texture images.  Mipmapped textures can be made to appear sharper or
    blurrier by supplying a negative or positive bias respectively. 
    
    Examples of textures which can benefit from this LOD control include
    video-capture images which are filtered differently horizontally and
    vertically; a texture which appears blurry because it is mapped with 
    a nonuniform scale, such as a road texture which is repeated hundreds of 
    times in one dimension and only once in the other; and textures which
    had to be magnified to a power-of-two for mipmapping.

The official definition of this extension is available here:
http://oss.sgi.com/projects/ogl-sample/registry/SGIX/texture_lod_bias.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_SGIX_texture_lod_bias'
_DEPRECATED = False
GL_TEXTURE_LOD_BIAS_S_SGIX = constant.Constant( 'GL_TEXTURE_LOD_BIAS_S_SGIX', 0x818E )
GL_TEXTURE_LOD_BIAS_T_SGIX = constant.Constant( 'GL_TEXTURE_LOD_BIAS_T_SGIX', 0x818F )
GL_TEXTURE_LOD_BIAS_R_SGIX = constant.Constant( 'GL_TEXTURE_LOD_BIAS_R_SGIX', 0x8190 )


def glInitTextureLodBiasSGIX():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )