import math


class TransformerValueClass:
    def __init__(self):
        super().__init__()

        self.InputVoltageShape = 'Sinus'
        self.CurrentDensity = 0
        self.Bmax = 0
        self.CoreCrossSection = 0
        self.CoreWindingArea = 0
        self.FillFactor = 1
        self.Frequency = 0
        self.InputVoltage = 0
        self.OutputPower = 0
        self.OutputVoltage = 0
        self.MagneticPathLength = 0
        self.CorePermeability = 0
        self.CoreConductivity = 0
        self.CorePermittivity = 0
        self.PrimaryWireInsulationThickness = 0
        self.SecondaryWireInsulationThickness = 0
        self.PrimaryWireInsulationMaterialPermittivity = 0
        self.SecondaryWireInsulationMaterialPermittivity = 0
        self.PrimaryWireInsulationName = ''
        self.SecondaryWireInsulationName = ''
        self.PrimaryWindingSelected = 0
        self.PrimaryWireCrossSectionSelected = 0
        self.SecondaryWindingSelected = 0
        self.SecondaryWireCrossSectionSelected = 0

#       Core Size
        self.CoreShape = 'EE'
        self.SizeA = 0
        self.SizeB = 0
        self.SizeC = 0
        self.SizeD = 0
        self.SizeE = 0
        self.SizeF = 0
        self.CoreMaterialName = 'Core name'
        self.BobbinXmargine = 0
        self.BobbinY1margine = 0

        self.ModelType = ''

        self.PrimaryWindingMaterial = 'Copper primary'
        self.PrimaryWindingMaterialConductivity = 58000000
        self.SecondaryWindingMaterial = 'Copper secondary'
        self.SecondaryWindingMaterialConductivity = 58000000
        self.BobbinMaterial = 'new material'
        self.BobbinMaterialPermittivity = 0
        self.BetweenWireLayerInsulationMaterial = 'new material'
        self.BetweenWireLayerInsulationMaterialPermittivity = 0
        self.BobbinY2margine = 0
        self.BetweenWireLayerInsulationThickness = 0

        #inductor params
        self.Inductance = 0
        self.CurrentMax = 0
        self.WindingNumInductance = 0
        self.WindingNumInductanceSelected = 0;
        self.Gap = 0
        self.WireCrossSectionInductance = 0
        self.WireCrossSectionSelectedInductance = 0

        self.SimplifiedWireModel = 0


class TransformerOutputValueClass:
    def __init__(self):
        super().__init__()

        self.PrimaryWinding = 0
        self.SecondaryWinding = 0
        self.MagnetizationCurrentMax = 0
        self.PrimaryWireCrossSection = 0
        self.SecondaryWireCrossSection = 0
        self.ApTheory = 0
        self.ApCalculated = 0
        self.ApTheoryInductance = 0
        self.ApCalculatedInductance = 0



class Transformer:
    def __init__(self):
        super().__init__()

        self.TransformerValue = TransformerValueClass()
        self.TransformerOutputValue = TransformerOutputValueClass()

    def SelectValue(self, Calculated, UserValue):
        if UserValue > 0:
            return UserValue
        else:
            return Calculated

    def is_float(self, string):
        try:
            float(string)
            return True
        except:
            return False

    def update_params(self, TransformerValue):
        a = vars(TransformerValue)
        for key, value in a.items():
            if getattr(TransformerValue, key) == '':
                setattr(TransformerValue, key, 0)
            attr = getattr(TransformerValue, key)
            if not self.is_float(attr):
                setattr(self.TransformerValue, key, attr)
            else:
                setattr(self.TransformerValue, key, float(attr))

    def Calculate_VoltSecond(self):
        Frequency = self.TransformerValue.Frequency
        InputVoltage = self.TransformerValue.InputVoltage
        if self.TransformerValue.InputVoltageShape == 'Sinus':
            VoltSecond = InputVoltage/(math.pi*Frequency)
        elif self.TransformerValue.InputVoltageShape == 'Square':
            VoltSecond = InputVoltage/(Frequency*2)
        return VoltSecond

    def Calculate_winding_number(self):
        Bmax = self.TransformerValue.Bmax / 1000
        CoreCrossSection = self.TransformerValue.CoreCrossSection / 1000000
        InputVoltage = self.TransformerValue.InputVoltage
        OutputVoltage = self.TransformerValue.OutputVoltage
        VoltSecond = self.Calculate_VoltSecond()

        PrimaryWinding = VoltSecond/(2*Bmax*CoreCrossSection)

        if self.TransformerValue.PrimaryWindingSelected > 0:
            PrimaryWinding = self.TransformerValue.PrimaryWindingSelected

        SecondaryWinding = (OutputVoltage/InputVoltage)*PrimaryWinding

        self.TransformerOutputValue.PrimaryWinding = VoltSecond/(2*Bmax*CoreCrossSection)
        self.TransformerOutputValue.SecondaryWinding = SecondaryWinding

    def Calculate_magnetization_current(self):
        VoltSecond = self.Calculate_VoltSecond()
        A_e = self.TransformerValue.CoreCrossSection / 1000000
        Permability = self.TransformerValue.CorePermeability * 0.000001256637 #Vacuum permeability, around 4PI*10^-7 H/m
        Magnetic_path_lenght = self.TransformerValue.MagneticPathLength / 1000
        if self.TransformerValue.PrimaryWindingSelected > 0:
            Primary_winding = self.TransformerValue.PrimaryWindingSelected
        else:
            Primary_winding = self.TransformerOutputValue.PrimaryWinding

        #divided by 2, because result is delta current, so max value is half of it
        MagnetizationCurrentMax = (VoltSecond*Magnetic_path_lenght) / \
                                  (Primary_winding * Primary_winding * A_e * Permability*2)

        self.TransformerOutputValue.MagnetizationCurrentMax = MagnetizationCurrentMax

    def Calculate_wire_cross_section(self):
        PrimaryCurrent = (self.TransformerValue.OutputPower/self.TransformerValue.InputVoltage)\
                         + self.TransformerOutputValue.MagnetizationCurrentMax
        SecondaryCurrent = self.TransformerValue.OutputPower/self.TransformerValue.OutputVoltage
        CurrentDensity = self.TransformerValue.CurrentDensity

        PrimaryWireCrossSection = PrimaryCurrent/CurrentDensity
        SecondaryWireCrossSection = SecondaryCurrent/CurrentDensity

        self.TransformerOutputValue.PrimaryWireCrossSection = PrimaryWireCrossSection
        self.TransformerOutputValue.SecondaryWireCrossSection = SecondaryWireCrossSection

    def Calculate_Ap(self):
        Ae = self.TransformerValue.CoreCrossSection / 1000000

        Wa1 = self.SelectValue(self.TransformerOutputValue.PrimaryWireCrossSection,
                               self.TransformerValue.PrimaryWireCrossSectionSelected) / 1000000
        N1 = self.SelectValue(self.TransformerOutputValue.PrimaryWinding,
                              self.TransformerValue.PrimaryWindingSelected)
        Wa2 = self.SelectValue(self.TransformerOutputValue.SecondaryWireCrossSection,
                               self.TransformerValue.SecondaryWireCrossSectionSelected) / 1000000
        N2 = self.SelectValue(self.TransformerOutputValue.SecondaryWinding,
                              self.TransformerValue.SecondaryWindingSelected)
        k = self.TransformerValue.FillFactor

        self.TransformerOutputValue.ApCalculated = ((Wa1*N1 + Wa2*N2)/k) * Ae
        Aw = self.TransformerValue.CoreWindingArea / 1000000
        self.TransformerOutputValue.ApTheory = Ae * Aw

    def Calculate_Ap_inductance(self):
        Ae = self.TransformerValue.CoreCrossSection / 1000000

        Wa = self.SelectValue(self.TransformerValue.WireCrossSectionInductance,
                               self.TransformerValue.WireCrossSectionSelectedInductance) / 1000000
        N = self.SelectValue(self.TransformerValue.WindingNumInductance,
                               self.TransformerValue.WindingNumInductanceSelected)

        k = self.TransformerValue.FillFactor

        self.TransformerOutputValue.ApCalculatedInductance = (Wa*N/k) * Ae
        Aw = self.TransformerValue.CoreWindingArea / 1000000
        self.TransformerOutputValue.ApTheoryInductance = Ae * Aw

    def validate_input_data_basic_simulation(self):
        if not(self.TransformerValue.InputVoltage > 0.0 and self.TransformerValue.CoreCrossSection > 0.0 and
               self.TransformerValue.OutputVoltage > 0.0 and self.TransformerValue.Bmax > 0.0 and
               self.TransformerValue.MagneticPathLength > 0.0 and self.TransformerValue.CurrentDensity and
               self.TransformerValue.CoreWindingArea > 0.0 and self.TransformerValue.OutputPower > 0.0 and
               self.TransformerValue.Frequency > 0.0 and self.TransformerValue.CorePermeability > 0.0 and
               1 >= self.TransformerValue.FillFactor > 0.0):
            raise Exception('incorrect value of param')

    def validate_dimensions(self):
        if not (self.TransformerValue.SizeA > 0.0 and self.TransformerValue.SizeB > 0.0 and
                self.TransformerValue.SizeC > 0.0 and self.TransformerValue.SizeD > 0.0 and
                self.TransformerValue.SizeE > 0.0 and self.TransformerValue.SizeF):
            raise Exception('incorrect dimension of param')

    def Calculate_inductor_gap_turns_wire_cross_section(self):
        ind = self.TransformerValue.Inductance / 1000
        curr = self.TransformerValue.CurrentMax
        Bmax = self.TransformerValue.Bmax / 1000
        SizeC = self.TransformerValue.SizeC
        SizeF = self.TransformerValue.SizeF
        CoreRelu = ((self.TransformerValue.MagneticPathLength / 1000) / self.TransformerValue.CorePermeability)
        uo = 0.0000012563706

        Ae = SizeC * SizeF / 1000000
        curr_dens = self.TransformerValue.CurrentDensity

        cross_section = curr / curr_dens


        for x in range(10):
            N = (ind * curr) / (Ae * Bmax)
            lg = ((uo * N * curr) / Bmax) - CoreRelu
            Ae = (SizeC + lg) * (SizeF + lg) / 1000000
        self.TransformerValue.WindingNumInductance = N

        if self.TransformerValue.WindingNumInductanceSelected > 0:
            N = self.TransformerValue.WindingNumInductanceSelected
            for x in range(10):
                lg = N*N*(uo*Ae)/ind - CoreRelu
                Ae = (SizeC + lg) * (SizeF + lg) / 1000000

        self.TransformerValue.Gap = lg * 1000
        self.TransformerValue.PrimaryWireCrossSectionInductance = cross_section
