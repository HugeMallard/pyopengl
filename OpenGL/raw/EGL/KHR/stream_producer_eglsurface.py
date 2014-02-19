'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.EGL import _types as _cs
# End users want this...
from OpenGL.raw.EGL._types import *
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'EGL_KHR_stream_producer_eglsurface'
def _f( function ):
    return _p.createFunction( function,_p.EGL,'EGL_KHR_stream_producer_eglsurface')
EGL_STREAM_BIT_KHR=_C('EGL_STREAM_BIT_KHR',0x0800)
@_f
@_p.types(_cs.EGLSurface,_cs.EGLDisplay,_cs.EGLConfig,_cs.EGLStreamKHR,arrays.GLintArray)
def eglCreateStreamProducerSurfaceKHR(dpy,config,stream,attrib_list):pass