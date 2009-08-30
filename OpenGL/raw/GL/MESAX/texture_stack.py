'''OpenGL extension MESAX.texture_stack

Overview (from the spec)
    
    There are a number of circumstances where an application may wish to
    blend two textures out of a larger set of textures.  Moreover, in some
    cases the selected textures may vary on a per-fragment basis within
    a polygon.  Several examples include:
    
       1. High dynamic range textures.  The application stores several
       different "exposures" of an image as different textures.  On a
       per-fragment basis, the application selects which exposures are
       used.
    
       2. A terrain engine where the altitude of a point determines the
       texture applied to it.  If the transition is from beach sand to
       grass to rocks to snow, the application will store each texture
       in a different texture map, and dynamically select which two
       textures to blend at run-time.
    
       3. Storing short video clips in textures.  Each depth slice is a
       single frame of video.
    
    Several solutions to this problem have been proposed, but they either
    involve using a separate texture unit for each texture map or using 3D
    textures without mipmaps.  Both of these options have major drawbacks.
    
    This extension provides a third alternative that eliminates the major
    drawbacks of both previous methods.  A new texture target,
    TEXTURE_2D_STACK, is added that functions identically to TEXTURE_3D in
    all aspects except the sizes of the non-base level images.  In
    traditional 3D texturing, the size of the N+1 LOD is half the size
    of the N LOD in all three dimensions.  For the TEXTURE_2D_STACK target,
    the height and width of the N+1 LOD is halved, but the depth is the
    same for all levels of detail. The texture then becomes a "stack" of
    2D textures.  The per-fragment texel is selected by the R texture
    coordinate.
    
    References:
    
        http://www.opengl.org/discussion_boards/cgi_directory/ultimatebb.cgi?ubb=get_topic;f=3;t=011557
        http://www.opengl.org/discussion_boards/cgi_directory/ultimatebb.cgi?ubb=get_topic;f=3;t=000516
        http://www.opengl.org/discussion_boards/cgi_directory/ultimatebb.cgi?ubb=get_topic;f=3;t=011903
        http://www.delphi3d.net/articles/viewarticle.php?article=terraintex.htm

The official definition of this extension is available here:
http://oss.sgi.com/projects/ogl-sample/registry/MESAX/texture_stack.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_MESAX_texture_stack'
_DEPRECATED = False
GL_TEXTURE_1D_STACK_MESAX = constant.Constant( 'GL_TEXTURE_1D_STACK_MESAX', 0x8759 )
GL_TEXTURE_2D_STACK_MESAX = constant.Constant( 'GL_TEXTURE_2D_STACK_MESAX', 0x875A )
GL_PROXY_TEXTURE_1D_STACK_MESAX = constant.Constant( 'GL_PROXY_TEXTURE_1D_STACK_MESAX', 0x875B )
GL_PROXY_TEXTURE_2D_STACK_MESAX = constant.Constant( 'GL_PROXY_TEXTURE_2D_STACK_MESAX', 0x875C )
GL_TEXTURE_1D_STACK_BINDING_MESAX = constant.Constant( 'GL_TEXTURE_1D_STACK_BINDING_MESAX', 0x875D )
GL_TEXTURE_2D_STACK_BINDING_MESAX = constant.Constant( 'GL_TEXTURE_2D_STACK_BINDING_MESAX', 0x875E )


def glInitTextureStackMESAX():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )