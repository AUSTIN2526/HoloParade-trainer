import sys
import threading
from PyQt5.QtWidgets import QApplication, QMessageBox, QWidget
from UI import Ui_Form
from pymem import Pymem
from pymem.process import module_from_name
import base64
import os
import json
from config import load_data

class AppWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        
        func_name = self.ui.ui_text['group_names']
        title_name = self.ui.ui_text['group_titles']
        self.groups = self.ui.groups
        
        # Load modify data
        modify_data = load_data()
        self.modify_data = {
            title_name[i]: {
                func_name[i][j]: [self.groups[i][j]] + [modify_data[i][j]]
                for j in range(len(func_name[i]))
            }
            for i in range(len(func_name))
        }

        # System language
        info = {
            'zh_TW': {
                'scan': ['掃描', '已掃描到遊戲'],
                'error': ['錯誤', '請先開啟遊戲後再按偵測程式'],
                
            },
            'en': {
                'scan': ['Scan', 'Game scanned'],
                'error': ['Error', 'Please open the game before pressing the detect button'],                
            },
        }
        self.info = info[self.ui.language]

        # Find HoloCure windows
        self.ui.page_button.clicked.connect(self.find_windows) 

        # Connect QCheckBox with modify function
        for idx in range(len(self.ui.groups)):        
            for fucn_ID in range(len(self.ui.groups[idx])):
                title = title_name[idx]
                name = func_name[idx][fucn_ID]
                checkbox = self.ui.groups[idx][fucn_ID]
                checkbox.clicked.connect(lambda state, x=(title, name): self.modify_thread(x))
               

        
        self.move(40, 40)
        self.show()
        
    

    def find_windows(self):
        try:
            self.windows = Pymem("HoloParade.exe")
            for functions in self.ui.groups:
                for function in functions:
                    function.setEnabled(True)
            
            QMessageBox.information(None, self.info['scan'][0], self.info['scan'][1])
            
        except:
            QMessageBox.critical(None, self.info['error'][0], self.info['error'][1])
            
        

    def modify_thread(self, parameter):
        t = threading.Thread(target=self.dynamic_modify, args=(parameter,))
        t.setDaemon(True)
        t.start()

    def dynamic_modify(self, parameter):
        # Unpack parameters
        title, name = parameter

        # Extract data from the modification dictionary
        checkbox, modify_data = self.modify_data[title][name]
        value, dll_address, offsets, dll_name = modify_data.values()

        # Get the base address of the game module
        game_module = module_from_name(self.windows.process_handle, dll_name).lpBaseOfDll
        base_address = game_module + dll_address

        # Modify memory while the checkbox is checked
        while checkbox.isChecked():
            try:
                # Calculate the memory address based on the base address and offsets
                addr = self.calculate_address(base_address, offsets)

                # Check if the value is a float
                if isinstance(value, float):
                    current_value = self.windows.read_float(addr)
                    if current_value > 1:
                        self.windows.write_float(addr, value)
                else:
                    self.windows.write_int(addr, value)

            except:
                pass
    
      
    def calculate_address(self, address, offsets):
        addr = self.windows.read_longlong(address)
        for cnt,offset in enumerate(offsets):
            if cnt+1 != len(offsets):
                addr = self.windows.read_longlong(addr + offset)           
        return addr + offsets[-1]
        
   


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(True)
    w = AppWindow()
    w.show()
    sys.exit(app.exec_())
