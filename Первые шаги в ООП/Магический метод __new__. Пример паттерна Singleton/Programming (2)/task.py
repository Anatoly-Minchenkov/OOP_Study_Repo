TYPE_OS = 1 # 1 - Windows; 2 - Linux

class DialogWindows:
    name_class = "DialogWindows"


class DialogLinux:
    name_class = "DialogLinux"
    
class Dialog:
    
    def __new__(cls, *args, **kwargs):
        if TYPE_OS == 1:
            a = DialogWindows()
            a.name = args[0]
            return a
            
        else:
            a = DialogLinux()
            a.name = args[0]
            return a