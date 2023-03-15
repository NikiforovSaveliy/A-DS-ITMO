import wikipedia
wikipedia.set_lang('ru')
print(wikipedia.page('Научный метод').content)