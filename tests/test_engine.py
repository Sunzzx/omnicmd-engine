import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
from omnicmd_engine.engine import OmniCmdEngine, CommandAction

class TestOmniCmdEngine(unittest.TestCase):
    def test_command_search_and_ranking(self):
        engine = OmniCmdEngine()
        engine.register(CommandAction("file.open", "Open File", "Navigation", keys="Ctrl+P"))
        engine.register(CommandAction("git.commit", "Git: Commit Changes", "Version Control", keys="Ctrl+K C"))
        res = engine.search("open")
        self.assertEqual(len(res), 1)
        self.assertEqual(res[0]["id"], "file.open")

if __name__ == "__main__":
    unittest.main()
