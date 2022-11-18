class SmartPhone:
    def __init__(self, model):
        self.model = model
        self.apps = []

    def add_app(self, app):
        if type(app) not in [type(x) for x in self.apps]:
            self.apps.append(app)

    def remove_app(self, app):
        self.apps.remove(app)


class AppVK:
    def __init__(self, name='ВКонтакте'):
        self.name = name


class AppYouTube:

    def __init__(self, memory_max=1024, name='YouTube'):
        self.name = name
        self.memory_max = memory_max


class AppPhone:

    def __init__(self, phone_list, name = 'Phone'):
        self.name = name
        self.phone_list = phone_list



# a = SmartPhone('nokia')
# a.add_app(AppVK('wd'))
# a.add_app(AppYouTube())
# a.add_app(AppPhone({1:'1', 2:'2'}))
# print(a.apps)
# for i in a.apps:
#     print(type(i))
#
# sm = SmartPhone("Honor 1.0")
# sm.add_app(AppVK())
# sm.add_app(AppVK())  # второй раз добавляться не должно
# sm.add_app(AppYouTube(2048))
# for a in sm.apps:
#     print(a.name)