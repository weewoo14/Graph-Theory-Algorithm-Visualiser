# Importing all the functions and modules
import pygame
import webbrowser
from settings import *
from buttons import *
from bfs import *
from dfs import *
from dijkstras import *
from kruskals import *

# Initializing PyGame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Graph Theory Algorithm Visualizer")
clock = pygame.time.Clock()

# Main Game Loop
game_running = True
while game_running:

    # Getting the users mouse position
    mouse_xpos,mouse_ypos = pygame.mouse.get_pos()

    # Checking for functionality from the user
    for event in pygame.event.get():

        # Check if the user has pressed the red X
        if event.type == pygame.QUIT:
            game_running = False

        # Check if the user has clicked
        if event.type == pygame.MOUSEBUTTONDOWN:

            # Checking if the user has clicked on the menu buttons
            for button_idx in range(MENU_BUTTON_COUNT):
                rx1,ry1,rx2,ry2 = menu_button_rect_dict[button_idx]
                if is_collision(mouse_xpos,mouse_ypos,rx1,ry1,rx1+rx2,ry1+ry2):
                    inside_algorithm_check_dict[button_idx] = True

            # Checking if the user has clicked on the home button
            if is_collision(mouse_xpos,mouse_ypos,home_button_rect[0],home_button_rect[1],home_button_rect[0]+home_button_rect[2],home_button_rect[1]+home_button_rect[3]):
                for button_idx in range(MENU_BUTTON_COUNT):
                    inside_algorithm_check_dict[button_idx] = False
            
            # Checking if the user hs clicked on the 'Learn More' button
            if is_collision(mouse_xpos,mouse_ypos,learn_more_about_rect[0],learn_more_about_rect[1],learn_more_about_rect[0]+learn_more_about_rect[2],learn_more_about_rect[1]+learn_more_about_rect[3]):
                selected_alg = -1
                for key,val in inside_algorithm_check_dict.items():
                    if val:
                        selected_alg = key
                        break
                if selected_alg == -1:
                    continue

                # Redirecting the user to the wikipedia article for each graph theory algorithm
                webbrowser.open(webbrowser_url[selected_alg])
                
    # Getting the current graph theory algorithm. If none is selected, on the menu page
    selected_alg = -1
    for key,val in inside_algorithm_check_dict.items():
        if val:
            selected_alg = key
            break
    # Resetting the screen
    screen.fill(BLACK)

    if selected_alg == -1:

        # Resetting everything
        visualiser_timer = 0
        cur_bfs_edge = 0
        cur_dfs_edge = 0
        cur_dijkstras_edge = 0
        cur_kruskal_edge = 0
        temp_bfs_visited = [False] * NODE_COUNT
        temp_dfs_visited = [False] * NODE_COUNT
        temp_dijkstras_visited = [False] * NODE_COUNT
        temp_kruskals_visited = [False] * NODE_COUNT
        minimum_spanning_tree = []

        # Rendering the title text to the screen
        title_font.render_to(screen,title_text_rect,"Graph Theory",WHITE)
        title_font.render_to(screen,(275,75,TITLE_WIDTH,MENU_BUTTON_HEIGHT),"Algorithm",WHITE)
        title_font.render_to(screen,(275,140,TITLE_WIDTH,MENU_BUTTON_HEIGHT),"Visualizer",WHITE)

        # Rendering Graph Theory Algorithm Buttons to the screen
        for button_idx in range(MENU_BUTTON_COUNT):
            rx1,ry1,rx2,ry2 = menu_button_rect_dict[button_idx]
            button_color = menu_button_color_dict[is_collision(mouse_xpos,mouse_ypos,rx1,ry1,rx1+MENU_BUTTON_WIDTH,ry1+MENU_BUTTON_HEIGHT)]
            pygame.draw.rect(screen, button_color,menu_button_rect_dict[button_idx])
            menu_button_font.render_to(screen,(rx1+TEXT_OFFSET,ry1+TEXT_OFFSET,rx1+rx2+TEXT_OFFSET,ry1+ry2+TEXT_OFFSET),menu_button_text_dict[button_idx],WHITE)
    else:

        # Rendering the learn more button to the screen
        learn_more_about_rect_color = menu_button_color_dict[is_collision(mouse_xpos,mouse_ypos,learn_more_about_rect[0],learn_more_about_rect[1],learn_more_about_rect[0]+learn_more_about_rect[2],learn_more_about_rect[1]+learn_more_about_rect[3])]
        pygame.draw.rect(screen,learn_more_about_rect_color,learn_more_about_rect)
        learn_more_font.render_to(screen,(learn_more_about_rect[0]+TEXT_OFFSET,learn_more_about_rect[1]+TEXT_OFFSET,learn_more_about_rect[0]+learn_more_about_rect[2],learn_more_about_rect[1]+learn_more_about_rect[3]),'LEARN MORE',WHITE)

        # Checking to see if we are able to progress with the graph theory algorithm
        visualiser_timer += 1

        # Rendering the title of the graph theory algorithm
        algorithm_title_font.render_to(screen,algorithm_title_text_rect,menu_button_text_dict[selected_alg],WHITE)
        
        # Rendering the edges and weights on the graph
        for key,val in edges_and_weights.items():
            n1,n2 = node_centers[int(key[0])-1],node_centers[int(key[1])-1]
            pygame.draw.line(screen,WHITE,n1,n2,5)

            # Rendering the weight by getting the midpoint
            mp = midpoint(n1[0],n1[1],n2[0],n2[1])
            node_font.render_to(screen,(mp[0],mp[1],mp[0],mp[1]),str(val),WHITE)

        # Checking for each individual graph theory algorithm
        
        # Breadth First Search
        if selected_alg == 0:
            # Getting the edges BFS has traversed through along with the current queue
            bfs_path,inside_queue = breadth_first_search(GRAPH_SETUP,NODE_COUNT,1)

            # Checking to see if we are able to move on
            if visualiser_timer >= 180 and cur_bfs_edge < BFS_EDGE-1:
                visualiser_timer = 0
                cur_bfs_edge += 1
            
            # Getting what edge we are on by getting both of the node centers
            u,v = bfs_path[cur_bfs_edge][0]-1,bfs_path[cur_bfs_edge][1]-1
            temp_bfs_visited[u],temp_bfs_visited[v] = True,True

            # Rendering the edge to the screen
            pygame.draw.line(screen,EDGE_COLOR,node_centers[u],node_centers[v],5)

            # Rendering the queue to the screen
            node_font.render_to(screen,(100,500,300,600),'QUEUE:',WHITE)
            node_font.render_to(screen,(225,500,400,600),' '.join(map(str,inside_queue[cur_bfs_edge])),WHITE)
        
        # Depth First Search
        elif selected_alg == 1:
            # Getting the paths in order DFS searched
            dfs_path = depth_first_search(GRAPH_SETUP,NODE_COUNT,1)

            # Checking to see if we are able to move on with the algorithm
            if visualiser_timer >= 180 and cur_dfs_edge < DFS_EDGE-1:
                visualiser_timer = 0
                cur_dfs_edge += 1
            
            # Obtaining the current edge we are on by find the the node centers
            u,v = dfs_path[cur_dfs_edge][0]-1,dfs_path[cur_dfs_edge][1]-1
            temp_dfs_visited[u],temp_dfs_visited[v] = True,True
            
            # Rendering the current edge to the screen
            pygame.draw.line(screen,EDGE_COLOR,node_centers[u],node_centers[v],5)

        # Dijkstras Algorithm
        elif selected_alg == 2:
            # Obtaining the edges Dijkstras traversed along with the priority queue at each instance
            dijkstras_path,inside_pq = dijkstras_algorithm(GRAPH_SETUP,NODE_COUNT,1)

            # Checking to see if we are able to move on with the algorithm
            if visualiser_timer >= 180 and cur_dijkstras_edge < DIJKSTRAS_EDGE-1:
                visualiser_timer = 0
                cur_dijkstras_edge += 1
            
            # Getting the current edge we are on by finding the node centers
            u,v = dijkstras_path[cur_dijkstras_edge][0]-1,dijkstras_path[cur_dijkstras_edge][1]-1
            temp_dijkstras_visited[u],temp_dijkstras_visited[v] = True,True

            # Rendering the current edge to the screen
            pygame.draw.line(screen,EDGE_COLOR,node_centers[u],node_centers[v],5)

            # Rendering the priority queue to the screnn
            node_font.render_to(screen,(100,500,300,600),'PRIORITY QUEUE:',WHITE)
            node_font.render_to(screen,(325,500,400,600),str(inside_pq[cur_dijkstras_edge]),WHITE)

        # Kruskals Algorithm      
        else:
            # Obtaining the edges Kruskal's algorithm traversed
            kruskals_path = kruskals_algorithm(GRAPH_SETUP,NODE_COUNT,EDGE_COUNT)

            # Checking to see if we are able to move on with the algorithm
            if visualiser_timer >= 180 and cur_kruskal_edge < KRUSKALS_EDGE-1:
                visualiser_timer = 0
                cur_kruskal_edge += 1
            
            # Obtaining our current edge by finding the two node centers
            u,v = kruskals_path[cur_kruskal_edge][0]-1,kruskals_path[cur_kruskal_edge][1]-1
            temp_kruskals_visited[u],temp_kruskals_visited[v] = True,True

            # Appending our current edge to define the minimum spanning tree
            minimum_spanning_tree.append([node_centers[u],node_centers[v]])

            # Rendering the current edge to the screen
            pygame.draw.line(screen,EDGE_COLOR,node_centers[u],node_centers[v],5)

        # Rendering the minimum spanning tree on Kruskals Algorithm. No checking is needed as only Kruskal's Algorithm modifies the miniumum spanning tree array
        for n1c,n2c in minimum_spanning_tree:
                pygame.draw.line(screen,EDGE_COLOR,n1c,n2c,5)
        
        # Rendering the nodes to the screen 
        for node in range(NODE_COUNT):
            circle_center = node_centers[node]
            node_color = EDGE_COLOR if temp_bfs_visited[node] or temp_dfs_visited[node] or temp_dijkstras_visited[node] or temp_kruskals_visited[node] else WHITE
            pygame.draw.circle(screen, node_color, circle_center,25)

            # Rendering the weight to the screen
            node_font.render_to(screen,(circle_center[0]-6,circle_center[1]-10,circle_center[0],circle_center[1]),str(node+1),BLACK)
    
    # Rendering the home button to the screen
    home_button_color = menu_button_color_dict[is_collision(mouse_xpos,mouse_ypos,home_button_rect[0],home_button_rect[1],home_button_rect[0]+home_button_rect[2],home_button_rect[1]+home_button_rect[3])]
    pygame.draw.rect(screen,home_button_color,home_button_rect)
    menu_button_font.render_to(screen,(home_button_rect[0]+TEXT_OFFSET,home_button_rect[1]+TEXT_OFFSET,home_button_rect[0]+home_button_rect[2]+TEXT_OFFSET,home_button_rect[1]+home_button_rect[3]+TEXT_OFFSET),home_button_text,WHITE)
    
    # Updating the screen
    pygame.display.flip()
    clock.tick(60)
pygame.quit()