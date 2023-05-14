import math
from FEMM_generator.draw import *

class BlockConductorPropsClass:
    def __init__(self):
        super().__init__()

        self.Conductor_block_dict = {
            "<ConductorName> = ": '"New Conductor"',
            "<vc> = ": 0,
            "<qc> = ": 0,
            "<ConductorType> = ": 1,
        }


class BlockPropsClass:
    def __init__(self):
        super().__init__()

        self.Block_dict = {
            "<BlockName> = ": '"New Material"',
            "<ex> = ": 1,
            "<ey> = ": 1,
            "<qv> = ": 0,
        }


class FEMMElectrostaticFormat:
    def __init__(self):
        super().__init__()

        self.FEMM_Data_dict = {
            "[Format]": 1,
            "[Precision]": 1.0000000000000001e-010,
            "[MinAngle]": 30,
            "[DoSmartMesh]": 1,
            "[Depth]": 1,
            "[LengthUnits]": 'millimeters',
            "[ProblemType]": 'planar',
            "[Coordinates]": 'cartesian',
            "[Comment]": '"Add comments here."',
            "[PointProps]": 0,
            "[BdryProps]": 0,
            "[BlockProps]": 0,
            "[ConductorProps]": 0,
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
        self.ConductorProps = []
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
                        file.write(str(n[0]) + '\t' + str(n[1]) + '\t' + str(n[2]) + '\t'
                                   + str(n[3]) + '\t' + str(n[4]) + '\n')
                elif str(k) == '[NumSegments]':
                    elements = len(self.Segments)
                    file.write(str(k) + ' = ' + str(elements) + '\n')
                    for n in self.Segments:
                        file.write(str(n[0]) + '\t' + str(n[1]) + '\t' + str(n[2]) + '\t' + str(n[3])
                                   + '\t' + str(n[4]) + '\t' + str(n[5]) + '\t' + str(n[6]) + '\n')
                elif str(k) == '[NumArcSegments]':
                    elements = len(self.ArcSegments)
                    file.write(str(k) + ' = ' + str(elements) + '\n')
                    for n in self.ArcSegments:
                        file.write(str(n[0]) + '\t' + str(n[1]) + '\t' + str(n[2]) + '\t' + str(n[3])
                                   + '\t' + str(n[4]) + '\t' + str(n[5]) + '\t' + str(n[6]) + '\t' + str(n[7])
                                   + '\t' + str(n[8]) + '\n')
                elif str(k) == '[BlockProps]':
                    elements = len(self.Blocks)
                    file.write(str(k) + ' = ' + str(elements) + '\n')
                    for n in self.Blocks:
                        file.write('  <BeginBlock>' + '\n')
                        for j, i in n.items():
                            file.write('    ' + str(j) + str(i) + '\n')
                        file.write('  <EndBlock>' + '\n')
                elif str(k) == '[ConductorProps]':
                    elements = len(self.ConductorProps)
                    file.write(str(k) + ' = ' + str(elements) + '\n')
                    for n in self.ConductorProps:
                        file.write('  <BeginConductor>' + '\n')
                        for j, i in n.items():
                            file.write('    ' + str(j) + str(i) + '\n')
                        file.write('  <EndConductor>' + '\n')
                elif str(k) == '[NumBlockLabels]':
                    elements = len(self.BlocksLabels)
                    file.write(str(k) + ' = ' + str(elements) + '\n')
                    for n in self.BlocksLabels:
                        file.write(str(n[0]) + '\t' + str(n[1]) + '\t' + str(n[2]) + '\t' + str(n[3])
                                   + '\t' + str(n[4]) + '\t' + str(n[5]) + '\n')
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

        self.FEMM_Data_dict["[Depth]"] = SizeF

        OutsideNodes = []
        OutsideNodes.append([0, 0])
        OutsideNodes.append([0, 2 * SizeD])
        OutsideNodes.append([SizeA, 2 * SizeD])
        OutsideNodes.append([SizeA, 0])
        draw_polygon(OutsideNodes, self.Nodes, self.Segments, [0])

        InsideNode1_1_corX = round((SizeA - SizeB) / 2, 6)
        InsideNode1_1_corY = round(SizeD - SizeE, 6)
        distance_tmp = round((SizeB - SizeC) / 2, 6)

        self.WindingBoundary['x_left'] = InsideNode1_1_corX
        self.WindingBoundary['x_right'] = InsideNode1_1_corX + distance_tmp
        self.WindingBoundary['y_down'] = InsideNode1_1_corY
        self.WindingBoundary['y_up'] = InsideNode1_1_corY + (2 * SizeE)
        self.WindingBoundary["center"] = SizeA / 2

        shift = SizeC + distance_tmp
        InsideNodes2 = []
        InsideNodes2.append([InsideNode1_1_corX + shift, InsideNode1_1_corY])
        InsideNodes2.append([InsideNode1_1_corX + distance_tmp + shift, InsideNode1_1_corY])
        InsideNodes2.append([InsideNode1_1_corX + distance_tmp + shift, InsideNode1_1_corY + (2 * SizeE)])
        InsideNodes2.append([InsideNode1_1_corX + shift, InsideNode1_1_corY + (2 * SizeE)])
        draw_polygon(InsideNodes2, self.Nodes, self.Segments, [0])

        middle_point = [SizeA / 2, SizeD]
        FrameNodes = []
        FrameNodes.append([middle_point[0] - (2 * SizeA), middle_point[1] - (4 * SizeD)])
        FrameNodes.append([middle_point[0] + (2 * SizeA), middle_point[1] - (4 * SizeD)])
        FrameNodes.append([middle_point[0] + (2 * SizeA), middle_point[1] + (4 * SizeD)])
        FrameNodes.append([middle_point[0] - (2 * SizeA), middle_point[1] + (4 * SizeD)])
        draw_polygon(FrameNodes, self.Nodes, self.Segments, [0])

        block_number = self.search_block_number(TransformerData.CoreMaterialName)
        blocklabelcore = [SizeA / 2, SizeD * 1.5, block_number, -1, 0, 0]
        self.BlocksLabels.append(blocklabelcore)

        block_number = self.search_block_number('Air')
        blocklabelcore = [SizeA / 2, SizeD * 3, block_number, -1, 0, 0]
        self.BlocksLabels.append(blocklabelcore)

    def create_material_block(self, material_name, permittivity):
        block = BlockPropsClass()
        block.Block_dict["<BlockName> = "] = '"' + material_name + '"'
        block.Block_dict["<ex> = "] = permittivity
        block.Block_dict["<ey> = "] = permittivity
        block.Block_dict["<qv> = "] = 0
        self.Blocks.append(block.Block_dict)

    def create_conductor_block(self, Conductor_name, voltage):
        Conductor_block = BlockConductorPropsClass()
        Conductor_block.Conductor_block_dict["<ConductorName> = "] = Conductor_name
        Conductor_block.Conductor_block_dict["<Vc> = "] = voltage
        self.ConductorProps.append(Conductor_block.Conductor_block_dict)

    def create_wire_primary(self, input_data, output_data, BobbinX, BobbinY1, BobbinY2, voltage, primary_dia, is_simple_wire):
        x_left = self.WindingBoundary["x_left"]
        x_right = self.WindingBoundary["x_right"]
        y_down = self.WindingBoundary["y_down"]
        y_up = self.WindingBoundary["y_up"]
        center = self.WindingBoundary["center"]
        margin = 0.01
        layer_thickness = input_data.BetweenWireLayerInsulationThickness
        insulation_thickness = input_data.PrimaryWireInsulationThickness
        if input_data.PrimaryWindingSelected > 0:
            windingNum = int(input_data.PrimaryWindingSelected)
        else:
            windingNum = int(output_data.PrimaryWinding)
        voltage_per_winding = voltage/windingNum
        node_number = len(self.Nodes)

        block_number_bobbin = self.search_block_number(input_data.BobbinMaterial)
        if block_number_bobbin == -1:
            raise Exception('failed search block')
        if BobbinX != 0 and BobbinY1 != 0 and BobbinY2 != 0 and \
           BobbinX > margin and BobbinY1 > margin and BobbinY2 > margin:
            bobbin = []
            bobbin.append([x_left, y_down])
            bobbin.append([x_right, y_down])
            bobbin.append([x_right, y_up])
            bobbin.append([x_left, y_up - margin])
            bobbin.append([x_left, y_up - BobbinY1])
            bobbin.append([x_right - BobbinX, y_up - BobbinY1])
            bobbin.append([x_right - BobbinX, y_down + BobbinY2])
            bobbin.append([x_left, y_down + BobbinY2])
            draw_polygon(bobbin, self.Nodes, self.Segments, [0])
            # This segment must be add as workaround
            self.Segments.append([node_number + 4, node_number + 7, -1, 0, 0, 0, 1])
            self.BlocksLabels.append([x_right - margin - (BobbinX / 2),
                                      y_down + margin + (BobbinY2 / 2), block_number_bobbin,
                                      -1, 1, 0, 0, 1, 1])
        else:
            bobbin = []
            bobbin.append([x_left, y_down])
            bobbin.append([x_right, y_down])
            bobbin.append([x_right, y_up])
            bobbin.append([x_left, y_up])
            draw_polygon(bobbin, self.Nodes, self.Segments, [0])

        y_up -= BobbinY1
        y_down += BobbinY2
        x_right -= BobbinX

        wireNum = 0

        block_number = self.search_block_number(input_data.PrimaryWindingMaterial + '_primary')
        if block_number == -1:
            raise Exception('failed search block')
        block_number_insulation = self.search_block_number('Primary_wire_insulation')
        if block_number == -1:
            raise Exception('failed search block')
        block_number_layer_insulation = self.search_block_number(input_data.BetweenWireLayerInsulationMaterial)
        if block_number == -1:
            raise Exception('failed search block')
        dia = primary_dia
        dia_insulation = dia + (2*insulation_thickness)

        num_of_winding_y = int((y_up - y_down) / (dia_insulation + margin))
        current_winding_y_pos = 0
        current_winding_x_pos = 0

        if not is_simple_wire:
            while windingNum > wireNum:
                while num_of_winding_y > current_winding_y_pos and windingNum > wireNum:

                    self.create_conductor_block('Primary' + str(wireNum), 0 + (wireNum * voltage_per_winding))

                    x = x_right - margin * 2 - ((4 * margin + layer_thickness) * current_winding_x_pos)\
                        - (dia_insulation * current_winding_x_pos) - (dia_insulation / 2)
                    y = y_down + margin * 2 + (margin * current_winding_y_pos)\
                        + (dia_insulation * current_winding_y_pos) + (dia_insulation / 2)

                    if dia_insulation != dia:
                        draw_circle(x, y, dia_insulation, self.Nodes, self.ArcSegments, [0])
                        self.BlocksLabels.append([x + (insulation_thickness / 2) + (dia / 2), y,
                                                  block_number_insulation, -1, 1, 0, 0, 1, 1])

                    draw_circle(x, y, dia, self.Nodes, self.ArcSegments, [wireNum + 1])
                    self.BlocksLabels.append([x, y, block_number, -1, 1, 0, 0, 1, 1])

                    current_winding_y_pos += 1
                    wireNum += 1

                if layer_thickness > margin:
                    insulation_layer = []
                    insulation_layer.append([x - (dia_insulation / 2) - margin, y_down + margin])
                    insulation_layer.append([x - (dia_insulation / 2) - margin, y_up - margin])
                    insulation_layer.append([x - (dia_insulation / 2) - margin - layer_thickness,
                                            y_up - margin])
                    insulation_layer.append([x - (dia_insulation / 2) - margin - layer_thickness,
                                        y_down + margin])
                    draw_polygon(insulation_layer, self.Nodes, self.Segments, [0])
                    self.BlocksLabels.append([x - (dia_insulation / 2) - margin - (layer_thickness / 2),
                                            (y_up + y_down) / 2, block_number_layer_insulation,
                                            -1, 1, 0, 0, 1, 1])

                current_winding_x_pos += 1
                current_winding_y_pos = 0
        else:
            first_x = x_right - margin * 2
            first_y = y_down + margin * 2
            self.create_conductor_block('Primary' + str(0),
                                        0 + (current_winding_x_pos * voltage_per_winding * num_of_winding_y))
            while windingNum > wireNum:
                while num_of_winding_y > current_winding_y_pos and windingNum > wireNum:
                    current_winding_y_pos += 1
                    wireNum += 1

                x = first_x - ((4 * margin + layer_thickness) * current_winding_x_pos) \
                    - (dia_insulation * current_winding_x_pos)
                y = y_down + margin * 2 + (margin * current_winding_y_pos) \
                    + (dia_insulation * current_winding_y_pos)

                winding_polygon = []
                winding_polygon.append([x, first_y])
                winding_polygon.append([x, y])
                winding_polygon.append([x - dia_insulation, y])
                winding_polygon.append([x - dia_insulation, first_y])
                draw_polygon(winding_polygon, self.Nodes, self.Segments, [current_winding_x_pos + 1])
                self.BlocksLabels.append([x - (dia_insulation / 2), (y + y_down) / 2, block_number, -1, 1, 0, 0, 1, 1])

                if layer_thickness > margin:
                    insulation_layer = []
                    x = x_right - margin * 2 - ((4 * margin + layer_thickness + dia_insulation) * current_winding_x_pos)
                    insulation_layer.append([x - dia_insulation - (margin * 2), y_down + margin])
                    insulation_layer.append([x - dia_insulation - (margin * 2), y_up - margin])
                    insulation_layer.append([x - dia_insulation - (margin * 2) - layer_thickness,
                                            y_up - margin])
                    insulation_layer.append([x - dia_insulation - (margin * 2) - layer_thickness,
                                            y_down + margin])
                    draw_polygon(insulation_layer, self.Nodes, self.Segments, [0])
                    self.BlocksLabels.append([x - dia_insulation - margin - (layer_thickness / 2),
                                            (y_up - y_down) / 2, block_number_layer_insulation,
                                            -1, 1, 0, 0, 1, 1])

                current_winding_x_pos += 1
                self.create_conductor_block('Primary' + str(wireNum),
                                            0 + (current_winding_x_pos * voltage_per_winding * num_of_winding_y))
                current_winding_y_pos = 0

        #       Add air
        x = x_right - margin
        y = y_down + margin
        block_number = self.search_block_number('Air')
        block_label_core = [x, y, block_number, -1, 0, 0]
        self.BlocksLabels.append(block_label_core)

        x = x_right + ((center - x_right) * 2) + margin
        y = y_down + margin
        block_label_core = [x, y, block_number, -1, 0, 0]
        self.BlocksLabels.append(block_label_core)

    def create_electrostatic_model(self, input_data, output_data, file_name, is_simple_wire):
        if input_data.PrimaryWireCrossSectionSelected > 0:
            primary_cross_section = input_data.PrimaryWireCrossSectionSelected
        else:
            primary_cross_section = output_data.PrimaryWireCrossSection
        if input_data.SecondaryWireCrossSectionSelected > 0:
            secondary_cross_section = input_data.SecondaryWireCrossSectionSelected
        else:
            secondary_cross_section = output_data.SecondaryWireCrossSection
        primary_dia = math.sqrt(primary_cross_section / math.pi) * 2
        secondary_dia = math.sqrt(secondary_cross_section / math.pi) * 2

        self.create_material_block(input_data.CoreMaterialName,
                                   input_data.CorePermittivity)
        self.create_material_block(input_data.BetweenWireLayerInsulationMaterial,
                                   input_data.BetweenWireLayerInsulationMaterialPermittivity)
        self.create_material_block(input_data.BobbinMaterial,
                                   input_data.BobbinMaterialPermittivity)
        self.create_material_block('Primary_wire_insulation',
                                   input_data.PrimaryWireInsulationMaterialPermittivity)
        self.create_material_block('Secondary_wire_insulation',
                                   input_data.SecondaryWireInsulationMaterialPermittivity)
        self.create_material_block('Air', 1)

        self.create_material_block(input_data.PrimaryWindingMaterial + '_primary', 1)

        self.create_material_block(input_data.SecondaryWindingMaterial + '_secondary', 1)

        if input_data.CoreShape == 'EE':
            self.create_node_coordinate_and_core_air_label(input_data)

            self.create_wire_primary(input_data,
                                     output_data,
                                     float(input_data.BobbinXmargine),
                                     float(input_data.BobbinY1margine),
                                     float(input_data.BobbinY2margine),
                                     input_data.InputVoltage,
                                     primary_dia,
                                     is_simple_wire)
            self.save_FEMM_file(file_name)
