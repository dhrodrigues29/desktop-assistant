# Architecture

## Core idea

The project separates automation into small modules:

- `config.py`: coordinates, message, delays and runtime settings
- `keyboard.py`: keyboard shortcuts
- `mouse.py`: mouse clicks and movement
- `clipboard.py`: copy/paste helpers
- `contacts.py`: reads contacts from CSV
- `workflow.py`: coordinates the task sequence
- `main.py`: command-line entrypoint

## First workflow

1. Wait for user to type `ready`
2. Switch between browser tabs/windows
3. Read one contact at a time
4. Open WhatsApp search
5. Paste number
6. Select conversation
7. Paste message
8. Pause for user to manually send
9. Return to list
10. Repeat

## Future workflows

The same modules can later automate other browser-based tasks by replacing only:

- coordinates
- message content
- workflow steps
- contact/input source
