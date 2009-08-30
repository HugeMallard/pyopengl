'''OpenGL extension EXT.framebuffer_object

Overview (from the spec)
    
    This extension defines a simple interface for drawing to rendering
    destinations other than the buffers provided to the GL by the
    window-system.
    
    In this extension, these newly defined rendering destinations are
    known collectively as "framebuffer-attachable images".  This
    extension provides a mechanism for attaching framebuffer-attachable
    images to the GL framebuffer as one of the standard GL logical
    buffers: color, depth, and stencil.  (Attaching a
    framebuffer-attachable image to the accum logical buffer is left for
    a future extension to define).  When a framebuffer-attachable image
    is attached to the framebuffer, it is used as the source and
    destination of fragment operations as described in Chapter 4.
    
    By allowing the use of a framebuffer-attachable image as a rendering
    destination, this extension enables a form of "offscreen" rendering.
    Furthermore, "render to texture" is supported by allowing the images
    of a texture to be used as framebuffer-attachable images.  A
    particular image of a texture object is selected for use as a
    framebuffer-attachable image by specifying the mipmap level, cube
    map face (for a cube map texture), and z-offset (for a 3D texture)
    that identifies the image.  The "render to texture" semantics of
    this extension are similar to performing traditional rendering to
    the framebuffer, followed immediately by a call to CopyTexSubImage.
    However, by using this extension instead, an application can achieve
    the same effect, but with the advantage that the GL can usually
    eliminate the data copy that would have been incurred by calling
    CopyTexSubImage.
    
    This extension also defines a new GL object type, called a
    "renderbuffer", which encapsulates a single 2D pixel image.  The
    image of renderbuffer can be used as a framebuffer-attachable image
    for generalized offscreen rendering and it also provides a means to
    support rendering to GL logical buffer types which have no
    corresponding texture format (stencil, accum, etc).  A renderbuffer
    is similar to a texture in that both renderbuffers and textures can
    be independently allocated and shared among multiple contexts.  The
    framework defined by this extension is general enough that support
    for attaching images from GL objects other than textures and
    renderbuffers could be added by layered extensions.
    
    To facilitate efficient switching between collections of
    framebuffer-attachable images, this extension introduces another new
    GL object, called a framebuffer object.  A framebuffer object
    contains the state that defines the traditional GL framebuffer,
    including its set of images.  Prior to this extension, it was the
    window-system which defined and managed this collection of images,
    traditionally by grouping them into a "drawable".  The window-system
    API's would also provide a function (i.e., wglMakeCurrent,
    glXMakeCurrent, aglSetDrawable, etc.) to bind a drawable with a GL
    context (as is done in the WGL_ARB_pbuffer extension).  In this
    extension however, this functionality is subsumed by the GL and the
    GL provides the function BindFramebufferEXT to bind a framebuffer
    object to the current context.  Later, the context can bind back to
    the window-system-provided framebuffer in order to display rendered
    content.
    
    Previous extensions that enabled rendering to a texture have been
    much more complicated.  One example is the combination of
    ARB_pbuffer and ARB_render_texture, both of which are window-system
    extensions.  This combination requires calling MakeCurrent, an
    operation that may be expensive, to switch between the window and
    the pbuffer drawables.  An application must create one pbuffer per
    renderable texture in order to portably use ARB_render_texture.  An
    application must maintain at least one GL context per texture
    format, because each context can only operate on a single
    pixelformat or FBConfig.  All of these characteristics make
    ARB_render_texture both inefficient and cumbersome to use.
    
    EXT_framebuffer_object, on the other hand, is both simpler to use
    and more efficient than ARB_render_texture.  The
    EXT_framebuffer_object API is contained wholly within the GL API and
    has no (non-portable) window-system components.  Under
    EXT_framebuffer_object, it is not necessary to create a second GL
    context when rendering to a texture image whose format differs from
    that of the window.  Finally, unlike the pbuffers of
    ARB_render_texture, a single framebuffer object can facilitate
    rendering to an unlimited number of texture objects.

The official definition of this extension is available here:
http://oss.sgi.com/projects/ogl-sample/registry/EXT/framebuffer_object.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_EXT_framebuffer_object'
_DEPRECATED = False
GL_INVALID_FRAMEBUFFER_OPERATION_EXT = constant.Constant( 'GL_INVALID_FRAMEBUFFER_OPERATION_EXT', 0x506 )
GL_MAX_RENDERBUFFER_SIZE_EXT = constant.Constant( 'GL_MAX_RENDERBUFFER_SIZE_EXT', 0x84E8 )
glget.addGLGetConstant( GL_MAX_RENDERBUFFER_SIZE_EXT, (1,) )
GL_FRAMEBUFFER_BINDING_EXT = constant.Constant( 'GL_FRAMEBUFFER_BINDING_EXT', 0x8CA6 )
glget.addGLGetConstant( GL_FRAMEBUFFER_BINDING_EXT, (1,) )
GL_RENDERBUFFER_BINDING_EXT = constant.Constant( 'GL_RENDERBUFFER_BINDING_EXT', 0x8CA7 )
glget.addGLGetConstant( GL_RENDERBUFFER_BINDING_EXT, (1,) )
GL_FRAMEBUFFER_ATTACHMENT_OBJECT_TYPE_EXT = constant.Constant( 'GL_FRAMEBUFFER_ATTACHMENT_OBJECT_TYPE_EXT', 0x8CD0 )
GL_FRAMEBUFFER_ATTACHMENT_OBJECT_NAME_EXT = constant.Constant( 'GL_FRAMEBUFFER_ATTACHMENT_OBJECT_NAME_EXT', 0x8CD1 )
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LEVEL_EXT = constant.Constant( 'GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LEVEL_EXT', 0x8CD2 )
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_CUBE_MAP_FACE_EXT = constant.Constant( 'GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_CUBE_MAP_FACE_EXT', 0x8CD3 )
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_3D_ZOFFSET_EXT = constant.Constant( 'GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_3D_ZOFFSET_EXT', 0x8CD4 )
GL_FRAMEBUFFER_COMPLETE_EXT = constant.Constant( 'GL_FRAMEBUFFER_COMPLETE_EXT', 0x8CD5 )
GL_FRAMEBUFFER_INCOMPLETE_ATTACHMENT_EXT = constant.Constant( 'GL_FRAMEBUFFER_INCOMPLETE_ATTACHMENT_EXT', 0x8CD6 )
GL_FRAMEBUFFER_INCOMPLETE_MISSING_ATTACHMENT_EXT = constant.Constant( 'GL_FRAMEBUFFER_INCOMPLETE_MISSING_ATTACHMENT_EXT', 0x8CD7 )
GL_FRAMEBUFFER_INCOMPLETE_DIMENSIONS_EXT = constant.Constant( 'GL_FRAMEBUFFER_INCOMPLETE_DIMENSIONS_EXT', 0x8CD9 )
GL_FRAMEBUFFER_INCOMPLETE_FORMATS_EXT = constant.Constant( 'GL_FRAMEBUFFER_INCOMPLETE_FORMATS_EXT', 0x8CDA )
GL_FRAMEBUFFER_INCOMPLETE_DRAW_BUFFER_EXT = constant.Constant( 'GL_FRAMEBUFFER_INCOMPLETE_DRAW_BUFFER_EXT', 0x8CDB )
GL_FRAMEBUFFER_INCOMPLETE_READ_BUFFER_EXT = constant.Constant( 'GL_FRAMEBUFFER_INCOMPLETE_READ_BUFFER_EXT', 0x8CDC )
GL_FRAMEBUFFER_UNSUPPORTED_EXT = constant.Constant( 'GL_FRAMEBUFFER_UNSUPPORTED_EXT', 0x8CDD )
GL_MAX_COLOR_ATTACHMENTS_EXT = constant.Constant( 'GL_MAX_COLOR_ATTACHMENTS_EXT', 0x8CDF )
glget.addGLGetConstant( GL_MAX_COLOR_ATTACHMENTS_EXT, (1,) )
GL_COLOR_ATTACHMENT0_EXT = constant.Constant( 'GL_COLOR_ATTACHMENT0_EXT', 0x8CE0 )
GL_COLOR_ATTACHMENT1_EXT = constant.Constant( 'GL_COLOR_ATTACHMENT1_EXT', 0x8CE1 )
GL_COLOR_ATTACHMENT2_EXT = constant.Constant( 'GL_COLOR_ATTACHMENT2_EXT', 0x8CE2 )
GL_COLOR_ATTACHMENT3_EXT = constant.Constant( 'GL_COLOR_ATTACHMENT3_EXT', 0x8CE3 )
GL_COLOR_ATTACHMENT4_EXT = constant.Constant( 'GL_COLOR_ATTACHMENT4_EXT', 0x8CE4 )
GL_COLOR_ATTACHMENT5_EXT = constant.Constant( 'GL_COLOR_ATTACHMENT5_EXT', 0x8CE5 )
GL_COLOR_ATTACHMENT6_EXT = constant.Constant( 'GL_COLOR_ATTACHMENT6_EXT', 0x8CE6 )
GL_COLOR_ATTACHMENT7_EXT = constant.Constant( 'GL_COLOR_ATTACHMENT7_EXT', 0x8CE7 )
GL_COLOR_ATTACHMENT8_EXT = constant.Constant( 'GL_COLOR_ATTACHMENT8_EXT', 0x8CE8 )
GL_COLOR_ATTACHMENT9_EXT = constant.Constant( 'GL_COLOR_ATTACHMENT9_EXT', 0x8CE9 )
GL_COLOR_ATTACHMENT10_EXT = constant.Constant( 'GL_COLOR_ATTACHMENT10_EXT', 0x8CEA )
GL_COLOR_ATTACHMENT11_EXT = constant.Constant( 'GL_COLOR_ATTACHMENT11_EXT', 0x8CEB )
GL_COLOR_ATTACHMENT12_EXT = constant.Constant( 'GL_COLOR_ATTACHMENT12_EXT', 0x8CEC )
GL_COLOR_ATTACHMENT13_EXT = constant.Constant( 'GL_COLOR_ATTACHMENT13_EXT', 0x8CED )
GL_COLOR_ATTACHMENT14_EXT = constant.Constant( 'GL_COLOR_ATTACHMENT14_EXT', 0x8CEE )
GL_COLOR_ATTACHMENT15_EXT = constant.Constant( 'GL_COLOR_ATTACHMENT15_EXT', 0x8CEF )
GL_DEPTH_ATTACHMENT_EXT = constant.Constant( 'GL_DEPTH_ATTACHMENT_EXT', 0x8D00 )
GL_STENCIL_ATTACHMENT_EXT = constant.Constant( 'GL_STENCIL_ATTACHMENT_EXT', 0x8D20 )
GL_FRAMEBUFFER_EXT = constant.Constant( 'GL_FRAMEBUFFER_EXT', 0x8D40 )
GL_RENDERBUFFER_EXT = constant.Constant( 'GL_RENDERBUFFER_EXT', 0x8D41 )
GL_RENDERBUFFER_WIDTH_EXT = constant.Constant( 'GL_RENDERBUFFER_WIDTH_EXT', 0x8D42 )
GL_RENDERBUFFER_HEIGHT_EXT = constant.Constant( 'GL_RENDERBUFFER_HEIGHT_EXT', 0x8D43 )
GL_RENDERBUFFER_INTERNAL_FORMAT_EXT = constant.Constant( 'GL_RENDERBUFFER_INTERNAL_FORMAT_EXT', 0x8D44 )
GL_STENCIL_INDEX1_EXT = constant.Constant( 'GL_STENCIL_INDEX1_EXT', 0x8D46 )
GL_STENCIL_INDEX4_EXT = constant.Constant( 'GL_STENCIL_INDEX4_EXT', 0x8D47 )
GL_STENCIL_INDEX8_EXT = constant.Constant( 'GL_STENCIL_INDEX8_EXT', 0x8D48 )
GL_STENCIL_INDEX16_EXT = constant.Constant( 'GL_STENCIL_INDEX16_EXT', 0x8D49 )
GL_RENDERBUFFER_RED_SIZE_EXT = constant.Constant( 'GL_RENDERBUFFER_RED_SIZE_EXT', 0x8D50 )
GL_RENDERBUFFER_GREEN_SIZE_EXT = constant.Constant( 'GL_RENDERBUFFER_GREEN_SIZE_EXT', 0x8D51 )
GL_RENDERBUFFER_BLUE_SIZE_EXT = constant.Constant( 'GL_RENDERBUFFER_BLUE_SIZE_EXT', 0x8D52 )
GL_RENDERBUFFER_ALPHA_SIZE_EXT = constant.Constant( 'GL_RENDERBUFFER_ALPHA_SIZE_EXT', 0x8D53 )
GL_RENDERBUFFER_DEPTH_SIZE_EXT = constant.Constant( 'GL_RENDERBUFFER_DEPTH_SIZE_EXT', 0x8D54 )
GL_RENDERBUFFER_STENCIL_SIZE_EXT = constant.Constant( 'GL_RENDERBUFFER_STENCIL_SIZE_EXT', 0x8D55 )
glIsRenderbufferEXT = platform.createExtensionFunction( 
'glIsRenderbufferEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=constants.GLboolean, 
argTypes=(constants.GLuint,),
doc='glIsRenderbufferEXT(GLuint(renderbuffer)) -> constants.GLboolean',
argNames=('renderbuffer',),
deprecated=_DEPRECATED,
)

glBindRenderbufferEXT = platform.createExtensionFunction( 
'glBindRenderbufferEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLuint,),
doc='glBindRenderbufferEXT(GLenum(target), GLuint(renderbuffer)) -> None',
argNames=('target','renderbuffer',),
deprecated=_DEPRECATED,
)

glDeleteRenderbuffersEXT = platform.createExtensionFunction( 
'glDeleteRenderbuffersEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLsizei,arrays.GLuintArray,),
doc='glDeleteRenderbuffersEXT(GLsizei(n), GLuintArray(renderbuffers)) -> None',
argNames=('n','renderbuffers',),
deprecated=_DEPRECATED,
)

glGenRenderbuffersEXT = platform.createExtensionFunction( 
'glGenRenderbuffersEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLsizei,arrays.GLuintArray,),
doc='glGenRenderbuffersEXT(GLsizei(n), GLuintArray(renderbuffers)) -> None',
argNames=('n','renderbuffers',),
deprecated=_DEPRECATED,
)

glRenderbufferStorageEXT = platform.createExtensionFunction( 
'glRenderbufferStorageEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLenum,constants.GLsizei,constants.GLsizei,),
doc='glRenderbufferStorageEXT(GLenum(target), GLenum(internalformat), GLsizei(width), GLsizei(height)) -> None',
argNames=('target','internalformat','width','height',),
deprecated=_DEPRECATED,
)

glGetRenderbufferParameterivEXT = platform.createExtensionFunction( 
'glGetRenderbufferParameterivEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLenum,arrays.GLintArray,),
doc='glGetRenderbufferParameterivEXT(GLenum(target), GLenum(pname), GLintArray(params)) -> None',
argNames=('target','pname','params',),
deprecated=_DEPRECATED,
)

glIsFramebufferEXT = platform.createExtensionFunction( 
'glIsFramebufferEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=constants.GLboolean, 
argTypes=(constants.GLuint,),
doc='glIsFramebufferEXT(GLuint(framebuffer)) -> constants.GLboolean',
argNames=('framebuffer',),
deprecated=_DEPRECATED,
)

glBindFramebufferEXT = platform.createExtensionFunction( 
'glBindFramebufferEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLuint,),
doc='glBindFramebufferEXT(GLenum(target), GLuint(framebuffer)) -> None',
argNames=('target','framebuffer',),
deprecated=_DEPRECATED,
)

glDeleteFramebuffersEXT = platform.createExtensionFunction( 
'glDeleteFramebuffersEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLsizei,arrays.GLuintArray,),
doc='glDeleteFramebuffersEXT(GLsizei(n), GLuintArray(framebuffers)) -> None',
argNames=('n','framebuffers',),
deprecated=_DEPRECATED,
)

glGenFramebuffersEXT = platform.createExtensionFunction( 
'glGenFramebuffersEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLsizei,arrays.GLuintArray,),
doc='glGenFramebuffersEXT(GLsizei(n), GLuintArray(framebuffers)) -> None',
argNames=('n','framebuffers',),
deprecated=_DEPRECATED,
)

glCheckFramebufferStatusEXT = platform.createExtensionFunction( 
'glCheckFramebufferStatusEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=constants.GLenum, 
argTypes=(constants.GLenum,),
doc='glCheckFramebufferStatusEXT(GLenum(target)) -> constants.GLenum',
argNames=('target',),
deprecated=_DEPRECATED,
)

glFramebufferTexture1DEXT = platform.createExtensionFunction( 
'glFramebufferTexture1DEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLenum,constants.GLenum,constants.GLuint,constants.GLint,),
doc='glFramebufferTexture1DEXT(GLenum(target), GLenum(attachment), GLenum(textarget), GLuint(texture), GLint(level)) -> None',
argNames=('target','attachment','textarget','texture','level',),
deprecated=_DEPRECATED,
)

glFramebufferTexture2DEXT = platform.createExtensionFunction( 
'glFramebufferTexture2DEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLenum,constants.GLenum,constants.GLuint,constants.GLint,),
doc='glFramebufferTexture2DEXT(GLenum(target), GLenum(attachment), GLenum(textarget), GLuint(texture), GLint(level)) -> None',
argNames=('target','attachment','textarget','texture','level',),
deprecated=_DEPRECATED,
)

glFramebufferTexture3DEXT = platform.createExtensionFunction( 
'glFramebufferTexture3DEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLenum,constants.GLenum,constants.GLuint,constants.GLint,constants.GLint,),
doc='glFramebufferTexture3DEXT(GLenum(target), GLenum(attachment), GLenum(textarget), GLuint(texture), GLint(level), GLint(zoffset)) -> None',
argNames=('target','attachment','textarget','texture','level','zoffset',),
deprecated=_DEPRECATED,
)

glFramebufferRenderbufferEXT = platform.createExtensionFunction( 
'glFramebufferRenderbufferEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLenum,constants.GLenum,constants.GLuint,),
doc='glFramebufferRenderbufferEXT(GLenum(target), GLenum(attachment), GLenum(renderbuffertarget), GLuint(renderbuffer)) -> None',
argNames=('target','attachment','renderbuffertarget','renderbuffer',),
deprecated=_DEPRECATED,
)

glGetFramebufferAttachmentParameterivEXT = platform.createExtensionFunction( 
'glGetFramebufferAttachmentParameterivEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLenum,constants.GLenum,arrays.GLintArray,),
doc='glGetFramebufferAttachmentParameterivEXT(GLenum(target), GLenum(attachment), GLenum(pname), GLintArray(params)) -> None',
argNames=('target','attachment','pname','params',),
deprecated=_DEPRECATED,
)

glGenerateMipmapEXT = platform.createExtensionFunction( 
'glGenerateMipmapEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,),
doc='glGenerateMipmapEXT(GLenum(target)) -> None',
argNames=('target',),
deprecated=_DEPRECATED,
)


def glInitFramebufferObjectEXT():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )