import json
import argparse
from pathlib import Path

def load_analysis(analysis_file):
    """Load analysis results"""
    with open(analysis_file, 'r', encoding='utf-8') as f:
        return json.load(f)

def generate_category_page(cat_id, cat_info, scripts, stats):
    """Generate a category page"""
    cat_scripts = [s for s in scripts if cat_id in s['categories']]
    
    # Sort by importance (size, classes, functions)
    cat_scripts.sort(key=lambda x: (x['classes'], x['functions'], x['size_kb']), reverse=True)
    
    # Split into core and supporting
    core_scripts = cat_scripts[:5]  # Top 5 are "core"
    supporting_scripts = cat_scripts[5:]
    
    md = f"""# {cat_info['name']}

{cat_info['description']}

## Overview

This category contains **{len(cat_scripts)} scripts** that handle {cat_info['description'].lower()}.

"""
    
    # Core Scripts section
    if core_scripts:
        md += "## Core Scripts\n\n"
        for script in core_scripts:
            desc = script['description'][:100] + '...' if len(script['description']) > 100 else script['description']
            md += f"### [{script['filename']}.fos](../files/{script['filename']}.fos.md)\n\n"
            if desc:
                md += f"{desc}\n\n"
            
            stats_line = []
            if script['classes'] > 0:
                stats_line.append(f"{script['classes']} classes")
            if script['functions'] > 0:
                stats_line.append(f"{script['functions']} functions")
            if script['variables'] > 0:
                stats_line.append(f"{script['variables']} variables")
            
            if stats_line:
                md += f"**Contains**: {', '.join(stats_line)}\n\n"
    
    # Supporting Scripts section
    if supporting_scripts:
        md += "## Supporting Scripts\n\n"
        md += "| Script | Classes | Functions | Size |\n"
        md += "| :--- | :---: | :---: | :---: |\n"
        for script in supporting_scripts:
            md += f"| [{script['filename']}.fos](../files/{script['filename']}.fos.md) | {script['classes']} | {script['functions']} | {script['size_kb']} KB |\n"
        md += "\n"
    
    # Related categories
    md += "## Related Categories\n\n"
    related = get_related_categories(cat_id, scripts)
    if related:
        for rel_cat in related[:3]:  # Top 3 related
            md += f"- [{rel_cat['name']}]({rel_cat['id']}.md)\n"
    else:
        md += "*No strongly related categories*\n"
    
    md += "\n---\n\n[← Back to Index](../index.md)\n"
    
    return md

def get_related_categories(cat_id, scripts):
    """Find related categories based on script overlap"""
    # Scripts in this category
    cat_scripts = set(s['filename'] for s in scripts if cat_id in s['categories'])
    
    # Count overlaps with other categories
    overlaps = {}
    for script in scripts:
        for other_cat in script['categories']:
            if other_cat != cat_id and script['filename'] in cat_scripts:
                overlaps[other_cat] = overlaps.get(other_cat, 0) + 1
    
    # Sort by overlap count
    related = []
    # Access CATEGORIES from global scope or pass it in. 
    # Since we are inside a function, we need to ensure CATEGORIES is available.
    # It is passed in main, but here we rely on the global one which is loaded from JSON.
    # Actually, let's pass categories dict to this function or rely on it being available.
    # In the original code it was global.
    
    for other_cat, count in sorted(overlaps.items(), key=lambda x: x[1], reverse=True):
        if count > 2:  # At least 3 scripts in common
            related.append({
                'id': other_cat,
                'name': CATEGORIES[other_cat]['name'],
                'count': count
            })
    
    return related

def generate_main_index(scripts, stats, categories):
    """Generate main index.md"""
    
    md = """# FOnline 2238 Script Documentation

Welcome to the comprehensive documentation for FOnline 2238 scripts. This codebase contains **{total} scripts** with **{classes} classes** and **{functions} functions**, organized into **13 major categories**.

## Quick Start

**New to the codebase?** Start with these essential scripts:

1. **[main.fos](files/main.fos.md)** - Server entry point and core event handlers
2. **[utils.fos](files/utils.fos.md)** - Essential utility functions used throughout
3. **[_defines.fos](files/_defines.fos.md)** - Global definitions and constants
4. **[_macros.fos](files/_macros.fos.md)** - Macro definitions

## Browse by Category

""".format(
        total=stats['total_scripts'],
        classes=stats['total_classes'],
        functions=stats['total_functions']
    )
    
    # Category cards
    for cat_id, cat_data in sorted(stats['by_category'].items(), key=lambda x: x[1]['count'], reverse=True):
        cat_info = categories[cat_id]
        md += f"### [{cat_info['name']}](categories/{cat_id}.md)\n\n"
        md += f"{cat_info['description']}\n\n"
        md += f"**{cat_data['count']} scripts** | "
        
        # Show top 3 scripts
        top_scripts = [s for s in scripts if cat_id in s['categories']][:3]
        top_names = [f"`{s['filename']}.fos`" for s in top_scripts]
        md += f"Key: {', '.join(top_names)}\n\n"
    
    # Statistics section
    md += """
## Statistics

| Metric | Count |
| :--- | ---: |
| Total Scripts | {total_scripts} |
| Total Classes | {total_classes} |
| Total Functions | {total_functions} |
| Total Variables | {total_variables} |
| Total Constants | {total_constants} |
| Total Defines | {total_defines} |

### Largest Scripts

""".format(**stats)
    
    md += "| Script | Size | Classes | Functions |\n"
    md += "| :--- | ---: | ---: | ---: |\n"
    for script in stats['largest_scripts']:
        md += f"| [{script['filename']}.fos](files/{script['filename']}.fos.md) | {script['size_kb']} KB | {script['classes']} | {script['functions']} |\n"
    
    md += "\n### Most Included Scripts\n\n"
    md += "| Script | Included By |\n"
    md += "| :--- | ---: |\n"
    for item in stats['most_included']:
        md += f"| `{item['name']}.fos` | {item['count']} scripts |\n"
    
    md += """

## All Scripts

For a complete alphabetical list of all scripts, see [README.md](files/README.md).

## Documentation Features

This documentation includes:
- ✅ **Detailed API documentation** for all classes, functions, and variables
- ✅ **Type linking** - Click on types to navigate to their definitions
- ✅ **Include tracking** - See which scripts include or are included by others
- ✅ **Category organization** - Browse scripts by functional area
- ✅ **Search-friendly** - All content is indexed and searchable

---

*Documentation generated for FOnline 2238 | Last updated: {date}*
""".format(date="2025-11-26")
    
    return md

def generate_metrics_page(stats):
    """Generate metrics.md dashboard"""
    
    md = """# Documentation Metrics

## Overview Statistics

| Metric | Value |
| :--- | ---: |
| Total Scripts | {total_scripts} |
| Total Classes | {total_classes} |
| Total Functions | {total_functions} |
| Total Variables | {total_variables} |
| Total Constants | {total_constants} |
| Total Defines | {total_defines} |

## Top 10 Largest Scripts

| Rank | Script | Size (KB) | Classes | Functions |
| :---: | :--- | ---: | ---: | ---: |
""".format(**stats)
    
    for i, script in enumerate(stats['largest_scripts'], 1):
        md += f"| {i} | [{script['filename']}.fos](files/{script['filename']}.fos.md) | {script['size_kb']} | {script['classes']} | {script['functions']} |\n"
    
    md += "\n## Top 10 Scripts by Class Count\n\n"
    md += "| Rank | Script | Classes | Functions | Size (KB) |\n"
    md += "| :---: | :--- | ---: | ---: | ---: |\n"
    
    for i, script in enumerate(stats['most_classes'], 1):
        md += f"| {i} | [{script['filename']}.fos](files/{script['filename']}.fos.md) | {script['classes']} | {script['functions']} | {script['size_kb']} |\n"
    
    md += "\n## Top 10 Scripts by Function Count\n\n"
    md += "| Rank | Script | Functions | Classes | Size (KB) |\n"
    md += "| :---: | :--- | ---: | ---: | ---: |\n"
    
    for i, script in enumerate(stats['most_functions'], 1):
        md += f"| {i} | [{script['filename']}.fos](files/{script['filename']}.fos.md) | {script['functions']} | {script['classes']} | {script['size_kb']} |\n"
    
    md += "\n## Most Included Scripts\n\n"
    md += "These scripts are dependencies for many other scripts:\n\n"
    md += "| Rank | Script | Included By |\n"
    md += "| :---: | :--- | ---: |\n"
    
    for i, item in enumerate(stats['most_included'], 1):
        md += f"| {i} | `{item['name']}.fos` | {item['count']} scripts |\n"
    
    md += "\n## Scripts by Category\n\n"
    md += "| Category | Script Count |\n"
    md += "| :--- | ---: |\n"
    
    for cat_id, cat_data in sorted(stats['by_category'].items(), key=lambda x: x[1]['count'], reverse=True):
        md += f"| [{cat_data['name']}](categories/{cat_id}.md) | {cat_data['count']} |\n"
    
    md += "\n---\n\n[← Back to Index](../index.md)\n"
    
    return md

# Global variable to hold categories, populated in main
CATEGORIES = {}

def main():
    global CATEGORIES
    
    parser = argparse.ArgumentParser(description='Generate FOnline documentation overview.')
    parser.add_argument('--analysis', '-a', default=r"ai\docs\analysis.json", help='Path to analysis.json file')
    parser.add_argument('--output', '-o', default=r"ai\docs", help='Output directory for overview files')
    
    args = parser.parse_args()
    
    analysis_file = Path(args.analysis)
    output_dir = Path(args.output)
    
    print(f"Loading analysis from: {analysis_file}")
    if not analysis_file.exists():
        print(f"Error: Analysis file '{analysis_file}' does not exist.")
        return

    data = load_analysis(analysis_file)
    scripts = data['scripts']
    stats = data['statistics']
    CATEGORIES = data['categories']
    
    # Create directories
    (output_dir / 'categories').mkdir(parents=True, exist_ok=True)
    (output_dir / 'guides').mkdir(parents=True, exist_ok=True)
    
    print("\nGenerating category pages...")
    for cat_id, cat_info in CATEGORIES.items():
        content = generate_category_page(cat_id, cat_info, scripts, stats)
        output_file = output_dir / f'categories/{cat_id}.md'
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(content)
        # print(f"  Created: {output_file}")
    
    print("\nGenerating main index...")
    index_content = generate_main_index(scripts, stats, CATEGORIES)
    with open(output_dir / 'index.md', 'w', encoding='utf-8') as f:
        f.write(index_content)
    print(f"  Created: {output_dir / 'index.md'}")
    
    print("\nGenerating metrics dashboard...")
    metrics_content = generate_metrics_page(stats)
    with open(output_dir / 'metrics.md', 'w', encoding='utf-8') as f:
        f.write(metrics_content)
    print(f"  Created: {output_dir / 'metrics.md'}")
    
    print("\nOverview generation complete!")
    print(f"   - 13 category pages")
    print(f"   - 1 main index")
    print(f"   - 1 metrics dashboard")

if __name__ == '__main__':
    main()
