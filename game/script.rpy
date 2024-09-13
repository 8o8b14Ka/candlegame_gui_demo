#bgs
image black = Solid("#000")
image red = Solid("#f00")
image pink = Solid("#f0a")
image white = Solid("#fff")


image splashcoop:
    "splashscreen.png"
    alpha 0
    ease 1.5 alpha 1
    pause 4.5
    ease 1 alpha 0
    pause 1
    "dedication.png"
    alpha 0
    ease 1.5 alpha 1

screen spcoop:
    add "splashcoop"    

image dedication = "dedication.png"

image splash = "splashscreen.jpg"
image logo = "logo.jpg"
image titl:
    "logo.png"
    alpha 1
    ease .6 alpha 0
    ease .6 alpha 1
    repeat



image tree_sky = "bgs/tree_sky.jpg"
image night_sky = "bgs/night_sky.jpg"
image night_sky_2 = "bgs/night_sky_2.jpg"
#image cloudy_sky = "bgs/cloudy_sky"
image sky = "bgs/red_bgs.jpg"
image park_day = 'bgs/park_day.png'
image park_night = 'bgs/park_night.png'
image park_dusk = 'bgs/park_dusk.png'
image park_dawn = 'bgs/park_dawn.png'





image park = "bgs/park.jpg"
image park2 = "bgs/park_night.jpg"


  



image moon = "bgs/moon2.jpg"
image moon_2 = "bgs/moon.jpg"
image ashes = "bgs/ashes.png"
image ashes_blurred = "bgs/ashes_blurred.jpg"
image city = "bgs/city.jpg"
image city_0 = "bgs/city_0.jpg"
image room_nc = "bgs/room_nc.jpg"
image room_black = "bgs/room_black.jpg"
image room_fault:
    "bgs/room_black.jpg"
    pause 0.5
    "bgs/room_virus.jpg"
    pause 0.5
    repeat
image room_old = "bgs/room_old.jpg"
image room_broken = "bgs/room_broken.jpg"

image noemie_entrance = "bgs/noemie_entrance.jpg"

image o_jury = "bgs/office_jury.jpg"
image o_repo = "bgs/office_repo.jpg"
image o_ritual = "bgs/office_ritual.jpg"
image o_tru = "bgs/office_tru.jpg"

image sparkle = SnowBlossom('interface/sparkle.png',start=5,count=4,border=300,xspeed=(20,50),yspeed=(-1050,-550))

image burn:
    "cgs/burning_house/1.png"
    pause .2
    "cgs/burning_house/2.png"
    pause .2
    "cgs/burning_house/3.png"
    pause .2
    repeat

image fume:
    "cgs/burning_house/fume.png"
    xoffset 0
    alpha .3
    ease 1 xoffset 200 alpha 0
    repeat
    
image fume2:
    "cgs/burning_house/fume2.png"
    xoffset 0
    alpha .3
    ease .9 xoffset -200 alpha 0
    repeat

image fume3:
    "cgs/burning_house/fume3.png"
    xoffset 0
    alpha .3
    ease .7 xoffset 200 alpha 0
    repeat
    
image fume4:
    "cgs/burning_house/fume4.png"
    xoffset 0
    alpha .3
    ease .8 xoffset -200 alpha 0
    repeat

    
image house_safe = "bgs/house_safe.png"

#sprs

image doll = "sprites/a-doll.png"
image diskette = "sprites/diskette_2.png"
image wallet = "sprites/wallet.png"



image c_fire:
    "sprites/chimera/fire-1.png"
    pause .15
    "sprites/chimera/fire-2.png"
    pause .15
    "sprites/chimera/fire-3.png"
    pause .15
    repeat
    
# image noemie = "sprites/noemie.png"
image noemie_alter = "sprites/noemiea/normal.png"
image noemie_after = "sprites/noemie_after.png"
image noemie_shadow = "sprites/noemie_shadow.png"

image chimera = LiveComposite((1500,2800),(0,0),"sprites/chimera/normal.png",(0,0),"c_fire")
image chimera = LiveComposite((1500,2800),(0,0),"sprites/chimera/normal.png",(0,0),"c_fire")
image chimera normal = LiveComposite((1500,2800),(0,0),"sprites/chimera/normal.png",(0,0),"c_fire")
image chimera e_smile = LiveComposite((1500,2800),(0,0),"sprites/chimera/e_smile.png",(0,0),"c_fire")
image chimera kiss = LiveComposite((1500,2800),(0,0),"sprites/chimera/kiss.png",(0,0),"c_fire")
image chimera pout = LiveComposite((1500,2800),(0,0),"sprites/chimera/pout.png",(0,0),"c_fire")
image chimera sad = LiveComposite((1500,2800),(0,0),"sprites/chimera/sad.png",(0,0),"c_fire")
image chimera say = LiveComposite((1500,2800),(0,0),"sprites/chimera/say.png",(0,0),"c_fire")
image chimera smile = LiveComposite((1500,2800),(0,0),"sprites/chimera/smile.png",(0,0),"c_fire")
image chimera chant = LiveComposite((1500,2800),(0,0),"sprites/chimera/chant.png",(0,0),"c_fire")
image chimera origin = "sprites/chimera/normal.png"


image side chimera = "emo/chimera/normal.png"
image side chimera normal= "emo/chimera/normal.png"
image side chimera e_smile = "emo/chimera/e_smile.png"
image side chimera kiss = "emo/chimera/kiss.png"
image side chimera pout = "emo/chimera/pout.png"
image side chimera sad = "emo/chimera/sad.png"
image side chimera say = "emo/chimera/say.png"
image side chimera smile = "emo/chimera/smile.png"
image side chimera chant = "emo/chimera/chant.png"

image noemie = "sprites/noemie/normal.png"
image noemie normal = "sprites/noemie/normal.png"
image noemie eye_normal = "sprites/noemie/eye_normal.png"
image noemie eye_smile = "sprites/noemie/eye_smile.png"
image noemie smile = "sprites/noemie/smile.png"
image noemie say = "sprites/noemie/say.png"
image noemie kiss = "sprites/noemie/kiss.png"
image noemie tears = "sprites/noemie/tears.png"

image noemiea = "sprites/noemiea/normal.png"
image noemiea normal = "sprites/noemiea/normal.png"
image noemiea eye_normal = "sprites/noemiea/eye_normal.png"
image noemiea eye_smile = "sprites/noemiea/eye_smile.png"
image noemiea smile = "sprites/noemiea/smile.png"
image noemiea say = "sprites/noemiea/say.png"
image noemiea kiss = "sprites/noemiea/kiss.png"
image noemiea tears = "sprites/noemiea/tears.png"


image side noemie = "emo/noemie/normal.png"
image side noemie normal = "emo/noemie/normal.png"
image side noemie eye_normal = "emo/noemie/eye_normal.png"
image side noemie eye_smile = "emo/noemie/eye_smile.png"
image side noemie smile = "emo/noemie/smile.png"
image side noemie say = "emo/noemie/say.png"
image side noemie kiss = "emo/noemie/kiss.png"
image side noemie tears = "emo/noemie/tears.png"


image side noemiea = "emo/noemie/normal.png"
image side noemiea normal = "emo/noemie/normal.png"
image side noemiea eye_normal = "emo/noemie/eye_normal.png"
image side noemiea eye_smile = "emo/noemie/eye_smile.png"
image side noemiea smile = "emo/noemie/smile.png"
image side noemiea say = "emo/noemie/say.png"
image side noemiea kiss = "emo/noemie/kiss.png"
image side noemiea tears = "emo/noemie/tears.png"




image chimera_adult = "sprites/chimera_adult.png"




image aya_shadow = "sprites/aya/aya_shadow.png"
image aya_reporter = "sprites/aya/normal.png"
image aya_ritual = "sprites/aya/aya_ritual.png"


image aya = "sprites/aya/normal.png"
image aya normal = "sprites/aya/normal.png"
image aya creep = "sprites/aya/creep.png"
image aya kiss = "sprites/aya/kiss.png"
image aya say = "sprites/aya/say.png"
image aya serious = "sprites/aya/serious.png"
image aya smile = "sprites/aya/smile.png"
image aya what = "sprites/aya/what.png"
image aya wry = "sprites/aya/wry.png"

image aya_blood big = "sprites/aya/blood_big.png"
image aya_blood small = "sprites/aya/blood_small.png"
image aya_blood stained = "sprites/aya/blood_stained.png"



image side aya = "emo/aya/normal.png"
image side aya normal = "emo/aya/normal.png"
image side aya creep = "emo/aya/creep.png"
image side aya kiss = "emo/aya/kiss.png"
image side aya say = "emo/aya/say.png"
image side aya serious = "emo/aya/serious.png"
image side aya smile = "emo/aya/smile.png"
image side aya what = "emo/aya/what.png"
image side aya wry = "emo/aya/wry.png"


image ayar = "sprites/ayar/normal.png"
image ayar normal = "sprites/ayar/normal.png"
image ayar creep = "sprites/ayar/creep.png"
image ayar kiss = "sprites/ayar/kiss.png"
image ayar say = "sprites/ayar/say.png"
image ayar serious = "sprites/ayar/serious.png"
image ayar smile = "sprites/ayar/smile.png"
image ayar what = "sprites/ayar/what.png"
image ayar wry = "sprites/ayar/wry.png"

image side ayar = "emo/ayar/normal.png"
image side ayar normal = "emo/ayar/normal.png"
image side ayar creep = "emo/ayar/creep.png"
image side ayar kiss = "emo/ayar/kiss.png"
image side ayar say = "emo/ayar/say.png"
image side ayar serious = "emo/ayar/serious.png"
image side ayar smile = "emo/ayar/smile.png"
image side ayar what = "emo/ayar/what.png"
image side ayar wry = "emo/ayar/wry.png"



image ernest = "sprites/ernest/normal.png"
image ernest normal = "sprites/ernest/normal.png"
image ernest dark = "sprites/ernest/dark.png"
image ernest confused = "sprites/ernest/confused.png"
image ernest eyes_closed = "sprites/ernest/eyes_closed.png"
image ernest say = "sprites/ernest/say.png"
image ernest scared = "sprites/ernest/scared.png"
image ernest smile = "sprites/ernest/smile.png"
image ernest tears = "sprites/ernest/tears.png"
image ernest v_scared = "sprites/ernest/very_scared.png"
image ernest wry = "sprites/ernest/wry_smile.png"
image ernest_dark = "sprites/ernest/dark.png"


image side ernest = "emo/ernest/normal.png"
image side ernest normal = "emo/ernest/normal.png"
image side ernest confused = "emo/ernest/confused.png"
image side ernest eyes_closed = "emo/ernest/eyes_closed.png"
image side ernest say = "emo/ernest/say.png"
image side ernest scared = "emo/ernest/scared.png"
image side ernest smile = "emo/ernest/smile.png"
image side ernest tears = "emo/ernest/tears.png"
image side ernest v_scared = "emo/ernest/v_scared.png"
image side ernest wry = "emo/ernest/wry.png"

image firefighter = "sprites/firefighter.png"

#cgs
image c_sleep = "cgs/chimera_sleep1.jpg"
image c_sleep awake = "cgs/chimera_sleep2.jpg"
image c_kiss = "cgs/chimera_kiss.png"
image choise = "interface/choise.jpg"


image dinner0 = "cgs/dinner0.jpg"
image dinner1 = "cgs/dinner1.jpg"
#image dinner2 = "cgs/dinner2.jpg"
#image dinner3 = "cgs/dinner3.jpg"
image dinner4 = "cgs/dinner4.jpg"

image dinner_w:
    "cgs/dinner_w1.png"
    pause .15
    "#0000"
    pause .15
    "cgs/dinner_w2.png"
    pause .15
    "#0000"
    pause .15
    repeat
    
#image dinner1 = LiveComposite((1920,1080),(0,0),"cgs/dinner1.jpg",(0,0),"dinner_w")
image dinner2 = LiveComposite((1920,1080),(0,0),"cgs/dinner2.jpg",(0,0),"dinner_w")
image dinner3 = LiveComposite((1920,1080),(0,0),"cgs/dinner3.jpg",(0,0),"dinner_w")



image chimera_ero = "cgs/chimera_ero.jpg"
image chimera_tru = "cgs/chimera_vast.jpg"
image chimera_tru_bg = "cgs/chimera_tru_bg.jpg"
image chimera_tru_front = "cgs/chimera_tru_front.png"
image aya_ero = "cgs/aya_ero.jpg"
image aya_ending = "cgs/aya_ending.jpg"
image chimera_after = "cgs/chimera_after.jpg"
image noemie_ending = "cgs/noemie_ending.jpg"
image noemie_ero = "cgs/noemie_ero.jpg"
image noemie_tru = "cgs/noemie_tru.jpg"
image tru = "cgs/tru.jpg"
image creator = "cgs/creator.jpg"
image she = "cgs/she.jpg"

image movie = Movie(size = (1920,1080))


#effects

init python:
    eye_open = ImageDissolve("effects/id_eye.png", 2.0, 32)

image rain:
    alpha 0.3
    "bgs/rain1.jpg"
    pause 0.1
    "bgs/rain2.jpg"
    pause 0.1
    "bgs/rain3.jpg"
    pause 0.1
    "bgs/rain4.jpg"
    pause 0.1
    "bgs/rain5.jpg"
    pause 0.1
    repeat

image thunder:
    "bgs/thunder1.jpg"
    pause 0.1
    "bgs/thunder2.jpg"
    pause 0.1
    "bgs/thunder1.jpg"
    pause 0.1
    "#000"
    
    
image fire:
    "effects/fire/fire-1.png"
    pause 0.04
    "effects/fire/fire-2.png"
    pause 0.04
    "effects/fire/fire-3.png"
    pause 0.04
    "effects/fire/fire-4.png"
    pause 0.04
    "effects/fire/fire-5.png"
    pause 0.04
    "effects/fire/fire-6.png"
    pause 0.04
    "effects/fire/fire-7.png"
    pause 0.04
    "effects/fire/fire-8.png"
    pause 0.04
    "effects/fire/fire-9.png"
    pause 0.04
    "effects/fire/fire-10.png"
    pause 0.04
    "effects/fire/fire-11.png"
    pause 0.04
    "effects/fire/fire-12.png"
    pause 0.04
    "effects/fire/fire-13.png"
    pause 0.04
    "effects/fire/fire-14.png"
    pause 0.04
    "effects/fire/fire-15.png"
    pause 0.04
    "effects/fire/fire-16.png"
    pause 0.04
    "effects/fire/fire-17.png"
    pause 0.04
    "effects/fire/fire-18.png"
    pause 0.04
    "effects/fire/fire-19.png"
    pause 0.04
    "effects/fire/fire-20.png"
    pause 0.04
    "effects/fire/fire-21.png"
    pause 0.04
    "effects/fire/fire-22.png"
    pause 0.04
    "effects/fire/fire-23.png"
    pause 0.04
    "effects/fire/fire-24.png"
    pause 0.04
    "effects/fire/fire-25.png"
    pause 0.04
    repeat

image smoke1:
    "effects/clouds/smoke1.png"
    alpha .8
    xalign 1.0
    zoom 1.5
    linear 10 xalign 0.0
    repeat
image smoke2:
    alpha .8
    "effects/clouds/smoke2.png"
    xalign 1.0
    zoom 1.5
    linear 20 xalign 0
    repeat

image smoke = LiveComposite((1920,600),(0,0),"smoke1",(0,0),"smoke2")

    
image leaffall = SnowBlossom(Animation("sprites/leaf1-1.png", 0.15,
                                       "sprites/leaf1-2.png", 0.15,
                                       "sprites/leaf1-3.png", 0.15,
                                       "sprites/leaf1-2.png", 0.15),start=10)

image leaffal2 = SnowBlossom(Animation("sprites/leaf2-1.png", 0.15,
                                       "sprites/leaf2-2.png", 0.15,
                                       "sprites/leaf2-3.png", 0.15,
                                       "sprites/leaf2-2.png", 0.15),start=10)

image book:
    "sprites/flying_stuff/book.png"
    rotate 60
    
image book2:
    "sprites/flying_stuff/book2.png"
    rotate 50

image notebook:
    "sprites/flying_stuff/notebook.png"
    rotate -30

image shroom = "sprites/flying_stuff/shroom.png"

image skull:
    "sprites/flying_stuff/skull.png"
    rotate 40

image skull2:
    "sprites/flying_stuff/skull2.png"
    rotate -20

image teapot:
    "sprites/flying_stuff/teapot.png"
    rotate 10

image sb_book = SnowBlossom('book',start=5,count=2,border=300,xspeed=(20,70),yspeed=(-150,-50))
image sb_book2 = SnowBlossom('book2',start=5,count=2,border=300,xspeed=(-70,-20),yspeed=(100,150))
image sb_notebook = SnowBlossom('notebook',start=5,count=2,border=300,xspeed=(10,60),yspeed=(60,120))
image sb_shroom = SnowBlossom('shroom',start=5,count=2,border=300,xspeed=(-100,-20),yspeed=(-120,-90))
image sb_skull = SnowBlossom('skull',count=2,start=5,border=300,horizontal=True,xspeed=(100,200),yspeed=(-50,-10))
image sb_skull2 = SnowBlossom('skull2',count=2,start=5,border=300,horizontal=True,xspeed=(-100,-200),yspeed=(10,30))
image sb_teapot = SnowBlossom('teapot',count=2,start=5,border=300,horizontal=True,xspeed=(-200,-100),yspeed=(-100,-50))

init -2 python:

    def e_sound(event, **kwargs):
        if event == "show":
            renpy.music.play("sfx/e_voice.ogg", channel="sound")
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

    def c_sound(event, **kwargs):
        if event == "show":
            renpy.music.play("sfx/c_voice.ogg", channel="sound")
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

    def a_sound(event, **kwargs):
        if event == "show":
            renpy.music.play("sfx/a_voice.ogg", channel="sound")
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

    def ae_sound(event, **kwargs):
        if event == "show":
            renpy.music.play("sfx/ae_voice.ogg", channel="sound")
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

    def ar_sound(event, **kwargs):
        if event == "show":
            renpy.music.play("sfx/ar_voice.ogg", channel="sound",fadeout = 1.0)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")


    def ab_sound(event, **kwargs):
        if event == "show":
            renpy.music.play("sfx/ab_voice.ogg", channel="sound")
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

    def t_sound(event, **kwargs):
        if event == "show":
            renpy.music.play("sfx/type0.ogg", channel="sound")
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")


#chars

define o = Character('', what_prefix = "{b}{color=#503}???: {/color}{/b}",callback=c_sound)
define v = Character('', what_prefix = "{b}{color=#503}???: {/color}{/b}",show_side_image="emo/vendor.png",callback=c_sound)
define w = Character('', what_prefix = "{b}{color=#467}Мы: {/color}{/b}",callback=ae_sound)

define cs = Character('', image="chimera")
define ns = Character('', image="noemie")
define nas = Character('', image="noemiea")
define ass = Character('', image="aya")
define ars = Character('', image="ayar")


define co = Character('', what_prefix = "{b}{color=#500}??? {/color}{/b}", image="chimera",callback=c_sound)
define c = Character('', what_prefix = "{b}{color=#500}химера: {/color}{/b}", image="chimera",callback=c_sound)
define cb = Character('', what_prefix = "{b}{color=#500}ХИМЕРА: {/color}{/b}", image="chimera",callback=a_sound)
define a = Character('', what_prefix = "{b}{color=#334}Айя: {/color}{/b}",image="aya",callback=a_sound)
define ar = Character('', what_prefix = "{b}{color=#334}Айя: {/color}{/b}",image="ayar",callback=a_sound)
define ab = Character('',what_color = "#d00", what_prefix = "{b}{color=#334}АNR: {/color}{/b}",image="aya",callback=ab_sound)
define n = Character('', what_prefix = "{b}{color=#050}Ноэми: {/color}{/b}", image="noemie",callback=a_sound)
define na = Character('', what_prefix = "{b}{color=#050}Ноэми: {/color}{/b}", image="noemiea",callback=a_sound)
define es = Character('', image="ernest")
define e = Character('', what_prefix = "{b}{color=#404}Эрнест: {/color}{/b}", image="ernest",callback=e_sound)
define children = Character('', what_prefix = "{b}{color=#606}Дети: {/color}{/b}",callback=c_sound)
define p = Character(None, kind=nvl, what_color = "#fff",text_align = 0.5, callback=t_sound)
define pn = Character(u'Noémie: ', color = "#aa3", kind=nvl, what_color = "#ffc",text_align = 0.5, callback=t_sound)
define pc = Character('chimera: ', color = "#a33", kind=nvl, what_color = "#faa", text_align = 0.5, callback=ar_sound)

define t = Character('', callback=t_sound)
define txt = Character('', what_color = "#005", callback=e_sound)



image ash_chimera = "interface/choice/chimera_ash.png"
image ash_aya = "interface/choice/aya_ash.png"
image ash_noemie = "interface/choice/noemie_ash.png"
image unnamed = "interface/choice/unnamed.png"
image unnamed_eyelids:
    "interface/choice/unnamed_eyelids.png"
    yalign 1.0
image unnamed_noeyes = "interface/choice/unnamed_noeyes.png"
image unnamed_eyes = Animation("interface/choice/unnamed_eyes.png", 0.1,
                               "interface/choice/unnamed_eyes2.png", 0.1)

image unnamed_hov = "interface/choice/unnamed_hov.png"

image chimera_idle =             Animation("interface/choice/chimera-1.png", 0.15,
                                            "interface/choice/chimera-2.png", 0.15,
                                            "interface/choice/chimera-3.png", 0.15)      





image noemie_idle = "interface/choice/noemie.png"
image aya_idle = "interface/choice/aya.png"

image chimera_hov_0 =             Animation("interface/choice/chimera_hov_0-1.png", 0.25,
                                            "interface/choice/chimera_hov_0-2.png", 0.25,
                                            "interface/choice/chimera_hov_0-3.png", 0.25)      

image chimera_hov_1 =             Animation("interface/choice/chimera_hov_1-1.png", 0.25,
                                            "interface/choice/chimera_hov_1-2.png", 0.25,
                                            "interface/choice/chimera_hov_1-3.png", 0.25)      

image chimera_hov_2 =             Animation("interface/choice/chimera_hov_2-1.png", 0.25,
                                            "interface/choice/chimera_hov_2-2.png", 0.25,
                                            "interface/choice/chimera_hov_2-3.png", 0.25)      


image noemie_hov_0 =             Animation("interface/choice/noemie_hov_0-1.png", 0.25,
                                            "interface/choice/noemie_hov_0-2.png", 0.25,
                                            "interface/choice/noemie_hov_0-3.png", 0.25)      

image noemie_hov_1 =             Animation("interface/choice/noemie_hov_1-1.png", 0.25,
                                            "interface/choice/noemie_hov_1-2.png", 0.25,
                                            "interface/choice/noemie_hov_1-3.png", 0.25)      

image noemie_hov_2 =             Animation("interface/choice/noemie_hov_2-1.png", 0.25,
                                            "interface/choice/noemie_hov_2-2.png", 0.25,
                                            "interface/choice/noemie_hov_2-3.png", 0.25)      


image aya_hov_0 =             Animation("interface/choice/aya_hov_0-1.png", 0.25,
                                            "interface/choice/aya_hov_0-2.png", 0.25,
                                            "interface/choice/aya_hov_0-3.png", 0.25)      

image aya_hov_1 =             Animation("interface/choice/aya_hov_1-1.png", 0.25,
                                            "interface/choice/aya_hov_1-2.png", 0.25,
                                            "interface/choice/aya_hov_1-3.png", 0.25)      

image aya_hov_2 =             Animation("interface/choice/aya_hov_2-1.png", 0.25,
                                            "interface/choice/aya_hov_2-2.png", 0.25,
                                            "interface/choice/aya_hov_2-3.png", 0.25)      


image dis_ground = "interface/disclaimer/disclaimer.jpg"
image dis_yes = "interface/disclaimer/yes.png"
image dis_yes_hov = Animation ("interface/disclaimer/yes_hov.png",.15,
                               "interface/disclaimer/yes_hov2.png",.15,
                               "interface/disclaimer/yes_hov3.png",.15)
image dis_no = "interface/disclaimer/no.png"
image dis_no_hov = Animation ("interface/disclaimer/no_hov.png",.15,
                               "interface/disclaimer/no_hov2.png",.15,
                               "interface/disclaimer/no_hov3.png",.15)

init -1 python:
    disclaimer_quit = False

screen disclaimer:
    add "dis_ground"
    imagebutton focus_mask True idle "dis_yes" hover "dis_yes_hov" action Return()
    imagebutton focus_mask True idle "dis_no" hover "dis_no_hov" action [SetVariable("disclaimer_quit",True),Quit(confirm = False)]
    
screen startvalues:
    timer .01 action Preference("text speed", 60)
    timer .01 action Preference("music volume", .1)
    timer .01 action Preference("sound volume", .1)
    timer .01 action Preference("voice volume", .1)
    timer 1 action Return()



image tree_skys:
    subpixel True
    "bgs/tree_sky.jpg"
    zoom 1.3
    align (1.0,0.5)
    ease 60 xalign 0.0
    
image night_skys:
    subpixel True
    "bgs/night_sky.jpg"
    zoom 1.3
    align (1.0,0.5)
    ease 60 xalign 0.0
    
    
image night_skys_2:
    subpixel True
    "bgs/night_sky.jpg"
    zoom 1.3
    align (1.0,0.5)
    ease 60 xalign 0.0

image eve_sky:
    subpixel True
    "bgs/red_bgs_2.jpg"
    align (1.0,0.5)
    ease 60 xalign 0.0

image cloudy_sky:
    subpixel True
    "bgs/cloudy_sky.jpg"
    align (1.0,0.5)
    ease 60 xalign 0.0

image noise:
    alpha .3
    "effects/noise/1.jpg"
    pause .08
    "effects/noise/2.jpg"
    pause .08
    "effects/noise/3.jpg"
    pause .08
    "effects/noise/4.jpg"
    pause .08
    "effects/noise/5.jpg"
    pause .08
    repeat

image black_unfade:
    "#000"
    alpha 1.0
    ease 2 alpha 0.0


init python:
    class EyeMovement(renpy.Displayable):
        def __init__(self, child):
            super(EyeMovement, self).__init__()
            self.child = renpy.displayable(child)
            self.x = 0
            self.y = 0

        def render(self, width, height, st, at):

            rv = renpy.Render(width, height)

            cr = renpy.render(self.child, width, height, st, at)
            rv.blit(cr, (self.x, self.y))

            return rv

        def event(self, ev, x, y, st):
            self.x = x//80 - 10
            self.y = y//40 + 165
            renpy.redraw(self, 0)


screen choisse:
    add cho
    if clear_chimera and clear_aya and clear_noemie:
        add "cloudy_sky"
        add "noise"
        timer .01 action Play("amb","amb/noise.ogg")
        timer .05 action Stop("music")
        timer 2 action Play("sound","sfx/kom_til_meg.ogg")
        add "ash_noemie" yalign 1.0
        add "ash_aya" yalign 1.0
        add "ash_chimera" yalign 1.0
        add "unnamed_eyelids"
        add EyeMovement("unnamed_eyes")
        imagebutton idle "unnamed_noeyes" hover "unnamed_hov" focus_mask True yalign 1.0 hovered Play("sound","sfx/laugh.ogg") unhovered Play("sound","sfx/unhover.ogg") action [Play("sound","sfx/unhover.ogg"), Return('tru')]
        
    else:
        if clear_noemie:
            add "rain"
            timer .001 action Play("amb","amb/rain.ogg")
            add "ash_noemie" yalign 1.0
            imagebutton idle "interface/choice/noemie_hov_3-1.png" hover "interface/choice/noemie_hov_3-1-2.png" focus_mask True yalign 1.0 hovered Play("sound","sfx/hover.ogg") unhovered Play("sound","sfx/unhover.ogg") action [Play("sound","sfx/action.ogg"),  Return('n1')]
            imagebutton idle "interface/choice/noemie_hov_3-2.png" hover "interface/choice/noemie_hov_3-2-2.png" focus_mask True yalign 1.0 hovered Play("sound","sfx/hover.ogg") unhovered Play("sound","sfx/unhover.ogg") action [Play("sound","sfx/action.ogg"),  Return('n2')]
            imagebutton idle "interface/choice/noemie_hov_3-3.png" hover "interface/choice/noemie_hov_3-3-2.png" focus_mask True yalign 1.0 hovered Play("sound","sfx/hover.ogg") unhovered Play("sound","sfx/unhover.ogg") action [Play("sound","sfx/action.ogg"),  Return('n3')]
        else:
            if lp_noemie == 1:
                imagebutton idle "noemie_idle" hover "noemie_hov_0" focus_mask True yalign 1.0 hovered Play("sound","sfx/hover.ogg") unhovered Play("sound","sfx/unhover.ogg") action [Play("sound","sfx/action.ogg"),  Return('n1')]
            if lp_noemie == 2:
                imagebutton idle "noemie_idle" hover "noemie_hov_1" focus_mask True yalign 1.0 hovered Play("sound","sfx/hover.ogg") unhovered Play("sound","sfx/unhover.ogg") action [Play("sound","sfx/action.ogg"),  Return('n2')]
            if lp_noemie == 3:
                imagebutton idle "noemie_idle" hover "noemie_hov_2" focus_mask True yalign 1.0 hovered Play("sound","sfx/hover.ogg") unhovered Play("sound","sfx/unhover.ogg") action [Play("sound","sfx/action.ogg"),  Return('n3')]

        if clear_aya:
            add "smoke1"
            add "smoke2"
            add "ash_aya" yalign 1.0
            imagebutton idle "interface/choice/aya_hov_3-1.png" hover "interface/choice/aya_hov_3-1-2.png" focus_mask True yalign 1.0 hovered Play("sound","sfx/hover.ogg") unhovered Play("sound","sfx/unhover.ogg") action [Play("sound","sfx/action.ogg"),  Return('a1')]
            imagebutton idle "interface/choice/aya_hov_3-2.png" hover "interface/choice/aya_hov_3-2-2.png" focus_mask True yalign 1.0 hovered Play("sound","sfx/hover.ogg") unhovered Play("sound","sfx/unhover.ogg") action [Play("sound","sfx/action.ogg"),  Return('a2')]
            imagebutton idle "interface/choice/aya_hov_3-3.png" hover "interface/choice/aya_hov_3-3-2.png" focus_mask True yalign 1.0 hovered Play("sound","sfx/hover.ogg") unhovered Play("sound","sfx/unhover.ogg") action [Play("sound","sfx/action.ogg"),  Return('a3')]
        else:
            if lp_aya == 1:
                imagebutton idle "aya_idle" hover "aya_hov_0" focus_mask True yalign 1.0 hovered Play("sound","sfx/hover.ogg") unhovered Play("sound","sfx/unhover.ogg") action [Play("sound","sfx/action.ogg"),  Return('a1')]
            if lp_aya == 2:
                imagebutton idle "aya_idle" hover "aya_hov_1" focus_mask True yalign 1.0 hovered Play("sound","sfx/hover.ogg") unhovered Play("sound","sfx/unhover.ogg") action [Play("sound","sfx/action.ogg"),  Return('a2')]
            if lp_aya == 3:
                imagebutton idle "aya_idle" hover "aya_hov_2" focus_mask True yalign 1.0 hovered Play("sound","sfx/hover.ogg") unhovered Play("sound","sfx/unhover.ogg") action [Play("sound","sfx/action.ogg"),  Return('a3')]
                
        add "unnamed" yalign 1.0

        if clear_chimera:
            add "sparkle"
            add "ash_chimera" yalign 1.0
            imagebutton idle "interface/choice/chimera_hov_3-1.png" hover "interface/choice/chimera_hov_3-1-2.png" focus_mask True yalign 1.0 hovered Play("sound","sfx/hover.ogg") unhovered Play("sound","sfx/unhover.ogg") action [Play("sound","sfx/action.ogg"),  Return('c1')]
            imagebutton idle "interface/choice/chimera_hov_3-2.png" hover "interface/choice/chimera_hov_3-2-2.png" focus_mask True yalign 1.0 hovered Play("sound","sfx/hover.ogg") unhovered Play("sound","sfx/unhover.ogg") action [Play("sound","sfx/action.ogg"),  Return('c2')]
            imagebutton idle "interface/choice/chimera_hov_3-3.png" hover "interface/choice/chimera_hov_3-3-2.png" focus_mask True yalign 1.0 hovered Play("sound","sfx/hover.ogg") unhovered Play("sound","sfx/unhover.ogg") action [Play("sound","sfx/action.ogg"),  Return('c3')]
        else:
            if lp_chimera == 1:
                imagebutton idle "chimera_idle" hover "chimera_hov_0" focus_mask True yalign 1.0 hovered Play("sound","sfx/hover.ogg") unhovered Play("sound","sfx/unhover.ogg") action [Play("sound","sfx/action.ogg"),  Return('c1')]
            if lp_chimera == 2:
                imagebutton idle "chimera_idle" hover "chimera_hov_1" focus_mask True yalign 1.0 hovered Play("sound","sfx/hover.ogg") unhovered Play("sound","sfx/unhover.ogg") action [Play("sound","sfx/action.ogg"),  Return('c2')]
            if lp_chimera == 3:
                imagebutton idle "chimera_idle" hover "chimera_hov_2" focus_mask True yalign 1.0 hovered Play("sound","sfx/hover.ogg") unhovered Play("sound","sfx/unhover.ogg") action [Play("sound","sfx/action.ogg"),  Return('c3')]
    add "black_unfade"
    if renpy.emscripten:
        add TrackCursor('cursor','cursors/fired_shadow.png')










# Игра начинается здесь.
label start:
    python:
        lp_chimera = 1
        lp_aya = 1
        lp_noemie = 1
        clear_chimera = False
        clear_aya = False
        clear_noemie = False
        token = ""
        aya_promise = False
        aya_read = True
        chimera_believe = False
        chimera_return = True

    scene black
    play music "bgm/night.mp3"


label choise:
    scene black
    stop amb
    play music "bgm/night.mp3" fadein 1.0 fadeout 1.0
    $cho = renpy.random.choice(["eve_sky","cloudy_sky","tree_skys","night_skys","night_skys_2"])

    call screen choisse
    $renpy.jump("%s"%_return)
    jump choise

label c1:
    $lp_chimera = 2
    jump choise

label c2:
    $lp_chimera = 3
    jump choise

label c3:
    $clear_chimera = True
    jump choise




label n1:
    $lp_noemie = 2
    jump choise

label n2:
    $lp_noemie = 3
    jump choise

label n3:
    $clear_noemie = True
    jump choise


label a1:
    $lp_aya = 2
    jump choise

label a2:
    $lp_aya = 3
    jump choise

label a3:
    $clear_aya = True
    jump choise

label tru:
    ##############
    #Тру эндинг
    ##############
    $persistent.gameclear = True
    $renpy.pause(6,hard=True)
    $renpy.full_restart()
    return


