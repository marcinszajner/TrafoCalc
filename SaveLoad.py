import json
from PyQt6.QtWidgets import QFileDialog


class SaveLoad:
    def __init__(self):
        super().__init__()
        self.jsonFile = 0

    def create_json(self, TransformerValue):
        a = vars(TransformerValue)
        self.jsonFile = json.dumps(a, indent=4)

    def save_json(self, main_window_obj):
        name, _ = QFileDialog.getSaveFileName(main_window_obj, 'Save file', '', 'Json Files(*.json);;all Files(*)')
        if name:
            if not name.find('.*'):
                name = name + '.json'
            file = open(name, 'w')
            file.write(self.jsonFile)
            file.close()

    def load_json(self, main_window_obj, transformer_type):
        name, _ = QFileDialog.getOpenFileName(main_window_obj, 'Load file', '', 'Json Files(*.json);;all Files(*)')
        if name:
            json_file = open(name)
            data = json.load(json_file)
            a = vars(transformer_type)
            name = 'Value'
            for key, value in a.items():
                loaded_data = data[key]
                main_menu_transformer_values = getattr(main_window_obj, key + name)
                if getattr(main_menu_transformer_values, 'setText', None):
                    main_menu_transformer_values.setText(str(loaded_data))
                elif getattr(main_menu_transformer_values, 'setCurrentText', None):
                    main_menu_transformer_values.setCurrentText(str(loaded_data))
