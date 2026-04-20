#Lecture 1
#Unit 1

def practice_1_basic_exceptions():
    """
    Practice identifying and handling common exceptions
    """
    print("\n" + "="*50)
    print("EXERCISE 1: Handle the Exceptions")
    print("="*50)

    # TODO 1: Fix division by zero
    def safe_divide(a, b):
        """Return a/b or None if division by zero"""
        try:
            return a / b
        except ZeroDivisionError:
            return None

    # Test your function
    print(f"10 / 2 = {safe_divide(10, 2)}")
    print(f"10 / 0 = {safe_divide(10, 0)}")

    # TODO 2: Fix list index error
    def safe_get_item(lst, index):
        """Get item at index or return 'Not found'"""
        try:
            return lst[index]
        except IndexError:
            return "Not found"

    # Test your function
    my_list = [1, 2, 3]
    print(f"Item at index 1: {safe_get_item(my_list, 1)}")
    print(f"Item at index 10: {safe_get_item(my_list, 10)}")

    # TODO 3: Handle multiple exceptions
    def convert_to_number(value):
        """Convert string to int or float, return None if impossible"""
        try:
            return int(value)        # Try integer first
        except (ValueError, TypeError):
            try:
                return float(value)  # Fall back to float
            except (ValueError, TypeError):
                return None          # Give up — not a number

    # Test conversions
    test_values = ["42", "3.14", "hello", None]
    for val in test_values:
        result = convert_to_number(val)
        print(f"Converting '{val}': {result}")

# Run the practice
practice_1_basic_exceptions()


#Unit 2
def practice_2_exception_hierarchy():
    """
    Practice with exception hierarchy
    """
    print("\n" + "="*50)
    print("EXERCISE 2: Exception Hierarchy")
    print("="*50)

    # TODO 1: Catch multiple related exceptions efficiently
    def access_data(data_structure, key):
        """
        Access data[key] whether data is list or dict.
        Return None if key doesn't exist.
        """
        try:
            return data_structure[key]
        except (IndexError, KeyError):  # Both inherit from LookupError
            return None

    # Test with different data structures
    test_list = [10, 20, 30]
    test_dict = {"a": 1, "b": 2}
    print(f"List[1]:   {access_data(test_list, 1)}")
    print(f"List[10]:  {access_data(test_list, 10)}")
    print(f"Dict['a']: {access_data(test_dict, 'a')}")
    print(f"Dict['z']: {access_data(test_dict, 'z')}")

    # TODO 2: Order exception handlers correctly
    def parse_value(value):
        """
        Try to parse value as int, then float, then return as string.
        """
        try:
            return int(value)           # Step 1: try strictest type first
        except (ValueError, TypeError): # int() failed — not a whole number
            try:
                return float(value)     # Step 2: try less strict type
            except (ValueError, TypeError):
                return str(value)       # Step 3: fall back to string

    # Test parsing
    test_values = ["42", "3.14", "hello", None]
    for val in test_values:
        result = parse_value(val)
        print(f"Parsing '{val}': {result} (type: {type(result).__name__})")

# Run the practice
practice_2_exception_hierarchy()


#Unit 3
import os
import random

def practice_3_complete_pattern():
    """
    Practice with try-except-else-finally
    """
    print("\n" + "="*50)
    print("EXERCISE 3: Complete Exception Pattern")
    print("="*50)

    # Setup: create a test file so we have one that actually exists
    with open("exists.txt", "w") as f:
        f.write("hello\nworld\npython")

    # TODO 1: File processor with complete error handling
    def process_file(filename):
        """
        Read file, process content, ensure file is closed.
        Return processed content or None.
        """
        file = None
        try:
            file = open(filename, "r")                      # Attempt to open

        except FileNotFoundError:
            print(f"  [ERROR] File not found: '{filename}'")
            return None

        except PermissionError:
            print(f"  [ERROR] Permission denied: '{filename}'")
            return None

        else:
            # Only runs if try block succeeded — no exception was raised
            content = file.read()
            word_count = len(content.split())
            line_count = len(content.splitlines())
            return f"{line_count} lines, {word_count} words"

        finally:
            # ALWAYS runs — open or not, exception or not
            if file is not None:
                file.close()
                print(f"  [FINALLY] File '{filename}' closed.")

    # Test with different scenarios
    test_files = ["exists.txt", "missing.txt", "/root/protected.txt"]
    for filename in test_files:
        result = process_file(filename)
        print(f"  Result for '{filename}': {result}\n")

    # ----------------------------------------------------------------

    # TODO 2: Resource manager
    class ResourceManager:
        def __init__(self, name):
            self.name = name
            self.resource = None

        def acquire(self):
            """Acquire resource — might fail randomly to simulate real errors."""
            if random.random() < 0.4:               # 40% chance of failure
                raise RuntimeError(f"Could not connect to {self.name}")
            self.resource = f"{self.name}_connection"
            print(f"  [ACQUIRE] {self.resource} established.")

        def release(self):
            """Release resource — must always happen if acquired."""
            if self.resource:
                print(f"  [RELEASE] {self.resource} closed.")
                self.resource = None
            else:
                print(f"  [RELEASE] Nothing to release for {self.name}.")

        def use(self):
            """Use resource — only safe to call after acquire()."""
            result = f"Query result from {self.resource}"
            print(f"  [USE] {result}")
            return result

    # Test resource management
    print("-" * 40)
    print("Resource Manager Test:")
    print("-" * 40)

    rm = ResourceManager("Database")
    result = None

    try:
        rm.acquire()                    # Might raise RuntimeError

    except RuntimeError as e:
        print(f"  [ERROR] Acquire failed: {e}")

    else:
        # Only runs if acquire() succeeded — safe to use resource here
        result = rm.use()

    finally:
        # Always runs — guarantees cleanup whether acquire worked or not
        rm.release()

    print(f"\n  Final result: {result}")

    # Cleanup test file
    if os.path.exists("exists.txt"):
        os.remove("exists.txt")

# Run the practice
practice_3_complete_pattern()





#Lecture 2
#Unit 1: No exxcercises
#Unit 2

def practice_2_custom_exceptions():
    """
    Practice creating and using custom exceptions
    """
    print("\n" + "="*50)
    print("EXERCISE 5: Custom Exceptions")
    print("="*50)

    # TODO 1: Create custom exceptions
    class GameError(Exception):
        """Base class for all game exceptions."""
        pass

    class InvalidMoveError(GameError):
        """Raised when a player attempts an illegal move."""
        def __init__(self, position, reason):
            self.position = position        # Store structured data on the exception
            self.reason = reason
            # Build a readable message and pass it up to Exception
            super().__init__(f"Position {position} is invalid — {reason}")

    class GameOverError(GameError):
        """Raised when a move is attempted after the game has ended."""
        def __init__(self, winner):
            self.winner = winner
            message = f"The game is already over. Winner: {winner}" \
                      if winner != "Draw" else "The game already ended in a draw."
            super().__init__(message)

    # TODO 2: Use custom exceptions
    class TicTacToe:
        def __init__(self):
            self.board = [[' ' for _ in range(3)] for _ in range(3)]
            self.current_player = 'X'
            self.game_over = False
            self.winner = None

        def make_move(self, row, col):
            # Guard 1: no moves allowed once the game is finished
            if self.game_over:
                raise GameOverError(self.winner or "Draw")

            # Guard 2: position must be inside the 3×3 grid
            if not (0 <= row <= 2 and 0 <= col <= 2):
                raise InvalidMoveError(
                    position=(row, col),
                    reason="position is out of bounds (must be 0–2)"
                )

            # Guard 3: cell must be empty
            if self.board[row][col] != ' ':
                raise InvalidMoveError(
                    position=(row, col),
                    reason=f"already occupied by '{self.board[row][col]}'"
                )

            # Valid move — place the piece and switch players
            self.board[row][col] = self.current_player
            self._check_winner()
            self.current_player = 'O' if self.current_player == 'X' else 'X'

        def _check_winner(self):
            """Check rows, columns, and diagonals for a win."""
            b = self.board
            lines = (
                [b[r] for r in range(3)]            +   # rows
                [[b[r][c] for r in range(3)]
                    for c in range(3)]               +   # columns
                [[b[0][0], b[1][1], b[2][2]]]       +   # diagonal
                [[b[0][2], b[1][1], b[2][0]]]           # anti-diagonal
            )
            for line in lines:
                if line[0] != ' ' and len(set(line)) == 1:
                    self.winner = line[0]
                    self.game_over = True
                    return

    # ----------------------------------------------------------------
    # Test the game
    game = TicTacToe()
    test_moves = [
        (0, 0),   # ✅ Valid — X plays
        (0, 0),   # ❌ Already taken
        (5, 5),   # ❌ Out of bounds
        (1, 1),   # ✅ Valid — O plays
        (0, 1),   # ✅ Valid — X plays
        (2, 2),   # ✅ Valid — O plays
        (0, 2),   # ✅ Valid — X wins!
        (1, 0),   # 🏁 Game is over
    ]

    for row, col in test_moves:
        try:
            game.make_move(row, col)
            print(f"  ✅ Move ({row},{col}) accepted  "
                  f"— player {('O' if game.current_player == 'X' else 'X')} played")
        except InvalidMoveError as e:
            # Access structured attributes directly on the exception object
            print(f"  ❌ Invalid move at {e.position}: {e.reason}")
        except GameOverError as e:
            print(f"  🏁 Game over — {e.winner} won! No more moves allowed.")

# Run the practice
practice_2_custom_exceptions()


#Unit 3
import os
import traceback
from dataclasses import dataclass, field
from typing import Optional

def practice_3_complete_system():
    """
    Build a complete error handling system
    """
    print("\n" + "="*50)
    print("EXERCISE 6: Complete Error Handler")
    print("="*50)

    # ----------------------------------------------------------------
    # Custom exceptions for the file processing domain
    # ----------------------------------------------------------------
    class FileProcessingError(Exception):
        """Base class for all file processing errors."""
        def __init__(self, filename, reason):
            self.filename = filename
            self.reason   = reason
            super().__init__(f"[{filename}] {reason}")

    class FileReadError(FileProcessingError):
        """File exists but could not be read."""
        pass

    class FileAccessError(FileProcessingError):
        """File exists but access is denied."""
        pass

    # ----------------------------------------------------------------
    # Structured result object — replaces raw strings in failure list
    # ----------------------------------------------------------------
    @dataclass
    class FileResult:
        filename:   str
        success:    bool
        content:    Optional[str] = None   # populated on success
        error_type: Optional[str] = None   # exception class name on failure
        message:    Optional[str] = None   # human-readable failure reason

    # ----------------------------------------------------------------
    # Core processor
    # ----------------------------------------------------------------
    class FileProcessor:
        def __init__(self):
            self.processed_files: list[FileResult] = []
            self.failed_files:    list[FileResult] = []

        # ── single-file processing ───────────────────────────────────
        def process_file(self, filename: str) -> Optional[str]:
            """
            Process a single file with complete error handling.
            Returns processed content string, or None on failure.
            """
            file = None
            result = None

            try:
                print(f"\n  Opening '{filename}'...")
                file = open(filename, "r")                  # may raise FileNotFoundError
                                                            # or PermissionError

            except FileNotFoundError:
                msg = "File does not exist."
                print(f"  ✗ Not found — {msg}")
                self.failed_files.append(FileResult(
                    filename=filename, success=False,
                    error_type="FileNotFoundError", message=msg
                ))
                return None

            except PermissionError:
                msg = "Read permission denied."
                print(f"  ✗ Permission error — {msg}")
                self.failed_files.append(FileResult(
                    filename=filename, success=False,
                    error_type="PermissionError", message=msg
                ))
                return None

            except Exception as e:
                # Catch-all for truly unexpected errors (disk errors, etc.)
                msg = f"Unexpected error: {type(e).__name__}: {e}"
                print(f"  ✗ Unexpected — {msg}")
                self.failed_files.append(FileResult(
                    filename=filename, success=False,
                    error_type=type(e).__name__, message=msg
                ))
                return None

            else:
                # Runs ONLY when open() succeeded — safe to read here
                try:
                    raw     = file.read()
                    lines   = raw.splitlines()
                    words   = raw.split()
                    result  = (
                        f"{len(lines)} lines, "
                        f"{len(words)} words, "
                        f"{len(raw)} chars"
                    )
                    print(f"  ✓ Processed — {result}")
                    self.processed_files.append(FileResult(
                        filename=filename, success=True, content=result
                    ))
                    return result

                except Exception as e:
                    # File opened fine but reading/processing failed
                    msg = f"Read error after open: {e}"
                    print(f"  ✗ Read failed — {msg}")
                    self.failed_files.append(FileResult(
                        filename=filename, success=False,
                        error_type="FileReadError", message=msg
                    ))
                    return None

            finally:
                # Runs ALWAYS — guarantees the file handle is released
                if file is not None:
                    file.close()
                    print(f"  ↩ File handle closed.")

        # ── directory processing ─────────────────────────────────────
        def process_directory(self, directory: str) -> None:
            """
            Process every file in a directory, never stopping on errors.
            """
            print(f"\n  Scanning directory: '{directory}'")
            try:
                entries = os.listdir(directory)
            except FileNotFoundError:
                print(f"  ✗ Directory not found: '{directory}'")
                return
            except PermissionError:
                print(f"  ✗ Permission denied: '{directory}'")
                return

            files = [
                os.path.join(directory, e)
                for e in entries
                if os.path.isfile(os.path.join(directory, e))
            ]

            if not files:
                print("  No files found.")
                return

            for filepath in files:
                self.process_file(filepath)   # errors are handled inside — never stops loop

        # ── summary report ───────────────────────────────────────────
        def get_report(self) -> dict:
            """Return a structured summary of all processing activity."""
            total    = len(self.processed_files) + len(self.failed_files)
            failures = [
                {"file": r.filename, "error": r.error_type, "reason": r.message}
                for r in self.failed_files
            ]
            return {
                "total_attempted": total,
                "succeeded":       len(self.processed_files),
                "failed":          len(self.failed_files),
                "success_rate":    f"{len(self.processed_files)/total*100:.0f}%"
                                   if total else "N/A",
                "failures":        failures,
            }

    # ----------------------------------------------------------------
    # Setup: create a real file so we have one valid case
    # ----------------------------------------------------------------
    with open("valid.txt", "w") as f:
        f.write("line one\nline two\nline three\n")

    # ----------------------------------------------------------------
    # Run tests
    # ----------------------------------------------------------------
    processor  = FileProcessor()
    test_files = ["valid.txt", "missing.txt", "/root/restricted.txt"]

    for filename in test_files:
        processor.process_file(filename)

    report = processor.get_report()

    print("\n" + "="*50)
    print("FINAL REPORT")
    print("="*50)
    print(f"  Total attempted : {report['total_attempted']}")
    print(f"  Succeeded        : {report['succeeded']}")
    print(f"  Failed           : {report['failed']}")
    print(f"  Success rate     : {report['success_rate']}")
    if report["failures"]:
        print("\n  Failure details:")
        for f in report["failures"]:
            print(f"    • {f['file']}")
            print(f"      Error : {f['error']}")
            print(f"      Reason: {f['reason']}")

    # Cleanup
    if os.path.exists("valid.txt"):
        os.remove("valid.txt")

practice_3_complete_system()

