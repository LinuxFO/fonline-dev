# Documentation Improvement Plan

This document outlines the steps to enhance the automatically generated documentation for FOnline scripts.

## Phase 1: Enhanced Parsing & Content Extraction

The current parser uses basic regex which misses context and details.

1.  **Implement State-Based Parsing**
    *   **Goal**: Correctly identify nested structures like classes, interfaces, and their members.
    *   **Action**: Update the parsing logic to track scope (e.g., `in_class`, `in_function`). This allows capturing class methods and properties which are currently missing.

2.  **Docstring/Comment Extraction**
    *   **Goal**: Enrich documentation with human-written descriptions.
    *   **Action**: Modify the parser to read comments immediately preceding declarations (`//`, `///`, `/** ... */`).
    *   **Output**: Add a "Description" field to every documented element.

3.  **File Header Analysis**
    *   **Goal**: Provide a high-level summary of each script.
    *   **Action**: Extract the first block of comments in the file to serve as the "Script Description" or "Module Overview".

## Phase 2: Cross-Referencing & Linking

1.  **Type Indexing**
    *   **Goal**: Link variable types and return types to their definitions.
    *   **Action**: First pass: Scan all files to build a map of `Type Name -> File Path`.
    *   **Action**: Second pass: When generating Markdown, replace known types (e.g., `Critter`, `Item`) with links (e.g., `[Critter](Critter.fos.md)`).

2.  **Include Graph**
    *   **Goal**: Visualize dependencies.
    *   **Action**: List "Included By" in addition to "Includes" to show reverse dependencies.

## Phase 3: Formatting & Presentation

1.  **Improved Markdown Structure**
    *   **Goal**: Better readability.
    *   **Action**:
        *   Use **Tables** for Defines, Constants, and Variables (Columns: Name, Type, Value, Description).
        *   Use **Collapsible Sections** (`<details>`) for long lists or complex code blocks if supported.
        *   Add **Table of Contents** (TOC) at the top of each file.

2.  **Frontmatter for Static Sites**
    *   **Goal**: Compatibility with tools like Astro/Starlight (mentioned in project context).
    *   **Action**: Add YAML frontmatter to each `.md` file.
        ```yaml
        ---
        title: _defines.fos
        description: Global definitions and constants
        ---
        ```

## Phase 4: Scope & Automation

1.  **Multi-Directory Support**
    *   **Goal**: Cover the entire codebase.
    *   **Action**: Update the script to recursively search `foclassic`, `PReloaded`, and other relevant directories, preserving the directory structure in the documentation output (e.g., `docs/Server/scripts/...`).



## Execution Order

1.  **Refine Parser** (Class members + Comments) - *High Priority*
2.  **Improve Formatting** (Tables + Frontmatter) - *Medium Priority*
3.  **Cross-Linking** - *Medium Priority*
4.  **Full Directory Scan** - *Low Priority (can be done anytime)*
