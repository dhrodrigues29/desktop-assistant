# WhatsApp Desktop Assistant

A modular Python desktop automation assistant using mouse, keyboard and clipboard actions.

This project does not auto-send bulk messages.

The first scenario prepares WhatsApp Web chats from a list of contacts and pastes a preset message. The user must manually confirm sending each message.

## Goals

- Reusable desktop automation structure
- Coordinate-based mouse actions
- Keyboard shortcuts
- Clipboard helper
- Configurable message and coordinates
- Manual confirmation before each send

## Install

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```
