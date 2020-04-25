knowledge3 = And(
    # TODO
    Or(AKnight,AKnave),
    Or(BKnight,BKnave),
    Or(CKnight,CKnave),
    Not(And(AKnight,BKnight)),
    Not(And(AKnave,BKnave)),
    Biconditional(AKnight, Not(AKnave)),
    Biconditional(AKnave, Not(AKnight)),

    Implication(AKnight,Or(AKnight,AKnave)),
    Implication(AKnave,Not(Or(AKnight,AKnave))),
    Implication(BKnight,Implication(BKnave,And(AKnave,AKnight))),
    Implication(CKnight,Implication(AKnight,Or(AKnight,AKnave))),
    Implication(CKnave,Not(Implication(AKnight,Or(AKnight,AKnave))))
)
