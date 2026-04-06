#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script to repair and restructure the Analyse-data notebook.
Reorganizes sections 8-12 to place titles BEFORE code cells.
"""

import json
from pathlib import Path

def repair_notebook():
    nb_path = Path(r"c:\Users\ouiss\OneDrive\Desktop\INGD\Recherche\code_analyse_algo\Analyse-data.ipynb")
    
    with open(nb_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    cells = nb['cells']
    
    # Find section 7 end (cell with "return agg_df, curves, run_ids")
    section_7_idx = None
    for i, cell in enumerate(cells):
        if cell['cell_type'] == 'code':
            source = ''.join(cell['source']) if isinstance(cell['source'], list) else cell['source']
            if 'return agg_df, curves, run_ids' in source:
                section_7_idx = i
                break
    
    if section_7_idx is None:
        print("ERROR: Could not find section 7 end")
        return
    
    print(f"Section 7 ends at cell index: {section_7_idx}")
    print(f"Total cells: {len(cells)}")
    
    # Extract cells after section 7
    cells_to_reorder = cells[section_7_idx + 1:]
    
    # Group cells for sections 8-12 (should come in pairs: code then markdown title)
    # We need to reorder them so title comes BEFORE code
    
    new_cells_8_12 = []
    i = 0
    while i < len(cells_to_reorder):
        cell = cells_to_reorder[i]
        src = ''.join(cell['source']) if isinstance(cell['source'], list) else cell['source']
        
        # Check if this is a section code cell
        if cell['cell_type'] == 'code' and any(f'# {i+1}. ' in src for j in range(8, 13) for i in [j]):
            # This is a code cell, next should be markdown title
            code_cell = cell
            markdown_cell = None
            
            # Look ahead for markdown cell
            if i + 1 < len(cells_to_reorder):
                next_cell = cells_to_reorder[i + 1]
                if next_cell['cell_type'] == 'markdown':
                    next_src = ''.join(next_cell['source']) if isinstance(next_cell['source'], list) else next_cell['source']
                    if '##' in next_src:
                        markdown_cell = next_cell
                        i += 1  # Skip next iteration
            
            # Add markdown first, then code
            if markdown_cell:
                new_cells_8_12.append(markdown_cell)
            new_cells_8_12.append(code_cell)
        else:
            # Not a code cell or already processed
            new_cells_8_12.append(cell)
        
        i += 1
    
    # Rebuild cells list
    nb['cells'] = cells[:section_7_idx + 1] + new_cells_8_12
    
    # Write back
    with open(nb_path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)
    
    print("Notebook repaired successfully!")

if __name__ == '__main__':
    repair_notebook()
