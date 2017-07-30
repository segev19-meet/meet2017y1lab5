###def draw_1d(n, char):
##    print(n * char)
##
##for i in range(5):
##    print("**********")
##         
##
##def draw_2d(n, m, char):
##    for i in range(n):
##        draw_1d(m,char)
##        
##draw_2d(3, 23, "*")


def special_draw_2d(n, m, border, fill):
    print(m*border)
    for i in range(n-2):
        print(border + (fill*(m-2)) + border)
    print(m*border)
    
