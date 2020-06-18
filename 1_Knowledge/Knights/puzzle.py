from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

def XOR(p, q):
    return And(Or(p, q), Not(And(p, q)))

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    XOR(AKnight, AKnave),
    Biconditional(AKnight, And(AKnight, AKnave)),
    Not(Biconditional(AKnave, And(AKnight, AKnave)))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    XOR(AKnight, AKnave),
    XOR(BKnight, BKnave),
    Biconditional(AKnight, And(AKnave, BKnave)),
    Not(Biconditional(AKnave, And(AKnave, BKnave)))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    XOR(AKnight, AKnave),
    XOR(BKnight, BKnave),
    Biconditional(AKnight, XOR(And(AKnight, BKnight), And(AKnave, BKnave))),
    Not(Biconditional(AKnave, XOR(And(AKnight, BKnight), And(AKnave, BKnave)))),
    Biconditional(BKnight, XOR(And(AKnight, BKnave), And(AKnave, BKnight))),
    Not(Biconditional(BKnave, XOR(And(AKnight, BKnave), And(AKnave, BKnight))))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    XOR(AKnight, AKnave),
    XOR(BKnight, BKnave),
    XOR(CKnight, CKnave),

    Biconditional(AKnight, XOR(AKnight, AKnave)),
    Not(Biconditional(AKnave, XOR(AKnight, AKnave))),

    Biconditional(BKnight, And(Biconditional(AKnight, AKnave), Not(Biconditional(AKnave, AKnave)))),
    Not(Biconditional(BKnave, And(Biconditional(AKnight, AKnave), Not(Biconditional(AKnave, AKnave))))),
    
    Biconditional(BKnight, CKnave),
    Not(Biconditional(BKnave, CKnave)),

    Biconditional(CKnight, AKnight),
    Not(Biconditional(CKnave, AKnight))
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
