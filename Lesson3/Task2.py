# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.

import string

test_string = """Различные средства искусственного интеллекта также широко используются в области обеспечения
безопасности, распознавании речи и текста, интеллектуального анализа данных и фильтрации спама в электронной почте.
Также разрабатываются приложения для распознавания жестов (понимание языка жестов машинами),
индивидуальное распознавание голоса, глобальное распознавание голоса (от множества людей в шумной комнате),
распознавание лица для интерпретации эмоций и невербальных сигналов. Другие приложения — это роботизированная
навигация, преодоление препятствий и распознавание объектов. Объединение искусственного интеллекта с
экспериментальными данными ускорило создание новой разновидности металлического стекла в 200 раз.
Стеклянная природа нового материала делает его более прочным, легким и коррозионно-стойким, чем современная сталь.
Группа, возглавляемая учёными Национальной ускорительной лаборатории SLAC Министерства энергетики,
Национального института стандартов и технологий и Северо-западного университета США, сообщила о сокращении затрат
для обнаружения и улучшения металлического стекла на долю времени и стоимости. Как сообщил представитель группы
разработчиков Апурва Мехта[80], «Мы смогли сделать и отобрать 20 000 вариантов за один год»[81]. В феврале 2021 года
в США провели испытания искусственного интеллекта в воздушном бою «двое против одного».
Новый этап испытаний, который получил название Scrimmage 1, проводился в лаборатории прикладной физики Университета
Джонса Хопкинса. В этом воздушном бою два истребителя F-16 Fighting Falcon под управлением искусственного интеллекта
действовали в группе и вели бой против одного такого же самолёта. Во время нового этапа испытаний нейросетевые
алгоритмы вели не только ближний маневренный воздушный бой, но и действовали на расстоянии от противника,
выявляя его с помощью радаров и поражая ракетами на расстоянии[82]."""

# Избавляемся от знаков препинания и регистра
test_string = test_string.translate(str.maketrans('', '', string.punctuation)).lower()

words = test_string.split(" ")
words_list = set(words)
words_dic = {}
for element in words_list:
    words_dic.setdefault(element, words.count(element))

sorted_tuple = sorted(words_dic.items(), key=lambda x: x[1], reverse=True)
print(*sorted_tuple[:10], sep = "\n")