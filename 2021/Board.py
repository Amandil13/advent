class Board:
    def __init__(self, numbers):
        self.board = []
        self.column_totals = [0,0,0,0,0]
        self.row_totals = [0,0,0,0,0]
        self.winner = 0
        for i in range(0,5):
            row = []
            for j in range(0,5): 
                row.append({'value': numbers.pop(0),'found': 0})
            self.board.append(row)

    def call_number(self,number):
        for i in range(0,5):
            for j in range(0,5): 
                if (self.board[i][j]["value"] == number): 
                    self.board[i][j]["found"] = 1
                    self.row_totals[i] += 1
                    self.column_totals[j] += 1
                    return self.check_winner()

    def check_winner(self): 
        if 5 in self.row_totals: 
                return 1
        if 5 in self.column_totals: 
                return 1
        return 0

    def score_board(self,number): 
        score = 0
        for i in range(0,5):
            for j in range(0,5): 
                if self.board[i][j]["found"] == 0:
                    score += int(self.board[i][j]["value"])
        return score * int(number)

    def reset(self): 
        self.column_totals = [0,0,0,0,0]
        self.row_totals = [0,0,0,0,0]
        self.winner = 0
        for i in range(0,5):
            for j in range(0,5): 
                self.board[i][j]["found"] = 0


