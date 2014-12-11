'''OpenGL extension PGI.vertex_hints

This module customises the behaviour of the 
OpenGL.raw.GL.PGI.vertex_hints to provide a more 
Python-friendly API

Overview (from the spec)
	
	The extension allows the app to give hints regarding what kinds of
	OpenGL function calls will happen between Begin/End pairs.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/PGI/vertex_hints.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL import _types
from OpenGL.raw.GL.PGI.vertex_hints import *
from OpenGL.raw.GL.PGI.vertex_hints import _EXTENSION_NAME

def glInitVertexHintsPGI():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

### END AUTOGENERATED SECTION