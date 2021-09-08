FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"

def board(pieces):
    game = ""
    game += "---------------------------------\n"
    for y in range(8):
        temp = ""
        temp += "{} ".format(8-y)
        for x in range(8):
            temp += "| | "

        game += temp + "\n"
        game += "---------------------------------\n"
    game += "   a   b   c   d   e   f   g   h"
    print(game)

def parseFEN(FEN):
    pass

if __name__ == "__main__":
    pieces = parseFEN(FEN)
    board(pieces)
