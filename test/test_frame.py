from src.frame import Frame

frame_prueba = Frame("45")


def test_str():
    assert str(frame_prueba) == "Este frame es: |4,5|"
