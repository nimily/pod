from .core import PodConverterCatalog
from .catalogs import get_catalog
from .decorators import pod, pod_json, pod_bytes, field
from .types import (
    Bool,
    I8l,
    I8b,
    I8,
    U8l,
    U8b,
    U8,
    I16l,
    I16b,
    I16,
    U16l,
    U16b,
    U16,
    I32l,
    I32b,
    I32,
    U32l,
    U32b,
    U32,
    I64l,
    I64b,
    I64,
    U64l,
    U64b,
    U64,
    I128l,
    I128b,
    I128,
    U128l,
    U128b,
    U128,
    F32l,
    F32b,
    F32,
    F64l,
    F64b,
    F64,
    FixedLenArray,
    FixedLenBytes,
    FixedLenStr,
    Vec,
    Bytes,
    Str,
    Enum,
    Variant,
    named_fields,
    Option,
    Static,
    Default,
    ForwardRef,
    AutoTagType,
)
from .bytes import (
    dataclass_is_static,
    dataclass_calc_max_size,
    dataclass_to_bytes_partial,
    dataclass_from_bytes_partial,
    BYTES_CATALOG,
    AutoTagTypeValueManager,
)
from .errors import PodPathError
from .json import JSON_CATALOG
from ._utils import (
    FORMAT_ZERO_COPY,
    FORMAT_AUTO,
    FORMAT_BORSH,
    FORMAT_PASS,
    FORMAT_TO_TYPE,
)

# prevent cycles between _utils and types.atomic
AutoTagTypeValueManager.TAG_TYPE[0] = U64
