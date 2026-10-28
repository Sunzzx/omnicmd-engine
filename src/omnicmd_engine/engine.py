"""OmniCmd Fuzzy Action Graph Engine."""
from typing import List, Dict, Any, Optional, Callable
import re

class CommandAction:
    def __init__(self, id: str, title: str, category: str, handler: Optional[Callable] = None, keys: Optional[str] = None):
        self.id = id
        self.title = title
        self.category = category
        self.handler = handler or (lambda: True)
        self.keys = keys

    def execute(self) -> Any:
        return self.handler()

class OmniCmdEngine:
    def __init__(self):
        self._actions: Dict[str, CommandAction] = {}

    def register(self, action: CommandAction) -> None:
        self._actions[action.id] = action

    def search(self, query: str) -> List[Dict[str, Any]]:
        if not query:
            return [{"id": a.id, "title": a.title, "score": 1.0, "category": a.category} for a in self._actions.values()]
        
        q = query.lower()
        results = []
        for a in self._actions.values():
            t = a.title.lower()
            score = 0.0
            if q == t:
                score = 100.0
            elif t.startswith(q):
                score = 50.0 + (len(q) / len(t)) * 10
            elif q in t:
                score = 20.0 + (len(q) / len(t)) * 10
            else:
                # Subsequence matching
                idx = 0
                matched = 0
                for ch in q:
                    pos = t.find(ch, idx)
                    if pos != -1:
                        matched += 1
                        idx = pos + 1
                if matched == len(q):
                    score = 10.0 + (matched / len(t)) * 5
            
            if score > 0:
                results.append({"id": a.id, "title": a.title, "score": round(score, 2), "category": a.category})
        
        results.sort(key=lambda x: x["score"], reverse=True)
        return results
