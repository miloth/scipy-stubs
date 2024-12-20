from collections.abc import Sequence
from typing import Any, Literal, TypeAlias, overload
from typing_extensions import TypeVar

import numpy as np
import numpy.typing as npt
import optype.numpy as onp
import optype.typing as opt
from scipy._typing import CorrelateMode

__all__ = [
    "block_diag",
    "circulant",
    "companion",
    "convolution_matrix",
    "dft",
    "fiedler",
    "fiedler_companion",
    "hadamard",
    "hankel",
    "helmert",
    "hilbert",
    "invhilbert",
    "invpascal",
    "kron",
    "leslie",
    "pascal",
    "toeplitz",
]

_SCT = TypeVar("_SCT", bound=np.generic, default=np.number[Any] | np.bool_ | np.object_)

_Matrix: TypeAlias = onp.Array2D[_SCT]
_Kind: TypeAlias = Literal["symmetric", "upper", "lower"]

###

#
@overload
def toeplitz(c: Sequence[opt.JustInt], r: Sequence[opt.JustInt] | None = None) -> _Matrix[np.int_]: ...
@overload
def toeplitz(c: Sequence[opt.Just[float]], r: Sequence[opt.Just[float]] | None = None) -> _Matrix[np.float64]: ...
@overload
def toeplitz(c: Sequence[opt.Just[complex]], r: Sequence[opt.Just[complex]] | None = None) -> _Matrix[np.complex128]: ...
@overload
def toeplitz(c: onp.CanArrayND[_SCT] | Sequence[_SCT], r: onp.CanArrayND[_SCT] | None = None) -> _Matrix[_SCT]: ...

#
@overload
def circulant(c: Sequence[opt.JustInt]) -> _Matrix[np.int_]: ...
@overload
def circulant(c: Sequence[opt.Just[float]]) -> _Matrix[np.float64]: ...
@overload
def circulant(c: Sequence[opt.Just[complex]]) -> _Matrix[np.complex128]: ...
@overload
def circulant(c: onp.CanArrayND[_SCT] | Sequence[_SCT]) -> _Matrix[_SCT]: ...

#
@overload
def hankel(c: Sequence[opt.JustInt], r: Sequence[opt.JustInt] | None = None) -> _Matrix[np.int_]: ...
@overload
def hankel(c: Sequence[opt.Just[float]], r: Sequence[opt.Just[float]] | None = None) -> _Matrix[np.float64]: ...
@overload
def hankel(c: Sequence[opt.Just[complex]], r: Sequence[opt.Just[complex]] | None = None) -> _Matrix[np.complex128]: ...
@overload
def hankel(c: onp.CanArrayND[_SCT] | Sequence[_SCT], r: onp.CanArrayND[_SCT] | None = None) -> _Matrix[_SCT]: ...

#
@overload
def hadamard(n: onp.ToInt, dtype: type[opt.JustInt]) -> _Matrix[np.int_]: ...
@overload
def hadamard(n: onp.ToInt, dtype: type[opt.Just[float]]) -> _Matrix[np.float64]: ...
@overload
def hadamard(n: onp.ToInt, dtype: type[opt.Just[complex]]) -> _Matrix[np.complex128]: ...
@overload
def hadamard(n: onp.ToInt, dtype: onp.HasDType[np.dtype[_SCT]] | np.dtype[_SCT]) -> _Matrix[_SCT]: ...
@overload
def hadamard(n: onp.ToInt, dtype: npt.DTypeLike = ...) -> _Matrix[np.generic]: ...

#
@overload
def leslie(f: Sequence[opt.JustInt], s: Sequence[opt.JustInt]) -> _Matrix[np.int_]: ...
@overload
def leslie(f: Sequence[opt.Just[float]], s: Sequence[opt.Just[float]]) -> _Matrix[np.float64]: ...
@overload
def leslie(f: Sequence[opt.Just[complex]], s: Sequence[opt.Just[complex]]) -> _Matrix[np.complex128]: ...
@overload
def leslie(f: onp.CanArrayND[_SCT] | Sequence[_SCT], s: onp.CanArrayND[_SCT] | Sequence[_SCT]) -> _Matrix[_SCT]: ...

#
def kron(a: onp.ArrayND[_SCT], b: onp.ArrayND[_SCT]) -> _Matrix[_SCT]: ...

#
@overload
def block_diag() -> _Matrix[np.float64]: ...
@overload
def block_diag(arr0: Sequence[opt.JustInt], /, *arrs: Sequence[opt.JustInt]) -> _Matrix[np.int_]: ...
@overload
def block_diag(arr0: Sequence[opt.Just[float]], /, *arrs: Sequence[opt.Just[float]]) -> _Matrix[np.float64]: ...
@overload
def block_diag(arr0: Sequence[opt.Just[complex]], /, *arrs: Sequence[opt.Just[complex]]) -> _Matrix[np.complex128]: ...
@overload
def block_diag(arr0: onp.CanArrayND[_SCT] | Sequence[_SCT], /, *arrs: onp.CanArrayND[_SCT] | Sequence[_SCT]) -> _Matrix[_SCT]: ...

#
@overload
def companion(a: Sequence[opt.JustInt]) -> _Matrix[np.int_]: ...
@overload
def companion(a: Sequence[opt.Just[float]]) -> _Matrix[np.float64]: ...
@overload
def companion(a: Sequence[opt.Just[complex]]) -> _Matrix[np.complex128]: ...
@overload
def companion(a: onp.CanArrayND[_SCT] | Sequence[_SCT]) -> _Matrix[_SCT]: ...

#
def helmert(n: onp.ToInt, full: bool = False) -> _Matrix[np.float64]: ...

#
def hilbert(n: onp.ToInt) -> _Matrix[np.float64]: ...

#
@overload
def fiedler(a: Sequence[opt.JustInt]) -> _Matrix[np.int_]: ...
@overload
def fiedler(a: Sequence[opt.Just[float]]) -> _Matrix[np.float64]: ...
@overload
def fiedler(a: Sequence[opt.Just[complex]]) -> _Matrix[np.complex128]: ...
@overload
def fiedler(a: onp.CanArrayND[_SCT] | Sequence[_SCT]) -> _Matrix[_SCT]: ...

#
@overload
def fiedler_companion(a: Sequence[opt.JustInt]) -> _Matrix[np.int_]: ...
@overload
def fiedler_companion(a: Sequence[opt.Just[float]]) -> _Matrix[np.float64]: ...
@overload
def fiedler_companion(a: Sequence[opt.Just[complex]]) -> _Matrix[np.complex128]: ...
@overload
def fiedler_companion(a: onp.CanArrayND[_SCT] | Sequence[_SCT]) -> _Matrix[_SCT]: ...

# TODO
@overload
def convolution_matrix(a: Sequence[opt.JustInt], n: onp.ToInt, mode: CorrelateMode = "full") -> _Matrix[np.int_]: ...
@overload
def convolution_matrix(a: Sequence[opt.Just[float]], n: onp.ToInt, mode: CorrelateMode = "full") -> _Matrix[np.float64]: ...
@overload
def convolution_matrix(a: Sequence[opt.Just[complex]], n: onp.ToInt, mode: CorrelateMode = "full") -> _Matrix[np.complex128]: ...
@overload
def convolution_matrix(a: onp.CanArrayND[_SCT] | Sequence[_SCT], n: onp.ToInt, mode: CorrelateMode = "full") -> _Matrix[_SCT]: ...

#
@overload
def invhilbert(n: onp.ToInt, exact: Literal[False] = False) -> _Matrix[np.float64]: ...
@overload
def invhilbert(n: onp.ToInt, exact: Literal[True]) -> _Matrix[np.int64] | _Matrix[np.object_]: ...

#
@overload
def pascal(n: onp.ToInt, kind: _Kind = "symmetric", exact: Literal[True] = True) -> _Matrix[np.uint64 | np.object_]: ...
@overload
def pascal(n: onp.ToInt, kind: _Kind = "symmetric", *, exact: Literal[False]) -> _Matrix[np.float64]: ...
@overload
def pascal(n: onp.ToInt, kind: _Kind, exact: Literal[False]) -> _Matrix[np.float64]: ...

#
@overload
def invpascal(n: onp.ToInt, kind: _Kind = "symmetric", exact: Literal[True] = True) -> _Matrix[np.int64 | np.object_]: ...
@overload
def invpascal(n: onp.ToInt, kind: _Kind = "symmetric", *, exact: Literal[False]) -> _Matrix[np.float64]: ...
@overload
def invpascal(n: onp.ToInt, kind: _Kind, exact: Literal[False]) -> _Matrix[np.float64]: ...

#
def dft(n: onp.ToInt, scale: Literal["sqrtn", "n"] | None = None) -> _Matrix[np.complex128]: ...
