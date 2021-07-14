def find_where(items, search_request):
    # Значение object() в качестве умолчательного используется для того,
    # чтобы не получилось получить от get значение None и случайно
    # успешно сравнить с value == None.
    # Каждое значение object() всегда равно только самому себе.
    default = object()
    for item in items:
        for key, value in search_request.items():
            # Здесь можно было бы использовать
            # что-то вроде "key in book and book[key] !=..." и обойтись
            # без всяких object(). Но хочется обращаться по ключу
            # ровно один раз!
            if item.get(key, default) != value:
                break
        else:
            return item
