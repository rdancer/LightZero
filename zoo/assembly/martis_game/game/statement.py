import re

from my_types import Opcode, Index, Increment, Label

class Statement:
    INDENT_COUNT = 4
    INDENT = " " * INDENT_COUNT

    def __init__(self, line: str):
        self.line = line.strip()
        self.opcode_mnemonic = Opcode()
        self.destination_index = Index()
        self.source_index1 = Index()
        self.source_index2 = Index()
        self.increment = Increment()
        self.label = None
        self.immediate_value = 0.000
        self.cursor_position = 0
        self.parse_from_file()

    def parse_from_file(self):
        # Regex patterns to match different operations
        self.patterns = {
            'scalar_assign': re.compile(r's(\d+)\s*=\s*(-?\d+(\.\d+)?)'),
            'dot_product': re.compile(r's(\d+)\s*=\s*dot\(v(\d+),\s*v(\d+)\)'),
            'subtraction': re.compile(r's(\d+)\s*=\s*s(\d+)\s*-\s*s(\d+)'),
            'multiplication': re.compile(r's(\d+)\s*=\s*s(\d+)\s*\*\s*s(\d+)'),
            'vector_scalar_mult': re.compile(r'v(\d+)\s*=\s*v(\d+)\s*\*\s*s(\d+)'),
            'vector_add': re.compile(r'v(\d+)\s*=\s*v(\d+)\s*\+\s*v(\d+)'),
            'section_label': re.compile(r'(Setup|Predict|Learn)'),
        }
        self.opcode_mnemonic_map = {
            "scalar_assign": "let",
            "dot_product": "dot",
            "subtraction": "sub",
            "multiplication": "mul",
            "vector_scalar_mult": "muv",
            "vector_add": "add",
            "section_label": "label",
        }
        

        # Attempt to match each pattern and parse tokens
        for key, pattern in self.patterns.items():
            match = pattern.search(self.line)
            if match:
                self.operation = key
                try:
                    self.tokens = [int(x) if x.isdigit() else float(x) for x in match.groups()]
                except:
                    # label
                    self.tokens = [match.group(1)]
                if self.operation == "section_label":
                    self.label = self.tokens[0]
                    if self.label not in Label.LABELS:
                        raise ValueError(f"Invalid label '{self.label}'")
                elif self.operation == "scalar_assign":
                    self.opcode_mnemonic.set("let")
                    self.destination_index.set(self.tokens[0])
                    self.immediate_value = self.tokens[1]
                else:
                    self.opcode_mnemonic.set(self.opcode_mnemonic_map[self.operation])
                    self.destination_index.set(self.tokens[0])
                    self.source_index1.set(self.tokens[1])
                    self.source_index2.set(self.tokens[2])
                self.tokens = None # force exception if referenced subsequently
                break
        else:
            raise ValueError(f"Invalid statement: >>{self.line}<<")

    def serialize_for_file(self):
        # Serialize tokens back into a string using the operation format
        if self.operation == 'scalar_assign':
            return f'{self.INDENT}s{self.destination_index} = {self.immediate_value:.3f}'
        elif self.operation == 'dot_product':
            return f'{self.INDENT}s{self.destination_index} = dot(v{self.source_index1}, v{self.source_index2})'
        elif self.operation in ['subtraction', 'multiplication']:
            op = '-' if self.operation == 'subtraction' else '*'
            return f'{self.INDENT}s{self.destination_index} = s{self.source_index1} {op} s{self.source_index2}'
        elif self.operation == 'vector_scalar_mult':
            return f'{self.INDENT}v{self.destination_index} = v{self.source_index1} * s{self.source_index2}'
        elif self.operation == 'vector_add':
            return f'{self.INDENT}v{self.destination_index} = v{self.source_index1} + v{self.source_index2}'
        elif self.operation == 'section_label':
            return f'def {self.label}():'
        return self.line

    def serialize_for_display(self):
        if self.label is not None:
            return f'label {self.label}:'
        elif str(self.opcode_mnemonic) == 'let':
            return f'let {self.destination_index} {self.immediate_value:.3f}'
        else:
            return f'{self.opcode_mnemonic.current()} {self.destination_index} {self.source_index1} {self.source_index2}'

    def get_cursor_display_column(self):
        """Return the display column corresponding to the current cursor position. Because our mnemonic is always 3 characters long, and our exceptions (label and let) can only take a cursor position 0 and [0, 1] respectively, we can do this uniformly for every operation."""
        # label Label:
        # ^----------- cursor position
        # mne 1 2 3
        # ^---^-^-^--- cursor positions
        # let 0.000
        # ^---^------- cursor positions
        return 0 if self.cursor_position == 0 else len("mne")-1 + len(" 1") * self.cursor_position

    def increment_token(self):
        # Increment the value of the current token, with wrapping if needed
        if self.label is not None:
            return
        elif self.cursor_position == 0:
            next(self.opcode_mnemonic)
        elif self.cursor_position == 1:
            next(self.destination_index)
        else:
            if self.opcode_mnemonic.current() == 'let':
                if self.cursor_position == 2:
                    self.immediate_value += self.increment.current()
                else:
                    raise RuntimeError(f"Invalid cursor position {self.cursor_position} for opcode 'let'")
            else:
                if self.cursor_position == 2:
                    next(self.source_index1)
                elif self.cursor_position == 3:
                    next(self.source_index2)
                else:
                    raise RuntimeError(f"Invalid cursor position {self.cursor_position} for opcode '{self.opcode_mnemonic.current()}'")
        self.redraw()
    
    def redraw(self):
        pass

    def decrement_token(self):
        raise NotImplementedError("Decrementing tokens is not supported")

    def move_cursor_right(self):
        # Move the cursor to the right, wrapping around
        if self.label is not None or \
                (self.opcode_mnemonic.current() == 'let' and self.cursor_position == 2) or \
                self.cursor_position == 3:
            # Move to the next statement
            raise NextStatementException(self)
        else:
            self.cursor_position += 1
        self.redraw()

    def move_cursor_left(self):
        raise NotImplementedError("Moving the cursor left is not supported")
    
    def change_increment(self):
        next(self.increment)
    
    def reset_token(self):
        # Not implemented
        pass


class NextStatementException(Exception):
    def __init__(self, statement: Statement):
        self.statement = statement
        super().__init__(f"Statement is finished: {statement.serialize_for_file()}")