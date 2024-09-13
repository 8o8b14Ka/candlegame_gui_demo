# Этот файл публично доступен. Модифицируйте его под свои сообственные экраны.
##################################################
# Cursor position
# для тестовых нужд. показывает кординаты курсора
##################################################
init -1 python:
    cur_x = 0
    cur_y = 0
    cursor = "just loaded"
    def get_cur_pos():
        global cur_x, cur_y
        cur_x, cur_y = renpy.get_mouse_pos()

screen cursor:
    timer 0.1 repeat True action [get_cur_pos(),SetVariable("cursor" ,"%i"%cur_x+" : "+ "%i"%cur_y)]
    text cursor

image ic_load = "interface/icons/load.png"
image ic_mainmenu = "interface/icons/mainmenu.png"
image ic_no = "interface/icons/no.png"
image ic_options = "interface/icons/options.png"
image ic_overwrite = "interface/icons/overwrite.png"
image ic_quit = "interface/icons/quit.png"
image ic_return = "interface/icons/return.png"
image ic_save = "interface/icons/save.png"
image ic_to_mainmenu = "interface/icons/to_mainmenu.png"
image ic_yes = "interface/icons/yes.png"

image ic_mainmenu_hov:
    "interface/icons/mainmenu.png"
    zoom 1
    ease .5 zoom 1.3
    ease .5 zoom 1
    repeat

image ic_no_hov:
    "interface/icons/no.png"
    zoom 1
    ease .5 zoom 1.3
    ease .5 zoom 1
    repeat

image ic_options_hov:
    "interface/icons/options.png"
    zoom 1
    ease .5 zoom 1.3
    ease .5 zoom 1
    repeat

image ic_save_hov:
    "interface/icons/save.png"
    zoom 1
    ease .5 zoom 1.3
    ease .5 zoom 1
    repeat

image ic_yes_hov:
    "interface/icons/yes.png"
    zoom 1
    ease .5 zoom 1.3
    ease .5 zoom 1
    repeat

image ic_return_hov:
    "interface/icons/return.png"
    zoom 1
    ease .5 zoom 1.3
    ease .5 zoom 1
    repeat

init -1 python:
    cls = False
    ccls = False
    def clrscr():
        global cls
        cls = True
        renpy.say("","")
        cls = False
        return None

image say_cls = "interface/say_cls.png"
image say_cls_hov = "interface/say_cls_hov.png"
image say_save = "interface/say_save.png"
image say_save_hov = "interface/say_save_hov.png"
image say_options = "interface/say_options.png"
image say_options_hov = "interface/say_options_hov.png"
##############################################################################
# Say
#
# Экран отображения ADV-диалога.
# http://www.renpy.org/doc/html/screen_special.html#say
screen say:

    # Умолчания для side_image и two_window
    default side_image = None
    default two_window = False

    # Решаем, нужен ли нам двухоконный или однооконный вариант.
    if not two_window:

        # Вариант с одним окном.
        #timer 0.1 repeat True action SetVariable("ccls",cls)
        add "interface/say2.png"
        imagebutton focus_mask True idle "say_cls" hover "say_cls_hov"  action Hide("say")
        imagebutton focus_mask True idle "say_options" hover "say_options_hov"  action ShowMenu("preferences")
        imagebutton focus_mask True idle "say_save" hover "say_save_hov"  action ShowMenu("save")
            
        window:
            id "window"

            has vbox:
                style "say_vbox"

            if who:
                text who id "who"

            text what id "what"

    else:

        # Вариант с двумя окнами.
        vbox:
            style "say_two_window_vbox"

            if who:
                window:
                    style "say_who_window"

                    text who:
                        id "who"

            window:
                id "window"

                has vbox:
                    style "say_vbox"

                text what id "what"

    # Если есть изображение, отобразить его над текстом.
    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0

    # Использовать быстрое меню.
    #use quick_menu



##############################################################################
# Choice
#
# Экран для отображения внутриигровых меню.
# http://www.renpy.org/doc/html/screen_special.html#choice

screen choice:

    window:
        style "menu_window"
        xalign 0.5
        yalign 0.5
        vbox:
            style "menu"
            xalign 0.5
            yalign 0.5
            
            spacing 4
            for caption, action, chosen in items:

                if action:

                    button:
                        action action
                        style "menu_choice_button"

                        text caption style "menu_choice"
                else:
                    text caption style "menu_caption"

init -2 python:
    config.narrator_menu = True

    style.menu_window.set_parent(style.default)
    style.menu_choice.set_parent(style.button_text)
    style.menu_choice.clear()
    style.menu_choice_button.set_parent(style.button)
    style.menu_choice_button.xminimum = 1920
    style.menu_choice_button.xmaximum = 1920
    

##############################################################################
# Input
#
# Экран для отображения renpy.input()
# http://www.renpy.org/doc/html/screen_special.html#input

screen input:

    window style "input_window":
        has vbox

        text prompt style "input_prompt"
        input id "input" style "input_text"

    use quick_menu

##############################################################################
# Nvl
#
# Экран для NVL-диалога и меню.
# http://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl:

    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"

        # Отображать диалог.
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id

        # Отображать меню, если есть.
        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0

    use quick_menu

##############################################################################
# Main Menu
#
# Экран для отображения главного меню при запуске Ren'Py.
# http://www.renpy.org/doc/html/screen_special.html#main-menu

image background = Animation("interface/mainmenu2.jpg", 0.15,
                                                  "interface/mainmenu3.jpg", 0.15,
                                                  "interface/mainmenu4.jpg", 0.15,
                                                  "interface/mainmenu3.jpg", 0.15)


init python:

    class TrackCursor(renpy.Displayable):

        def __init__(self, child,child2):

            super(TrackCursor, self).__init__()

            self.child = renpy.displayable(child)
            self.child2 = renpy.displayable(child2)

            self.x = None
            self.y = None
            self.xx = 0
            self.yy = 0
            self.o = 1.0

        def render(self, width, height, st, at):

            rv = renpy.Render(width, height)

            if self.x is not None:
                cr = renpy.render(self.child, width, height, st, at)
                cw, ch = cr.get_size()

                t = Transform(child=self.child2, alpha=self.o)
                cr = renpy.render(t, width, height, st, at)
                rv.blit(cr, (self.xx - cw / 2, self.yy - ch / 2))
                if renpy.emscripten:
                    cr = renpy.render(self.child, width, height, st, at)
                    rv.blit(cr, (self.x - cw / 2, self.y - ch / 2))

            return rv

        def event(self, ev, x, y, st):

            if (x != self.x) or (y != self.y):
                self.x = x-20
                self.y = y+5
                renpy.redraw(self, 0)
                self.o-=0.03
            if self.o <= 0:
                self.o = 1.0
                self.xx = x-20
                self.yy = y+5
            renpy.timeout(0.1)

    renpy.image('cursor',Animation("cursors/fired1.png", 0.15,
                                                      "cursors/fired2.png", 0.15,
                                                      "cursors/fired1.png", 0.15,
                                                      "cursors/fired3.png", 0.15))

image line:
    "interface/line.jpg"
    align (.0,0.9)

image stafff:
    align (.0,0.9)
    Text("- - - You cleared the game!! - - - ")
    xanchor .0
    xpos 1.0
    ease 2 xalign .5
    pause 5
    ease 1 xpos -2000
    Text("- - - some credits there")
    xanchor .0
    xpos 1.0
    ease 2 xalign .5
    pause 5
    ease 1 xpos -2000
    Text("- - - some links there - - - ")
    xanchor .0
    xpos 1.0
    ease 2 xalign .5
    pause 5
    ease 1 xpos -2000
    Text("- - - thank you - - - ")
    xanchor .0
    xpos 1.0
    ease 2 xalign .5


screen main_menu:

    # Это заменяет другие меню.
    tag menu
    # Фон главного меню.
    window:
        style "mm_root"

    add "background"
    if persistent.gameclear:
        add "line"
        add "stafff"

    # Кнопки главного меню.
    imagebutton focus_mask True idle "interface/mainmenu_start_ground.png" hover "interface/mainmenu_start.png" action Start()
    imagebutton focus_mask True idle "interface/mainmenu_load_ground.png" hover "interface/mainmenu_load.png" action ShowMenu("load")
    imagebutton focus_mask True idle "interface/mainmenu_options_ground.png" hover "interface/mainmenu_options.png" action ShowMenu("preferences")
    imagebutton focus_mask True idle "interface/mainmenu_exit_ground.png" hover "interface/mainmenu_exit.png" action Quit(confirm=True)

#    frame:
#        style_group "mm"
#        xalign .98
#        yalign .98

#        has vbox

#        textbutton _("Начать игру") action Start()
#        textbutton _("Загрузить игру") action ShowMenu("load")
#        textbutton _("Настройки") action ShowMenu("preferences")
#        textbutton _("Справка") action Help()
#        textbutton _("Выход") action Quit(confirm=False)

    add TrackCursor('cursor','cursors/fired_shadow.png')

init -2 python:

    # Сделать все кнопки главного меню одноразмерными.
    style.mm_button.size_group = "mm"


##############################################################################
# Navigation
#
# Экран, включаемый в другие экраны для отображения навигации и фона.
# http://www.renpy.org/doc/html/screen_special.html#navigation
screen navigation:

    # Фон игрового меню.
#    window:
#        style "gm_root"

    # Кнопки.
    frame:
        style_group "gm_nav"
        xalign .98
        yalign .98

        has vbox

        textbutton _("Назад") action Return()
        textbutton _("Настройки") action ShowMenu("preferences")
        textbutton _("Сохранить игру") action ShowMenu("save")
        textbutton _("Загрузить игру") action ShowMenu("load")
        textbutton _("Главное меню") action MainMenu()
        textbutton _("Справка") action Help()
        textbutton _("Выход") action Quit()

init -2 python:
    style.gm_nav_button.size_group = "gm_nav"


##############################################################################
# Save, Load
#
# Экраны для сохранения и загрузки игры.
# http://www.renpy.org/doc/html/screen_special.html#save
# http://www.renpy.org/doc/html/screen_special.html#load

# Ибо сохранение и загрузка очень похожи, мы совмещаем их в один экран,
# file_picker. Потом мы используем его из экранов
# загрузки и сохранения.

image load_ground = "interface/load_ground.jpg" 
image load_names:
    "interface/load_names.png"
    alpha 0
    linear 1 alpha 1

image load_slots:
    "interface/load_slots.png"
    ypos -1000
    ease 1 ypos 0

image save_load:
    "interface/icons/save_load.png"
    align (1.0,0.0)
    
init -1 python:
    fp_timer = False
    load_c = 0
    save_c = 0

init python:
    def fs(x):
        global slot
        screenshot = renpy.slot_screenshot("1-"+str(x))
        slot = screenshot
        if screenshot is not None:
            return screenshot
        return "interface/270144.png"
    
    
screen file_picker:
    add "load_ground"
    add "load_names"
    add "load_slots"
    add "save_load"
    timer .00001 action SetVariable("fp_timer",False)
    timer 1 action SetVariable("fp_timer",True)
    timer 0.1 repeat True action If(load_c<>0,true=[SetVariable("load_c",0),FileLoad(load_c)],false=NullAction())
    timer 0.1 repeat True action If(save_c<>0,true=[SetVariable("save_c",0),FileSave(save_c)],false=NullAction())
    if fp_timer:
        #(515,140),(815,340),(1120,500), 720
        imagebutton idle im.Sepia(fs(1)) hover fs(1) pos (515,140) action SetVariable("save_c",1) alternate SetVariable("load_c",1) 
        imagebutton idle im.Sepia(fs(2)) hover fs(2) pos (815,140) action SetVariable("save_c",2) alternate SetVariable("load_c",2) 
        imagebutton idle im.Sepia(fs(3)) hover fs(3) pos (1120,140) action SetVariable("save_c",3) alternate SetVariable("load_c",3) 
        imagebutton idle im.Sepia(fs(4)) hover fs(4) pos (515,340) action SetVariable("save_c",4) alternate SetVariable("load_c",4) 
        imagebutton idle im.Sepia(fs(5)) hover fs(5) pos (815,340) action SetVariable("save_c",5) alternate SetVariable("load_c",5) 
        imagebutton idle im.Sepia(fs(6)) hover fs(6) pos (1120,340) action SetVariable("save_c",6) alternate SetVariable("load_c",6) 
        imagebutton idle im.Sepia(fs(7)) hover fs(7) pos (515,500) action SetVariable("save_c",7) alternate SetVariable("load_c",7) 
        imagebutton idle im.Sepia(fs(8)) hover fs(8) pos (815,500) action SetVariable("save_c",8) alternate SetVariable("load_c",8) 
        imagebutton idle im.Sepia(fs(9)) hover fs(9) pos (1120,500) action SetVariable("save_c",9) alternate SetVariable("load_c",9) 
        imagebutton idle im.Sepia(fs(10)) hover fs(10) pos (515,720) action SetVariable("save_c",10) alternate SetVariable("load_c",10) 
        imagebutton idle im.Sepia(fs(11)) hover fs(11) pos (815,720) action SetVariable("save_c",11) alternate SetVariable("load_c",11) 
        imagebutton idle im.Sepia(fs(12)) hover fs(12) pos (1120,720) action SetVariable("save_c",12) alternate SetVariable("load_c",12) 

    imagebutton focus_mask True idle "ic_return" hover "ic_return_hov" align (.03,.2) action Return()
    imagebutton focus_mask True idle "ic_options" hover "ic_options_hov" align (.03,.5) action ShowMenu("preferences")
    imagebutton focus_mask True idle "ic_mainmenu" hover "ic_mainmenu_hov" align (.03,.8) action MainMenu()


#_##_#frame:
#_##_##_#style "file_picker_frame"

#_##_##_#has vbox

#_##_##_## Кнопки сверху для выбора страницы.
#_##_##_#hbox:
#_##_##_##_#style_group "file_picker_nav"

#_##_##_##_#textbutton _("Пред"):
#_##_##_##_##_#action FilePagePrevious()

#_##_##_##_#textbutton _("Авто"):
#_##_##_##_##_#action FilePage("auto")

#_##_##_##_#textbutton _("Быстро"):
#_##_##_##_##_#action FilePage("quick")

#_##_##_##_#for i in range(1, 9):
#_##_##_##_##_#textbutton str(i):
#_##_##_##_##_##_#action FilePage(i)

#_##_##_##_#textbutton _("След"):
#_##_##_##_##_#action FilePageNext()

#_##_##_#$ columns = 3
#_##_##_#$ rows = 4

#_##_##_## Отобразить сетку файловых слотов.
#_##_##_#grid columns rows:
#_##_##_##_#transpose True
#_##_##_##_#xfill True
#_##_##_##_#style_group "file_picker"

#_##_##_##_## Отобразить 10 слотов, с номерами от 1 до 10.
#_##_##_##_#for i in range(1, columns * rows + 1):

#_##_##_##_##_## Каждый из них - кнопка.
#_##_##_##_##_#button:
#_##_##_##_##_##_#action FileAction(i)
#_##_##_##_##_##_#xfill True

#_##_##_##_##_##_#has vbox

#_##_##_##_##_##_## Добавить скриншот.
#_##_##_##_##_##_#add FileScreenshot(i)

#_##_##_##_##_##_#$ file_name = FileSlotName(i, columns * rows)
#_##_##_##_##_##_#$ file_time = FileTime(i, empty=_("Empty Slot."))
#_##_##_##_##_##_#$ save_name = FileSaveName(i)

#_##_##_##_##_##_#text "[file_name]. [file_time!t]\n[save_name!t]"

#_##_##_##_##_##_#key "save_delete" action FileDelete(i)


screen save:

    # Это заменяет другие меню.
    tag menu

    use file_picker
#    use navigation

screen load:

    # Это заменяет другие меню.
    tag menu
    use file_picker
#    use navigation

init -2 python:
    style.file_picker_frame = Style(style.menu_frame)

    style.file_picker_nav_button = Style(style.small_button)
    style.file_picker_nav_button_text = Style(style.small_button_text)

    style.file_picker_button = Style(style.large_button)
    style.file_picker_text = Style(style.large_button_text)



##############################################################################
# Preferences
#
# Экран, позволяющий пользователю изменять настройки.
# http://www.renpy.org/doc/html/screen_special.html#prefereces

init -1 python:
    import pygame
    firebool = True
    strx = {}
    stry = {}    

    lclick = False
    mclick = False
    rclick = False
    string = ""
    strx[1] = (768,836,910,980,1050,1115,1180,1250,1325,1400)
    stry[1] = (490,490,490,490,485,485,485,500,490,490)
    strx[2] = (755,818,893,955,1030,1100,1170,1235,1300,1375)
    stry[2] = (590,595,610,590,585,585,620,585,620,610)
    strx[3] = (730,800,860,935,1003,1072,1143,1212,1280,1350)
    stry[3] = (680,683,685,683,680,675,690,685,690,690)
    strx[4] = (700,770,850,910,980,1050,1120,1190,1260,1330)
    stry[4] = (785,790,790,790,780,780,790,780,785,790)

    strp = {}

    if not persistent.strb:
        persistent.strb = {}
        for i in range (10,50):
            persistent.strb[i] = True
    fscr = _preferences.fullscreen
    for xx in range (0,10):
        for yy in range (1,5):
            strp[(xx,yy)]=(strx[yy][xx],stry[yy][xx])
 
    class GetMouse(renpy.Displayable):

        def __init__(self):
            super(GetMouse, self).__init__()

        def render(self, width, height, st, at):
            rv = renpy.Render(width, height)
            return rv

        def event(self, ev, x, y, st):
            global lclick,mclick,rclick
            lclick,mclick,rclick = pygame.mouse.get_pressed()          
            return None



image options = "interface/options.jpg"
image fires =             Animation("interface/fire1.png", 0.25,
                                                  "interface/fire2.png", 0.25,
                                                  "interface/fire3.png", 0.25,
                                                  "interface/fire2.png", 0.25)      

image fire0 = Solid('#00000001',xysize=(80,78))

image fire0h = Solid('#00ff0011',xysize=(80,78))#"interface/fire0.png"

image on_off:
    "interface/icons/on_off.png"
    align (1.0,0.0)
    
init python:
    def pref_timers_update(st,at):
       preferences.set_mixer("sfx",sum((persistent.strb[i] for i in range(10,20)))/10)
       preferences.set_mixer("music",sum((persistent.strb[i] for i in range(20,30)))/10)
       preferences.set_mixer("voice",sum((persistent.strb[i] for i in range(30,40)))/10)
       preferences.text_cps = (sum((persistent.strb[i] for i in range(40,50)))*20)
       return Null(),.1#Text('%s,%s,%s'%(str(lclick),str(mclick),str(rclick))), .1

    def pref_func_hovered(candle):
        global persistent
        if lclick and not persistent.strb[candle]:
            persistent.strb[candle] = True
            play_sound("sfx/fire_bring.ogg")
            #Play("sound","sfx/fire_bring.ogg")()
        elif rclick and persistent.strb[candle]:
            persistent.strb[candle] = False
            #Play("sound","sfx/fire_calm.ogg")()
            play_sound("sfx/fire_calm.ogg")

    def pref_func_action(candle):
        global persistent
        if not persistent.strb[candle]:
            persistent.strb[candle] = True
            play_sound("sfx/fire_bring.ogg")
            #Play("sound","sfx/fire_bring.ogg")()

    def pref_func_alternate(candle):
        global persistent
        if persistent.strb[candle]:
            persistent.strb[candle] = False
            play_sound("sfx/fire_calm.ogg")
#             Play("sound","sfx/fire_calm.ogg")()


# Multi-Channel Sound Module for Ren'Py
    import renpy.audio.audio as audio
    from collections import deque

    class MultiChannelSound(object):
        def __init__(self, num_channels=8):
            self.num_channels = num_channels
            self.channels = deque(maxlen=num_channels)
            for i in range(num_channels):
                channel_name = f"multi_sound_{i}"
                renpy.music.register_channel(channel_name, "sfx", loop=False)
                self.channels.append(channel_name)

        def play(self, filename, loop=False, volume=1.0):
            channel = self.channels[0]
            self.channels.rotate(-1)
            renpy.music.play(filename, channel=channel, loop=loop, relative_volume=volume)

        def stop_all(self):
            for channel in self.channels:
                renpy.music.stop(channel=channel)

    # Initialize the multi-channel sound system
    multi_sound = MultiChannelSound()

    def play_sound(filename, loop=False, volume=1.0):
        multi_sound.play(filename, loop=loop, volume=volume)

    def stop_all_sounds():
        multi_sound.stop_all()



image pref_timers = DynamicDisplayable(pref_timers_update)
        
    
screen preferences:
    tag menu
    # Включить навигацию.
    add "options"
    add "on_off"
    add 'pref_timers'
    add GetMouse()
    imagebutton idle "fire0" hover "fire0h"  pos (1040,320) anchor (0.5,1.0) action If(not fscr, true=[SetVariable("fscr",True),Preference("display", "fullscreen"), Play("sound","sfx/fire_bring.ogg")], false=NullAction()) alternate If(fscr,true=[SetVariable("fscr",False),Preference("display","window"),Play("sound","sfx/fire_calm.ogg")])
    if fscr:
        add "fires" pos (1040,320) anchor (0.5,0.8)
    
    for xx in range (0,10):
        for yy in range (1,5):
            $candle = yy*10+xx
            if persistent.strb[candle]:
                add "fires" pos strp[(xx,yy)] anchor (0.5,0.8)
            imagebutton:
                idle "fire0"
                pos strp[(xx,yy)]
                anchor (0.5,0.8)
                #hover_sound 'sfx/fire_bring.ogg'

                hovered Function(pref_func_hovered,candle)
                action Function(pref_func_action,candle)
                alternate Function(pref_func_alternate,candle)





            text string
    imagebutton focus_mask True idle "ic_return" hover "ic_return_hov" align (.03,.2) action Return()
    imagebutton focus_mask True idle "ic_save" hover "ic_save_hov" align (.03,.5) action ShowMenu("save")
    imagebutton focus_mask True idle "ic_mainmenu" hover "ic_mainmenu_hov" align (.03,.8) action MainMenu()
        
#    use navigation

init -2 python:
    style.pref_frame.xfill = True
    style.pref_frame.xmargin = 5
    style.pref_frame.top_margin = 5

    style.pref_vbox.xfill = True

    style.pref_button.size_group = "pref"
    style.pref_button.xalign = 1.0

    style.pref_slider.xmaximum = 192
    style.pref_slider.xalign = 1.0

    style.soundtest_button.xalign = 1.0


##############################################################################
# Yes/No Prompt
#
# Экран, спрашивающий у пользователя вопрос да/нет.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt

image quit = Animation("interface/quit1.jpg",0.2,
                                     "interface/quit2.jpg",0.2)

screen yesno_prompt:

    modal True
    
    window:
        style "gm_root"

    add "quit"
    if message == layout.OVERWRITE_SAVE:
        add "ic_overwrite"
    elif message == layout.LOADING:
        add "ic_load"
    elif message == layout.QUIT:
        add "ic_quit"
    elif message == layout.MAIN_MENU:
        add "ic_to_mainmenu"

    imagebutton focus_mask True idle "ic_yes" hover "ic_yes_hov" align (.0,.9) action yes_action
    imagebutton focus_mask True idle "ic_no" hover "ic_no_hov" align (.2,.9) action no_action
    

#    frame:
#        style_group "yesno"

#        xfill True
#        xmargin .05
#        ypos .1
#        yanchor 0
#        ypadding .05

#        has vbox:
#            xalign .5
#            yalign .5
#            spacing 30

#        label _(message):
#            xalign 0.5

#        hbox:
#            xalign 0.5
#            spacing 100

#            textbutton _("Да") action yes_action
#            textbutton _("Нет") action no_action

    # Правый щелчок и escape отвечают "нет".
    key "game_menu" action no_action

init -2 python:
    style.yesno_button.size_group = "yesno"
    style.yesno_label_text.text_align = 0.5
    style.yesno_label_text.layout = "subtitle"

############################
image quit4 = "interface/quit4.jpg"
image quit5 = "interface/quit5.jpg"
image black = Solid("#000")
label quit:
    if disclaimer_quit:
        return
    hide screen main_menu
    hide screen save
    hide screen load
    hide screen preferences
    show quit4
    show quit5:
        alpha 0
        linear 2 alpha 1
    $renpy.pause(2.5,hard=True)    
    return
##############################################################################
# Quick Menu
#
# Экран, входящий в экран save и дающий некоторые полезные функции
screen quick_menu:

    # Быстрое внутриигровое меню.
    hbox:
        style_group "quick"

        xalign 1.0
        yalign 1.0

        textbutton _("Назад") action Rollback()
        textbutton _("Сохранить") action ShowMenu('save')
        textbutton _("Б.Сохр") action QuickSave()
        textbutton _("Б.Загр") action QuickLoad()
        textbutton _("Пропуск") action Skip()
        textbutton _("Б.Пропуск") action Skip(fast=True, confirm=True)
        textbutton _("Авто") action Preference("auto-forward", "toggle")
        textbutton _("Настр") action ShowMenu('preferences')

init -2 python:
    style.quick_button.set_parent('default')
    style.quick_button.background = None
    style.quick_button.xpadding = 5

    style.quick_button_text.set_parent('default')
    style.quick_button_text.size = 12
    style.quick_button_text.idle_color = "#8888"
    style.quick_button_text.hover_color = "#ccc"
    style.quick_button_text.selected_idle_color = "#cc08"
    style.quick_button_text.selected_hover_color = "#cc0"
    style.quick_button_text.insensitive_color = "#4448"
