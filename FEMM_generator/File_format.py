from src.Transformer import Transformer
from FEMM_generator import Magnetic
from FEMM_generator import Electrostatic
from FEMM_generator import Magnetic_inductor


class FEMMmodelclass:
    def __init__(self):
        super().__init__()

    def CreateFEMMfile(self, transformer_data: Transformer, file_name, is_simple_wire):
        input_data = transformer_data.TransformerValue
        output_data = transformer_data.TransformerOutputValue
        if input_data.ModelType == 'Magnetic field simulation':
            magnetic = Magnetic.FEMMMagneticFormat()
            magnetic.create_magnetic_model(input_data, output_data, file_name, is_simple_wire)
        elif input_data.ModelType == 'Electrostatic field simulation':
            electrostatic = Electrostatic.FEMMElectrostaticFormat()
            electrostatic.create_electrostatic_model(input_data, output_data, file_name, is_simple_wire)
        elif input_data.ModelType == 'Inductance':
            magnetic_inductor = Magnetic_inductor.FEMMMagneticInductorFormat()
            magnetic_inductor.create_magnetic_inductor_model(input_data, output_data, file_name, is_simple_wire)
