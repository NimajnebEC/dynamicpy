"""
A python module for dynamically importing modules to improve expandability.

https://github.com/NimajnebEC/dynamicpy
"""
from dynamicpy.errors import DynamicPyError, NoForeignModulesError, NoParentError
from dynamicpy.utils import get_foreign_module, get_module_parent
from dynamicpy.dependencies import DependencyLibrary
from dynamicpy.loader import DynamicLoader

__all__ = (
    "DynamicLoader",
    "DependencyLibrary",
    "DynamicPyError",
    "NoForeignModulesError",
    "NoParentError",
    "get_foreign_module",
    "get_module_parent",
)
