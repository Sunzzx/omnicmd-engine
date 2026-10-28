import unittest
import sys
from pathlib import Path

# Ensure src in sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
from omnicmd_engine.engine import OmniCmdEngine, CommandAction

class TestOmniCmdEngine(unittest.TestCase):
    def test_command_search_and_ranking(self):
        engine = OmniCmdEngine()
        engine.register(CommandAction("file.open", "Open File", "Navigation", keys="Ctrl+P"))
        engine.register(CommandAction("git.commit", "Git: Commit Changes", "Version Control", keys="Ctrl+K C"))
        engine.register(CommandAction("term.toggle", "Terminal: Toggle Console", "View", keys="Ctrl+`"))

        res = engine.search("open")
        self.assertEqual(len(res), 1)
        self.assertEqual(res[0]["id"], "file.open")
        self.assertGreater(res[0]["score"], 40.0)

    def test_subsequence_fuzzy_matching(self):
        engine = OmniCmdEngine()
        engine.register(CommandAction("proj.build", "Project: Build Production Artifact", "Build"))
        res = engine.search("pjbld")
        self.assertEqual(len(res), 1)
        self.assertEqual(res[0]["id"], "proj.build")

if __name__ == "__main__":
    unittest.main()
