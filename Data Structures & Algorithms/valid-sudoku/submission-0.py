class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        num_rows = len(board) 
        num_cols = len(board[0])
        for i in range(len(board)):
            for row in board: 
                setNumY = set() 
                for column in row: 
                    if not(column.isdigit()):
                        continue 
                    elif column not in setNumY: 
                        setNumY.add(column) 
                    else: 
                        print("reeee 1")
                        return False 

            for col in range(num_cols): 
                setNumX = set() 
                for row in range(num_rows): 
                    val = board[row][col]
                    if not(val.isdigit()):
                        continue 
                    if val not in setNumX: 
                        setNumX.add(val) 
                    else: 
                        print("reee 2")
                        return False

        #this needs to go 9 times for all the boxes... how do I do that? 
        print("3x3")

        for box_row in range(3):
            for box_col in range(3):
                seen = set()                      # reset per box
                start_r, start_c = box_row * 3, box_col * 3
                for dr in range(3):
                    for dc in range(3):
                        val = board[start_r + dr][start_c + dc]
                        if val == ".":
                            continue
                        if val in seen:
                            return False
                        seen.add(val)
                
        return True 
            

        