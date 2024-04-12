import pygame

pygame.init()

fps = 1
timer = pygame.time.Clock()
WIDTH = 1000
HEIGHT = 600

font = pygame.font.Font('freesansbold.ttf', 20)

# take input of the matrix from the user
n = int(input("\nEnter the number of vertices( or number of rows of the matrix): "))
print("\nEnter the elements of the matrix seperated by sapce and each row in next line: \n")
matrix = []


for i in range(n):
    matrix.append([])
    mRow = list(input().split(" "))
    for j in range(n):
        matrix[i].append(0)
        matrix[i][j] = int(mRow[j])
        #print(matrix[i][j], end = ' ')

print()

# for i in range(n):
#     for j in range(n):
#         print(matrix[i][j], end = " ")
#     print()

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Adjancy Matrix visualizer")

def drawLine(matrix, pList):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 1:
                pygame.draw.line(screen, (0,0,0), pList[i], pList[j], 2)


pos_list = []

def findCoordinate(v , pList):
    right = True
    back = False
    x, y = 400, 90
    for i in range(v):
        if (i % 2 != 0):
            #i is odd
            if (right):
                x += 90
                y += 90
                right = (not right)
            else:
                x -= 90
                y += 90
                right = (not right)
        else:
            if (back):
                x -= 150
                back = (not back)
            else:
                x += 150
                back = (not back)
        pos_list.append((x, y))
    # print(pos_list)

findCoordinate(n, pos_list)     


def showNumbers(pList):
    for i in range(len(pList)):
        text = font.render(str(i + 1), True, (0,0,0) )
        textRect = text.get_rect()
        textRect.center = (pList[i])
        screen.blit(text, textRect)
showNumbers(pos_list)


active = True
# main loop
while active:
    timer.tick(fps)
    screen.fill((255,255,255))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False
    drawLine(matrix, pos_list)
    for i in pos_list:
        pygame.draw.circle(screen, (0,0,0), i, 15)
        pygame.draw.circle(screen, (255,255,255), i, 12)
    
    showNumbers(pos_list)
    pygame.display.flip()

pygame.quit()
