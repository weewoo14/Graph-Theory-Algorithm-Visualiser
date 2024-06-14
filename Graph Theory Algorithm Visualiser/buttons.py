from settings import *

menu_button_rect_dict = {0:(300,200,MENU_BUTTON_WIDTH,MENU_BUTTON_HEIGHT),1:(300,300,MENU_BUTTON_WIDTH,MENU_BUTTON_HEIGHT),2:(300,400,MENU_BUTTON_WIDTH,MENU_BUTTON_HEIGHT),3:(300,500,MENU_BUTTON_WIDTH,MENU_BUTTON_HEIGHT)}
menu_button_color_dict = {0:BRIGHT_PURPLE,1:BRIGHT_PURPLE2}
menu_button_text_dict = {0:"Breadth First Search", 1:"Depth First Search", 2:"Dijkstras Algorithm",3:"Kruskals Algorithm"}

inside_algorithm_check_dict = {0:False,1:False,2:False,3:False}
title_text_rect = (175,10,TITLE_WIDTH,MENU_BUTTON_HEIGHT)
algorithm_title_text_rect = (0,10,TITLE_WIDTH,MENU_BUTTON_HEIGHT)

home_button_rect = (900,0,HOME_BUTTON_WIDTH,MENU_BUTTON_HEIGHT)
home_button_text = 'HOME'

node_centers = {0:(400,100),1:(300,200),2:(500,200),3:(200,300),4:(200,400),5:(600,300),6:(400,300),7:(300,400)}
edges_and_weights = {'12':3,'13':6,'24':5,'27':3,'36':1,'37':2,'45':10,'48':4}

learn_more_about_rect = (600,500,MENU_BUTTON_WIDTH,MENU_BUTTON_HEIGHT)
webbrowser_url = {0:'https://en.wikipedia.org/wiki/Breadth-first_search',1:'https://en.wikipedia.org/wiki/Depth-first_search',2:'https://en.wikipedia.org/wiki/Dijkstras_algorithm',3:'https://en.wikipedia.org/wiki/Kruskals_algorithm'}