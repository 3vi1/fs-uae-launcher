'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_SGIS_texture4D'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GL,'GL_SGIS_texture4D',error_checker=_errors._error_checker)
GL_MAX_4D_TEXTURE_SIZE_SGIS=_C('GL_MAX_4D_TEXTURE_SIZE_SGIS',0x8138)
GL_PACK_IMAGE_DEPTH_SGIS=_C('GL_PACK_IMAGE_DEPTH_SGIS',0x8131)
GL_PACK_SKIP_VOLUMES_SGIS=_C('GL_PACK_SKIP_VOLUMES_SGIS',0x8130)
GL_PROXY_TEXTURE_4D_SGIS=_C('GL_PROXY_TEXTURE_4D_SGIS',0x8135)
GL_TEXTURE_4DSIZE_SGIS=_C('GL_TEXTURE_4DSIZE_SGIS',0x8136)
GL_TEXTURE_4D_BINDING_SGIS=_C('GL_TEXTURE_4D_BINDING_SGIS',0x814F)
GL_TEXTURE_4D_SGIS=_C('GL_TEXTURE_4D_SGIS',0x8134)
GL_TEXTURE_WRAP_Q_SGIS=_C('GL_TEXTURE_WRAP_Q_SGIS',0x8137)
GL_UNPACK_IMAGE_DEPTH_SGIS=_C('GL_UNPACK_IMAGE_DEPTH_SGIS',0x8133)
GL_UNPACK_SKIP_VOLUMES_SGIS=_C('GL_UNPACK_SKIP_VOLUMES_SGIS',0x8132)
@_f
@_p.types(None,_cs.GLenum,_cs.GLint,_cs.GLenum,_cs.GLsizei,_cs.GLsizei,_cs.GLsizei,_cs.GLsizei,_cs.GLint,_cs.GLenum,_cs.GLenum,ctypes.c_void_p)
def glTexImage4DSGIS(target,level,internalformat,width,height,depth,size4d,border,format,type,pixels):pass
# Calculate length of pixels from format:PixelFormat, type:PixelType
@_f
@_p.types(None,_cs.GLenum,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLsizei,_cs.GLsizei,_cs.GLsizei,_cs.GLsizei,_cs.GLenum,_cs.GLenum,ctypes.c_void_p)
def glTexSubImage4DSGIS(target,level,xoffset,yoffset,zoffset,woffset,width,height,depth,size4d,format,type,pixels):pass
# Calculate length of pixels from format:PixelFormat, type:PixelType
