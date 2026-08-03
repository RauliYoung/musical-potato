## Future Design Note: Project-Owned Sheets

### Project Sheet Ownership

Projects should eventually own their own worksheet instead of storing every task in a single shared sheet.

Proposed structure:

- One workbook contains all project data.
- Each project has its own worksheet.
- The worksheet name is the project name (or a stable project identifier if renaming becomes supported).
- All tasks belonging to a project are stored only in that project's worksheet.

### Why

- Keeps project data isolated and easier to navigate.
- Makes loading a single project more efficient.
- Simplifies future features such as project archiving, exporting, and statistics.
- Avoids one massive task table as the application grows.
- Provides a natural mapping between the storage layer and the application's concept of a project.

### Things to Consider

- Project names may change. If renaming is supported, decide whether worksheet names should also change or whether each project should instead have a permanent internal identifier.
- Shared metadata (project description, creation date, archived status, etc.) should eventually live in a dedicated `Projects` sheet rather than being inferred from task data.
- `TaskManager` should remain responsible for project operations, while `ExcelStorage` is responsible only for reading and writing the correct worksheet.

This is an architectural goal rather than an immediate implementation. The current single-sheet approach is acceptable while building the core functionality.
