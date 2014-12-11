'''OpenGL extension IBM.vertex_array_lists

This module customises the behaviour of the 
OpenGL.raw.GL.IBM.vertex_array_lists to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension introduces seven (7) new functions that set the 
	vertex array pointers. However, instead of a single pointer, these
	functions provide a list of array pointers that can be used by the 
	EXT_multi_draw_arrays and IBM_multimode_draw_arrays extension 
	functions to draw from multiple of vertex arrays. The first 
	primitive will use the first array in the list, the second primitive
	will use the second array in the list, and so forth. If a glDrawArray,
	DrawElements, or DrawRangeElements function is used, then 
	only the first vertex array in the list is used.
	
	When a vertex array list is specified, only the list pointer
	is kept by the underlying OpenGL function. Therefore, the list
	must be staticly defined for the entire duration of its usage,
	much in the same manner as the vertex arrays themselves. Also
	note that the list function can therefore also be used to change
	array pointers without making a OpenGL API function call.
	
	A <ptrstride> value of zero (0) can be used to force all primitives
	of a multi-vertex array to use only the first vertex array in 
	the list. 
	
	The <stride> parameter of the list pointer functions differs from
	that of the non-list vertex array pointer functions in that 1)
	both negative and positive strides are accepted thusly allowing
	vertex lists to be rendered in reverse order; 2) a <stride> of
	zero (0) results in no stride and can be used to specify a single
	vertex attribute for each vertex of the primitive.
	
	These new functions are a superset of the standard OpenGL 1.2 vertex
	array (non-list) pointer functions and share common state. Therefore,
	the list pointer and non-list pointer functions can be used
	interchangably.
	
	New queries are provided by this extension so that ZAPdb can be extended
	to query the list pointer state whenever a vertex array function 
	is traced. The pointer returned by a query of *_ARRAY_POINTER returns
	the first entry in the array list.
	

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/IBM/vertex_array_lists.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL import _types
from OpenGL.raw.GL.IBM.vertex_array_lists import *
from OpenGL.raw.GL.IBM.vertex_array_lists import _EXTENSION_NAME

def glInitVertexArrayListsIBM():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

### END AUTOGENERATED SECTION