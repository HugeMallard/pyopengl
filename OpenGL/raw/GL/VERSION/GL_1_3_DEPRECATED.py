'''OpenGL extension VERSION.GL_1_3_DEPRECATED

The official definition of this extension is available here:
http://oss.sgi.com/projects/ogl-sample/registry/VERSION/GL_1_3_DEPRECATED.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_VERSION_GL_1_3'
_DEPRECATED = True
GL_CLIENT_ACTIVE_TEXTURE = constant.Constant( 'GL_CLIENT_ACTIVE_TEXTURE', 0x84E1 )
GL_MAX_TEXTURE_UNITS = constant.Constant( 'GL_MAX_TEXTURE_UNITS', 0x84E2 )
GL_TRANSPOSE_MODELVIEW_MATRIX = constant.Constant( 'GL_TRANSPOSE_MODELVIEW_MATRIX', 0x84E3 )
GL_TRANSPOSE_PROJECTION_MATRIX = constant.Constant( 'GL_TRANSPOSE_PROJECTION_MATRIX', 0x84E4 )
GL_TRANSPOSE_TEXTURE_MATRIX = constant.Constant( 'GL_TRANSPOSE_TEXTURE_MATRIX', 0x84E5 )
GL_TRANSPOSE_COLOR_MATRIX = constant.Constant( 'GL_TRANSPOSE_COLOR_MATRIX', 0x84E6 )
GL_MULTISAMPLE_BIT = constant.Constant( 'GL_MULTISAMPLE_BIT', 0x20000000 )
GL_NORMAL_MAP = constant.Constant( 'GL_NORMAL_MAP', 0x8511 )
GL_REFLECTION_MAP = constant.Constant( 'GL_REFLECTION_MAP', 0x8512 )
GL_COMPRESSED_ALPHA = constant.Constant( 'GL_COMPRESSED_ALPHA', 0x84E9 )
GL_COMPRESSED_LUMINANCE = constant.Constant( 'GL_COMPRESSED_LUMINANCE', 0x84EA )
GL_COMPRESSED_LUMINANCE_ALPHA = constant.Constant( 'GL_COMPRESSED_LUMINANCE_ALPHA', 0x84EB )
GL_COMPRESSED_INTENSITY = constant.Constant( 'GL_COMPRESSED_INTENSITY', 0x84EC )
GL_COMBINE = constant.Constant( 'GL_COMBINE', 0x8570 )
GL_COMBINE_RGB = constant.Constant( 'GL_COMBINE_RGB', 0x8571 )
GL_COMBINE_ALPHA = constant.Constant( 'GL_COMBINE_ALPHA', 0x8572 )
GL_SOURCE0_RGB = constant.Constant( 'GL_SOURCE0_RGB', 0x8580 )
GL_SOURCE1_RGB = constant.Constant( 'GL_SOURCE1_RGB', 0x8581 )
GL_SOURCE2_RGB = constant.Constant( 'GL_SOURCE2_RGB', 0x8582 )
GL_SOURCE0_ALPHA = constant.Constant( 'GL_SOURCE0_ALPHA', 0x8588 )
GL_SOURCE1_ALPHA = constant.Constant( 'GL_SOURCE1_ALPHA', 0x8589 )
GL_SOURCE2_ALPHA = constant.Constant( 'GL_SOURCE2_ALPHA', 0x858A )
GL_OPERAND0_RGB = constant.Constant( 'GL_OPERAND0_RGB', 0x8590 )
GL_OPERAND1_RGB = constant.Constant( 'GL_OPERAND1_RGB', 0x8591 )
GL_OPERAND2_RGB = constant.Constant( 'GL_OPERAND2_RGB', 0x8592 )
GL_OPERAND0_ALPHA = constant.Constant( 'GL_OPERAND0_ALPHA', 0x8598 )
GL_OPERAND1_ALPHA = constant.Constant( 'GL_OPERAND1_ALPHA', 0x8599 )
GL_OPERAND2_ALPHA = constant.Constant( 'GL_OPERAND2_ALPHA', 0x859A )
GL_RGB_SCALE = constant.Constant( 'GL_RGB_SCALE', 0x8573 )
GL_ADD_SIGNED = constant.Constant( 'GL_ADD_SIGNED', 0x8574 )
GL_INTERPOLATE = constant.Constant( 'GL_INTERPOLATE', 0x8575 )
GL_SUBTRACT = constant.Constant( 'GL_SUBTRACT', 0x84E7 )
GL_CONSTANT = constant.Constant( 'GL_CONSTANT', 0x8576 )
GL_PRIMARY_COLOR = constant.Constant( 'GL_PRIMARY_COLOR', 0x8577 )
GL_PREVIOUS = constant.Constant( 'GL_PREVIOUS', 0x8578 )
GL_DOT3_RGB = constant.Constant( 'GL_DOT3_RGB', 0x86AE )
GL_DOT3_RGBA = constant.Constant( 'GL_DOT3_RGBA', 0x86AF )
glClientActiveTexture = platform.createExtensionFunction( 
'glClientActiveTexture',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,),
doc='glClientActiveTexture(GLenum(texture)) -> None',
argNames=('texture',),
deprecated=_DEPRECATED,
)

glMultiTexCoord1d = platform.createExtensionFunction( 
'glMultiTexCoord1d',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLdouble,),
doc='glMultiTexCoord1d(GLenum(target), GLdouble(s)) -> None',
argNames=('target','s',),
deprecated=_DEPRECATED,
)

glMultiTexCoord1dv = platform.createExtensionFunction( 
'glMultiTexCoord1dv',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,arrays.GLdoubleArray,),
doc='glMultiTexCoord1dv(GLenum(target), GLdoubleArray(v)) -> None',
argNames=('target','v',),
deprecated=_DEPRECATED,
)

glMultiTexCoord1f = platform.createExtensionFunction( 
'glMultiTexCoord1f',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLfloat,),
doc='glMultiTexCoord1f(GLenum(target), GLfloat(s)) -> None',
argNames=('target','s',),
deprecated=_DEPRECATED,
)

glMultiTexCoord1fv = platform.createExtensionFunction( 
'glMultiTexCoord1fv',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,arrays.GLfloatArray,),
doc='glMultiTexCoord1fv(GLenum(target), GLfloatArray(v)) -> None',
argNames=('target','v',),
deprecated=_DEPRECATED,
)

glMultiTexCoord1i = platform.createExtensionFunction( 
'glMultiTexCoord1i',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLint,),
doc='glMultiTexCoord1i(GLenum(target), GLint(s)) -> None',
argNames=('target','s',),
deprecated=_DEPRECATED,
)

glMultiTexCoord1iv = platform.createExtensionFunction( 
'glMultiTexCoord1iv',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,arrays.GLintArray,),
doc='glMultiTexCoord1iv(GLenum(target), GLintArray(v)) -> None',
argNames=('target','v',),
deprecated=_DEPRECATED,
)

glMultiTexCoord1s = platform.createExtensionFunction( 
'glMultiTexCoord1s',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLshort,),
doc='glMultiTexCoord1s(GLenum(target), GLshort(s)) -> None',
argNames=('target','s',),
deprecated=_DEPRECATED,
)

glMultiTexCoord1sv = platform.createExtensionFunction( 
'glMultiTexCoord1sv',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,arrays.GLshortArray,),
doc='glMultiTexCoord1sv(GLenum(target), GLshortArray(v)) -> None',
argNames=('target','v',),
deprecated=_DEPRECATED,
)

glMultiTexCoord2d = platform.createExtensionFunction( 
'glMultiTexCoord2d',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLdouble,constants.GLdouble,),
doc='glMultiTexCoord2d(GLenum(target), GLdouble(s), GLdouble(t)) -> None',
argNames=('target','s','t',),
deprecated=_DEPRECATED,
)

glMultiTexCoord2dv = platform.createExtensionFunction( 
'glMultiTexCoord2dv',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,arrays.GLdoubleArray,),
doc='glMultiTexCoord2dv(GLenum(target), GLdoubleArray(v)) -> None',
argNames=('target','v',),
deprecated=_DEPRECATED,
)

glMultiTexCoord2f = platform.createExtensionFunction( 
'glMultiTexCoord2f',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLfloat,constants.GLfloat,),
doc='glMultiTexCoord2f(GLenum(target), GLfloat(s), GLfloat(t)) -> None',
argNames=('target','s','t',),
deprecated=_DEPRECATED,
)

glMultiTexCoord2fv = platform.createExtensionFunction( 
'glMultiTexCoord2fv',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,arrays.GLfloatArray,),
doc='glMultiTexCoord2fv(GLenum(target), GLfloatArray(v)) -> None',
argNames=('target','v',),
deprecated=_DEPRECATED,
)

glMultiTexCoord2i = platform.createExtensionFunction( 
'glMultiTexCoord2i',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLint,constants.GLint,),
doc='glMultiTexCoord2i(GLenum(target), GLint(s), GLint(t)) -> None',
argNames=('target','s','t',),
deprecated=_DEPRECATED,
)

glMultiTexCoord2iv = platform.createExtensionFunction( 
'glMultiTexCoord2iv',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,arrays.GLintArray,),
doc='glMultiTexCoord2iv(GLenum(target), GLintArray(v)) -> None',
argNames=('target','v',),
deprecated=_DEPRECATED,
)

glMultiTexCoord2s = platform.createExtensionFunction( 
'glMultiTexCoord2s',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLshort,constants.GLshort,),
doc='glMultiTexCoord2s(GLenum(target), GLshort(s), GLshort(t)) -> None',
argNames=('target','s','t',),
deprecated=_DEPRECATED,
)

glMultiTexCoord2sv = platform.createExtensionFunction( 
'glMultiTexCoord2sv',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,arrays.GLshortArray,),
doc='glMultiTexCoord2sv(GLenum(target), GLshortArray(v)) -> None',
argNames=('target','v',),
deprecated=_DEPRECATED,
)

glMultiTexCoord3d = platform.createExtensionFunction( 
'glMultiTexCoord3d',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLdouble,constants.GLdouble,constants.GLdouble,),
doc='glMultiTexCoord3d(GLenum(target), GLdouble(s), GLdouble(t), GLdouble(r)) -> None',
argNames=('target','s','t','r',),
deprecated=_DEPRECATED,
)

glMultiTexCoord3dv = platform.createExtensionFunction( 
'glMultiTexCoord3dv',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,arrays.GLdoubleArray,),
doc='glMultiTexCoord3dv(GLenum(target), GLdoubleArray(v)) -> None',
argNames=('target','v',),
deprecated=_DEPRECATED,
)

glMultiTexCoord3f = platform.createExtensionFunction( 
'glMultiTexCoord3f',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLfloat,constants.GLfloat,constants.GLfloat,),
doc='glMultiTexCoord3f(GLenum(target), GLfloat(s), GLfloat(t), GLfloat(r)) -> None',
argNames=('target','s','t','r',),
deprecated=_DEPRECATED,
)

glMultiTexCoord3fv = platform.createExtensionFunction( 
'glMultiTexCoord3fv',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,arrays.GLfloatArray,),
doc='glMultiTexCoord3fv(GLenum(target), GLfloatArray(v)) -> None',
argNames=('target','v',),
deprecated=_DEPRECATED,
)

glMultiTexCoord3i = platform.createExtensionFunction( 
'glMultiTexCoord3i',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLint,constants.GLint,constants.GLint,),
doc='glMultiTexCoord3i(GLenum(target), GLint(s), GLint(t), GLint(r)) -> None',
argNames=('target','s','t','r',),
deprecated=_DEPRECATED,
)

glMultiTexCoord3iv = platform.createExtensionFunction( 
'glMultiTexCoord3iv',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,arrays.GLintArray,),
doc='glMultiTexCoord3iv(GLenum(target), GLintArray(v)) -> None',
argNames=('target','v',),
deprecated=_DEPRECATED,
)

glMultiTexCoord3s = platform.createExtensionFunction( 
'glMultiTexCoord3s',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLshort,constants.GLshort,constants.GLshort,),
doc='glMultiTexCoord3s(GLenum(target), GLshort(s), GLshort(t), GLshort(r)) -> None',
argNames=('target','s','t','r',),
deprecated=_DEPRECATED,
)

glMultiTexCoord3sv = platform.createExtensionFunction( 
'glMultiTexCoord3sv',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,arrays.GLshortArray,),
doc='glMultiTexCoord3sv(GLenum(target), GLshortArray(v)) -> None',
argNames=('target','v',),
deprecated=_DEPRECATED,
)

glMultiTexCoord4d = platform.createExtensionFunction( 
'glMultiTexCoord4d',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLdouble,constants.GLdouble,constants.GLdouble,constants.GLdouble,),
doc='glMultiTexCoord4d(GLenum(target), GLdouble(s), GLdouble(t), GLdouble(r), GLdouble(q)) -> None',
argNames=('target','s','t','r','q',),
deprecated=_DEPRECATED,
)

glMultiTexCoord4dv = platform.createExtensionFunction( 
'glMultiTexCoord4dv',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,arrays.GLdoubleArray,),
doc='glMultiTexCoord4dv(GLenum(target), GLdoubleArray(v)) -> None',
argNames=('target','v',),
deprecated=_DEPRECATED,
)

glMultiTexCoord4f = platform.createExtensionFunction( 
'glMultiTexCoord4f',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLfloat,constants.GLfloat,constants.GLfloat,constants.GLfloat,),
doc='glMultiTexCoord4f(GLenum(target), GLfloat(s), GLfloat(t), GLfloat(r), GLfloat(q)) -> None',
argNames=('target','s','t','r','q',),
deprecated=_DEPRECATED,
)

glMultiTexCoord4fv = platform.createExtensionFunction( 
'glMultiTexCoord4fv',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,arrays.GLfloatArray,),
doc='glMultiTexCoord4fv(GLenum(target), GLfloatArray(v)) -> None',
argNames=('target','v',),
deprecated=_DEPRECATED,
)

glMultiTexCoord4i = platform.createExtensionFunction( 
'glMultiTexCoord4i',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLint,constants.GLint,constants.GLint,constants.GLint,),
doc='glMultiTexCoord4i(GLenum(target), GLint(s), GLint(t), GLint(r), GLint(q)) -> None',
argNames=('target','s','t','r','q',),
deprecated=_DEPRECATED,
)

glMultiTexCoord4iv = platform.createExtensionFunction( 
'glMultiTexCoord4iv',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,arrays.GLintArray,),
doc='glMultiTexCoord4iv(GLenum(target), GLintArray(v)) -> None',
argNames=('target','v',),
deprecated=_DEPRECATED,
)

glMultiTexCoord4s = platform.createExtensionFunction( 
'glMultiTexCoord4s',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLshort,constants.GLshort,constants.GLshort,constants.GLshort,),
doc='glMultiTexCoord4s(GLenum(target), GLshort(s), GLshort(t), GLshort(r), GLshort(q)) -> None',
argNames=('target','s','t','r','q',),
deprecated=_DEPRECATED,
)

glMultiTexCoord4sv = platform.createExtensionFunction( 
'glMultiTexCoord4sv',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,arrays.GLshortArray,),
doc='glMultiTexCoord4sv(GLenum(target), GLshortArray(v)) -> None',
argNames=('target','v',),
deprecated=_DEPRECATED,
)

glLoadTransposeMatrixf = platform.createExtensionFunction( 
'glLoadTransposeMatrixf',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(arrays.GLfloatArray,),
doc='glLoadTransposeMatrixf(GLfloatArray(m)) -> None',
argNames=('m',),
deprecated=_DEPRECATED,
)

glLoadTransposeMatrixd = platform.createExtensionFunction( 
'glLoadTransposeMatrixd',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(arrays.GLdoubleArray,),
doc='glLoadTransposeMatrixd(GLdoubleArray(m)) -> None',
argNames=('m',),
deprecated=_DEPRECATED,
)

glMultTransposeMatrixf = platform.createExtensionFunction( 
'glMultTransposeMatrixf',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(arrays.GLfloatArray,),
doc='glMultTransposeMatrixf(GLfloatArray(m)) -> None',
argNames=('m',),
deprecated=_DEPRECATED,
)

glMultTransposeMatrixd = platform.createExtensionFunction( 
'glMultTransposeMatrixd',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(arrays.GLdoubleArray,),
doc='glMultTransposeMatrixd(GLdoubleArray(m)) -> None',
argNames=('m',),
deprecated=_DEPRECATED,
)
