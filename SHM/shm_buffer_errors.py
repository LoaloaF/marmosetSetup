# -*- coding: utf-8 -*-
# Copyright (c) 2021 tandemdude
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import typing

__all__: typing.List[str] = [
    "CBuffException",
    "WriteOperationsForbidden",
    "ReadOperationsForbidden",
    "BufferAlreadyCreated",
]


class CBuffException(Exception):
    """Base exception for all exceptions raised by the library."""

    pass

class ItemLengthExceededError(CBuffException):
    "Exception raised when write operation is attempted with a item larger than available item length"
    pass

class WriteOperationsForbidden(CBuffException):
    """Exception raised when a write operation is attempted but is not permitted."""

    pass


class ReadOperationsForbidden(CBuffException):
    """Exception raised when a read operation is attempted but is not permitted."""

    pass


class BufferAlreadyCreated(CBuffException):
    """Exception raised when attempting to create multiple buffers with the same name."""

    pass