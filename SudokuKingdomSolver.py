
from selenium import webdriver 
import time
#from selenium.webdriver.chrome.options import Options

"""

Defining Difficulty and the functions to the solve Sudoku..

"""
# Easy / Medium / Hard / Very Hard
difficulty = "Very Hard"
n_times = 500
diff_color = {"Very Hard" : "g4" , "Hard" : "g3","Medium" : "g2", "Easy" : "g1"}



def possible(x,y,n,sudoku):
    for i in range(9):
        if sudoku[x][i] == n or sudoku[i][y] == n:
            return False

    x2 = x//3 * 3
    y2 = y//3 * 3
    for i in range(3):
        for j in range(3):
            if sudoku[x2 + i][y2 + j] == n:
                return False

    return True

def find_empty_cell(sudoku):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                return (i,j)

    return (-1,-1)

def solve(sudoku):
    (x, y) = find_empty_cell(sudoku)
    if (x, y) == (-1, -1):
        return True

    for i in range(1,10):
        if possible(x,y,i,sudoku):
            sudoku[x][y] = i
            if solve(sudoku):
                return sudoku
            sudoku[x][y] = 0


"""

Opening the Web-browser..

"""

#options = Options()
#options.headless = True
url = r"https://www.sudokukingdom.com/"
driver = webdriver.Chrome()#options=options)
driver.maximize_window()
driver.get(url)


"""

Logging in ... 

"""

driver.find_element_by_xpath('//*[@id="rx"]/div[2]/ul/li[2]/a').click()
time.sleep(2)
driver.find_element_by_id("login_name").send_keys("Mehdein")
time.sleep(1)
driver.find_element_by_id("member_password").send_keys("sudokuhacker")
time.sleep(1)
driver.find_element_by_xpath('//*[@id="b2"]/div/form/div[5]/input').click()
time.sleep(1)


"""

A loop to solve n sudokus..

"""


for do in range(n_times):
    sudoku , to_fill = [] , []
    for i in range(9):
        sudoku.append(list(range(9)))
    
    """
    
    Choosing Difficulty..
    
    """
    
    time.sleep(2)
    driver.find_element_by_id(diff_color[difficulty]).click()
    
    """

    Reading the sudoku board and putting it in a python list..
    
    """
    
    for l in range(9):
        for c in range(9):
            step = driver.find_element_by_id("c_"+str(c)+"_"+str(l))
            try:
                cell = step.find_element_by_class_name("k1").text
            except:
                cell = step.find_element_by_class_name("k1 i3").text
            if len(cell)>0:    
                sudoku[l][c]=int(cell)
            else:
                sudoku[l][c]=0
                to_fill.append([c,l])
    
    """
    
    Calling the function to solve Sudoku..
    
    """
    
    
    solve(sudoku)
    

    """

    Filling the Sudoku on the website by clicking..
    
    """
    
    for case in to_fill:
        c , l = case[0] , case[1]
        clicker = driver.find_element_by_id("M"+str(sudoku[l][c]))
        clicker.click()
        time.sleep(0.5)
        step = driver.find_element_by_id("c_"+str(c)+"_"+str(l))
        cell = step.find_element_by_id("vc_"+str(c)+"_"+str(l))       
        cell.click()
        time.sleep(0.5)
    time.sleep(0.5)
    del (sudoku)    
    driver.refresh()
    
    
    
    


    
    
    
    
    
    
    
    
    
    
    
    