
def draw_circle(x, y, dia, dst_node_list, dst_arc_list, material_param=[]):
    if not type(material_param) == list:
        material_param = [material_param]
    node_number = len(dst_node_list)
    dst_node_list.append([x + (dia / 2), y, 0, 0] + material_param)
    dst_node_list.append([x, y + (dia / 2), 0, 0] + material_param)
    dst_node_list.append([x - (dia / 2), y, 0, 0] + material_param)
    dst_node_list.append([x, y - (dia / 2), 0, 0] + material_param)
    dst_arc_list.append([node_number, node_number + 1, 90, 1, 0, 0, 0] + material_param + [1])
    dst_arc_list.append([node_number + 1, node_number + 2, 90, 1, 0, 0, 0] + material_param + [1])
    dst_arc_list.append([node_number + 2, node_number + 3, 90, 1, 0, 0, 0] + material_param + [1])
    dst_arc_list.append([node_number + 3, node_number, 90, 1, 0, 0, 0] + material_param + [1])


def draw_polygon(coordinates, dst_node_list, dst_segment_list, material_param=[]):
    if not type(material_param) == list:
        material_param = [material_param]
    node_number = len(dst_node_list)
    coordinates_len = len(coordinates)
    for x, y in coordinates:
        dst_node_list.append([x, y, 0, 0] + material_param)
    index = 0
    while index < coordinates_len - 1:
        dst_segment_list.append([node_number + index, node_number + index + 1, -1, 0, 0, 0] + material_param)
        index += 1
    dst_segment_list.append([node_number + index, node_number, -1, 0, 0, 0] + material_param)

