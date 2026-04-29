# QuickInput

A powerful keyboard and mouse automation tool for Windows that supports rapid key input, continuous press simulation,
and macro execution.

## Features

- **Rapid Key/Mouse Clicking**: Automatically repeat keyboard or mouse clicks at specified intervals
- **Continuous Press Simulation**: Hold down keys or mouse buttons continuously
- **Macro System**: Create and execute complex automation sequences with trigger-based macros
- **Audio Feedback**: Built-in beep sounds to indicate start/stop of operations
- **Easy to Use**: Simple command-line interface with clear parameter options

## Installation

### Prerequisites

- Python 3.6 or higher
- Windows operating system (for Linux/macOS, audio feedback may vary)

### Dependencies

Install required packages:

```bash
pip install keyboard mouse
```

### Setup

1. Clone or download this repository
2. Navigate to the `src` directory:
    ```bash
    cd src
    ```
3. Run the tool:
    ```bash
    python QuickInput.py --help
    ```

## Usage

### Basic Syntax

```bash
python QuickInput.py
```

### Options

| Option            | Description                                           | Conflicts With                         |
|-------------------|-------------------------------------------------------|----------------------------------------|
| `--key KEY`       | Press specified key(s) (can be used multiple times)   | `--press`, `--pmouse`, `--func`        |
| `--mouse BUTTON`  | Click mouse button(s) (can be used multiple times)    | `--press`, `--pmouse`, `--func`        |
| `--time SECONDS`  | Interval between clicks in seconds                    | Must be used with `--key` or `--mouse` |
| `--press KEY`     | Continuously hold key(s) (can be used multiple times) | `--key`, `--mouse`, `--time`, `--func` |
| `--pmouse BUTTON` | Continuously hold mouse button(s)                     | `--key`, `--mouse`, `--time`, `--func` |
| `--func FILE`     | Load and run a macro file from `func/` folder         | All other mode parameters              |
| `--view`          | Display all available keys and mouse buttons          | All other parameters                   |
| `--showfunc`      | List all available macro files                        | All other parameters                   |

### Control Keys

- **F8**: Stop any running operation (hold to exit)
- **2-second delay**: All modes have a 2-second countdown before starting

## Examples

### Rapid Key Clicking

Press keys 'a', 'b', 'c' repeatedly with 0.5 second intervals:

```bash
python QuickInput.py --key=a --key=b --key=c --time=0.5
```

### Rapid Mouse Clicking

Click left and right mouse buttons alternately every 1 second:

```bash
python QuickInput.py --mouse=left --mouse=right --time=1.0
```

### Continuous Key Press

Hold down keys '2', '3', and '6' simultaneously:

```bash
python QuickInput.py --press=2 --press=3 --press=6
```

### Continuous Mouse Press

Hold down the left mouse button:

```bash
python QuickInput.py --pmouse=left
```

### View Available Keys

Display all supported keyboard keys and mouse buttons:

```bash
python QuickInput.py --view
```

### List Macro Files

Show all available macro files in the `func/` directory:

```bash
python QuickInput.py --showfunc
```

### Run a Macro

Execute a macro from a JSON file:

```bash
python QuickInput.py --func=my_macro.json
```

## Macro System

### Creating Macros

Macros are stored as JSON files in the `func/` directory. The directory is automatically created when you first run the
program.

### Macro File Format

```json
[
  {
    "key": "trigger_key",
    "keys": [
      "key1",
      "key2",
      "key3"
    ],
    "mouses": [
      "button1",
      "button2"
    ]
  },
  {
    "key": "another_trigger",
    "keys": [
      "ctrl",
      "c"
    ],
    "mouses": []
  },
  "..."
]
```

### Macro Structure

- **`key`**: The trigger key that activates this macro action
- **`keys`**: Array of keyboard keys to simulate when triggered
- **`mouses`**: Array of mouse buttons to click when triggered

### Example Macro File

Create a file `func/copy_paste.json`:

```json
[
  {
    "key": "f1",
    "keys": [
      "ctrl",
      "c"
    ],
    "mouses": []
  },
  {
    "key": "f2",
    "keys": [
      "ctrl",
      "v"
    ],
    "mouses": []
  },
  {
    "key": "f3",
    "keys": [],
    "mouses": [
      "left"
    ]
  }
]
```

Run it with:

```bash
python QuickInput.py --func=copy_paste.json
```

When running:

- Press **F1** → Simulates Ctrl+C (copy)
- Press **F2** → Simulates Ctrl+V (paste)
- Press **F3** → Simulates left mouse click
- Press **F8** → Exit macro mode

## Supported Keys

### Keyboard Keys

- **Letters**: a - z
- **Numbers**: 0 - 9
- **Function Keys**: f1 - f12
- **Special Keys**: enter, esc, tab, backspace, delete, space
- **Arrow Keys**: up, down, left, right
- **Modifier Keys**: ctrl, alt, shift, win
- **Lock Keys**: caps lock, num lock, scroll lock

### Mouse Buttons

- `left` - Left mouse button
- `right` - Right mouse button
- `middle` - Middle mouse button (scroll wheel click)

## How It Works

### Operation Modes

1. **Click Mode** (`--key`/`--mouse` + `--time`)
    - Repeatedly presses keys or clicks mouse at specified intervals
    - Starts after 2-second delay with audio feedback
    - Press F8 to stop

2. **Press Mode** (`--press`/`--pmouse`)
    - Holds down keys or mouse buttons continuously
    - Useful for games or applications requiring sustained input
    - Press F8 to release and stop

3. **Macro Mode** (`--func`)
    - Loads predefined automation sequences
    - Trigger actions by pressing specified keys
    - Runs until F8 is pressed

### Safety Features

- **2-second startup delay**: Gives you time to switch to target application
- **Audio feedback**: Beep sounds confirm operation start/stop
- **F8 emergency stop**: Hold F8 to immediately stop any operation
- **Parameter validation**: Prevents conflicting parameter combinations

## Tips & Best Practices

1. **Test in Safe Environment**: Always test macros in a safe environment first
2. **Use Appropriate Intervals**: Set `--time` values that won't overwhelm applications
3. **Keep Macros Organized**: Use descriptive filenames for your macro files
4. **Remember F8**: Always remember that F8 stops the current operation
5. **Administrator Rights**: Some applications may require running as administrator

## Troubleshooting

### Common Issues

**Issue**: Tool doesn't respond to key presses

- **Solution**: Try running as administrator

**Issue**: Macro file not found

- **Solution**: Ensure the file exists in the `func/` directory and use the exact filename

**Issue**: Keys not working in certain applications

- **Solution**: Some games/applications block simulated input; try running as administrator

**Issue**: Audio feedback not working on Linux/macOS

- **Solution**: This is expected; terminal bell may not be enabled on all systems

## Contributing

Contributions are welcome! Please feel free to submit issues and enhancement requests.

## License

This project uses the MIT License.

## Disclaimer

This tool is intended for legitimate automation purposes only. Use responsibly and in compliance with applicable laws
and terms of service of any software you interact with.

---

**Note**: This tool uses the `keyboard` and `mouse` libraries which may require administrator/root privileges on some
systems for full functionality.
