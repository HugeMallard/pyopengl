'''OpenGL extension VERSION.GL_1_5_DEPRECATED

The official definition of this extension is available here:
http://oss.sgi.com/projects/ogl-sample/registry/VERSION/GL_1_5_DEPRECATED.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_VERSION_GL_1_5'
_DEPRECATED = True
GL_VERTEX_ARRAY_BUFFER_BINDING = constant.Constant( 'GL_VERTEX_ARRAY_BUFFER_BINDING', 0x8896 )
GL_NORMAL_ARRAY_BUFFER_BINDING = constant.Constant( 'GL_NORMAL_ARRAY_BUFFER_BINDING', 0x8897 )
GL_COLOR_ARRAY_BUFFER_BINDING = constant.Constant( 'GL_COLOR_ARRAY_BUFFER_BINDING', 0x8898 )
GL_INDEX_ARRAY_BUFFER_BINDING = constant.Constant( 'GL_INDEX_ARRAY_BUFFER_BINDING', 0x8899 )
GL_TEXTURE_COORD_ARRAY_BUFFER_BINDING = constant.Constant( 'GL_TEXTURE_COORD_ARRAY_BUFFER_BINDING', 0x889A )
GL_EDGE_FLAG_ARRAY_BUFFER_BINDING = constant.Constant( 'GL_EDGE_FLAG_ARRAY_BUFFER_BINDING', 0x889B )
GL_SECONDARY_COLOR_ARRAY_BUFFER_BINDING = constant.Constant( 'GL_SECONDARY_COLOR_ARRAY_BUFFER_BINDING', 0x889C )
GL_FOG_COORDINATE_ARRAY_BUFFER_BINDING = constant.Constant( 'GL_FOG_COORDINATE_ARRAY_BUFFER_BINDING', 0x889D )
GL_WEIGHT_ARRAY_BUFFER_BINDING = constant.Constant( 'GL_WEIGHT_ARRAY_BUFFER_BINDING', 0x889E )
GL_FOG_COORD_SRC = constant.Constant( 'GL_FOG_COORD_SRC', 0x8450 )
GL_FOG_COORD = constant.Constant( 'GL_FOG_COORD', 0x8451 )
GL_CURRENT_FOG_COORD = constant.Constant( 'GL_CURRENT_FOG_COORD', 0x8453 )
GL_FOG_COORD_ARRAY_TYPE = constant.Constant( 'GL_FOG_COORD_ARRAY_TYPE', 0x8454 )
GL_FOG_COORD_ARRAY_STRIDE = constant.Constant( 'GL_FOG_COORD_ARRAY_STRIDE', 0x8455 )
GL_FOG_COORD_ARRAY_POINTER = constant.Constant( 'GL_FOG_COORD_ARRAY_POINTER', 0x8456 )
GL_FOG_COORD_ARRAY = constant.Constant( 'GL_FOG_COORD_ARRAY', 0x8457 )
GL_FOG_COORD_ARRAY_BUFFER_BINDING = constant.Constant( 'GL_FOG_COORD_ARRAY_BUFFER_BINDING', 0x889D )
GL_SRC0_RGB = constant.Constant( 'GL_SRC0_RGB', 0x8580 )
GL_SRC1_RGB = constant.Constant( 'GL_SRC1_RGB', 0x8581 )
GL_SRC2_RGB = constant.Constant( 'GL_SRC2_RGB', 0x8582 )
GL_SRC0_ALPHA = constant.Constant( 'GL_SRC0_ALPHA', 0x8588 )
GL_SRC1_ALPHA = constant.Constant( 'GL_SRC1_ALPHA', 0x8589 )
GL_SRC2_ALPHA = constant.Constant( 'GL_SRC2_ALPHA', 0x858A )
