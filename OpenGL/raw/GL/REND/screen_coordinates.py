'''OpenGL extension REND.screen_coordinates

Overview (from the spec)
    
        This extension allows the specification of screen coordinate vertex
        data. Screen coordinate vertices completely bypass transformation,
        texture generation, lighting and frustum clipping. It also allow for
        fewer floating point computations to the performed by OpenGL.
    
        If we get screen coordinate inputs then in order to perspectively
        correct data (eg texture), the input data currently has to be
        specified in one of the following manners
    
        1. Specify all the data normally
           eg.
              glTexture2T(s, t);
           and the coordinates as
              glVertex4T(x*w, y*w, z*w, w);
        or
        2. Divide each data by w
           eg.
              glTexture4T(s/w, t/w, r/w, q/w);
           and the coordinates as
              glVertex3T(x, y, z);
    
        Most hardware already performs some form of correction of the
        coordinate data with respect to the w term prior to interpolation.
        This is normally in the form of a multiplication of the terms by the
        inverse w. It would be much more efficient to simply specify screen
        coordinates as shown in the following example
           glTexture2T(s, t, r, q);
        and the coordinates as
           glVertex4T(x, y, z, w);
        and allow the hardware to bring the interpolated terms into a linear
        screen space.
    
        Additionally if the application derives screen coordinates it is
        also highly likely that the 1/w term may already be computed. So it
        would be advantageous to be able to specify 1/w directly instead of
        w in the input screen coordinates.
    
        For hardware that linearly interpolates data, the hardware
        interpolates the following data:
        s/w, t/w, r/w, q/w, x, y, z
        If the input w represents the original 1/w, then the hardware can
        avoid the division and instead interpolate:
        s*w, t*w, r*w, q*w, x, y, z
    

The official definition of this extension is available here:
http://oss.sgi.com/projects/ogl-sample/registry/REND/screen_coordinates.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_REND_screen_coordinates'
_DEPRECATED = False
GL_SCREEN_COORDINATES_REND = constant.Constant( 'GL_SCREEN_COORDINATES_REND', 0x8490 )
GL_INVERTED_SCREEN_W_REND = constant.Constant( 'GL_INVERTED_SCREEN_W_REND', 0x8491 )


def glInitScreenCoordinatesREND():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )