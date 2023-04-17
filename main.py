import os
import docx
from kivy.properties import NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.utils import get_color_from_hex
from kivy.app import App
from kivy.uix.widget import WidgetException
from kivy.core.text import LabelBase, DEFAULT_FONT


class MyBoxLayout(BoxLayout):
    @staticmethod
    def on_button_press(text_input):
        print(text_input.text)


class MyScrollView(ScrollView):
    scroll_pos = NumericProperty(0)

    @staticmethod
    def on_scroll_pos(self, instance, value):
        print("scroll position: ", value)


class ScrollableGridLayout(GridLayout):
    """ Initialize a scrollable GridLayout """
    def __init__(self, **kwargs):
        super(ScrollableGridLayout, self).__init__(**kwargs)
        self.cols = 1
        self.rows = None
        self.size_hint_y = None
        self.spacing = 10
        self.bind(minimum_height=self.setter('height'))


class MyTabbedPanel(TabbedPanel):
    """
    Class for creating table panel and buttons on each tab
    """

    def __init__(self, **kwargs):
        super(MyTabbedPanel, self).__init__(**kwargs)
        but_test = Button(text='test', size_hint=(None, None), size=(400, 40))
        self.add_widget(but_test)
        self.text = ''

        # Creating table panel
        tab7 = TabbedPanelItem(text='7 класс')
        tab8 = TabbedPanelItem(text='8 класс')
        tab9 = TabbedPanelItem(text='9 класс')
        tab10 = TabbedPanelItem(text='10 класс')
        tab11 = TabbedPanelItem(text='11 класс')
        creators_info = TabbedPanelItem(text='info')

        # Set the background color of the tab item to blue
        tab7.background_color = get_color_from_hex("#0077ff")
        tab8.background_color = get_color_from_hex("#0077ff")
        tab9.background_color = get_color_from_hex("#0077ff")
        tab10.background_color = get_color_from_hex("#0077ff")
        tab11.background_color = get_color_from_hex("#0077ff")
        creators_info.background_color = get_color_from_hex("#0077ff")

        # Create a grid layout with space between buttons for each tab item
        self.tab7_layout = ScrollableGridLayout()
        self.tab8_layout = ScrollableGridLayout()
        self.tab9_layout = ScrollableGridLayout()
        self.tab10_layout = ScrollableGridLayout()
        self.tab11_layout = ScrollableGridLayout()

        # Create input box for all tabs
        self.input_box_tab7 = TextInput(multiline=False, text=self.text, hint_text='Поиск', size_hint=(None, None),
                                        size=(400, 35))
        self.input_box_tab7.bind(text=self.update_search_results)
        self.tab7_layout.add_widget(self.input_box_tab7)
        self.input_box_tab8 = TextInput(multiline=False, text=self.text, hint_text='Поиск', size_hint=(None, None),
                                        size=(400, 35))
        self.input_box_tab8.bind(text=self.update_search_results)
        self.tab8_layout.add_widget(self.input_box_tab8)
        self.input_box_tab9 = TextInput(multiline=False, text=self.text, hint_text='Поиск', size_hint=(None, None),
                                        size=(400, 35))
        self.input_box_tab9.bind(text=self.update_search_results)
        self.tab9_layout.add_widget(self.input_box_tab9)
        self.input_box_tab10 = TextInput(multiline=False, text=self.text, hint_text='Поиск', size_hint=(None, None),
                                         size=(400, 35))
        self.input_box_tab10.bind(text=self.update_search_results)
        self.tab10_layout.add_widget(self.input_box_tab10)
        self.input_box_tab11 = TextInput(multiline=False, text=self.text, hint_text='Поиск', size_hint=(None, None),
                                         size=(400, 35))
        self.input_box_tab11.bind(text=self.update_search_results)
        self.tab11_layout.add_widget(self.input_box_tab11)

        """ ----------------------------------------------------------- """
        """ HERE YOU INSERT ALL BUTTONS FOR EACH TAB ON SCREEN """

        # Add buttons to layout for each tab
        # tab7
        tab7_button1 = Button(text='Что изучает физика', size_hint=(None, None), size=(400, 40))
        self.tab7_layout.add_widget(tab7_button1)
        tab7_button1.bind(on_press=self.on_button_click)  # action on click
        tab7_button2 = Button(text='Некоторые физические термины', size_hint=(None, None), size=(400, 40))
        self.tab7_layout.add_widget(tab7_button2)
        tab7_button2.bind(on_press=self.on_button_click)
        tab7_button4 = Button(text='Физические величины и их измерение', size_hint=(None, None), size=(400, 40))
        tab7_button4.text_size = tab7_button4.size
        tab7_button4.halign = 'center'  # Place button text in center for a long texts
        tab7_button4.valign = 'middle'
        self.tab7_layout.add_widget(tab7_button4)
        tab7_button4.bind(on_press=self.on_button_click)  # action on click
        tab7_button5 = Button(text='Точность и погрешность', size_hint=(None, None), size=(400, 40))
        tab7_button5.text_size = tab7_button5.size
        tab7_button5.halign = 'center'
        tab7_button5.valign = 'middle'
        self.tab7_layout.add_widget(tab7_button5)
        tab7_button5.bind(on_press=self.on_button_click)
        tab7_button6 = Button(text='Связь физики и техники', size_hint=(None, None), size=(400, 40))
        self.tab7_layout.add_widget(tab7_button6)
        tab7_button6.bind(on_press=self.on_button_click)
        tab7_button7 = Button(text='Строение вещества', size_hint=(None, None), size=(400, 40))
        self.tab7_layout.add_widget(tab7_button7)
        tab7_button7.bind(on_press=self.on_button_click)
        tab7_button8 = Button(text='Молекулы', size_hint=(None, None), size=(400, 40))
        self.tab7_layout.add_widget(tab7_button8)
        tab7_button8.bind(on_press=self.on_button_click)
        tab7_button9 = Button(text='Диффузия', size_hint=(None, None), size=(400, 40))
        self.tab7_layout.add_widget(tab7_button9)
        tab7_button9.bind(on_press=self.on_button_click)
        tab7_button10 = Button(text='Взаимное движение молекул', size_hint=(None, None),size=(400, 40))
        tab7_button10.text_size = tab7_button10.size
        tab7_button10.halign = 'center'
        tab7_button10.valign = 'middle'
        self.tab7_layout.add_widget(tab7_button10)
        tab7_button10.bind(on_press=self.on_button_click)
        tab7_button11 = Button(text='Агрегатные состояния вещества', size_hint=(None, None), size=(400, 40))
        self.tab7_layout.add_widget(tab7_button11)
        tab7_button11.bind(on_press=self.on_button_click)
        tab7_button12 = Button(text='Различие в молекулярном строении твердых тел, жидкостей и газов',
                               size_hint=(None, None), size=(400, 40))
        tab7_button12.text_size = tab7_button12.size
        tab7_button12.halign = 'center'
        tab7_button12.valign = 'middle'
        self.tab7_layout.add_widget(tab7_button12)
        tab7_button12.bind(on_press=self.on_button_click)
        tab7_button13 = Button(text='Механическое движение', size_hint=(None, None), size=(400, 40))
        self.tab7_layout.add_widget(tab7_button13)
        tab7_button13.bind(on_press=self.on_button_click)
        tab7_button14 = Button(text='Равномерное и неравномерное движение', size_hint=(None, None), size=(400, 40))
        tab7_button14.text_size = tab7_button14.size
        tab7_button14.halign = 'center'
        tab7_button14.valign = 'middle'
        self.tab7_layout.add_widget(tab7_button14)
        tab7_button14.bind(on_press=self.on_button_click)
        tab7_button15 = Button(text='Скорость. Единицы скорости', size_hint=(None, None), size=(400, 40))
        self.tab7_layout.add_widget(tab7_button15)
        tab7_button15.bind(on_press=self.on_button_click)
        tab7_button16 = Button(text='Расчёт пути и времени движения', size_hint=(None, None), size=(400, 40))
        self.tab7_layout.add_widget(tab7_button16)
        tab7_button16.bind(on_press=self.on_button_click)
        tab7_button17 = Button(text='Инерция', size_hint=(None, None), size=(400, 40))
        self.tab7_layout.add_widget(tab7_button17)
        tab7_button17.bind(on_press=self.on_button_click)
        tab7_button18 = Button(text='Взаимодействие тел', size_hint=(None, None), size=(400, 40))
        self.tab7_layout.add_widget(tab7_button18)
        tab7_button18.bind(on_press=self.on_button_click)
        tab7_button19 = Button(text='Масса тела. Единицы массы', size_hint=(None, None), size=(400, 40))
        self.tab7_layout.add_widget(tab7_button19)
        tab7_button19.bind(on_press=self.on_button_click)
        tab7_button20 = Button(text='Изменение массы тела на весах', size_hint=(None, None), size=(400, 40))
        self.tab7_layout.add_widget(tab7_button20)
        tab7_button20.bind(on_press=self.on_button_click)
        tab7_button21 = Button(text='Плотность вещества', size_hint=(None, None), size=(400, 40))
        self.tab7_layout.add_widget(tab7_button21)
        tab7_button21.bind(on_press=self.on_button_click)
        tab7_button22 = Button(text='Расчёт массы тела по его плотности', size_hint=(None, None), size=(400, 40))
        self.tab7_layout.add_widget(tab7_button22)
        tab7_button22.bind(on_press=self.on_button_click)
        tab7_button23 = Button(text='Сила', size_hint=(None, None), size=(400, 40))
        self.tab7_layout.add_widget(tab7_button23)
        tab7_button23.bind(on_press=self.on_button_click)
        tab7_button24 = Button(text='Явление тяготения. Сила тяжести', size_hint=(None, None), size=(400, 40))
        self.tab7_layout.add_widget(tab7_button24)
        tab7_button24.bind(on_press=self.on_button_click)
        tab7_button25 = Button(text='Сила упругости. Закон Гука', size_hint=(None, None), size=(400, 40))
        self.tab7_layout.add_widget(tab7_button25)
        tab7_button25.bind(on_press=self.on_button_click)
        tab7_button26 = Button(text='Вес тела', size_hint=(None, None), size=(400, 40))
        self.tab7_layout.add_widget(tab7_button26)
        tab7_button26.bind(on_press=self.on_button_click)
        tab7_button27 = Button(text='Единицы силы. Связь между силой тяжести и массой тела', size_hint=(None, None),
                               size=(400, 40))
        tab7_button27.text_size = tab7_button27.size
        tab7_button27.halign = 'center'
        tab7_button27.valign = 'middle'
        self.tab7_layout.add_widget(tab7_button27)
        tab7_button27.bind(on_press=self.on_button_click)
        tab7_button30 = Button(text='Сила трения', size_hint=(None, None), size=(400, 40))
        self.tab7_layout.add_widget(tab7_button30)
        tab7_button30.bind(on_press=self.on_button_click)
        tab7_button29 = Button(text='Сложение двух сил, направленных по одной прямой. Равнодействующая сил',
                               size_hint=(None, None), size=(400, 40))
        tab7_button29.text_size = tab7_button29.size
        tab7_button29.halign = 'center'
        tab7_button29.valign = 'middle'
        self.tab7_layout.add_widget(tab7_button29)
        tab7_button29.bind(on_press=self.on_button_click)
        tab7_button31 = Button(text='Трение покоя', size_hint=(None, None), size=(400, 40))
        self.tab7_layout.add_widget(tab7_button31)
        tab7_button31.bind(on_press=self.on_button_click)
        tab7_button32 = Button(text='Трение в природе и технике', size_hint=(None, None), size=(400, 40))
        self.tab7_layout.add_widget(tab7_button32)
        tab7_button32.bind(on_press=self.on_button_click)
        tab7_button33 = Button(text='Давление. Единицы давления', size_hint=(None, None), size=(400, 40))
        self.tab7_layout.add_widget(tab7_button33)
        tab7_button33.bind(on_press=self.on_button_click)
        tab7_button34 = Button(text='Способы уменьшения и увеличения давления', size_hint=(None, None), size=(400, 40))
        tab7_button34.text_size = tab7_button34.size
        tab7_button34.halign = 'center'
        tab7_button34.valign = 'middle'
        self.tab7_layout.add_widget(tab7_button34)
        tab7_button34.bind(on_press=self.on_button_click)
        tab7_button35 = Button(text='Давление газа', size_hint=(None, None), size=(400, 40))
        self.tab7_layout.add_widget(tab7_button35)
        tab7_button35.bind(on_press=self.on_button_click)
        tab7_button36 = Button(text='Передача давления жидкостями и газами. Закон Паскаля', size_hint=(None, None),
                               size=(400, 40))
        tab7_button36.text_size = tab7_button36.size
        tab7_button36.halign = 'center'
        tab7_button36.valign = 'middle'
        self.tab7_layout.add_widget(tab7_button36)
        tab7_button36.bind(on_press=self.on_button_click)
        tab7_button37 = Button(text='Давление в жидкости и газе', size_hint=(None, None), size=(400, 40))
        self.tab7_layout.add_widget(tab7_button37)
        tab7_button37.bind(on_press=self.on_button_click)
        tab7_button38 = Button(text='Расчёт давления жидкости на дно и стенки сосуда', size_hint=(None, None),
                               size=(400, 40))
        tab7_button38.text_size = tab7_button38.size
        tab7_button38.halign = 'center'
        tab7_button38.valign = 'middle'
        self.tab7_layout.add_widget(tab7_button38)
        tab7_button38.bind(on_press=self.on_button_click)
        tab7_button39 = Button(text='Сообщающиеся сосуды', size_hint=(None, None), size=(400, 40))
        self.tab7_layout.add_widget(tab7_button39)
        tab7_button39.bind(on_press=self.on_button_click)
        tab7_button40 = Button(text='Вес воздуха. Атмосферное давление', size_hint=(None, None), size=(400, 40))
        self.tab7_layout.add_widget(tab7_button40)
        tab7_button40.bind(on_press=self.on_button_click)
        tab7_button42 = Button(text='Измерение атмосферного давления. Опыт Торричелли', size_hint=(None, None),
                               size=(400, 40))
        tab7_button42.text_size = tab7_button42.size
        tab7_button42.halign = 'center'
        tab7_button42.valign = 'middle'
        self.tab7_layout.add_widget(tab7_button42)
        tab7_button42.bind(on_press=self.on_button_click)
        tab7_button43 = Button(text='Барометр-анероид', size_hint=(None, None), size=(400, 40))
        self.tab7_layout.add_widget(tab7_button43)
        tab7_button43.bind(on_press=self.on_button_click)
        tab7_button45 = Button(text='Манометры', size_hint=(None, None), size=(400, 40))
        self.tab7_layout.add_widget(tab7_button45)
        tab7_button45.bind(on_press=self.on_button_click)
        tab7_button46 = Button(text='Поршневой жидкостный насос', size_hint=(None, None), size=(400, 40))
        self.tab7_layout.add_widget(tab7_button46)
        tab7_button46.bind(on_press=self.on_button_click)
        tab7_button47 = Button(text='Гидравлический пресс', size_hint=(None, None), size=(400, 40))
        self.tab7_layout.add_widget(tab7_button47)
        tab7_button47.bind(on_press=self.on_button_click)
        tab7_button48 = Button(text='Действие жидкости и газа на погруженное в них тело', size_hint=(None, None),
                               size=(400, 40))
        tab7_button48.text_size = tab7_button48.size
        tab7_button48.halign = 'center'
        tab7_button48.valign = 'middle'
        self.tab7_layout.add_widget(tab7_button48)
        tab7_button48.bind(on_press=self.on_button_click)
        tab7_button49 = Button(text='Архимедова сила', size_hint=(None, None), size=(400, 40))
        self.tab7_layout.add_widget(tab7_button49)
        tab7_button49.bind(on_press=self.on_button_click)
        tab7_button50 = Button(text='Плавание тел', size_hint=(None, None), size=(400, 40))
        self.tab7_layout.add_widget(tab7_button50)
        tab7_button50.bind(on_press=self.on_button_click)
        tab7_button53 = Button(text='Механическая работа. Единицы работы', size_hint=(None, None), size=(400, 40))
        tab7_button53.text_size = tab7_button53.size
        tab7_button53.halign = 'center'
        tab7_button53.valign = 'middle'
        self.tab7_layout.add_widget(tab7_button53)
        tab7_button53.bind(on_press=self.on_button_click)
        tab7_button54 = Button(text='Мощность. Единицы мощности', size_hint=(None, None), size=(400, 40))
        self.tab7_layout.add_widget(tab7_button54)
        tab7_button54.bind(on_press=self.on_button_click)
        tab7_button55 = Button(text='Простые механизмы', size_hint=(None, None), size=(400, 40))
        self.tab7_layout.add_widget(tab7_button55)
        tab7_button55.bind(on_press=self.on_button_click)
        tab7_button56 = Button(text='Рычаг. Равновесие сил на рычаге', size_hint=(None, None), size=(400, 40))
        self.tab7_layout.add_widget(tab7_button56)
        tab7_button56.bind(on_press=self.on_button_click)
        tab7_button57 = Button(text='Момент силы', size_hint=(None, None), size=(400, 40))
        self.tab7_layout.add_widget(tab7_button57)
        tab7_button57.bind(on_press=self.on_button_click)
        tab7_button59 = Button(text='Применения закона равновесия рычага к блоку', size_hint=(None, None),
                               size=(400, 40))
        tab7_button59.text_size = tab7_button59.size
        tab7_button59.halign = 'center'
        tab7_button59.valign = 'middle'
        self.tab7_layout.add_widget(tab7_button59)
        tab7_button59.bind(on_press=self.on_button_click)
        tab7_button60 = Button(text='Равенство работ при использовании простых механизмов. Золотое правило механики', size_hint=(None, None), size=(400, 40))
        tab7_button60.text_size = tab7_button60.size
        tab7_button60.halign = 'center'
        tab7_button60.valign = 'middle'
        self.tab7_layout.add_widget(tab7_button60)
        tab7_button60.bind(on_press=self.on_button_click)
        tab7_button61 = Button(text='Коэффициент полезного действия механизма', size_hint=(None, None),
                               size=(400, 40))
        tab7_button61.text_size = tab7_button61.size
        tab7_button61.halign = 'center'
        tab7_button61.valign = 'middle'
        self.tab7_layout.add_widget(tab7_button61)
        tab7_button61.bind(on_press=self.on_button_click)
        tab7_button62 = Button(text='Энергия', size_hint=(None, None), size=(400, 40))
        self.tab7_layout.add_widget(tab7_button62)
        tab7_button62.bind(on_press=self.on_button_click)
        tab7_button63 = Button(text='Потенциальная и кинетическая энергия', size_hint=(None, None), size=(400, 40))
        tab7_button63.text_size = tab7_button63.size
        tab7_button63.halign = 'center'
        tab7_button63.valign = 'middle'
        self.tab7_layout.add_widget(tab7_button63)
        tab7_button63.bind(on_press=self.on_button_click)
        tab7_button64 = Button(text='Превращение одного вида механической энергии в другой', size_hint=(None, None), size=(400, 40))
        tab7_button64.text_size = tab7_button64.size
        tab7_button64.halign = 'center'
        tab7_button64.valign = 'middle'
        self.tab7_layout.add_widget(tab7_button64)
        tab7_button64.bind(on_press=self.on_button_click)

        # tab8
        tab8_button1 = Button(text='Тепловое движение. Температура', size_hint=(None, None), size=(400, 40))
        self.tab8_layout.add_widget(tab8_button1)
        tab8_button1.bind(on_press=self.on_button_click)
        tab8_button2 = Button(text='Внутренняя энергия', size_hint=(None, None), size=(400, 40))
        self.tab8_layout.add_widget(tab8_button2)
        tab8_button2.bind(on_press=self.on_button_click)
        tab8_button3 = Button(text='Способы изменения внутренней энергии тела', size_hint=(None, None), size=(400, 40))
        tab8_button3.text_size = tab8_button3.size
        tab8_button3.halign = 'center'
        tab8_button3.valign = 'middle'
        self.tab8_layout.add_widget(tab8_button3)
        tab8_button3.bind(on_press=self.on_button_click)
        tab8_button4 = Button(text='Теплопроводность', size_hint=(None, None), size=(400, 40))
        self.tab8_layout.add_widget(tab8_button4)
        tab8_button4.bind(on_press=self.on_button_click)
        tab8_button5 = Button(text='Конвекция', size_hint=(None, None), size=(400, 40))
        self.tab8_layout.add_widget(tab8_button5)
        tab8_button5.bind(on_press=self.on_button_click)
        tab8_button6 = Button(text='Излучение', size_hint=(None, None), size=(400, 40))
        self.tab8_layout.add_widget(tab8_button6)
        tab8_button6.bind(on_press=self.on_button_click)
        tab8_button7 = Button(text='Количество теплоты. Единицы количества теплоты', size_hint=(None, None),
                              size=(400, 40))
        tab8_button7.text_size = tab8_button7.size
        tab8_button7.halign = 'center'
        tab8_button7.valign = 'middle'
        self.tab8_layout.add_widget(tab8_button7)
        tab8_button7.bind(on_press=self.on_button_click)
        tab8_button8 = Button(text='Удельная теплоемкость', size_hint=(None, None), size=(400, 40))
        self.tab8_layout.add_widget(tab8_button8)
        tab8_button8.bind(on_press=self.on_button_click)
        tab8_button9 = Button(text='Расчет количества теплоты, необходимого для нагревания тела или выделяемого им при охлаждении',
                              size_hint=(None, None), size=(400, 40))
        tab8_button9.text_size = tab8_button9.size
        tab8_button9.halign = 'center'
        tab8_button9.valign = 'middle'
        self.tab8_layout.add_widget(tab8_button9)
        tab8_button9.bind(on_press=self.on_button_click)
        tab8_button10 = Button(text='Энергия топлива. Удельная теплота сгорания', size_hint=(None, None),
                               size=(400, 40))
        tab8_button10.text_size = tab8_button10.size
        tab8_button10.halign = 'center'
        tab8_button10.valign = 'middle'
        self.tab8_layout.add_widget(tab8_button10)
        tab8_button10.bind(on_press=self.on_button_click)
        tab8_button11 = Button(text='Закон сохранения и превращения энергии в механических и тепловых процессах',
                               size_hint=(None, None), size=(400, 40))
        tab8_button11.text_size = tab8_button11.size
        tab8_button11.halign = 'center'
        tab8_button11.valign = 'middle'
        self.tab8_layout.add_widget(tab8_button11)
        tab8_button11.bind(on_press=self.on_button_click)
        tab8_button12 = Button(text='Агрегатные состояния вещества', size_hint=(None, None), size=(400, 40))
        self.tab8_layout.add_widget(tab8_button12)
        tab8_button12.bind(on_press=self.on_button_click)
        tab8_button13 = Button(text='Плавление и отведевание кристаллических тел', size_hint=(None, None),
                               size=(400, 40))
        tab8_button13.text_size = tab8_button13.size
        tab8_button13.halign = 'center'
        tab8_button13.valign = 'middle'
        self.tab8_layout.add_widget(tab8_button13)
        tab8_button13.bind(on_press=self.on_button_click)
        tab8_button15 = Button(text='Удельная теплота плавления', size_hint=(None, None), size=(400, 40))
        self.tab8_layout.add_widget(tab8_button15)
        tab8_button15.bind(on_press=self.on_button_click)
        tab8_button16 = Button(text='Испарение. Насыщенный и ненасыщенный пар', size_hint=(None, None), size=(400, 40))
        tab8_button16.text_size = tab8_button16.size
        tab8_button16.halign = 'center'
        tab8_button16.valign = 'middle'
        self.tab8_layout.add_widget(tab8_button16)
        tab8_button16.bind(on_press=self.on_button_click)
        tab8_button17 = Button(text='Поглощение энергии при испарении жидкости и выделение ее при конденсации пара',
                               size_hint=(None, None), size=(400, 40))
        tab8_button17.text_size = tab8_button17.size
        tab8_button17.halign = 'center'
        tab8_button17.valign = 'middle'
        self.tab8_layout.add_widget(tab8_button17)
        tab8_button17.bind(on_press=self.on_button_click)
        tab8_button18 = Button(text='Кипение', size_hint=(None, None), size=(400, 40))
        self.tab8_layout.add_widget(tab8_button18)
        tab8_button18.bind(on_press=self.on_button_click)
        tab8_button19 = Button(text='Влажность воздуха. Способы определения влажности воздуха', size_hint=(None, None), size=(400, 40))
        tab8_button19.text_size = tab8_button19.size
        tab8_button19.halign = 'center'
        tab8_button19.valign = 'middle'
        self.tab8_layout.add_widget(tab8_button19)
        tab8_button19.bind(on_press=self.on_button_click)
        tab8_button20 = Button(text='Удельная теплота парообразования и конденсации', size_hint=(None, None),
                               size=(400, 40))
        tab8_button20.text_size = tab8_button20.size
        tab8_button20.halign = 'center'
        tab8_button20.valign = 'middle'
        self.tab8_layout.add_widget(tab8_button20)
        tab8_button20.bind(on_press=self.on_button_click)
        tab8_button21 = Button(text='Работа газа и пара при расширении', size_hint=(None, None), size=(400, 40))
        self.tab8_layout.add_widget(tab8_button21)
        tab8_button21.bind(on_press=self.on_button_click)
        tab8_button22 = Button(text='Двигатель внутреннего сгорания', size_hint=(None, None), size=(400, 40))
        self.tab8_layout.add_widget(tab8_button22)
        tab8_button22.bind(on_press=self.on_button_click)
        tab8_button24 = Button(text='КПД теплового двигателя', size_hint=(None, None), size=(400, 40))
        self.tab8_layout.add_widget(tab8_button24)
        tab8_button24.bind(on_press=self.on_button_click)
        tab8_button25 = Button(text='Электризация тел при соприкосновении', size_hint=(None, None), size=(400, 40))
        tab8_button25.text_size = tab8_button25.size
        tab8_button25.halign = 'center'
        tab8_button25.valign = 'middle'
        self.tab8_layout.add_widget(tab8_button25)
        tab8_button25.bind(on_press=self.on_button_click)
        tab8_button26 = Button(text='Взаимодействие заряженных тел. Два рода зарядов', size_hint=(None, None),
                               size=(400, 40))
        tab8_button26.text_size = tab8_button26.size
        tab8_button26.halign = 'center'
        tab8_button26.valign = 'middle'
        self.tab8_layout.add_widget(tab8_button26)
        tab8_button26.bind(on_press=self.on_button_click)
        tab8_button28 = Button(text='Электрическое поле', size_hint=(None, None), size=(400, 40))
        self.tab8_layout.add_widget(tab8_button28)
        tab8_button28.bind(on_press=self.on_button_click)
        tab8_button29 = Button(text='Делимость электрического заряда. Электрон', size_hint=(None, None), size=(400, 40))
        tab8_button29.text_size = tab8_button29.size
        tab8_button29.halign = 'center'
        tab8_button29.valign = 'middle'
        self.tab8_layout.add_widget(tab8_button29)
        tab8_button29.bind(on_press=self.on_button_click)
        tab8_button30 = Button(text='Строение атомов', size_hint=(None, None), size=(400, 40))
        self.tab8_layout.add_widget(tab8_button30)
        tab8_button30.bind(on_press=self.on_button_click)
        tab8_button31 = Button(text='Объяснение электрических явлений', size_hint=(None, None), size=(400, 40))
        self.tab8_layout.add_widget(tab8_button31)
        tab8_button31.bind(on_press=self.on_button_click)
        tab8_button32 = Button(text='Электрический ток. Источники электрического тока', size_hint=(None, None),
                               size=(400, 40))
        tab8_button32.text_size = tab8_button32.size
        tab8_button32.halign = 'center'
        tab8_button32.valign = 'middle'
        self.tab8_layout.add_widget(tab8_button32)
        tab8_button32.bind(on_press=self.on_button_click)
        tab8_button33 = Button(text='Электрическая цепь и ее составные части', size_hint=(None, None), size=(400, 40))
        tab8_button33.text_size = tab8_button33.size
        tab8_button33.halign = 'center'
        tab8_button33.valign = 'middle'
        self.tab8_layout.add_widget(tab8_button33)
        tab8_button33.bind(on_press=self.on_button_click)
        tab8_button35 = Button(text='Действия электрического тока', size_hint=(None, None), size=(400, 40))
        self.tab8_layout.add_widget(tab8_button35)
        tab8_button35.bind(on_press=self.on_button_click)
        tab8_button36 = Button(text='Направление электрического тока', size_hint=(None, None), size=(400, 40))
        self.tab8_layout.add_widget(tab8_button36)
        tab8_button36.bind(on_press=self.on_button_click)
        tab8_button37 = Button(text='Единицы силы тока', size_hint=(None, None), size=(400, 40))
        self.tab8_layout.add_widget(tab8_button37)
        tab8_button37.bind(on_press=self.on_button_click)
        tab8_button38 = Button(text='Амперметр. Измерение силы тока', size_hint=(None, None), size=(400, 40))
        self.tab8_layout.add_widget(tab8_button38)
        tab8_button38.bind(on_press=self.on_button_click)
        tab8_button39 = Button(text='Электрическое напряжение', size_hint=(None, None), size=(400, 40))
        self.tab8_layout.add_widget(tab8_button39)
        tab8_button39.bind(on_press=self.on_button_click)
        tab8_button40 = Button(text='Единицы напряжения', size_hint=(None, None), size=(400, 40))
        self.tab8_layout.add_widget(tab8_button40)
        tab8_button40.bind(on_press=self.on_button_click)
        tab8_button41 = Button(text='Вольтметр. Измерение напряжения', size_hint=(None, None), size=(400, 40))
        self.tab8_layout.add_widget(tab8_button41)
        tab8_button41.bind(on_press=self.on_button_click)
        tab8_button42 = Button(text='Зависимость силы тока от напряжения', size_hint=(None, None), size=(400, 40))
        tab8_button42.text_size = tab8_button42.size
        tab8_button42.halign = 'center'
        tab8_button42.valign = 'middle'
        self.tab8_layout.add_widget(tab8_button42)
        tab8_button42.bind(on_press=self.on_button_click)
        tab8_button43 = Button(text='Электрическое сопротивление проводников. Единицы сопротивления',
                               size_hint=(None, None), size=(400, 40))
        tab8_button43.text_size = tab8_button43.size
        tab8_button43.halign = 'center'
        tab8_button43.valign = 'middle'
        self.tab8_layout.add_widget(tab8_button43)
        tab8_button43.bind(on_press=self.on_button_click)
        tab8_button44 = Button(text='Закон Ома для участка цепи', size_hint=(None, None), size=(400, 40))
        self.tab8_layout.add_widget(tab8_button44)
        tab8_button44.bind(on_press=self.on_button_click)
        tab8_button45 = Button(text='Расчет сопротивления проводника. Удельное сопротивление', size_hint=(None, None),
                               size=(400, 40))
        tab8_button45.text_size = tab8_button45.size
        tab8_button45.halign = 'center'
        tab8_button45.valign = 'middle'
        self.tab8_layout.add_widget(tab8_button45)
        tab8_button45.bind(on_press=self.on_button_click)
        tab8_button47 = Button(text='Реостаты', size_hint=(None, None), size=(400, 40))
        self.tab8_layout.add_widget(tab8_button47)
        tab8_button47.bind(on_press=self.on_button_click)
        tab8_button48 = Button(text='Последовательное соединение проводников', size_hint=(None, None), size=(400, 40))
        tab8_button48.text_size = tab8_button48.size
        tab8_button48.halign = 'center'
        tab8_button48.valign = 'middle'
        self.tab8_layout.add_widget(tab8_button48)
        tab8_button48.bind(on_press=self.on_button_click)
        tab8_button49 = Button(text='Параллельное соединение проводников', size_hint=(None, None), size=(400, 40))
        tab8_button49.text_size = tab8_button49.size
        tab8_button49.halign = 'center'
        tab8_button49.valign = 'middle'
        self.tab8_layout.add_widget(tab8_button49)
        tab8_button49.bind(on_press=self.on_button_click)
        tab8_button50 = Button(text='Работа электрического тока', size_hint=(None, None), size=(400, 40))
        self.tab8_layout.add_widget(tab8_button50)
        tab8_button50.bind(on_press=self.on_button_click)
        tab8_button51 = Button(text='Мощность электрического тока', size_hint=(None, None), size=(400, 40))
        self.tab8_layout.add_widget(tab8_button51)
        tab8_button51.bind(on_press=self.on_button_click)
        tab8_button52 = Button(text='Единицы работы электрического тока, применяемые на практике',
                               size_hint=(None, None), size=(400, 40))
        tab8_button52.text_size = tab8_button52.size
        tab8_button52.halign = 'center'
        tab8_button52.valign = 'middle'
        self.tab8_layout.add_widget(tab8_button52)
        tab8_button52.bind(on_press=self.on_button_click)
        tab8_button53 = Button(text='Нагревание проводников электрическим током. Закон Джоуля-Ленца',
                               size_hint=(None, None), size=(400, 40))
        tab8_button53.text_size = tab8_button53.size
        tab8_button53.halign = 'center'
        tab8_button53.valign = 'middle'
        self.tab8_layout.add_widget(tab8_button53)
        tab8_button53.bind(on_press=self.on_button_click)
        tab8_button54 = Button(text='Лампа накаливания. Электрические нагревательные приборы', size_hint=(None, None),
                               size=(400, 40))
        tab8_button54.text_size = tab8_button54.size
        tab8_button54.halign = 'center'
        tab8_button54.valign = 'middle'
        self.tab8_layout.add_widget(tab8_button54)
        tab8_button54.bind(on_press=self.on_button_click)
        tab8_button55 = Button(text='Короткое замыкание. Предохранители', size_hint=(None, None), size=(400, 40))
        tab8_button55.text_size = tab8_button55.size
        tab8_button55.halign = 'center'
        tab8_button55.valign = 'middle'
        self.tab8_layout.add_widget(tab8_button55)
        tab8_button55.bind(on_press=self.on_button_click)
        tab8_button56 = Button(text='Магнитное поле', size_hint=(None, None), size=(400, 40))
        self.tab8_layout.add_widget(tab8_button56)
        tab8_button56.bind(on_press=self.on_button_click)
        tab8_button57 = Button(text='Магнитное поле пряямого тока. Магнитные линии', size_hint=(None, None),
                               size=(400, 40))
        tab8_button57.text_size = tab8_button57.size
        tab8_button57.halign = 'center'
        tab8_button57.valign = 'middle'
        self.tab8_layout.add_widget(tab8_button57)
        tab8_button57.bind(on_press=self.on_button_click)
        tab8_button58 = Button(text='Магнитное поле катушки с током. Электромагниты и их применение',
                               size_hint=(None, None), size=(400, 40))
        tab8_button58.text_size = tab8_button58.size
        tab8_button58.halign = 'center'
        tab8_button58.valign = 'middle'
        self.tab8_layout.add_widget(tab8_button58)
        tab8_button58.bind(on_press=self.on_button_click)
        tab8_button59 = Button(text='Постоянные магниты. Магнитное поле постоянных магнитов', size_hint=(None, None), size=(400, 40))
        tab8_button59.text_size = tab8_button59.size
        tab8_button59.halign = 'center'
        tab8_button59.valign = 'middle'
        self.tab8_layout.add_widget(tab8_button59)
        tab8_button59.bind(on_press=self.on_button_click)
        tab8_button60 = Button(text='Магнитное поле Земли', size_hint=(None, None), size=(400, 40))
        tab8_button60.text_size = tab8_button60.size
        tab8_button60.halign = 'center'
        tab8_button60.valign = 'middle'
        self.tab8_layout.add_widget(tab8_button60)
        tab8_button60.bind(on_press=self.on_button_click)
        tab8_button61 = Button(text='Действие магнитного поля на проводник с током. Электрический двигатель',
                               size_hint=(None, None), size=(400, 40))
        tab8_button61.text_size = tab8_button61.size
        tab8_button61.halign = 'center'
        tab8_button61.valign = 'middle'
        self.tab8_layout.add_widget(tab8_button61)
        tab8_button61.bind(on_press=self.on_button_click)
        tab8_button62 = Button(text='Источники света. Распространение света', size_hint=(None, None), size=(400, 40))
        tab8_button62.text_size = tab8_button62.size
        tab8_button62.halign = 'center'
        tab8_button62.valign = 'middle'
        self.tab8_layout.add_widget(tab8_button62)
        tab8_button62.bind(on_press=self.on_button_click)
        tab8_button63 = Button(text='Отражение света. Закон отражения света', size_hint=(None, None), size=(400, 40))
        tab8_button63.text_size = tab8_button63.size
        tab8_button63.halign = 'center'
        tab8_button63.valign = 'middle'
        self.tab8_layout.add_widget(tab8_button63)
        tab8_button63.bind(on_press=self.on_button_click)
        tab8_button64 = Button(text='Плоское зеркало', size_hint=(None, None), size=(400, 40))
        self.tab8_layout.add_widget(tab8_button64)
        tab8_button64.bind(on_press=self.on_button_click)
        tab8_button65 = Button(text='Преломление света. Закон преломления света', size_hint=(None, None),
                               size=(400, 40))
        tab8_button65.text_size = tab8_button65.size
        tab8_button65.halign = 'center'
        tab8_button65.valign = 'middle'
        self.tab8_layout.add_widget(tab8_button65)
        tab8_button65.bind(on_press=self.on_button_click)
        tab8_button66 = Button(text='Линзы. Оптическая сила линзы', size_hint=(None, None), size=(400, 40))
        self.tab8_layout.add_widget(tab8_button66)
        tab8_button66.bind(on_press=self.on_button_click)

        # tab9
        tab9_button1 = Button(text='Материальная точка. Система отсчёта', size_hint=(None, None), size=(400, 40))
        self.tab9_layout.add_widget(tab9_button1)
        tab9_button1.bind(on_press=self.on_button_click)
        tab9_button2 = Button(text='Перемещение', size_hint=(None, None), size=(400, 40))
        self.tab9_layout.add_widget(tab9_button2)
        tab9_button2.bind(on_press=self.on_button_click)
        tab9_button3 = Button(text='Определение координаты движущегося тела', size_hint=(None, None), size=(400, 40))
        tab9_button3.text_size = tab9_button3.size
        tab9_button3.halign = 'center'
        tab9_button3.valign = 'middle'
        self.tab9_layout.add_widget(tab9_button3)
        tab9_button3.bind(on_press=self.on_button_click)
        tab9_button4 = Button(text='Перемещение при прямолинейном равномерном движении', size_hint=(None, None),
                              size=(400, 40))
        tab9_button4.text_size = tab9_button4.size
        tab9_button4.halign = 'center'
        tab9_button4.valign = 'middle'
        self.tab9_layout.add_widget(tab9_button4)
        tab9_button4.bind(on_press=self.on_button_click)
        tab9_button5 = Button(text='Прямолинейное равноускоренное движение. Ускорение', size_hint=(None, None),
                              size=(400, 40))
        tab9_button5.text_size = tab9_button5.size
        tab9_button5.halign = 'center'
        tab9_button5.valign = 'middle'
        self.tab9_layout.add_widget(tab9_button5)
        tab9_button5.bind(on_press=self.on_button_click)
        tab9_button6 = Button(text='Скорость прямолинейного равноускоренного движения.', size_hint=(None, None),
                              size=(400, 40))
        tab9_button6.text_size = tab9_button6.size
        tab9_button6.halign = 'center'
        tab9_button6.valign = 'middle'
        self.tab9_layout.add_widget(tab9_button6)
        tab9_button6.bind(on_press=self.on_button_click)
        tab9_button7 = Button(text='Перемещение при прямолинейном равноускоренном движении', size_hint=(None, None),
                              size=(400, 40))
        tab9_button7.text_size = tab9_button7.size
        tab9_button7.halign = 'center'
        tab9_button7.valign = 'middle'
        self.tab9_layout.add_widget(tab9_button7)
        tab9_button7.bind(on_press=self.on_button_click)
        tab9_button8 = Button(text='Перемещение тела при прямолинейном равноускоренном движении без начальной скорости',
                              size_hint=(None, None), size=(400, 40))
        tab9_button8.text_size = tab9_button8.size
        tab9_button8.halign = 'center'
        tab9_button8.valign = 'middle'
        self.tab9_layout.add_widget(tab9_button8)
        tab9_button8.bind(on_press=self.on_button_click)
        tab9_button10 = Button(text='Инерциальные системы отсчёта. Первый закон Ньютона', size_hint=(None, None),
                               size=(400, 40))
        tab9_button10.text_size = tab9_button10.size
        tab9_button10.halign = 'center'
        tab9_button10.valign = 'middle'
        self.tab9_layout.add_widget(tab9_button10)
        tab9_button10.bind(on_press=self.on_button_click)
        tab9_button11 = Button(text='Второй закон Ньютона', size_hint=(None, None), size=(400, 40))
        self.tab9_layout.add_widget(tab9_button11)
        tab9_button11.bind(on_press=self.on_button_click)
        tab9_button12 = Button(text='Третий закон Ньютона', size_hint=(None, None), size=(400, 40))
        self.tab9_layout.add_widget(tab9_button12)
        tab9_button12.bind(on_press=self.on_button_click)
        tab9_button13 = Button(text='Свободное падение тел', size_hint=(None, None), size=(400, 40))
        self.tab9_layout.add_widget(tab9_button13)
        tab9_button13.bind(on_press=self.on_button_click)
        tab9_button14 = Button(text='Движение тела, брошенного вертикально вверх', size_hint=(None, None),
                               size=(400, 40))
        tab9_button14.text_size = tab9_button14.size
        tab9_button14.halign = 'center'
        tab9_button14.valign = 'middle'
        self.tab9_layout.add_widget(tab9_button14)
        tab9_button14.bind(on_press=self.on_button_click)
        tab9_button15 = Button(text='Закон всемирного тяготения', size_hint=(None, None), size=(400, 40))
        self.tab9_layout.add_widget(tab9_button15)
        tab9_button15.bind(on_press=self.on_button_click)
        tab9_button18 = Button(text='Прямолинейное и криволинейное движение', size_hint=(None, None), size=(400, 40))
        tab9_button18.text_size = tab9_button18.size
        tab9_button18.halign = 'center'
        tab9_button18.valign = 'middle'
        self.tab9_layout.add_widget(tab9_button18)
        tab9_button18.bind(on_press=self.on_button_click)
        tab9_button19 = Button(text='Движение тела по окружности с постоянной по модулю скоростью',
                               size_hint=(None, None), size=(400, 40))
        tab9_button19.text_size = tab9_button19.size
        tab9_button19.halign = 'center'
        tab9_button19.valign = 'middle'
        self.tab9_layout.add_widget(tab9_button19)
        tab9_button19.bind(on_press=self.on_button_click)
        tab9_button21 = Button(text='Импульс тела', size_hint=(None, None), size=(400, 40))
        self.tab9_layout.add_widget(tab9_button21)
        tab9_button21.bind(on_press=self.on_button_click)
        tab9_button22 = Button(text='Закон сохранения импульса', size_hint=(None, None), size=(400, 40))
        self.tab9_layout.add_widget(tab9_button22)
        tab9_button22.bind(on_press=self.on_button_click)
        tab9_button23 = Button(text='Реактивное движение. Ракеты', size_hint=(None, None), size=(400, 40))
        self.tab9_layout.add_widget(tab9_button23)
        tab9_button23.bind(on_press=self.on_button_click)
        tab9_button24 = Button(text='Колебательное движение', size_hint=(None, None), size=(400, 40))
        self.tab9_layout.add_widget(tab9_button24)
        tab9_button24.bind(on_press=self.on_button_click)
        tab9_button25 = Button(text='Свободные колебания. Колебательные системы. Маятник', size_hint=(None, None),
                               size=(400, 40))
        tab9_button25.text_size = tab9_button25.size
        tab9_button25.halign = 'center'
        tab9_button25.valign = 'middle'
        self.tab9_layout.add_widget(tab9_button25)
        tab9_button25.bind(on_press=self.on_button_click)
        tab9_button26 = Button(text='Величины, характеризующие колебательное движение.', size_hint=(None, None),
                               size=(400, 40))
        tab9_button26.text_size = tab9_button26.size
        tab9_button26.halign = 'center'
        tab9_button26.valign = 'middle'
        self.tab9_layout.add_widget(tab9_button26)
        tab9_button26.bind(on_press=self.on_button_click)
        tab9_button27 = Button(text='Гармонические колебания', size_hint=(None, None), size=(400, 40))
        self.tab9_layout.add_widget(tab9_button27)
        tab9_button27.bind(on_press=self.on_button_click)
        tab9_button28 = Button(text='Затухающие колебания', size_hint=(None, None), size=(400, 40))
        self.tab9_layout.add_widget(tab9_button28)
        tab9_button28.bind(on_press=self.on_button_click)
        tab9_button29 = Button(text='Вынужденные колебания', size_hint=(None, None), size=(400, 40))
        self.tab9_layout.add_widget(tab9_button29)
        tab9_button29.bind(on_press=self.on_button_click)
        tab9_button30 = Button(text='Резонанс', size_hint=(None, None), size=(400, 40))
        self.tab9_layout.add_widget(tab9_button30)
        tab9_button30.bind(on_press=self.on_button_click)
        tab9_button31 = Button(text='Распространение колебаний в среде. Волны', size_hint=(None, None), size=(400, 40))
        tab9_button31.text_size = tab9_button31.size
        tab9_button31.halign = 'center'
        tab9_button31.valign = 'middle'
        self.tab9_layout.add_widget(tab9_button31)
        tab9_button31.bind(on_press=self.on_button_click)
        tab9_button32 = Button(text='Продольные и поперечные волны', size_hint=(None, None), size=(400, 40))
        self.tab9_layout.add_widget(tab9_button32)
        tab9_button32.bind(on_press=self.on_button_click)
        tab9_button33 = Button(text='Длина волны. Скорость распространения волн', size_hint=(None, None),
                               size=(400, 40))
        tab9_button33.text_size = tab9_button33.size
        tab9_button33.halign = 'center'
        tab9_button33.valign = 'middle'
        self.tab9_layout.add_widget(tab9_button33)
        tab9_button33.bind(on_press=self.on_button_click)
        tab9_button34 = Button(text='Источники звука. Звуковые колебания', size_hint=(None, None), size=(400, 40))
        tab9_button34.text_size = tab9_button34.size
        tab9_button34.halign = 'center'
        tab9_button34.valign = 'middle'
        self.tab9_layout.add_widget(tab9_button34)
        tab9_button34.bind(on_press=self.on_button_click)
        tab9_button35 = Button(text='Высота и тембр звука', size_hint=(None, None), size=(400, 40))
        self.tab9_layout.add_widget(tab9_button35)
        tab9_button35.bind(on_press=self.on_button_click)
        tab9_button36 = Button(text='Громкость звука', size_hint=(None, None), size=(400, 40))
        self.tab9_layout.add_widget(tab9_button36)
        tab9_button36.bind(on_press=self.on_button_click)
        tab9_button37 = Button(text='Распространение звука', size_hint=(None, None), size=(400, 40))
        self.tab9_layout.add_widget(tab9_button37)
        tab9_button37.bind(on_press=self.on_button_click)
        tab9_button38 = Button(text='Звуковые волны. Скорость звука', size_hint=(None, None), size=(400, 40))
        self.tab9_layout.add_widget(tab9_button38)
        tab9_button38.bind(on_press=self.on_button_click)
        tab9_button39 = Button(text='Отражение звука. Эхо', size_hint=(None, None), size=(400, 40))
        self.tab9_layout.add_widget(tab9_button39)
        tab9_button39.bind(on_press=self.on_button_click)
        tab9_button41 = Button(text='Ультразвук и инфразвук', size_hint=(None, None), size=(400, 40))
        self.tab9_layout.add_widget(tab9_button41)
        tab9_button41.bind(on_press=self.on_button_click)
        tab9_button43 = Button(text='Магнитное поле и его графическое изображение', size_hint=(None, None),
                               size=(400, 40))
        tab9_button43.text_size = tab9_button43.size
        tab9_button43.halign = 'center'
        tab9_button43.valign = 'middle'
        self.tab9_layout.add_widget(tab9_button43)
        tab9_button43.bind(on_press=self.on_button_click)
        tab9_button44 = Button(text='Неоднородное и однородное магнитное поле', size_hint=(None, None),
                               size=(400, 40))
        tab9_button44.text_size = tab9_button44.size
        tab9_button44.halign = 'center'
        tab9_button44.valign = 'middle'
        self.tab9_layout.add_widget(tab9_button44)
        tab9_button44.bind(on_press=self.on_button_click)
        tab9_button45 = Button(text='Направление тока и направление линий его магнитного поля', size_hint=(None, None),
                               size=(400, 40))
        tab9_button45.text_size = tab9_button45.size
        tab9_button45.halign = 'center'
        tab9_button45.valign = 'middle'
        self.tab9_layout.add_widget(tab9_button45)
        tab9_button45.bind(on_press=self.on_button_click)
        tab9_button46 = Button(text='Обнаружение магнитного поля по его действию на электрический ток. Правило левой руки',size_hint=(None, None), size=(400, 40))
        tab9_button46.text_size = tab9_button46.size
        tab9_button46.halign = 'center'
        tab9_button46.valign = 'middle'
        self.tab9_layout.add_widget(tab9_button46)
        tab9_button46.bind(on_press=self.on_button_click)
        tab9_button47 = Button(text='Индукция магнитного поля', size_hint=(None, None), size=(400, 40))
        self.tab9_layout.add_widget(tab9_button47)
        tab9_button47.bind(on_press=self.on_button_click)
        tab9_button48 = Button(text='Магнитный поток', size_hint=(None, None), size=(400, 40))
        self.tab9_layout.add_widget(tab9_button48)
        tab9_button48.bind(on_press=self.on_button_click)
        tab9_button49 = Button(text='Явление электромагнитной индукции', size_hint=(None, None), size=(400, 40))
        tab9_button49.text_size = tab9_button49.size
        tab9_button49.halign = 'center'
        tab9_button49.valign = 'middle'
        self.tab9_layout.add_widget(tab9_button49)
        tab9_button49.bind(on_press=self.on_button_click)
        tab9_button50 = Button(text='Получение переменного электрического тока', size_hint=(None, None), size=(400, 40))
        tab9_button50.text_size = tab9_button50.size
        tab9_button50.halign = 'center'
        tab9_button50.valign = 'middle'
        self.tab9_layout.add_widget(tab9_button50)
        tab9_button50.bind(on_press=self.on_button_click)
        tab9_button51 = Button(text='Электромагнитное поле', size_hint=(None, None), size=(400, 40))
        self.tab9_layout.add_widget(tab9_button51)
        tab9_button51.bind(on_press=self.on_button_click)
        tab9_button52 = Button(text='Электромагнитные волны', size_hint=(None, None), size=(400, 40))
        self.tab9_layout.add_widget(tab9_button52)
        tab9_button52.bind(on_press=self.on_button_click)
        tab9_button53 = Button(text='Интерференция света', size_hint=(None, None), size=(400, 40))
        self.tab9_layout.add_widget(tab9_button53)
        tab9_button53.bind(on_press=self.on_button_click)
        tab9_button54 = Button(text='Электромагнитная природа света', size_hint=(None, None), size=(400, 40))
        self.tab9_layout.add_widget(tab9_button54)
        tab9_button54.bind(on_press=self.on_button_click)
        tab9_button56 = Button(text='Модели атомов. Опыт Резерфорда', size_hint=(None, None), size=(400, 40))
        self.tab9_layout.add_widget(tab9_button56)
        tab9_button56.bind(on_press=self.on_button_click)
        tab9_button57 = Button(text='Радиоактивные превращения атомных ядер', size_hint=(None, None), size=(400, 40))
        tab9_button57.text_size = tab9_button57.size
        tab9_button57.halign = 'center'
        tab9_button57.valign = 'middle'
        self.tab9_layout.add_widget(tab9_button57)
        tab9_button57.bind(on_press=self.on_button_click)
        tab9_button58 = Button(text='Экспериментальные методы исследования частиц', size_hint=(None, None),
                               size=(400, 40))
        tab9_button58.text_size = tab9_button58.size
        tab9_button58.halign = 'center'
        tab9_button58.valign = 'middle'
        self.tab9_layout.add_widget(tab9_button58)
        tab9_button58.bind(on_press=self.on_button_click)
        tab9_button61 = Button(text='Состав атомного ядра. Массовое число. Зарядовое число', size_hint=(None, None),
                               size=(400, 40))
        tab9_button61.text_size = tab9_button61.size
        tab9_button61.halign = 'center'
        tab9_button61.valign = 'middle'
        self.tab9_layout.add_widget(tab9_button61)
        tab9_button61.bind(on_press=self.on_button_click)
        tab9_button62 = Button(text='Изотопы', size_hint=(None, None), size=(400, 40))
        self.tab9_layout.add_widget(tab9_button62)
        tab9_button62.bind(on_press=self.on_button_click)
        tab9_button63 = Button(text='Альфа- и бета-распад. Правило смещения', size_hint=(None, None), size=(400, 40))
        tab9_button63.text_size = tab9_button63.size
        tab9_button63.halign = 'center'
        tab9_button63.valign = 'middle'
        self.tab9_layout.add_widget(tab9_button63)
        tab9_button63.bind(on_press=self.on_button_click)
        tab9_button64 = Button(text='Ядерные силы', size_hint=(None, None), size=(400, 40))
        self.tab9_layout.add_widget(tab9_button64)
        tab9_button64.bind(on_press=self.on_button_click)
        tab9_button65 = Button(text='Энергия связи. Дефект масс', size_hint=(None, None), size=(400, 40))
        self.tab9_layout.add_widget(tab9_button65)
        tab9_button65.bind(on_press=self.on_button_click)
        tab9_button67 = Button(text='Цепная реакция', size_hint=(None, None), size=(400, 40))
        self.tab9_layout.add_widget(tab9_button67)
        tab9_button67.bind(on_press=self.on_button_click)
        tab9_button68 = Button(
            text='Ядерный реактор. Преобразование внутренней энергии атомных ядер в электрическую энергию',
            size_hint=(None, None), size=(400, 40))
        tab9_button68.text_size = tab9_button68.size
        tab9_button68.halign = 'center'
        tab9_button68.valign = 'middle'
        self.tab9_layout.add_widget(tab9_button68)
        tab9_button68.bind(on_press=self.on_button_click)
        tab9_button69 = Button(text='Атомная энергетика', size_hint=(None, None), size=(400, 40))
        self.tab9_layout.add_widget(tab9_button69)
        tab9_button69.bind(on_press=self.on_button_click)
        tab9_button71 = Button(text='Получение и применение радиоактивных изотопов', size_hint=(None, None),
                               size=(400, 40))
        tab9_button71.text_size = tab9_button71.size
        tab9_button71.halign = 'center'
        tab9_button71.valign = 'middle'
        self.tab9_layout.add_widget(tab9_button71)
        tab9_button71.bind(on_press=self.on_button_click)
        tab9_button72 = Button(text='Термоядерная реакция', size_hint=(None, None), size=(400, 40))
        self.tab9_layout.add_widget(tab9_button72)
        tab9_button72.bind(on_press=self.on_button_click)

        # tab10
        tab10_button2 = Button(text='Способы описания движения', size_hint=(None, None), size=(400, 40))
        self.tab10_layout.add_widget(tab10_button2)
        tab10_button2.bind(on_press=self.on_button_click)
        tab10_button4 = Button(text='Равномерное прямолинейное движение. Скорость. Уравнение движения',
                               size_hint=(None, None), size=(400, 40))
        tab10_button4.text_size = tab10_button4.size
        tab10_button4.halign = 'center'
        tab10_button4.valign = 'middle'
        self.tab10_layout.add_widget(tab10_button4)
        tab10_button4.bind(on_press=self.on_button_click)
        tab10_button6 = Button(text='Сложение скоростей', size_hint=(None, None), size=(400, 40))
        self.tab10_layout.add_widget(tab10_button6)
        tab10_button6.bind(on_press=self.on_button_click)
        tab10_button8 = Button(text='Мгновенная и средняя скорости', size_hint=(None, None), size=(400, 40))
        self.tab10_layout.add_widget(tab10_button8)
        tab10_button8.bind(on_press=self.on_button_click)
        tab10_button9 = Button(text='Ускорение', size_hint=(None, None), size=(400, 40))
        self.tab10_layout.add_widget(tab10_button9)
        tab10_button9.bind(on_press=self.on_button_click)
        tab10_button10 = Button(text='Движение с постоянным ускорением', size_hint=(None, None), size=(400, 40))
        self.tab10_layout.add_widget(tab10_button10)
        tab10_button10.bind(on_press=self.on_button_click)
        tab10_button13 = Button(text='Движение с постоянным ускорением свободного падения', size_hint=(None, None),
                                size=(400, 40))
        tab10_button13.text_size = tab10_button13.size
        tab10_button13.halign = 'center'
        tab10_button13.valign = 'middle'
        self.tab10_layout.add_widget(tab10_button13)
        tab10_button13.bind(on_press=self.on_button_click)
        tab10_button15 = Button(text='Равномерное движение точки по окружности', size_hint=(None, None), size=(400, 40))
        tab10_button15.text_size = tab10_button15.size
        tab10_button15.halign = 'center'
        tab10_button15.valign = 'middle'
        self.tab10_layout.add_widget(tab10_button15)
        tab10_button15.bind(on_press=self.on_button_click)
        tab10_button16 = Button(text='Кинематика абсолютно твёрдого тела', size_hint=(None, None), size=(400, 40))
        tab10_button16.text_size = tab10_button16.size
        tab10_button16.halign = 'center'
        tab10_button16.valign = 'middle'
        self.tab10_layout.add_widget(tab10_button16)
        tab10_button16.bind(on_press=self.on_button_click)
        tab10_button18 = Button(text='Основное утверждение механики', size_hint=(None, None), size=(400, 40))
        self.tab10_layout.add_widget(tab10_button18)
        tab10_button18.bind(on_press=self.on_button_click)
        tab10_button19 = Button(text='Сила. Масса. Единица массы', size_hint=(None, None), size=(400, 40))
        self.tab10_layout.add_widget(tab10_button19)
        tab10_button19.bind(on_press=self.on_button_click)
        tab10_button20 = Button(text='Первый закон Ньютона', size_hint=(None, None), size=(400, 40))
        self.tab10_layout.add_widget(tab10_button20)
        tab10_button20.bind(on_press=self.on_button_click)
        tab10_button21 = Button(text='Второй закон Ньютона', size_hint=(None, None), size=(400, 40))
        self.tab10_layout.add_widget(tab10_button21)
        tab10_button21.bind(on_press=self.on_button_click)
        tab10_button22 = Button(text='Принцип суперпозиции сил', size_hint=(None, None), size=(400, 40))
        self.tab10_layout.add_widget(tab10_button22)
        tab10_button22.bind(on_press=self.on_button_click)
        tab10_button24 = Button(text='Третий закон Ньютона', size_hint=(None, None), size=(400, 40))
        self.tab10_layout.add_widget(tab10_button24)
        tab10_button24.bind(on_press=self.on_button_click)
        tab10_button25 = Button(text='Геоцентрическая система отсчёта', size_hint=(None, None), size=(400, 40))
        self.tab10_layout.add_widget(tab10_button25)
        tab10_button25.bind(on_press=self.on_button_click)
        tab10_button26 = Button(text='Принцип относительности Галилея. Инвариантные и относительные величины',
                                size_hint=(None, None), size=(400, 40))
        tab10_button26.text_size = tab10_button26.size
        tab10_button26.halign = 'center'
        tab10_button26.valign = 'middle'
        self.tab10_layout.add_widget(tab10_button26)
        tab10_button26.bind(on_press=self.on_button_click)
        tab10_button27 = Button(text='Силы в природе', size_hint=(None, None), size=(400, 40))
        self.tab10_layout.add_widget(tab10_button27)
        tab10_button27.bind(on_press=self.on_button_click)
        tab10_button28 = Button(text='Сила тяжести и сила всемирного тяготения', size_hint=(None, None), size=(400, 40))
        tab10_button28.text_size = tab10_button28.size
        tab10_button28.halign = 'center'
        tab10_button28.valign = 'middle'
        self.tab10_layout.add_widget(tab10_button28)
        tab10_button28.bind(on_press=self.on_button_click)
        tab10_button29 = Button(text='Сила тяжести на других планетах', size_hint=(None, None), size=(400, 40))
        self.tab10_layout.add_widget(tab10_button29)
        tab10_button29.bind(on_press=self.on_button_click)
        tab10_button31 = Button(text='Первая космическая скорость', size_hint=(None, None), size=(400, 40))
        self.tab10_layout.add_widget(tab10_button31)
        tab10_button31.bind(on_press=self.on_button_click)
        tab10_button33 = Button(text='Вес. Невесомость', size_hint=(None, None), size=(400, 40))
        self.tab10_layout.add_widget(tab10_button33)
        tab10_button33.bind(on_press=self.on_button_click)
        tab10_button34 = Button(text='Деформация и силы упругости. Закое Гука', size_hint=(None, None), size=(400, 40))
        tab10_button34.text_size = tab10_button34.size
        tab10_button34.halign = 'center'
        tab10_button34.valign = 'middle'
        self.tab10_layout.add_widget(tab10_button34)
        tab10_button34.bind(on_press=self.on_button_click)
        tab10_button36 = Button(text='Силы трения', size_hint=(None, None), size=(400, 40))
        self.tab10_layout.add_widget(tab10_button36)
        tab10_button36.bind(on_press=self.on_button_click)
        tab10_button38 = Button(text='Импульс материальной точки. Закон сохранения импульса', size_hint=(None, None),
                                size=(400, 40))
        tab10_button38.text_size = tab10_button38.size
        tab10_button38.halign = 'center'
        tab10_button38.valign = 'middle'
        self.tab10_layout.add_widget(tab10_button38)
        tab10_button38.bind(on_press=self.on_button_click)
        tab10_button40 = Button(text='Механическая работа и мощность силы', size_hint=(None, None), size=(400, 40))
        tab10_button40.text_size = tab10_button40.size
        tab10_button40.halign = 'center'
        tab10_button40.valign = 'middle'
        self.tab10_layout.add_widget(tab10_button40)
        tab10_button40.bind(on_press=self.on_button_click)
        tab10_button41 = Button(text='Энергия. Кинетическая энергия', size_hint=(None, None), size=(400, 40))
        self.tab10_layout.add_widget(tab10_button41)
        tab10_button41.bind(on_press=self.on_button_click)
        tab10_button43 = Button(text='Работа силы тяжести и силы упругости. Консервативные силы',
                                size_hint=(None, None), size=(400, 40))
        tab10_button43.text_size = tab10_button43.size
        tab10_button43.halign = 'center'
        tab10_button43.valign = 'middle'
        self.tab10_layout.add_widget(tab10_button43)
        tab10_button43.bind(on_press=self.on_button_click)
        tab10_button44 = Button(text='Потенциальная энергия', size_hint=(None, None), size=(400, 40))
        self.tab10_layout.add_widget(tab10_button44)
        tab10_button44.bind(on_press=self.on_button_click)
        tab10_button45 = Button(text='Закон сохранения энергии в механике', size_hint=(None, None), size=(400, 40))
        tab10_button45.text_size = tab10_button45.size
        tab10_button45.halign = 'center'
        tab10_button45.valign = 'middle'
        self.tab10_layout.add_widget(tab10_button45)
        tab10_button46 = Button(text='Работа силы тяготения. Потенциальная энергия в поле тяготения',
                                size_hint=(None, None), size=(400, 40))
        tab10_button46.text_size = tab10_button46.size
        tab10_button46.halign = 'center'
        tab10_button46.valign = 'middle'
        self.tab10_layout.add_widget(tab10_button46)
        tab10_button46.bind(on_press=self.on_button_click)
        tab10_button48 = Button(text='Основное уравнение динамики вращательного движения', size_hint=(None, None),
                                size=(400, 40))
        tab10_button48.text_size = tab10_button48.size
        tab10_button48.halign = 'center'
        tab10_button48.valign = 'middle'
        self.tab10_layout.add_widget(tab10_button48)
        tab10_button48.bind(on_press=self.on_button_click)
        tab10_button49 = Button(
            text='Закон сохранения момента импульса. Кинетическая энергия абсолютно твёрдого тела, вращающегося относительно неподвижной оси',
            size_hint=(None, None), size=(400, 60))
        tab10_button49.text_size = tab10_button49.size
        tab10_button49.halign = 'center'
        tab10_button49.valign = 'middle'
        self.tab10_layout.add_widget(tab10_button49)
        tab10_button49.bind(on_press=self.on_button_click)
        tab10_button51 = Button(text='Равновесие тел', size_hint=(None, None), size=(400, 40))
        self.tab10_layout.add_widget(tab10_button51)
        tab10_button51.bind(on_press=self.on_button_click)
        tab10_button52 = Button(text='Молекулярная физика.Тепловые явления', size_hint=(None, None), size=(400, 40))
        tab10_button52.text_size = tab10_button52.size
        tab10_button52.halign = 'center'
        tab10_button52.valign = 'middle'
        self.tab10_layout.add_widget(tab10_button52)
        tab10_button52.bind(on_press=self.on_button_click)
        tab10_button53 = Button(text='Основные положения молекулярно-кинетической теории. Размеры молекул',
                                size_hint=(None, None), size=(400, 40))
        tab10_button53.text_size = tab10_button53.size
        tab10_button53.halign = 'center'
        tab10_button53.valign = 'middle'
        self.tab10_layout.add_widget(tab10_button53)
        tab10_button53.bind(on_press=self.on_button_click)
        tab10_button55 = Button(text='Броуновское движение', size_hint=(None, None), size=(400, 40))
        self.tab10_layout.add_widget(tab10_button55)
        tab10_button55.bind(on_press=self.on_button_click)
        tab10_button56 = Button(text='Силы взаимодействия молекул. Строение газообразных, жидких и твёрдых тел',
                                size_hint=(None, None), size=(400, 40))
        tab10_button56.text_size = tab10_button56.size
        tab10_button56.halign = 'center'
        tab10_button56.valign = 'middle'
        self.tab10_layout.add_widget(tab10_button56)
        tab10_button56.bind(on_press=self.on_button_click)
        tab10_button57 = Button(text='Основное уравнение молекулярно-кинетической теории газов', size_hint=(None, None),
                                size=(400, 40))
        tab10_button57.text_size = tab10_button57.size
        tab10_button57.halign = 'center'
        tab10_button57.valign = 'middle'
        self.tab10_layout.add_widget(tab10_button57)
        tab10_button57.bind(on_press=self.on_button_click)
        tab10_button59 = Button(text='Температура и тепловое равновесие', size_hint=(None, None), size=(400, 40))
        self.tab10_layout.add_widget(tab10_button59)
        tab10_button59.bind(on_press=self.on_button_click)
        tab10_button60 = Button(text='Определение температуры. Энергия теплового движения молекул',
                                size_hint=(None, None), size=(400, 40))
        tab10_button60.text_size = tab10_button60.size
        tab10_button60.halign = 'center'
        tab10_button60.valign = 'middle'
        self.tab10_layout.add_widget(tab10_button60)
        tab10_button60.bind(on_press=self.on_button_click)
        tab10_button61 = Button(text='Измерение скоростей молекул газа', size_hint=(None, None), size=(400, 40))
        self.tab10_layout.add_widget(tab10_button61)
        tab10_button61.bind(on_press=self.on_button_click)
        tab10_button63 = Button(text='Уравнение состояния идеального газа', size_hint=(None, None), size=(400, 40))
        tab10_button63.text_size = tab10_button63.size
        tab10_button63.halign = 'center'
        tab10_button63.valign = 'middle'
        self.tab10_layout.add_widget(tab10_button63)
        tab10_button63.bind(on_press=self.on_button_click)
        tab10_button65 = Button(text='Газовые законы', size_hint=(None, None), size=(400, 40))
        self.tab10_layout.add_widget(tab10_button65)
        tab10_button65.bind(on_press=self.on_button_click)
        tab10_button68 = Button(text='Насыщенный пар', size_hint=(None, None), size=(400, 40))
        self.tab10_layout.add_widget(tab10_button68)
        tab10_button68.bind(on_press=self.on_button_click)
        tab10_button69 = Button(text='Давление насыщенного пара', size_hint=(None, None), size=(400, 40))
        self.tab10_layout.add_widget(tab10_button69)
        tab10_button69.bind(on_press=self.on_button_click)
        tab10_button70 = Button(text='Влажность воздуха', size_hint=(None, None), size=(400, 40))
        self.tab10_layout.add_widget(tab10_button70)
        tab10_button70.bind(on_press=self.on_button_click)
        tab10_button72 = Button(text='Кристаллические и аморфные тела', size_hint=(None, None), size=(400, 40))
        self.tab10_layout.add_widget(tab10_button72)
        tab10_button72.bind(on_press=self.on_button_click)
        tab10_button73 = Button(text='Внутренняя энергия', size_hint=(None, None), size=(400, 40))
        self.tab10_layout.add_widget(tab10_button73)
        tab10_button73.bind(on_press=self.on_button_click)
        tab10_button74 = Button(text='Работа в термодинамике', size_hint=(None, None), size=(400, 40))
        self.tab10_layout.add_widget(tab10_button74)
        tab10_button74.bind(on_press=self.on_button_click)
        tab10_button76 = Button(text='Количество теплоты. Уравнение теплового баланса', size_hint=(None, None),
                                size=(400, 40))
        tab10_button76.text_size = tab10_button76.size
        tab10_button76.halign = 'center'
        tab10_button76.valign = 'middle'
        self.tab10_layout.add_widget(tab10_button76)
        tab10_button76.bind(on_press=self.on_button_click)
        tab10_button78 = Button(text='Первый закон термодинамики', size_hint=(None, None), size=(400, 40))
        self.tab10_layout.add_widget(tab10_button78)
        tab10_button78.bind(on_press=self.on_button_click)
        tab10_button79 = Button(text='Применение первого закона термодинамики к различным процессам',
                                size_hint=(None, None), size=(400, 40))
        tab10_button79.text_size = tab10_button79.size
        tab10_button79.halign = 'center'
        tab10_button79.valign = 'middle'
        self.tab10_layout.add_widget(tab10_button79)
        tab10_button79.bind(on_press=self.on_button_click)
        tab10_button81 = Button(text='Второй закон термодинамики', size_hint=(None, None), size=(400, 40))
        self.tab10_layout.add_widget(tab10_button81)
        tab10_button81.bind(on_press=self.on_button_click)
        tab10_button83 = Button(text='Основы электродинамики', size_hint=(None, None), size=(400, 40))
        self.tab10_layout.add_widget(tab10_button83)
        tab10_button83.bind(on_press=self.on_button_click)
        tab10_button84 = Button(text='Закон сохранения заряда и элементарные частицы', size_hint=(None, None),
                                size=(400, 40))
        self.tab10_layout.add_widget(tab10_button84)
        tab10_button84.bind(on_press=self.on_button_click)
        tab10_button85 = Button(text='Закон Кулона. Единица электрического заряда', size_hint=(None, None),
                                size=(400, 40))
        tab10_button85.text_size = tab10_button85.size
        tab10_button85.halign = 'center'
        tab10_button85.valign = 'middle'
        self.tab10_layout.add_widget(tab10_button85)
        tab10_button85.bind(on_press=self.on_button_click)
        tab10_button88 = Button(text='Электрическое поле', size_hint=(None, None), size=(400, 40))
        self.tab10_layout.add_widget(tab10_button88)
        tab10_button88.bind(on_press=self.on_button_click)
        tab10_button89 = Button(text='Напряжённость электрического тока. Силовые линии', size_hint=(None, None),
                                size=(400, 40))
        tab10_button89.text_size = tab10_button89.size
        tab10_button89.halign = 'center'
        tab10_button89.valign = 'middle'
        self.tab10_layout.add_widget(tab10_button89)
        tab10_button89.bind(on_press=self.on_button_click)
        tab10_button90 = Button(text='Поле точеченого заряда и заряженного шара. Принцип суперпозиции полей',
                                size_hint=(None, None), size=(400, 40))
        tab10_button90.text_size = tab10_button90.size
        tab10_button90.halign = 'center'
        tab10_button90.valign = 'middle'
        self.tab10_layout.add_widget(tab10_button90)
        tab10_button90.bind(on_press=self.on_button_click)
        tab10_button92 = Button(text='Проводники и диэлектрики в электростатическом поле', size_hint=(None, None),
                                size=(400, 40))
        tab10_button92.text_size = tab10_button92.size
        tab10_button92.halign = 'center'
        tab10_button92.valign = 'middle'
        self.tab10_layout.add_widget(tab10_button92)
        tab10_button92.bind(on_press=self.on_button_click)
        tab10_button95 = Button(
            text='Связь между напряжённостью электростатического поля и разностью потенциалов. Эквипотенциальные поверхности',
            size_hint=(None, None), size=(400, 40))
        tab10_button95.text_size = tab10_button95.size
        tab10_button95.halign = 'center'
        tab10_button95.valign = 'middle'
        self.tab10_layout.add_widget(tab10_button95)
        tab10_button95.bind(on_press=self.on_button_click)
        tab10_button97 = Button(text='Электроёмкость. Единицы электроёмкости. Конденсатор', size_hint=(None, None),
                                size=(400, 40))
        tab10_button97.text_size = tab10_button97.size
        tab10_button97.halign = 'center'
        tab10_button97.valign = 'middle'
        self.tab10_layout.add_widget(tab10_button97)
        tab10_button97.bind(on_press=self.on_button_click)
        tab10_button98 = Button(text='Энергия заряженного конденсатора.Применение конденсаторов', size_hint=(None, None), size=(400, 40))
        tab10_button98.text_size = tab10_button98.size
        tab10_button98.halign = 'center'
        tab10_button98.valign = 'middle'
        self.tab10_layout.add_widget(tab10_button98)
        tab10_button98.bind(on_press=self.on_button_click)
        tab10_button100 = Button(text='Электрический ток. Сила тока', size_hint=(None, None), size=(400, 40))
        self.tab10_layout.add_widget(tab10_button100)
        tab10_button100.bind(on_press=self.on_button_click)
        tab10_button105 = Button(text='Электродвижущая сила', size_hint=(None, None), size=(400, 40))
        self.tab10_layout.add_widget(tab10_button105)
        tab10_button105.bind(on_press=self.on_button_click)
        tab10_button106 = Button(text='Закон Ома для полной цепи', size_hint=(None, None), size=(400, 40))
        self.tab10_layout.add_widget(tab10_button106)
        tab10_button106.bind(on_press=self.on_button_click)
        tab10_button108 = Button(text='Электрическая проводимость различных веществ. Электроннаяпроводимость мателлов',
                                 size_hint=(None, None), size=(400, 40))
        tab10_button108.text_size = tab10_button108.size
        tab10_button108.halign = 'center'
        tab10_button108.valign = 'middle'
        self.tab10_layout.add_widget(tab10_button108)
        tab10_button108.bind(on_press=self.on_button_click)
        tab10_button109 = Button(text='Зависимость сопротивления проводника от температуры. Сверхпроводимость',
                                 size_hint=(None, None), size=(400, 40))
        tab10_button109.text_size = tab10_button109.size
        tab10_button109.halign = 'center'
        tab10_button109.valign = 'middle'
        self.tab10_layout.add_widget(tab10_button109)
        tab10_button109.bind(on_press=self.on_button_click)
        tab10_button110 = Button(
            text='Электрический ток в собственных проводниках. Собственная и примесная проводимости',
            size_hint=(None, None), size=(400, 40))
        tab10_button110.text_size = tab10_button110.size
        tab10_button110.halign = 'center'
        tab10_button110.valign = 'middle'
        self.tab10_layout.add_widget(tab10_button110)
        tab10_button110.bind(on_press=self.on_button_click)
        tab10_button111 = Button(
            text='Электрический ток через контакт полупроводников с разным типом проводимости. Транзисторы',
            size_hint=(None, None), size=(400, 40))
        tab10_button111.text_size = tab10_button111.size
        tab10_button111.halign = 'center'
        tab10_button111.valign = 'middle'
        self.tab10_layout.add_widget(tab10_button111)
        tab10_button111.bind(on_press=self.on_button_click)
        tab10_button112 = Button(text='Электрический ток в вакууме. Электронно-лучевая трубка', size_hint=(None, None),
                                 size=(400, 40))
        tab10_button112.text_size = tab10_button112.size
        tab10_button112.halign = 'center'
        tab10_button112.valign = 'middle'
        self.tab10_layout.add_widget(tab10_button112)
        tab10_button112.bind(on_press=self.on_button_click)
        tab10_button113 = Button(text='Электрический ток в жидкостях. Закон электролиза', size_hint=(None, None),
                                 size=(400, 40))
        tab10_button113.text_size = tab10_button113.size
        tab10_button113.halign = 'center'
        tab10_button113.valign = 'middle'
        self.tab10_layout.add_widget(tab10_button113)
        tab10_button113.bind(on_press=self.on_button_click)
        tab10_button114 = Button(text='Электрический ток в газах. Несамостоятельный и самостоятельный разряды',
                                 size_hint=(None, None), size=(400, 40))
        tab10_button114.text_size = tab10_button114.size
        tab10_button114.halign = 'center'
        tab10_button114.valign = 'middle'
        self.tab10_layout.add_widget(tab10_button114)
        tab10_button114.bind(on_press=self.on_button_click)
        tab10_button115 = Button(text='Плазма', size_hint=(None, None), size=(400, 40))
        self.tab10_layout.add_widget(tab10_button115)
        tab10_button115.bind(on_press=self.on_button_click)

        # tab11
        tab11_button1 = Button(text='Взаимодействие токов', size_hint=(None, None), size=(400, 40))
        self.tab11_layout.add_widget(tab11_button1)
        tab11_button1.bind(on_press=self.on_button_click)
        tab11_button2 = Button(text='Вектор магнитной индукции. Линии магнитной  ндукции', size_hint=(None, None),
                               size=(400, 40))
        tab11_button2.text_size = tab11_button2.size
        tab11_button2.halign = 'center'
        tab11_button2.valign = 'middle'
        self.tab11_layout.add_widget(tab11_button2)
        tab11_button2.bind(on_press=self.on_button_click)
        tab11_button3 = Button(text='Модуль вектора магнитной индукции. Сила Ампера', size_hint=(None, None),
                               size=(400, 40))
        tab11_button3.text_size = tab11_button3.size
        tab11_button3.halign = 'center'
        tab11_button3.valign = 'middle'
        self.tab11_layout.add_widget(tab11_button3)
        tab11_button3.bind(on_press=self.on_button_click)
        tab11_button5 = Button(text='Применение закона Ампера. Громкоговоритель', size_hint=(None, None),
                               size=(400, 40))
        tab11_button5.text_size = tab11_button5.size
        tab11_button5.halign = 'center'
        tab11_button5.valign = 'middle'
        self.tab11_layout.add_widget(tab11_button5)
        tab11_button5.bind(on_press=self.on_button_click)
        tab11_button6 = Button(text='Сила Лоренца', size_hint=(None, None), size=(400, 40))
        self.tab11_layout.add_widget(tab11_button6)
        tab11_button6.bind(on_press=self.on_button_click)
        tab11_button7 = Button(text='Магнитные свойства вещества', size_hint=(None, None), size=(400, 40))
        self.tab11_layout.add_widget(tab11_button7)
        tab11_button7.bind(on_press=self.on_button_click)
        tab11_button10 = Button(text='Направление индукционного тока. Правило Ленца', size_hint=(None, None),
                                size=(400, 40))
        tab11_button10.text_size = tab11_button10.size
        tab11_button10.halign = 'center'
        tab11_button10.valign = 'middle'
        self.tab11_layout.add_widget(tab11_button10)
        tab11_button10.bind(on_press=self.on_button_click)
        tab11_button11 = Button(text='Закон электромагнитной индукции', size_hint=(None, None), size=(400, 40))
        self.tab11_layout.add_widget(tab11_button11)
        tab11_button11.bind(on_press=self.on_button_click)
        tab11_button12 = Button(text='Вихревое электрическое поле', size_hint=(None, None), size=(400, 40))
        self.tab11_layout.add_widget(tab11_button12)
        tab11_button12.bind(on_press=self.on_button_click)
        tab11_button13 = Button(text='ЭДМ индукциив движущихся проводниках', size_hint=(None, None), size=(400, 40))
        tab11_button13.text_size = tab11_button13.size
        tab11_button13.halign = 'center'
        tab11_button13.valign = 'middle'
        self.tab11_layout.add_widget(tab11_button13)
        tab11_button13.bind(on_press=self.on_button_click)
        tab11_button14 = Button(text='Электродинамический микрофон', size_hint=(None, None), size=(400, 40))
        self.tab11_layout.add_widget(tab11_button14)
        tab11_button14.bind(on_press=self.on_button_click)
        tab11_button15 = Button(text='Самоиндукция. Индуктивность', size_hint=(None, None), size=(400, 40))
        self.tab11_layout.add_widget(tab11_button15)
        tab11_button15.bind(on_press=self.on_button_click)
        tab11_button16 = Button(text='Энергия магнитногополя тока', size_hint=(None, None), size=(400, 40))
        self.tab11_layout.add_widget(tab11_button16)
        tab11_button16.bind(on_press=self.on_button_click)
        tab11_button17 = Button(text='Электромагнитное поле', size_hint=(None, None), size=(400, 40))
        self.tab11_layout.add_widget(tab11_button17)
        tab11_button17.bind(on_press=self.on_button_click)
        tab11_button18 = Button(text='Свободные и вынужденные колебания', size_hint=(None, None), size=(400, 40))
        tab11_button18.text_size = tab11_button18.size
        tab11_button18.halign = 'center'
        tab11_button18.valign = 'middle'
        self.tab11_layout.add_widget(tab11_button18)
        tab11_button18.bind(on_press=self.on_button_click)
        tab11_button20 = Button(text='Математический маятник', size_hint=(None, None), size=(400, 40))
        self.tab11_layout.add_widget(tab11_button20)
        tab11_button20.bind(on_press=self.on_button_click)
        tab11_button21 = Button(text='Динамика колебательного движения', size_hint=(None, None), size=(400, 40))
        self.tab11_layout.add_widget(tab11_button21)
        tab11_button21.bind(on_press=self.on_button_click)
        tab11_button22 = Button(text='Гармонические колебания', size_hint=(None, None), size=(400, 40))
        self.tab11_layout.add_widget(tab11_button22)
        tab11_button22.bind(on_press=self.on_button_click)
        tab11_button24 = Button(text='Свободные и вынужденные колебания', size_hint=(None, None), size=(400, 40))
        tab11_button24.text_size = tab11_button24.size
        tab11_button24.halign = 'center'
        tab11_button24.valign = 'middle'
        self.tab11_layout.add_widget(tab11_button24)
        tab11_button24.bind(on_press=self.on_button_click)
        tab11_button25 = Button(text='Вынужденные колебания. Резонанс', size_hint=(None, None), size=(400, 40))
        self.tab11_layout.add_widget(tab11_button25)
        tab11_button25.bind(on_press=self.on_button_click)
        tab11_button27 = Button(text='Свободные и вынужденные электромагнитные колебания', size_hint=(None, None),
                                size=(400, 40))
        tab11_button27.text_size = tab11_button27.size
        tab11_button27.halign = 'center'
        tab11_button27.valign = 'middle'
        self.tab11_layout.add_widget(tab11_button27)
        tab11_button27.bind(on_press=self.on_button_click)
        tab11_button29 = Button(text='Аналогия между механическими и электромагнитными колебаниями',
                                size_hint=(None, None), size=(400, 40))
        tab11_button29.text_size = tab11_button29.size
        tab11_button29.halign = 'center'
        tab11_button29.valign = 'middle'
        self.tab11_layout.add_widget(tab11_button29)
        tab11_button29.bind(on_press=self.on_button_click)
        tab11_button30 = Button(
            text='Уравнение,описывающее процессы в колебательном контуре. Период свободных электрических колебаний',
            size_hint=(None, None), size=(400, 40))
        tab11_button30.text_size = tab11_button30.size
        tab11_button30.halign = 'center'
        tab11_button30.valign = 'middle'
        self.tab11_layout.add_widget(tab11_button30)
        tab11_button30.bind(on_press=self.on_button_click)
        tab11_button31 = Button(text='Переменный электрический ток', size_hint=(None, None), size=(400, 40))
        self.tab11_layout.add_widget(tab11_button31)
        tab11_button31.bind(on_press=self.on_button_click)
        tab11_button32 = Button(text='Активное сопротивление. Действующие значения силы тока и напряжения',
                                size_hint=(None, None), size=(400, 40))
        tab11_button32.text_size = tab11_button32.size
        tab11_button32.halign = 'center'
        tab11_button32.valign = 'middle'
        self.tab11_layout.add_widget(tab11_button32)
        tab11_button32.bind(on_press=self.on_button_click)
        tab11_button33 = Button(text='Конденсатор в цепи переменного тока', size_hint=(None, None), size=(400, 40))
        tab11_button33.text_size = tab11_button33.size
        tab11_button33.halign = 'center'
        tab11_button33.valign = 'middle'
        self.tab11_layout.add_widget(tab11_button33)
        tab11_button33.bind(on_press=self.on_button_click)
        tab11_button34 = Button(text='Катушка индуктивности в цепи переменного тока', size_hint=(None, None),
                                size=(400, 40))
        tab11_button34.text_size = tab11_button34.size
        tab11_button34.halign = 'center'
        tab11_button34.valign = 'middle'
        self.tab11_layout.add_widget(tab11_button34)
        tab11_button34.bind(on_press=self.on_button_click)
        tab11_button35 = Button(text='Резонанс в электрической цепи', size_hint=(None, None), size=(400, 40))
        tab11_button35.text_size = tab11_button35.size
        tab11_button35.halign = 'center'
        tab11_button35.valign = 'middle'
        self.tab11_layout.add_widget(tab11_button35)
        tab11_button35.bind(on_press=self.on_button_click)
        tab11_button36 = Button(text='Генератор на транзисторе. Автоколебания', size_hint=(None, None), size=(400, 40))
        tab11_button36.text_size = tab11_button36.size
        tab11_button36.halign = 'center'
        tab11_button36.valign = 'middle'
        self.tab11_layout.add_widget(tab11_button36)
        tab11_button36.bind(on_press=self.on_button_click)
        tab11_button38 = Button(text='Трансформаторы', size_hint=(None, None), size=(400, 40))
        self.tab11_layout.add_widget(tab11_button38)
        tab11_button38.bind(on_press=self.on_button_click)
        tab11_button40 = Button(text='Передача электроэнергии', size_hint=(None, None), size=(400, 40))
        self.tab11_layout.add_widget(tab11_button40)
        tab11_button40.bind(on_press=self.on_button_click)
        tab11_button42 = Button(text='Волновые явления', size_hint=(None, None), size=(400, 40))
        self.tab11_layout.add_widget(tab11_button42)
        tab11_button42.bind(on_press=self.on_button_click)
        tab11_button44 = Button(text='Длина волны. Скорость волны', size_hint=(None, None), size=(400, 40))
        self.tab11_layout.add_widget(tab11_button44)
        tab11_button44.bind(on_press=self.on_button_click)
        tab11_button45 = Button(text='Уравнение гармонической бегущей волны', size_hint=(None, None), size=(400, 40))
        tab11_button45.text_size = tab11_button45.size
        tab11_button45.halign = 'center'
        tab11_button45.valign = 'middle'
        self.tab11_layout.add_widget(tab11_button45)
        tab11_button45.bind(on_press=self.on_button_click)
        tab11_button46 = Button(text='Распространение волн в упругих средах', size_hint=(None, None), size=(400, 40))
        tab11_button46.text_size = tab11_button46.size
        tab11_button46.halign = 'center'
        tab11_button46.valign = 'middle'
        self.tab11_layout.add_widget(tab11_button46)
        tab11_button46.bind(on_press=self.on_button_click)
        tab11_button47 = Button(text='Звуковые волны', size_hint=(None, None), size=(400, 40))
        tab11_button47.text_size = tab11_button47.size
        tab11_button47.halign = 'center'
        tab11_button47.valign = 'middle'
        self.tab11_layout.add_widget(tab11_button47)
        tab11_button47.bind(on_press=self.on_button_click)
        tab11_button48 = Button(text='Что такое электромагнитная волна', size_hint=(None, None), size=(400, 40))
        tab11_button48.text_size = tab11_button48.size
        tab11_button48.halign = 'center'
        tab11_button48.valign = 'middle'
        self.tab11_layout.add_widget(tab11_button48)
        tab11_button48.bind(on_press=self.on_button_click)
        tab11_button50 = Button(text='Плотоность потокаэлектромагнитного излучения', size_hint=(None, None),
                                size=(400, 40))
        tab11_button50.text_size = tab11_button50.size
        tab11_button50.halign = 'center'
        tab11_button50.valign = 'middle'
        self.tab11_layout.add_widget(tab11_button50)
        tab11_button50.bind(on_press=self.on_button_click)
        tab11_button52 = Button(text='Принципы радиосвязи', size_hint=(None, None), size=(400, 40))
        self.tab11_layout.add_widget(tab11_button52)
        tab11_button52.bind(on_press=self.on_button_click)
        tab11_button53 = Button(text='Модуляция и детектирование', size_hint=(None, None), size=(400, 40))
        self.tab11_layout.add_widget(tab11_button53)
        tab11_button53.bind(on_press=self.on_button_click)
        tab11_button54 = Button(text='Свойства электромагнитных волн', size_hint=(None, None), size=(400, 40))
        self.tab11_layout.add_widget(tab11_button54)
        tab11_button54.bind(on_press=self.on_button_click)
        tab11_button55 = Button(text='Распространение радиоволн', size_hint=(None, None), size=(400, 40))
        self.tab11_layout.add_widget(tab11_button55)
        tab11_button55.bind(on_press=self.on_button_click)
        tab11_button56 = Button(text='Радиолокация', size_hint=(None, None), size=(400, 40))
        self.tab11_layout.add_widget(tab11_button56)
        tab11_button56.bind(on_press=self.on_button_click)
        tab11_button57 = Button(text='Понятие о телевидении', size_hint=(None, None), size=(400, 40))
        self.tab11_layout.add_widget(tab11_button57)
        tab11_button57.bind(on_press=self.on_button_click)
        tab11_button59 = Button(text='Оптика', size_hint=(None, None), size=(400, 40))
        self.tab11_layout.add_widget(tab11_button59)
        tab11_button59.bind(on_press=self.on_button_click)
        tab11_button60 = Button(text='Принцип Гюйгенса. Закон отражения света', size_hint=(None, None), size=(400, 40))
        tab11_button60.text_size = tab11_button60.size
        tab11_button60.halign = 'center'
        tab11_button60.valign = 'middle'
        self.tab11_layout.add_widget(tab11_button60)
        tab11_button60.bind(on_press=self.on_button_click)
        tab11_button61 = Button(text='Закон преломления света', size_hint=(None, None), size=(400, 40))
        tab11_button61.text_size = tab11_button61.size
        tab11_button61.halign = 'center'
        tab11_button61.valign = 'middle'
        self.tab11_layout.add_widget(tab11_button61)
        tab11_button61.bind(on_press=self.on_button_click)
        tab11_button62 = Button(text='Полное отражение', size_hint=(None, None), size=(400, 40))
        tab11_button62.text_size = tab11_button62.size
        tab11_button62.halign = 'center'
        tab11_button62.valign = 'middle'
        self.tab11_layout.add_widget(tab11_button62)
        tab11_button62.bind(on_press=self.on_button_click)
        tab11_button66 = Button(text='Дисперсия света', size_hint=(None, None), size=(400, 40))
        self.tab11_layout.add_widget(tab11_button66)
        tab11_button66.bind(on_press=self.on_button_click)
        tab11_button67 = Button(text='Интерференция механический волн', size_hint=(None, None), size=(400, 40))
        self.tab11_layout.add_widget(tab11_button67)
        tab11_button67.bind(on_press=self.on_button_click)
        tab11_button68 = Button(text='Интерференция света', size_hint=(None, None), size=(400, 40))
        self.tab11_layout.add_widget(tab11_button68)
        tab11_button68.bind(on_press=self.on_button_click)
        tab11_button70 = Button(text='Дифракция механических волн', size_hint=(None, None), size=(400, 40))
        self.tab11_layout.add_widget(tab11_button70)
        tab11_button70.bind(on_press=self.on_button_click)
        tab11_button71 = Button(text='Дифракция света', size_hint=(None, None), size=(400, 40))
        self.tab11_layout.add_widget(tab11_button71)
        tab11_button71.bind(on_press=self.on_button_click)
        tab11_button73 = Button(text='Поперечность световых волн', size_hint=(None, None), size=(400, 40))
        tab11_button73.text_size = tab11_button73.size
        tab11_button73.halign = 'center'
        tab11_button73.valign = 'middle'
        self.tab11_layout.add_widget(tab11_button73)
        tab11_button73.bind(on_press=self.on_button_click)
        tab11_button75 = Button(text='Законы электродинамики и принцип относительности', size_hint=(None, None),
                                size=(400, 40))
        tab11_button75.text_size = tab11_button75.size
        tab11_button75.halign = 'center'
        tab11_button75.valign = 'middle'
        self.tab11_layout.add_widget(tab11_button75)
        tab11_button75.bind(on_press=self.on_button_click)
        tab11_button77 = Button(text='Относительность одновременности', size_hint=(None, None), size=(400, 40))
        self.tab11_layout.add_widget(tab11_button77)
        tab11_button77.bind(on_press=self.on_button_click)
        tab11_button79 = Button(text='Элементы релятивистской динамики', size_hint=(None, None), size=(400, 40))
        self.tab11_layout.add_widget(tab11_button79)
        tab11_button79.bind(on_press=self.on_button_click)
        tab11_button80 = Button(text='Виды излучений. Источники света', size_hint=(None, None), size=(400, 40))
        self.tab11_layout.add_widget(tab11_button80)
        tab11_button80.bind(on_press=self.on_button_click)
        tab11_button81 = Button(text='Спектры и спектральные аппараты', size_hint=(None, None), size=(400, 40))
        self.tab11_layout.add_widget(tab11_button81)
        tab11_button81.bind(on_press=self.on_button_click)
        tab11_button82 = Button(text='Виды спектров', size_hint=(None, None), size=(400, 40))
        self.tab11_layout.add_widget(tab11_button82)
        tab11_button82.bind(on_press=self.on_button_click)
        tab11_button83 = Button(text='Спектральный анализ', size_hint=(None, None), size=(400, 40))
        self.tab11_layout.add_widget(tab11_button83)
        tab11_button83.bind(on_press=self.on_button_click)
        tab11_button84 = Button(text='Инфракрасное и ультрафиолетовое излучение', size_hint=(None, None),
                                size=(400, 40))
        tab11_button84.text_size = tab11_button84.size
        tab11_button84.halign = 'center'
        tab11_button84.valign = 'middle'
        self.tab11_layout.add_widget(tab11_button84)
        tab11_button85 = Button(text='Рентгеновские лучи', size_hint=(None, None), size=(400, 40))
        self.tab11_layout.add_widget(tab11_button85)
        tab11_button85.bind(on_press=self.on_button_click)
        tab11_button86 = Button(text='Шкала электромагнитных волн', size_hint=(None, None), size=(400, 40))
        self.tab11_layout.add_widget(tab11_button86)
        tab11_button86.bind(on_press=self.on_button_click)
        tab11_button871 = Button(text='Квантовая физика', size_hint=(None, None), size=(400, 40))
        self.tab11_layout.add_widget(tab11_button871)
        tab11_button871.bind(on_press=self.on_button_click)
        tab11_button87 = Button(text='Фотоэффект', size_hint=(None, None), size=(400, 40))
        self.tab11_layout.add_widget(tab11_button87)
        tab11_button87.bind(on_press=self.on_button_click)
        tab11_button88 = Button(text='Теория фотоэффекта', size_hint=(None, None), size=(400, 40))
        self.tab11_layout.add_widget(tab11_button88)
        tab11_button88.bind(on_press=self.on_button_click)
        tab11_button89 = Button(text='Фотоны', size_hint=(None, None), size=(400, 40))
        self.tab11_layout.add_widget(tab11_button89)
        tab11_button89.bind(on_press=self.on_button_click)
        tab11_button91 = Button(text='Давление света', size_hint=(None, None), size=(400, 40))
        self.tab11_layout.add_widget(tab11_button91)
        tab11_button91.bind(on_press=self.on_button_click)
        tab11_button93 = Button(text='Строение атома. Опыты резерфорда', size_hint=(None, None), size=(400, 40))
        self.tab11_layout.add_widget(tab11_button93)
        tab11_button93.bind(on_press=self.on_button_click)
        tab11_button94 = Button(text='Квантовые постулаты Бора. Модель атома водорода по Бору', size_hint=(None, None),
                                size=(400, 40))
        tab11_button94.text_size = tab11_button94.size
        tab11_button94.halign = 'center'
        tab11_button94.valign = 'middle'
        self.tab11_layout.add_widget(tab11_button94)
        tab11_button94.bind(on_press=self.on_button_click)
        tab11_button96 = Button(text='Лазеры', size_hint=(None, None), size=(400, 40))
        self.tab11_layout.add_widget(tab11_button96)
        tab11_button96.bind(on_press=self.on_button_click)
        tab11_button97 = Button(text='Методы наблюдения и регистрации элементарных частиц', size_hint=(None, None),
                                size=(400, 40))
        tab11_button97.text_size = tab11_button97.size
        tab11_button97.halign = 'center'
        tab11_button97.valign = 'middle'
        self.tab11_layout.add_widget(tab11_button97)
        tab11_button97.bind(on_press=self.on_button_click)
        tab11_button98 = Button(text='Открытие радиоактивности', size_hint=(None, None), size=(400, 40))
        self.tab11_layout.add_widget(tab11_button98)
        tab11_button98.bind(on_press=self.on_button_click)
        tab11_button99 = Button(text='Альфа-, Бета- и Гамма-излучения', size_hint=(None, None), size=(400, 40))
        self.tab11_layout.add_widget(tab11_button99)
        tab11_button99.bind(on_press=self.on_button_click)
        tab11_button100 = Button(text='Радиоактивные превращения', size_hint=(None, None), size=(400, 40))
        self.tab11_layout.add_widget(tab11_button100)
        tab11_button100.bind(on_press=self.on_button_click)
        tab11_button101 = Button(text='Закон радиоактивного распада. Период полураспада', size_hint=(None, None),
                                 size=(400, 40))
        tab11_button101.text_size = tab11_button101.size
        tab11_button101.halign = 'center'
        tab11_button101.valign = 'middle'
        self.tab11_layout.add_widget(tab11_button101)
        tab11_button101.bind(on_press=self.on_button_click)
        tab11_button102 = Button(text='Изотопы', size_hint=(None, None), size=(400, 40))
        self.tab11_layout.add_widget(tab11_button102)
        tab11_button102.bind(on_press=self.on_button_click)
        tab11_button103 = Button(text='Открытие нейрона', size_hint=(None, None), size=(400, 40))
        self.tab11_layout.add_widget(tab11_button103)
        tab11_button103.bind(on_press=self.on_button_click)
        tab11_button104 = Button(text='Строение атомного ядра. Ядерные силы', size_hint=(None, None), size=(400, 40))
        tab11_button104.text_size = tab11_button104.size
        tab11_button104.halign = 'center'
        tab11_button104.valign = 'middle'
        self.tab11_layout.add_widget(tab11_button104)
        tab11_button104.bind(on_press=self.on_button_click)
        tab11_button105 = Button(text='Энергия связи атомных ядер', size_hint=(None, None), size=(400, 40))
        self.tab11_layout.add_widget(tab11_button105)
        tab11_button105.bind(on_press=self.on_button_click)
        tab11_button106 = Button(text='Ядерные реакции', size_hint=(None, None), size=(400, 40))
        self.tab11_layout.add_widget(tab11_button106)
        tab11_button106.bind(on_press=self.on_button_click)
        tab11_button107 = Button(text='Деление ядер урана', size_hint=(None, None), size=(400, 40))
        self.tab11_layout.add_widget(tab11_button107)
        tab11_button107.bind(on_press=self.on_button_click)
        tab11_button108 = Button(text='Цепные ядерные реакции', size_hint=(None, None), size=(400, 40))
        self.tab11_layout.add_widget(tab11_button108)
        tab11_button108.bind(on_press=self.on_button_click)
        tab11_button109 = Button(text='Ядерный реактор', size_hint=(None, None), size=(400, 40))
        self.tab11_layout.add_widget(tab11_button109)
        tab11_button109.bind(on_press=self.on_button_click)
        tab11_button110 = Button(text='Термоядерные реакции', size_hint=(None, None), size=(400, 40))
        self.tab11_layout.add_widget(tab11_button110)
        tab11_button110.bind(on_press=self.on_button_click)
        tab11_button111 = Button(text='Применение ядерной энергии', size_hint=(None, None), size=(400, 40))
        self.tab11_layout.add_widget(tab11_button111)
        tab11_button111.bind(on_press=self.on_button_click)
        tab11_button112 = Button(text='Получение радиоактивных изотопов и их применение', size_hint=(None, None),
                                 size=(400, 40))
        tab11_button112.text_size = tab11_button112.size
        tab11_button112.halign = 'center'
        tab11_button112.valign = 'middle'
        self.tab11_layout.add_widget(tab11_button112)
        tab11_button112.bind(on_press=self.on_button_click)
        tab11_button113 = Button(text='Биологическое действие радиоактивных излучений', size_hint=(None, None), size=(400, 40))
        tab11_button113.text_size = tab11_button113.size
        tab11_button113.halign = 'center'
        tab11_button113.valign = 'middle'
        self.tab11_layout.add_widget(tab11_button113)
        tab11_button113.bind(on_press=self.on_button_click)
        tab11_button114 = Button(text='Три этапа в развитии физики элементарных частиц', size_hint=(None, None), size=(400, 40))
        tab11_button114.text_size = tab11_button114.size
        tab11_button114.halign = 'center'
        tab11_button114.valign = 'middle'
        self.tab11_layout.add_widget(tab11_button114)
        tab11_button114.bind(on_press=self.on_button_click)
        tab11_button115 = Button(text='Открытие позитрона. Античастицы', size_hint=(None, None), size=(400, 40))
        self.tab11_layout.add_widget(tab11_button115)
        tab11_button115.bind(on_press=self.on_button_click)
        tab11_button116 = Button(text='Видимые движения небесных тел', size_hint=(None, None), size=(400, 40))
        self.tab11_layout.add_widget(tab11_button116)
        tab11_button116.bind(on_press=self.on_button_click)
        tab11_button117 = Button(text='Законы движения планет', size_hint=(None, None), size=(400, 40))
        self.tab11_layout.add_widget(tab11_button117)
        tab11_button117.bind(on_press=self.on_button_click)
        tab11_button118 = Button(text='Система Земля-Луна', size_hint=(None, None), size=(400, 40))
        self.tab11_layout.add_widget(tab11_button118)
        tab11_button118.bind(on_press=self.on_button_click)
        tab11_button119 = Button(text='Физическая природа планет и малых тел солнечной системы', size_hint=(None, None),
                                 size=(400, 40))
        tab11_button119.text_size = tab11_button119.size
        tab11_button119.halign = 'center'
        tab11_button119.valign = 'middle'
        self.tab11_layout.add_widget(tab11_button119)
        tab11_button119.bind(on_press=self.on_button_click)
        tab11_button120 = Button(text='Солнце', size_hint=(None, None), size=(400, 40))
        self.tab11_layout.add_widget(tab11_button120)
        tab11_button120.bind(on_press=self.on_button_click)
        tab11_button121 = Button(text='Основные характеристики звезд', size_hint=(None, None), size=(400, 40))
        self.tab11_layout.add_widget(tab11_button121)
        tab11_button121.bind(on_press=self.on_button_click)
        tab11_button122 = Button(text='Внутренее строение солнца и звезд главной последовательности',
                                 size_hint=(None, None), size=(400, 40))
        tab11_button122.text_size = tab11_button122.size
        tab11_button122.halign = 'center'
        tab11_button122.valign = 'middle'
        self.tab11_layout.add_widget(tab11_button122)
        tab11_button122.bind(on_press=self.on_button_click)
        tab11_button123 = Button(text='Внутренее строение солнца и звезд главной последовательности',
                                 size_hint=(None, None), size=(400, 40))
        tab11_button123.text_size = tab11_button123.size
        tab11_button123.halign = 'center'
        tab11_button123.valign = 'middle'
        self.tab11_layout.add_widget(tab11_button123)
        tab11_button123.bind(on_press=self.on_button_click)
        tab11_button124 = Button(text='Млечный путь  наша Галактика', size_hint=(None, None), size=(400, 40))
        self.tab11_layout.add_widget(tab11_button124)
        tab11_button124.bind(on_press=self.on_button_click)
        tab11_button125 = Button(text='Галактики', size_hint=(None, None), size=(400, 40))
        self.tab11_layout.add_widget(tab11_button125)
        tab11_button125.bind(on_press=self.on_button_click)
        tab11_button126 = Button(text='Строение и эволюция Вселенной', size_hint=(None, None), size=(400, 40))
        self.tab11_layout.add_widget(tab11_button126)
        tab11_button126.bind(on_press=self.on_button_click)
        tab11_button127 = Button(text='Единая физическая картина мира', size_hint=(None, None), size=(400, 40))
        self.tab11_layout.add_widget(tab11_button127)
        tab11_button127.bind(on_press=self.on_button_click)

        """ END OF CREATING BUTTONS """
        """ ----------------------------------------------------------- """
        self.button_names7 = []
        self.button_names8 = []
        self.button_names9 = []
        self.button_names10 = []
        self.button_names11 = []

        # Make the grid layout scrollable
        tab7_scroll = MyScrollView()
        tab7_scroll.add_widget(self.tab7_layout)
        tab7_scroll.bind(scroll_pos=tab7_scroll.on_scroll_pos)
        tab7.add_widget(tab7_scroll)
        tab8_scroll = MyScrollView()
        tab8_scroll.add_widget(self.tab8_layout)
        tab8.add_widget(tab8_scroll)
        tab9_scroll = MyScrollView()
        tab9_scroll.add_widget(self.tab9_layout)
        tab9.add_widget(tab9_scroll)
        tab10_scroll = MyScrollView()
        tab10_scroll.add_widget(self.tab10_layout)
        tab10.add_widget(tab10_scroll)
        tab11_scroll = MyScrollView()
        tab11_scroll.add_widget(self.tab11_layout)
        tab11.add_widget(tab11_scroll)

        # Adding creator's information
        information_label = Label(text='Creator - "Матвей Сергеев" \n email: matveysergeev15@gmail.com')
        creators_info.add_widget(information_label)

        # Add tab items to the tabbed panel
        self.add_widget(tab7)
        self.add_widget(tab8)
        self.add_widget(tab9)
        self.add_widget(tab10)
        self.add_widget(tab11)
        self.add_widget(creators_info)

        # Add all button names to list
        self.button_names_all = [but.text for tabs in self.tab_list
                                 if isinstance(tabs, TabbedPanelItem)
                                 for item in tabs.content.children
                                 for but in item.children
                                 if isinstance(but, Button)]

        # Get all buttons from each tab layout
        self.tab7_buttons = list(reversed([but for but in self.tab7_layout.children if isinstance(but, Button)]))
        self.tab8_buttons = list(reversed([but for but in self.tab8_layout.children if isinstance(but, Button)]))
        self.tab9_buttons = list(reversed([but for but in self.tab9_layout.children if isinstance(but, Button)]))
        self.tab10_buttons = list(reversed([but for but in self.tab10_layout.children if isinstance(but, Button)]))
        self.tab11_buttons = list(reversed([but for but in self.tab11_layout.children if isinstance(but, Button)]))

        # Set default tab
        self.default_tab = self.tab_list[-2]

        # Change screen background color
        self.background_color = get_color_from_hex("#0077ff")

    @staticmethod
    def on_button_click(instance):
        """
        Define action on buttons click
        :param instance: Button instance
        :return:
        """
        popup = popup_button_action(instance.text)
        popup.open()

    def update_search_results(self, instance, text):
        """
        Update button names with users input in
        :param instance:
        :param text: Text of users input
        :return:
        """

        # Clear all tabs
        self.tab7_layout.clear_widgets()
        self.tab8_layout.clear_widgets()
        self.tab9_layout.clear_widgets()
        self.tab10_layout.clear_widgets()
        self.tab11_layout.clear_widgets()

        # Add input boxes to all tabs
        self.tab7_layout.add_widget(self.input_box_tab7)
        self.tab8_layout.add_widget(self.input_box_tab8)
        self.tab9_layout.add_widget(self.input_box_tab9)
        self.tab10_layout.add_widget(self.input_box_tab10)
        self.tab11_layout.add_widget(self.input_box_tab11)

        # Remove all previous added buttons in names
        self.button_names7 = []
        self.button_names8 = []
        self.button_names9 = []
        self.button_names10 = []
        self.button_names11 = []

        # Set default text for all input box
        self.text = text
        self.input_box_tab7.text = self.text
        self.input_box_tab8.text = self.text
        self.input_box_tab9.text = self.text
        self.input_box_tab10.text = self.text
        self.input_box_tab11.text = self.text

        if text:  # if user input some text
            # Get only appropriate button names within each tab for users input text
            results_7 = [button_name.text for button_name in self.tab7_buttons if text.lower() in button_name.text.lower()]
            results_7 = list(set(sorted(results_7)))
            results_8 = [button_name.text for button_name in self.tab8_buttons if text.lower() in button_name.text.lower()]
            results_8 = list(set(sorted(results_8)))
            results_9 = [button_name.text for button_name in self.tab9_buttons if text.lower() in button_name.text.lower()]
            results_9 = list(set(sorted(results_9)))
            results_10 = [button_name.text for button_name in self.tab10_buttons if text.lower() in button_name.text.lower()]
            results_10 = list(set(sorted(results_10)))
            results_11 = [button_name.text for button_name in self.tab11_buttons if text.lower() in button_name.text.lower()]
            results_11 = list(set(sorted(results_11)))

            # Add all fit buttons to each tab
            [self.button_names7.append(Button(text=result, size_hint=(None, None), size=(400, 40))) for result in
             results_7]
            [self.button_names8.append(Button(text=result, size_hint=(None, None), size=(400, 40))) for result in
             results_8]
            [self.button_names9.append(Button(text=result, size_hint=(None, None), size=(400, 40))) for result in
             results_9]
            [self.button_names10.append(Button(text=result, size_hint=(None, None), size=(400, 40))) for result in
             results_10]
            [self.button_names11.append(Button(text=result, size_hint=(None, None), size=(400, 40))) for result in
             results_11]

            # Align text in buttons and set action on click
            for btn in self.button_names7:
                btn.text_size = btn.size
                btn.halign = 'center'
                btn.valign = 'middle'
                btn.bind(on_press=self.on_button_click)
            for btn in self.button_names8:
                btn.text_size = btn.size
                btn.halign = 'center'
                btn.valign = 'middle'
                btn.bind(on_press=self.on_button_click)
            for btn in self.button_names9:
                btn.text_size = btn.size
                btn.halign = 'center'
                btn.valign = 'middle'
                btn.bind(on_press=self.on_button_click)
            for btn in self.button_names10:
                btn.text_size = btn.size
                btn.halign = 'center'
                btn.valign = 'middle'
                btn.bind(on_press=self.on_button_click)
            for btn in self.button_names11:
                btn.text_size = btn.size
                btn.halign = 'center'
                btn.valign = 'middle'
                btn.bind(on_press=self.on_button_click)

            # Add all suitable button
            try:
                [self.tab7_layout.add_widget(button_name) for button_name in self.button_names7]
                [self.tab8_layout.add_widget(button_name) for button_name in self.button_names8]
                [self.tab9_layout.add_widget(button_name) for button_name in self.button_names9]
                [self.tab10_layout.add_widget(button_name) for button_name in self.button_names10]
                [self.tab11_layout.add_widget(button_name) for button_name in self.button_names11]
            except WidgetException:
                pass
        else:  # if there is not text in input boxes
            # Add again previous deleted buttons for all tabs
            try:
                [self.tab7_layout.add_widget(button) for button in self.tab7_buttons if isinstance(button, Button)]
                [self.tab8_layout.add_widget(button) for button in self.tab8_buttons if isinstance(button, Button)]
                [self.tab9_layout.add_widget(button) for button in self.tab9_buttons if isinstance(button, Button)]
                [self.tab10_layout.add_widget(button) for button in self.tab10_buttons if isinstance(button, Button)]
                [self.tab11_layout.add_widget(button) for button in self.tab11_buttons if isinstance(button, Button)]
            except WidgetException:
                pass


class popup_button_action(Popup):
    """ Create popup with appropriate text for each button """

    def __init__(self, button_name):
        super(popup_button_action, self).__init__()
        # Read text in file
        path_file = self.find_docx_in_folders('./Text files', f'{button_name}.docx')
        if path_file:
            doc = docx.Document(path_file)
            text_in_file = '\n'.join([paragraph.text for paragraph in doc.paragraphs])
        else:
            text_in_file = ''
        LabelBase.register(DEFAULT_FONT, './fonts/STIXGeneral.ttf')

        # Init popup window settings
        self.title = button_name
        self.size_hint = (1, 1)
        self.size = (400, 600)
        self.auto_dismiss = False

        # Create a scrollable label
        scroll_view = ScrollView()
        label_box = BoxLayout(orientation='vertical', size_hint_y=None)
        label_box.bind(minimum_height=label_box.setter('height'))
        label = Label(text=text_in_file, font_size=18, size_hint_y=None, text_size=(350, None))
        label.bind(texture_size=label.setter('size'))
        label_box.add_widget(label)
        scroll_view.add_widget(label_box)

        # Add a close button
        close_button = Button(text='Выйти', size_hint=(1, None), height=50)
        close_button.bind(on_press=self.dismiss)
        self.content = BoxLayout(orientation='vertical')
        self.content.add_widget(scroll_view)
        self.content.add_widget(close_button)

    @staticmethod
    def find_docx_in_folders(root_folder, docx_name):
        """
        Parse root directory('Text files') and find .docx document with given name in any folder inside root
        :param root_folder: Root folder - ./Text files
        :param docx_name: .docx document name - name of the clicked button
        :return:
        """
        for subdir, dirs, files in os.walk(root_folder):
            for file in files:
                if file.endswith('.docx') and file == docx_name:
                    return os.path.join(subdir, file)
        return None


class Fizikavezde(App):
    """ Define main window settings """

    def build(self):
        Window.size = (400, 600)
        self.title = 'Физика везде'
        Window.set_icon('./icons/app_icon.png')
        return MyTabbedPanel()


# Running application
if __name__ == '__main__':
    Fizikavezde().run()
