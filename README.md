# Standard Form Minimizer (Mizer)
Given a list of variables representing binary inputs, and a target canonical form function, Mizer returns the standard form representation.

### Example
Given the binary variables $A$, $B$, and $C$, and the target canonical function $F = m_0 + m_2 + m_5$, Mizer returns $F = \bar{A}\bar{B}\bar{C} + \bar{A}B\bar{C} + A\bar{B}C$ and the simplified function $F = \bar{A}\bar{C} + A\bar{B}C$
