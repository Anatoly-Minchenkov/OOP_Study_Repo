


class AppStore:
    
    magazine = []
    
    def add_application(self, app):
        self.magazine.append(app)
    
    def remove_application(self, app):
        self.magazine.remove(app)
    
    def block_application(self, app):
        app.blocked = True
    
    def total_apps(self):
        return len(self.magazine)

class Application:
    
    def __init__(self, name, blocked = False):
        self.name = name
        self.blocked = blocked


