import pytest
from pySerialX.serialx_jit_interpreter import SerialXInterpreter


def test_encode_set_jit_values():
    assert SerialXInterpreter._encode_set(["set", "uint8_t", "led", 8]) == "su led 8"
    assert SerialXInterpreter._encode_set(["set", "uint16_t", "led", 16]) == "sw led 16"

    # TODO


def test_encode_set_bool_invalid():
    # Invalid value
    assert SerialXInterpreter._encode_set(["set", "uint16_", "led", 16]) is None
