# Question 1(A) – Nim211

**Game Setup:** Three piles (2, 1, 1). The last player to remove a stick loses.

## A (a) (1)
Initial State: [2 1 1 A] (A goes first).

Possible actions in order (left to right):
- Remove 1 from pile 1
- Remove 2 from pile 1
- Remove 1 from pile 2
- Remove 1 from pile 3

[2 1 1 A]
├─ (A removes 1 from pile1) → [1 1 1 B]
│   ├─ (B removes 1 from pile1) → [0 1 1 A]
│   │   ├─ (A removes 1 from pile2) → [0 0 1 B]
│   │   │   └─ (B removes 1 from pile3) → [0 0 0 A]  (terminal)
│   │   ├─ (A removes 1 from pile3) → [0 1 0 B] 
│   │   │   └─ (B removes 1 from pile2) → [0 0 0 A]  (terminal)
│   │   └─ (A cannot make any other moves)  
│   ├─ (B removes 1 from pile2) → [1 0 1 A]
│   │   └─ … etc.
│   ├─ (B removes 1 from pile3) → [1 1 0 A]
│   │   └─ … etc.
│   └─ (B removes 2 from pile1) → (not possible, as pile1=1)
├─ (A removes 2 from pile1) → [0 1 1 B]
│   ├─ (B removes 1 from pile2) → [0 0 1 A]
│   │   └─ … etc.
│   ├─ (B removes 1 from pile3) → [0 1 0 A]
│   │   └─ … etc.
│   └─ (B removes 2 from pile1) → (not possible, pile1=0)
├─ (A removes 1 from pile2) → [2 0 1 B]
│   └─ … etc.
└─ (A removes 1 from pile3) → [2 1 0 B]
    └─ … etc.

## A (a) (2)
(i) Terminal Nodes & Utility
Terminal state [ 0 0 0 𝐴 ] [000A]: B just took the last stick → A wins → utility = +1.
Terminal state [ 0 0 0 𝐵 ] [000B]: A just took the last stick → B wins → utility = −1.

(ii) Backed‐Up Minimax Values
We do a standard minimax backup:
-  At A nodes (MAX), choose the maximum child value. 
- At B nodes (MIN), choose the minimum child value. 

The final backed‐up value at [ 2 1 1 𝐴 ] [211A] is +1, meaning A can force a situation where B ends up taking the last stick

(iii) Alpha‐Beta Pruning (Left‐to‐Right)
Initialize 𝛼 = − 1 α=−1, 𝛽 = + 1 β=+1.
Depth‐first left‐to‐right. 
Once we have a subtree returning +1 at the root level (and if that sets 𝛼 ≥ 𝛽 α≥β), we can prune the remaining branches. 
In practice, after evaluating the first two main branches from [ 2 1 1 𝐴 ] [211A], the algorithm sees 𝛼 = + 1 α=+1 at the root, 𝛽 = + 1 β=+1. So 𝛼 ≥ 𝛽 α≥β triggers pruning of the other moves.

# Question 1(B) – Nim6

**Game Setup:** One pile of 6 sticks, remove 1 or 2 sticks each turn, last player to remove a stick loses.

**Analysis (winning/losing states):**
- n=0 → opponent just took last stick → you win.
- n=1 → forced to take last stick → you lose.
- n=2 → remove 1 (avoid removing last) → win.
- n=3 → remove 2 → leave 1 → opponent loses → win.
- n=4 → whichever you remove, you leave n=3 or n=2 for opponent (both winning for them) → lose.
- n=5 → remove 1 → leave 4 → opponent loses → win.
- n=6 → remove 2 → leave 4 → opponent loses → win.

**Conclusion:** With 6 sticks, A (the first player) is in a winning position. A can remove 2 immediately, leaving 4 for B, which is losing for B under these rules.

For Nim211: [ 2 1 1 𝐴 ] [211A] is a winning start for A. The minimax value is +1. With alpha‐beta (left‐to‐right), we prune after seeing a +1 at the root. 
For Nim6: The initial state [ 6 𝐴 ] [6A] is winning for A. A should remove 2 on the first move to force a loss on B eventually.

# Question 2

## Question 2 (a)

Minimax Values:
E=3, F=10, G=15 ⇒ B=3
H=2, T=20, U=8 ⇒ C=2
J=7, K=9 ⇒ D=7
Root A= max(B=3, C=2, D=7)= 7
First Move: A → D
Solution Path (optimal play): A → D → J → V (payoff = 7)


## Question 2 (b) (Left→Right)

We systematically check B, C, D.
No major 𝛼≥𝛽 cutoff at the top level.
Minor partial prunes might happen inside subtrees once we find a smaller MIN value, but overall no huge branch is omitted because each child must be checked to confirm the maximum for root.

## Question 2 (c) (Right→Left)

We explore D, C, B in that order.
We still end up needing to check each child’s subtree because the discovered values never trigger a large cutoff.
Final root value remains 7, same solution path.

Thus, the max player’s optimal payoff is 7, achieved via A→D→J→V.

# Question 3

Step 1: Identify Player 1’s best responses

If Player 2 plays L → Player 1 payoff: U = 1, M = 0, D = 2 ⇒ best is D
If Player 2 plays C → Player 1 payoff: U = 2, M = 1, D = 3 ⇒ best is D
If Player 2 plays R → Player 1 payoff: U = 2, M = 4, D = 3 ⇒ best is M
Step 2: Identify Player 2’s best responses

If Player 1 plays U → Player 2 payoff: L = 1, C = 0, R = 2 ⇒ best is R
If Player 1 plays M → Player 2 payoff: L = 3, C = 5, R = 4 ⇒ best is C
If Player 1 plays D → Player 2 payoff: L = 4, C = 6, R = 0 ⇒ best is C
Step 3: Find mutual best responses

Checking each (row, column):
(U, L)? P1 best vs L is D → not U ⇒ no
(U, C)? P1 best vs C is D → not U ⇒ no
(U, R)? P1 best vs R is M → not U ⇒ no
(M, L)? P1 best vs L is D → not M ⇒ no
(M, C)? P1 best vs C is D → not M ⇒ no
(M, R)? P1 best vs R is M (✓), but P2 best vs M is C → not R ⇒ no
(D, L)? P1 best vs L is D (✓), but P2 best vs D is C → not L ⇒ no
(D, C)? P1 best vs C is D (✓), and P2 best vs D is C (✓) ⇒ yes
(D, R)? P1 best vs R is M → not D ⇒ no
Conclusion:

The only pure‐strategy Nash equilibrium is (D, C) with payoffs (3, 6).