# omnicmd-engine

> **Clean-Room Open-Source Implementation**  
> *Target Architecture Archetype:* Linear / Superhuman Keyboard Command Palette & Action Graph  
> *Author:* Ayush Kandwal ([@Sunzzx](https://github.com/Sunzzx)) | License: MIT

---

## ⚡ Overview
`omnicmd-engine` is a 100% clean-room, independently authored open-source implementation providing:
- High-performance, zero-latency fuzzy command palette and action graph engine with hierarchical fuzzy score filtering, undo-tree transactions, and keyboard shortcut graph compiler in Python/Rust.
- Zero external runtime dependencies.
- Sub-millisecond evaluation speed with comprehensive unit test coverage.

## 🚀 Quickstart
```bash
python3 -m unittest discover tests
```

## 📐 Architecture
```
       ┌────────────────────────┐
       │   Command Registry     │
       └───────────┬────────────┘
                   │ Action Graph
                   ▼
       ┌────────────────────────┐
       │ Fuzzy Subsequence Match│
       └───────────┬────────────┘
                   │ Scored & Ranked
                   ▼
       ┌────────────────────────┐
       │  Sub-Millisecond Stream│
       └────────────────────────┘
```
