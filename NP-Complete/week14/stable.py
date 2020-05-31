"""
Input: bipartite graph G(U,V) (two sets)
       preference list for U and V


Initialize all men and women to free
while there exist a free man m who still has a woman w to propose to
{
    w = m's highest ranked such woman to whom he has not yet proposed
    if w is free
       (m, w) become engaged
    else some pair (m', w) already exists
       if w prefers m to m'
          (m, w) become engaged
           m' becomes free
       else
          (m', w) remain engaged
}
"""

def stableMarriage(men, women):
    """
    - iterate over man preferences women
    - check women free or women preference
    - finishwhen all men has pair
    """
    w_partners = [None for w in women]
    m_available = [True for m in men]
    m_free = len(men)


    while m_free > 0:
        m = m_available.index(True)
        # find couple for men
        for w in men[m]:
            # w is free
            if w_partners[w] is None:
                w_partners[w] = m
                m_available[m] = False
                m_free -= 1
                break
            # not free
            else:
                other_men = w_partners[w]
                # check w preference
                if women[m] > women[other_men]:
                    w_partners[w] = m
                    m_available[m] = False

                    m_available[other_men] = True
                    break
                else:
                    continue
    print(w_partners)
    print(m_available)
    print(m_free)



man = [[3, 2, 2, 0], [1, 0, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3]]
women = [[0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3]]

stableMarriage(man, women)
