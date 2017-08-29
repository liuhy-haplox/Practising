Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:18:55) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from inspect import signature
>>> def spam(x, y, z=42):
	pass

>>> sig = signature(spam)
>>> print(sig)
(x, y, z=42)
>>> sig.parameters
mappingproxy(OrderedDict([('x', <Parameter "x">), ('y', <Parameter "y">), ('z', <Parameter "z=42">)]))
>>> sig.parameters['z'].name
'z'
>>> sig.parameters['z'].default
42
>>> sig.parameters['z'].kind
<_ParameterKind.POSITIONAL_OR_KEYWORD: 1>
>>> bound_types = sig.bind_partial(int,z=int)
>>> bound_types
<BoundArguments (x=<class 'int'>, z=<class 'int'>)>
>>> bound_types.arguments
OrderedDict([('x', <class 'int'>), ('z', <class 'int'>)])
>>> bound_values = sig.bind(1, 2, 3)
>>> bound_values.arguments
OrderedDict([('x', 1), ('y', 2), ('z', 3)])
>>> 
