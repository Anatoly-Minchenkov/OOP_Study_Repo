class RenderList:
    def __init__(self, type_list):
        self.type_list = type_list if type_list in ('ul', 'ol') else 'ul'

    def __call__(self, ls, *args, **kwargs):
        a = f'<{self.type_list}>\n'
        for i in ls:
            a+= f'<li>{i}</li>\n'
        a += f'</{self.type_list}>'
        return a

# lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
# render = RenderList("odadl")
# html = render(lst)
# print(html)