'''OpenGL extension EXT.buffer_age

This module customises the behaviour of the 
OpenGL.raw.GLX.EXT.buffer_age to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/EXT/buffer_age.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper

import ctypes
from OpenGL.raw.GLX import _types
from OpenGL.raw.GLX.EXT.buffer_age import *
from OpenGL.raw.GLX.EXT.buffer_age import _EXTENSION_NAME

def glInitBufferAgeEXT():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

### END AUTOGENERATED SECTION