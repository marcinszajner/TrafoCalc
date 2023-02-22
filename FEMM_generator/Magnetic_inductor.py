import math


class BlockCircuitPropsClass:
    def __init__(self):
        super().__init__()

        self.Circuit_block_dict = {
            "<CircuitName> = ": '"New Circuit"',
            "<TotalAmps_re> = ": 0,
            "<TotalAmps_im> = ": 0,
            "<CircuitType> = ": 1,
        }


class BlockPropsClass:
    def __init__(self):
        super().__init__()

        self.Block_dict = {
            "<BlockName> = ": '"New Material"',
            "<Mu_x> = ": 1,
            "<Mu_y> = ": 1,
            "<H_c> = ": 0,
            "<H_cAngle> = ": 0,
            "<J_re> = ": 0,
            "<J_im> = ": 0,
            "<Sigma> = ": 0,
            "<d_lam> = ": 0,
            "<Phi_h> = ": 0,
            "<Phi_hx> = ": 0,
            "<Phi_hy> = ": 0,
            "<LamType> = ": 0,
            "<LamFill> = ": 1,
            "<NStrands> = ": 0,
            "<WireD> = ": 0,
            "<BHPoints> = ": 0
        }


class FEMMMagneticInductorFormat:
    def __init__(self):
        super().__init__()

        self.FEMM_Data_dict = {
            "[Format]": 4.0,
            "[Frequency]": 0,
            "[Precision]": 1.0000000000000001e-009,
            "[MinAngle]": 30,
            "[DoSmartMesh]": 1,
            "[Depth]": 1,
            "[LengthUnits]": 'millimeters',
            "[ProblemType]": 'planar',
            "[Coordinates]": 'cartesian',
            "[ACSolver]": 0,
            "[PrevType]": 0,
            "[PrevSoln]": '\'\'',
            "[Comment]": '"Add comments here."',
            "[PointProps]": 0,
            "[BdryProps]": 0,
            "[BlockProps]": 0,
            "[CircuitProps]": 0,
            "[NumPoints]": 0,
            "[NumSegments]": 0,
            "[NumArcSegments]": 0,
            "[NumHoles]": 0,
            "[NumBlockLabels]": 0,
        }
        self.Nodes = []
        self.OutsideNodesNum = 0
        self.InsideNodesNum1 = 0
        self.InsideNodesNum2 = 0
        self.FrameNodesNum = 0
        self.Segments = []
        self.ArcSegments = []
        self.Blocks = []
        self.BlocksLabels = []
        self.CircuitProps = []
        self.WindingBoundary = {
            "x_left": 0,
            "x_right": 0,
            "y_down": 0,
            "y_up": 0,
            "center": 0
        }

    def save_FEMM_file(self, file_name):
        with open(file_name, 'w') as file:
            for k, v in self.FEMM_Data_dict.items():
                if str(k) == '[NumPoints]':
                    elements = len(self.Nodes)
                    file.write(str(k) + ' = ' + str(elements) + '\n')
                    for n in self.Nodes:
                        file.write(str(n[0]) + '\t' + str(n[1]) + '\t' + str(n[2]) + '\t' + str(n[3]) + '\n')
                elif str(k) == '[NumSegments]':
                    elements = len(self.Segments)
                    file.write(str(k) + ' = ' + str(elements) + '\n')
                    for n in self.Segments:
                        file.write(str(n[0]) + '\t' + str(n[1]) + '\t' + str(n[2]) + '\t' + str(n[3])
                                   + '\t' + str(n[4]) + '\t' + str(n[5]) + '\n')
                elif str(k) == '[NumArcSegments]':
                    elements = len(self.ArcSegments)
                    file.write(str(k) + ' = ' + str(elements) + '\n')
                    for n in self.ArcSegments:
                        file.write(str(n[0]) + '\t' + str(n[1]) + '\t' + str(n[2]) + '\t' + str(n[3])
                                   + '\t' + str(n[4]) + '\t' + str(n[5]) + '\t' + str(n[6]) + '\t' + str(n[7]) + '\n')
                elif str(k) == '[BlockProps]':
                    elements = len(self.Blocks)
                    file.write(str(k) + ' = ' + str(elements) + '\n')
                    for n in self.Blocks:
                        file.write('  <BeginBlock>' + '\n')
                        for j, i in n.items():
                            file.write('    ' + str(j) + str(i) + '\n')
                        file.write('  <EndBlock>' + '\n')
                elif str(k) == '[CircuitProps]':
                    elements = len(self.CircuitProps)
                    file.write(str(k) + ' = ' + str(elements) + '\n')
                    for n in self.CircuitProps:
                        file.write('  <BeginCircuit>' + '\n')
                        for j, i in n.items():
                            file.write('    ' + str(j) + str(i) + '\n')
                        file.write('  <EndCircuit>' + '\n')
                elif str(k) == '[NumBlockLabels]':
                    elements = len(self.BlocksLabels)
                    file.write(str(k) + ' = ' + str(elements) + '\n')
                    for n in self.BlocksLabels:
                        file.write(str(n[0]) + '\t' + str(n[1]) + '\t' + str(n[2]) + '\t' + str(n[3])
                                   + '\t' + str(n[4]) + '\t' + str(n[5]) + '\t' + str(n[6])
                                   + '\t' + str(n[7]) + '\t' + str(n[8]) + '\n')
                else:
                    file.write(str(k) + ' = ' + str(v) + '\n')

    def search_block_number(self, name):
        block_number = -1
        tmp = 0
        for n in self.Blocks:
            tmp += 1
            for j, i in n.items():
                if str(i) == '"' + name + '"':
                    block_number = tmp
        return block_number

    def create_node_coordinate_and_core_air_label(self, TransformerData):
        SizeA = TransformerData.SizeA
        SizeB = TransformerData.SizeB
        SizeC = TransformerData.SizeC
        SizeD = TransformerData.SizeD
        SizeE = TransformerData.SizeE
        SizeF = TransformerData.SizeF
        gap = TransformerData.Gap

        self.FEMM_Data_dict["[Depth]"] = SizeF

        OutsideNodes = []
        OutsideNodes.append([0, 0, 0, 0])
        OutsideNodes.append([0, 2 * SizeD, 0, 0])
        OutsideNodes.append([SizeA, 2 * SizeD, 0, 0])
        OutsideNodes.append([SizeA, 0, 0, 0])

        InsideNode1_1_corX = round((SizeA - SizeB) / 2, 6)
        InsideNode1_1_corY = round(SizeD - SizeE, 6)
        distance_tmp = round((SizeB - SizeC) / 2, 6)
        SizeE_with_gap = SizeE - gap

        self.WindingBoundary['x_left'] = InsideNode1_1_corX
        self.WindingBoundary['x_right'] = InsideNode1_1_corX + distance_tmp
        self.WindingBoundary['y_down'] = InsideNode1_1_corY
        self.WindingBoundary['y_up'] = InsideNode1_1_corY + (2 * SizeE)
        self.WindingBoundary["center"] = SizeA / 2

        InsideNodes = []
        InsideNodes.append([InsideNode1_1_corX, InsideNode1_1_corY, 0, 0])
        InsideNodes.append([InsideNode1_1_corX + distance_tmp, InsideNode1_1_corY, 0, 0])
        InsideNodes.append([InsideNode1_1_corX + distance_tmp, InsideNode1_1_corY + SizeE_with_gap, 0, 0])
        InsideNodes.append([InsideNode1_1_corX + distance_tmp + SizeC, InsideNode1_1_corY + SizeE_with_gap, 0, 0])
        InsideNodes.append([InsideNode1_1_corX + distance_tmp + SizeC, InsideNode1_1_corY, 0, 0])
        InsideNodes.append([InsideNode1_1_corX + (2 * distance_tmp) + SizeC, InsideNode1_1_corY, 0, 0])
        InsideNodes.append([InsideNode1_1_corX + (2 * distance_tmp) + SizeC, InsideNode1_1_corY + (2 * SizeE), 0, 0])
        InsideNodes.append([InsideNode1_1_corX + distance_tmp + SizeC, InsideNode1_1_corY + (2 * SizeE), 0, 0])
        InsideNodes.append([InsideNode1_1_corX + distance_tmp + SizeC, InsideNode1_1_corY
                            + (2 * SizeE) - SizeE_with_gap, 0, 0])
        InsideNodes.append([InsideNode1_1_corX + distance_tmp, InsideNode1_1_corY + (2 * SizeE) - SizeE_with_gap, 0, 0])
        InsideNodes.append([InsideNode1_1_corX + distance_tmp, InsideNode1_1_corY + (2 * SizeE), 0, 0])
        InsideNodes.append([InsideNode1_1_corX, InsideNode1_1_corY + (2 * SizeE), 0, 0])

        middle_point = [SizeA / 2, SizeD]
        FrameNodes = []
        FrameNodes.append([middle_point[0] - (2 * SizeA), middle_point[1] - (4 * SizeD), 0, 0])
        FrameNodes.append([middle_point[0] + (2 * SizeA), middle_point[1] - (4 * SizeD), 0, 0])
        FrameNodes.append([middle_point[0] + (2 * SizeA), middle_point[1] + (4 * SizeD), 0, 0])
        FrameNodes.append([middle_point[0] - (2 * SizeA), middle_point[1] + (4 * SizeD), 0, 0])

        block_number = self.search_block_number(TransformerData.CoreMaterialName)
        blocklabelcore = [SizeA / 2, SizeD * 1.5, block_number, -1, 0, 0, 0, 0, 0]
        self.BlocksLabels.append(blocklabelcore)

        block_number = self.search_block_number('Air')
        blocklabelcore = [SizeA / 2, SizeD * 3, block_number, -1, 0, 0, 0, 0, 0]
        self.BlocksLabels.append(blocklabelcore)

        self.Nodes += OutsideNodes
        self.Nodes += InsideNodes
        self.Nodes += FrameNodes

        self.OutsideNodesNum = len(OutsideNodes)
        self.InsideNodesNum1 = len(InsideNodes)
        self.FrameNodesNum = len(FrameNodes)

    def create_segments_coordinate(self):
        SegmentNum = 0
        index = 0
        OutsideSegments = []
        while index < self.OutsideNodesNum - 1:
            OutsideSegments.append([SegmentNum, SegmentNum + 1, -1, 0, 0, 0])
            index += 1
            SegmentNum += 1
        OutsideSegments.append([SegmentNum, 0, -1, 0, 0, 0])
        SegmentNum += 1

        index = 0
        InsideSegments = []
        first_element = SegmentNum
        while index < self.InsideNodesNum1- 1:
            InsideSegments.append([SegmentNum, SegmentNum + 1, -1, 0, 0, 0])
            index += 1
            SegmentNum += 1
        InsideSegments.append([SegmentNum, first_element, -1, 0, 0, 0])
        SegmentNum += 1

        index = 0
        first_element = SegmentNum
        FrameSegments = []
        while index < self.FrameNodesNum - 1:
            FrameSegments.append([SegmentNum, SegmentNum + 1, -1, 0, 0, 0])
            index += 1
            SegmentNum += 1
        FrameSegments.append([SegmentNum, first_element, -1, 0, 0, 0])

        self.Segments += OutsideSegments
        self.Segments += InsideSegments
        self.Segments += FrameSegments

    def create_material_block(self, material_name, permeability, conductivity):
        block = BlockPropsClass()
        block.Block_dict["<BlockName> = "] = '"' + material_name + '"'
        block.Block_dict["<Mu_x> = "] = permeability
        block.Block_dict["<Mu_y> = "] = permeability
        block.Block_dict["<Sigma> = "] = conductivity / 1000000
        self.Blocks.append(block.Block_dict)

    def create_wire_material_block(self, material_name, permeability, conductivity, dia):
        block = BlockPropsClass()
        block.Block_dict["<BlockName> = "] = '"' + material_name + '"'
        block.Block_dict["<Mu_x> = "] = permeability
        block.Block_dict["<Mu_y> = "] = permeability
        block.Block_dict["<Sigma> = "] = conductivity / 1000000  # FEMM use M * ohm / m unit
        block.Block_dict["<LamType> = "] = 3
        block.Block_dict["<WireD> = "] = dia
        block.Block_dict["<NStrands> = "] = 1
        self.Blocks.append(block.Block_dict)

    def create_circuit_block(self, circuit_name, current):
        circuit_block = BlockCircuitPropsClass()
        circuit_block.Circuit_block_dict["<CircuitName> = "] = circuit_name
        circuit_block.Circuit_block_dict["<TotalAmps_re> = "] = current
        self.CircuitProps.append(circuit_block.Circuit_block_dict)

    def create_wire_primary(self, input_data, output_data, BobbinX, BobbinY):
        x_left = self.WindingBoundary["x_left"]
        x_right = self.WindingBoundary["x_right"]
        y_down = self.WindingBoundary["y_down"]
        y_up = self.WindingBoundary["y_up"]
        center = self.WindingBoundary["center"]
        margin = 0.01
        layer_thickness = input_data.BetweenWireLayerInsulationThickness
        insulation_thickness = input_data.PrimaryWireInsulationThickness
        # if input_data.PrimaryWindingSelected > 0:
        #     windingNum = input_data.PrimaryWindingSelected
        # else:
        #     windingNum = output_data.PrimaryWinding
        windingNum = input_data.WindingNumInductance

        y_up -= BobbinY + input_data.Margine
        y_down += BobbinY + input_data.Margine
        x_right -= BobbinX

        node_number = len(self.Nodes)
        wireNum = 0

        block_number = self.search_block_number(input_data.PrimaryWindingMaterial + '_primary')
        if block_number == -1:
            raise Exception('failed search block')
        dia = round(self.Blocks[block_number - 1]["<WireD> = "], 4) + 0.001
        dia_insulation = dia + (2*insulation_thickness)

        num_of_winding_y = int((y_up - y_down) / (dia_insulation + margin)) - 1
        current_winding_y_pos = 0
        current_winding_x_pos = 0

        while windingNum > wireNum:
            while num_of_winding_y > current_winding_y_pos and windingNum > wireNum:
                x = x_right - margin * 2 - ((4 * margin + layer_thickness) * current_winding_x_pos)\
                    - (dia_insulation * current_winding_x_pos)
                y = y_down + margin * 2 + (margin * current_winding_y_pos)\
                    + (dia_insulation * current_winding_y_pos) + (dia_insulation / 2)
                self.Nodes.append([x, y, 0, 0])
                self.Nodes.append([x - dia, y, 0, 0])
                self.ArcSegments.append([node_number, node_number + 1, 180, 1, 0, 0, 0, 1])
                self.ArcSegments.append([node_number + 1, node_number, 180, 1, 0, 0, 0, 1])
                self.BlocksLabels.append([x - (dia / 2), y, block_number, -1, 1, 0, 0, 1, 1])
                node_number = len(self.Nodes)

                x = x_right + ((center - x_right) * 2) + margin * 2\
                    + ((4 * margin + layer_thickness) * current_winding_x_pos)\
                    + (dia_insulation * current_winding_x_pos)
                y = y_down + margin * 2 + (margin * current_winding_y_pos)\
                    + (dia_insulation * current_winding_y_pos) + (dia_insulation / 2)
                self.Nodes.append([x, y, 0, 0])
                self.Nodes.append([x + dia, y, 0, 0])
                self.ArcSegments.append([node_number, node_number + 1, 180, 1, 0, 0, 0, 1])
                self.ArcSegments.append([node_number + 1, node_number, 180, 1, 0, 0, 0, 1])
                self.BlocksLabels.append([x + (dia / 2), y, block_number, -1, 1, 0, 0, -1, 1])
                node_number = len(self.Nodes)

                current_winding_y_pos += 1
                wireNum += 1

            current_winding_x_pos += 1
            current_winding_y_pos = 0
            #       Add air
        x = x_right - margin
        y = y_down + margin
        block_number = self.search_block_number('Air')
        block_label_core = [x - margin, y + margin, block_number, -1, 0, 0, 0, 0, 0]
        self.BlocksLabels.append(block_label_core)

    def set_frequency(self, frequency):
        self.FEMM_Data_dict["[Frequency]"] = frequency

    def create_magnetic_inductor_model(self, input_data, output_data, file_name):
        if input_data.WireCrossSectionSelectedInductance > 0:
            cross_section = input_data.WireCrossSectionSelectedInductance
        else:
            cross_section = input_data.WireCrossSectionInductance

        primary_dia = math.sqrt(cross_section / math.pi) * 2
        self.set_frequency(input_data.Frequency)

        self.create_material_block(input_data.CoreMaterialName,
                                   input_data.CorePermeability,
                                   input_data.CoreConductivity)
        self.create_material_block('Air', 1, 0)

        self.create_wire_material_block(input_data.PrimaryWindingMaterial + '_primary',
                                        1,
                                        input_data.PrimaryWindingMaterialConductivity,
                                        primary_dia)

        self.create_circuit_block('Primary', input_data.CurrentMax)

        if input_data.CoreShape == 'EE':
            self.create_node_coordinate_and_core_air_label(input_data)
            self.create_segments_coordinate()

            self.create_wire_primary(input_data,
                                     output_data,
                                     float(input_data.BobbinXmargine),
                                     float(input_data.BobbinYmargine))
            self.save_FEMM_file(file_name)
