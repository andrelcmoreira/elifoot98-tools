
class EquipaHeaderNotFound(Exception):

    def __init__(self, input_file):
        super().__init__(f"equipa header not found on '{input_file}'!")
