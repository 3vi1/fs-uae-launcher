'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_EXT_coordinate_frame'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GL,'GL_EXT_coordinate_frame',error_checker=_errors._error_checker)
GL_BINORMAL_ARRAY_EXT=_C('GL_BINORMAL_ARRAY_EXT',0x843A)
GL_BINORMAL_ARRAY_POINTER_EXT=_C('GL_BINORMAL_ARRAY_POINTER_EXT',0x8443)
GL_BINORMAL_ARRAY_STRIDE_EXT=_C('GL_BINORMAL_ARRAY_STRIDE_EXT',0x8441)
GL_BINORMAL_ARRAY_TYPE_EXT=_C('GL_BINORMAL_ARRAY_TYPE_EXT',0x8440)
GL_CURRENT_BINORMAL_EXT=_C('GL_CURRENT_BINORMAL_EXT',0x843C)
GL_CURRENT_TANGENT_EXT=_C('GL_CURRENT_TANGENT_EXT',0x843B)
GL_MAP1_BINORMAL_EXT=_C('GL_MAP1_BINORMAL_EXT',0x8446)
GL_MAP1_TANGENT_EXT=_C('GL_MAP1_TANGENT_EXT',0x8444)
GL_MAP2_BINORMAL_EXT=_C('GL_MAP2_BINORMAL_EXT',0x8447)
GL_MAP2_TANGENT_EXT=_C('GL_MAP2_TANGENT_EXT',0x8445)
GL_TANGENT_ARRAY_EXT=_C('GL_TANGENT_ARRAY_EXT',0x8439)
GL_TANGENT_ARRAY_POINTER_EXT=_C('GL_TANGENT_ARRAY_POINTER_EXT',0x8442)
GL_TANGENT_ARRAY_STRIDE_EXT=_C('GL_TANGENT_ARRAY_STRIDE_EXT',0x843F)
GL_TANGENT_ARRAY_TYPE_EXT=_C('GL_TANGENT_ARRAY_TYPE_EXT',0x843E)
@_f
@_p.types(None,_cs.GLbyte,_cs.GLbyte,_cs.GLbyte)
def glBinormal3bEXT(bx,by,bz):pass
@_f
@_p.types(None,arrays.GLbyteArray)
def glBinormal3bvEXT(v):pass
@_f
@_p.types(None,_cs.GLdouble,_cs.GLdouble,_cs.GLdouble)
def glBinormal3dEXT(bx,by,bz):pass
@_f
@_p.types(None,arrays.GLdoubleArray)
def glBinormal3dvEXT(v):pass
@_f
@_p.types(None,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat)
def glBinormal3fEXT(bx,by,bz):pass
@_f
@_p.types(None,arrays.GLfloatArray)
def glBinormal3fvEXT(v):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLint,_cs.GLint)
def glBinormal3iEXT(bx,by,bz):pass
@_f
@_p.types(None,arrays.GLintArray)
def glBinormal3ivEXT(v):pass
@_f
@_p.types(None,_cs.GLshort,_cs.GLshort,_cs.GLshort)
def glBinormal3sEXT(bx,by,bz):pass
@_f
@_p.types(None,arrays.GLshortArray)
def glBinormal3svEXT(v):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLsizei,ctypes.c_void_p)
def glBinormalPointerEXT(type,stride,pointer):pass
# Calculate length of pointer from type:BinormalPointerTypeEXT
@_f
@_p.types(None,_cs.GLbyte,_cs.GLbyte,_cs.GLbyte)
def glTangent3bEXT(tx,ty,tz):pass
@_f
@_p.types(None,arrays.GLbyteArray)
def glTangent3bvEXT(v):pass
@_f
@_p.types(None,_cs.GLdouble,_cs.GLdouble,_cs.GLdouble)
def glTangent3dEXT(tx,ty,tz):pass
@_f
@_p.types(None,arrays.GLdoubleArray)
def glTangent3dvEXT(v):pass
@_f
@_p.types(None,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat)
def glTangent3fEXT(tx,ty,tz):pass
@_f
@_p.types(None,arrays.GLfloatArray)
def glTangent3fvEXT(v):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLint,_cs.GLint)
def glTangent3iEXT(tx,ty,tz):pass
@_f
@_p.types(None,arrays.GLintArray)
def glTangent3ivEXT(v):pass
@_f
@_p.types(None,_cs.GLshort,_cs.GLshort,_cs.GLshort)
def glTangent3sEXT(tx,ty,tz):pass
@_f
@_p.types(None,arrays.GLshortArray)
def glTangent3svEXT(v):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLsizei,ctypes.c_void_p)
def glTangentPointerEXT(type,stride,pointer):pass
# Calculate length of pointer from type:TangentPointerTypeEXT
