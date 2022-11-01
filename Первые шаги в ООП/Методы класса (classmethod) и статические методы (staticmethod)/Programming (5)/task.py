class Message:
    
    def __init__(self, text, fl_like = False):
        self.text = text
        self.fl_like = fl_like
        
        
    
class Viber:
    
    MSG_LIST = []
    
    @classmethod
    def add_message(cls, msg):
        cls.MSG_LIST.append(msg)
    
    @classmethod
    def remove_message(cls, msg):
        cls.MSG_LIST.remove(msg)
    
    def set_like(msg):
        msg.fl_like = False if msg.fl_like else True
        
    @classmethod
    def show_last_message(cls, cnt):
        for i in range(cnt, 0, -1):
            print(cls.MSG_LIST[-i].text)
    
    @classmethod
    def total_messages(cls):
        return len(cls.MSG_LIST)




