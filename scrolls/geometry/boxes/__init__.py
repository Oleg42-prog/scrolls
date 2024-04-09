'''
Code style rules for transformations between bounding boxes formats:
1. One line - one transformation.
2. First convert to one coodinate system, then to one representation.
3. Do not use implicit (not named) transformations.


Example #1:
Wrong: xyxyn = xyxyn_to_cxywhn(xyxyp_to_xyxyn(xyxyp))
Right: xyxyn = xyxyp_to_xyxyn(xyxyp)
       cxywhn = xyxyn_to_cxywhn(xyxyn)


Example #2:
Wrong: xyxyn = cxywhn_to_xyxyn(cxywhn)
       xyxyp = xyxyn_to_xyxyp(xyxyn)
Right: cxywhp = cxywhn_to_cxywhp(cxywhn)
       xyxyp = cxywhp_to_xyxyp(cxywhp)


Example #3
Wrong: cxywhp = cxywhn * 100
Right: cxywhp = cxywhn_to_cxywhp(cxywhn)

'''
