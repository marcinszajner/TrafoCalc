from Transformer import Transformer
from FEMM_generator import Magnetic
from FEMM_generator import Electrostatic


class FEMMmodelclass:
    def __init__(self):
        super().__init__()

    def CreateFEMMfile(self, transformer_data: Transformer, file_name):
        input_data = transformer_data.TransformerValue
        output_data = transformer_data.TransformerOutputValue
        if input_data.ModelType == 'Magnetic field simulation':
            magnetic = Magnetic.FEMMMagneticFormat()
            magnetic.create_magnetic_model(input_data, output_data, file_name)
        elif input_data.ModelType == 'Electrostatic field simulation':
            electrostatic = Electrostatic.FEMMElectrostaticFormat()
            electrostatic.create_electrostatic_model(input_data, output_data, file_name)
