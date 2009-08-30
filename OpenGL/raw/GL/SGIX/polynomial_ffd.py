'''OpenGL extension SGIX.polynomial_ffd

The official definition of this extension is available here:
http://oss.sgi.com/projects/ogl-sample/registry/SGIX/polynomial_ffd.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_SGIX_polynomial_ffd'
_DEPRECATED = False
GL_GEOMETRY_DEFORMATION_SGIX = constant.Constant( 'GL_GEOMETRY_DEFORMATION_SGIX', 0x8194 )
GL_TEXTURE_DEFORMATION_SGIX = constant.Constant( 'GL_TEXTURE_DEFORMATION_SGIX', 0x8195 )
GL_DEFORMATIONS_MASK_SGIX = constant.Constant( 'GL_DEFORMATIONS_MASK_SGIX', 0x8196 )
GL_MAX_DEFORMATION_ORDER_SGIX = constant.Constant( 'GL_MAX_DEFORMATION_ORDER_SGIX', 0x8197 )
glDeformationMap3dSGIX = platform.createExtensionFunction( 
'glDeformationMap3dSGIX',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLdouble,constants.GLdouble,constants.GLint,constants.GLint,constants.GLdouble,constants.GLdouble,constants.GLint,constants.GLint,constants.GLdouble,constants.GLdouble,constants.GLint,constants.GLint,arrays.GLdoubleArray,),
doc='glDeformationMap3dSGIX(GLenum(target), GLdouble(u1), GLdouble(u2), GLint(ustride), GLint(uorder), GLdouble(v1), GLdouble(v2), GLint(vstride), GLint(vorder), GLdouble(w1), GLdouble(w2), GLint(wstride), GLint(worder), GLdoubleArray(points)) -> None',
argNames=('target','u1','u2','ustride','uorder','v1','v2','vstride','vorder','w1','w2','wstride','worder','points',),
deprecated=_DEPRECATED,
)

glDeformationMap3fSGIX = platform.createExtensionFunction( 
'glDeformationMap3fSGIX',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLfloat,constants.GLfloat,constants.GLint,constants.GLint,constants.GLfloat,constants.GLfloat,constants.GLint,constants.GLint,constants.GLfloat,constants.GLfloat,constants.GLint,constants.GLint,arrays.GLfloatArray,),
doc='glDeformationMap3fSGIX(GLenum(target), GLfloat(u1), GLfloat(u2), GLint(ustride), GLint(uorder), GLfloat(v1), GLfloat(v2), GLint(vstride), GLint(vorder), GLfloat(w1), GLfloat(w2), GLint(wstride), GLint(worder), GLfloatArray(points)) -> None',
argNames=('target','u1','u2','ustride','uorder','v1','v2','vstride','vorder','w1','w2','wstride','worder','points',),
deprecated=_DEPRECATED,
)

glDeformSGIX = platform.createExtensionFunction( 
'glDeformSGIX',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLbitfield,),
doc='glDeformSGIX(GLbitfield(mask)) -> None',
argNames=('mask',),
deprecated=_DEPRECATED,
)

glLoadIdentityDeformationMapSGIX = platform.createExtensionFunction( 
'glLoadIdentityDeformationMapSGIX',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLbitfield,),
doc='glLoadIdentityDeformationMapSGIX(GLbitfield(mask)) -> None',
argNames=('mask',),
deprecated=_DEPRECATED,
)


def glInitPolynomialFfdSGIX():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )