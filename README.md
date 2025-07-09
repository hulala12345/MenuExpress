# MenuExpress

MenuExpress is a simple command-line application that lets you browse local restaurants, build custom menus, and schedule pickup or delivery orders. It demonstrates a minimal implementation of the features requested in the project description.

## Features

- **Browse restaurants** with search and filter options (cuisine, location and minimum rating)
- **View menus** and add or remove dishes with quantity support
- **Persist custom menus** and orders to JSON files
- **Schedule orders** for delivery or pickup with date and time input

## Usage

1. Install Python 3 (>=3.8).
2. Run the application:
   ```bash
   python -m menu_express.app
   ```
   The first launch creates sample restaurant data automatically.
3. Follow the prompts to search restaurants, choose dishes and schedule an order.

All data is stored in `menu_express/data/` as JSON files.
