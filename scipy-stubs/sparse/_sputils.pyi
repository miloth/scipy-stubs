from collections.abc import Iterable
from typing import Any, Final, Literal, Protocol, TypeAlias, TypedDict, overload, type_check_only
from typing_extensions import Never, TypeIs

import numpy as np
import optype as op
import optype.numpy as onp
from scipy._typing import Untyped, UntypedArray
from scipy.sparse import spmatrix

_SupportedScalar: TypeAlias = np.bool_ | np.integer[Any] | np.float32 | np.float64 | np.longdouble | np.complexfloating[Any, Any]
_ShapeLike: TypeAlias = Iterable[op.CanIndex]
_ScalarLike: TypeAlias = complex | str | bytes | memoryview | np.generic | onp.Array[tuple[()]]
_SequenceLike: TypeAlias = tuple[()] | tuple[_ScalarLike, ...] | list[Never] | list[_ScalarLike] | onp.Array[tuple[int]]
_MatrixLike: TypeAlias = tuple[_SequenceLike, ...] | list[_SequenceLike] | onp.Array[tuple[int, int]]

@type_check_only
class _ReshapeKwargs(TypedDict, total=False):
    order: Literal["C", "F"]
    copy: bool

@type_check_only
class _SizedIndexIterable(Protocol):
    def __len__(self, /) -> int: ...
    def __iter__(self, /) -> op.CanNext[op.CanIndex]: ...

#
# public
#

supported_dtypes: Final[list[type[_SupportedScalar]]] = ...

#
def upcast(*args: Untyped) -> Untyped: ...
def upcast_char(*args: Untyped) -> Untyped: ...
def upcast_scalar(dtype: Untyped, scalar: Untyped) -> Untyped: ...
def downcast_intp_index(arr: Untyped) -> Untyped: ...
def to_native(A: Untyped) -> Untyped: ...

#
def getdtype(dtype: Untyped, a: Untyped | None = None, default: Untyped | None = None) -> Untyped: ...
def getdata(obj: Untyped, dtype: Untyped | None = None, copy: bool = False) -> UntypedArray: ...
def get_index_dtype(arrays: Untyped = (), maxval: Untyped | None = None, check_contents: bool = False) -> Untyped: ...
def get_sum_dtype(dtype: np.dtype[np.generic]) -> np.dtype[np.generic]: ...

#
def isintlike(x: op.CanIndex) -> bool: ...

# NOTE: all arrays implement `__index__` but if it raises this returns `False`, so `TypeIs` can't be used here
def isscalarlike(x: object) -> TypeIs[_ScalarLike]: ...
def isshape(x: _SizedIndexIterable, nonneg: bool = False, *, allow_1d: bool = False) -> bool: ...
def issequence(t: object) -> TypeIs[_SequenceLike]: ...
def ismatrix(t: object) -> TypeIs[_MatrixLike]: ...
def isdense(x: object) -> TypeIs[onp.Array]: ...

# NOTE: this checks for a `sparse.SparseArray`, which has no stubs at the moment
@overload
def is_pydata_spmatrix(m: _ScalarLike | _SequenceLike | _MatrixLike) -> Literal[False]: ...
@overload
def is_pydata_spmatrix(m: object) -> bool: ...

#
def validateaxis(axis: Literal[-2, -1, 0, 1] | bool | np.bool_ | np.integer[Any] | None) -> None: ...
def check_shape(
    args: _ShapeLike | tuple[_ShapeLike],
    current_shape: tuple[int] | tuple[int, int] | None = None,
    *,
    allow_1d: bool = False,
) -> tuple[int] | tuple[int, int]: ...
def check_reshape_kwargs(kwargs: _ReshapeKwargs) -> Literal["C", "F"] | bool: ...

#
def convert_pydata_sparse_to_scipy(arg: object, target_format: Literal["csc", "csr"] | None = None) -> object | spmatrix: ...
def matrix(*args: Untyped, **kwargs: Untyped) -> Untyped: ...
def asmatrix(data: Untyped, dtype: Untyped | None = None) -> Untyped: ...
