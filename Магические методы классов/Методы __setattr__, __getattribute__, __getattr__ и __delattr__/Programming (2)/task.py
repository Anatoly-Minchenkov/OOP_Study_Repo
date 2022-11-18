class LessonItem:
    typeses = {'title': (str,), 'practices': (int, float), 'duration': (int, float)}

    def __init__(self, title, practices, duration):

        self.title = title
        self.practices = practices
        self.duration = duration

    def __setattr__(self, key, value):
        if key not in self.typeses or type(value) not in self.typeses[key]:
            raise TypeError("Неверный тип присваиваемых данных.")
        if (key == 'practices' or key == 'duration') and value <= 0:
            raise TypeError("Неверный тип присваиваемых данных.")
        object.__setattr__(self, key, value)

    def __getattr__(self, item):
        return False

    def __delattr__(self, item):
        if item in self.typeses:
            return None
        else:
            object.__delattr__(self, item)

class Module:
    def __init__(self, name):
        self.name = name
        self.lessons = []

    def add_lesson(self, lesson):
        self.lessons.append(lesson)

    def remove_lesson(self, indx):
        del self.lessons[indx]

class Course:
    def __init__(self, name):
        self.name = name
        self.modules = []

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if type(name) == str:
            self._name = name

    def add_module(self, module):
        self.modules.append(module)

    def remove_module(self, indx):
        del self.modules[indx]




# lesson = LessonItem('tolik_lesson1', 22, 12)
# print(lesson.title, lesson.practices, lesson.duration)
# module = Module('tolik_module1')
# module.add_lesson(lesson)
# print(module.lessons)
# cours = Course('tolik_course')
# cours.add_module(module)
# print(cours.modules[0].name)
# print(cours.name)
