from pod import (
    FixedLenArray,
    Option,
    Vec,
    Str,
    Bytes,
    U32,
    pod,
    U8,
)


@pod
class Simple:
    num: U32
    string: Str


@pod
class MyStruct:
    # a_builtin: U8
    # a_string: Str[10]
    # a_array: FixedLenArray[U8, 10]
    # a_bytes: Bytes[512]
    a_vec: Vec[Option[U8], 10]


from pod.bytes import BYTES_CATALOG


def test_round_trip_bytes():
    O = Option[Str[10]]
    val = MyStruct(
        # 8,
        # "hi",
        # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        # bytes([1, 2, 3]),
        [
            Option[U8].NONE
            # Option[Str[10]].SOME("hi"),
            # Option[Str[10]].NONE,
            # O.SOME("bye"),
            # O.SOME("sad"),
        ],
    )
    print(val)
    serialized = MyStruct.to_bytes(val)
    print(serialized)
    deserialized = MyStruct.from_bytes(serialized)
    print(deserialized)

    assert val == deserialized


def test_fixed_len_array_wrong_size():
    @pod
    class AnArray:
        b: FixedLenArray[U8, 10]

    b = AnArray([1, 2, 3])
    print(b)
    try:
        ser = AnArray.to_bytes(b)
    except ValueError:
        pass
