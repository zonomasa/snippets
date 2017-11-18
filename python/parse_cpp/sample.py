#!/usr/bin/env python
# -*- coding: utf-8 -*-
# usage: $ python sample.py sample.cpp

import clang.cindex
from clang.cindex import Index
from clang.cindex import Config

Config.set_compatibility_check(False)


def print_method_area(node):
    if (node.kind.name == 'FUNCTION_DECL'):
        print("file : %s" % node.extent.start.file)
        print("function : %s" % node.displayname)
        print(" from line:%s column:%s" % (node.extent.start.line, node.extent.start.column))
        print(" to   line:%s column:%s" % (node.extent.end.line, node.extent.end.column))
    for child in node.get_children():
        print_method_area(child)

index = Index.create()
tu = index.parse("sample.cpp")
print_method_area(tu.cursor)
