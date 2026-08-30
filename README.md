# Proofline 🦖

**Proofline** is a zero-dependency static analysis tool for risk-aware Python code reviews. It is built as a strict verification gate to prevent AI-hallucinated bugs, orphaned code, and accidental attack surface expansions from merging into your main branch.

*Built for the Zero Dependency 2026 Hackathon (Track A).*

---

## 🎯 What it does

Half your code is written by AI, and AI sometimes hallucinates. It makes up standard library functions, silently changes exception handlers, and introduces un-tested routes. 

Proofline automatically audits your Pull Request diffs by building a **Caller Graph** and **Evidence Graph** purely from your Python AST. It detects risk by analyzing the changes in the context of the entire project:

*   **Public Signature Changes:** Did an AI silently alter a core API signature?
*   **Security & Exception Behavior:** Did a broad `except Exception:` get added to a critical auth function?
*   **Attack Surface Expansion:** (Rule 10) Scans `requirements.txt` to aggressively flag when a new third-party dependency is introduced.
*   **Orphan Code Detection:** Identifies dead code that has zero active callers.
*   **Test Stagnation:** Verifies that logic changes are actually accompanied by corresponding updates to test files.

If the calculated risk crosses the defined threshold (e.g., `HIGH`), Proofline exits with a non-zero status, blocking the commit or PR.

---

## 🚀 How to run it

Because Proofline adheres strictly to the **Zero Dependency** constraint, there is no `pip install` required, and no heavy virtual environments to set up.

Just clone the repo and run it directly against your Python 3.9+ installation!

**1. Scan a git repository against a base commit:**
```bash
python -m proofline scan --base HEAD~1
```

**2. Analyze two arbitrary directories (Baseline vs Patched):**
```bash
python -m proofline analyze --before ./baseline_dir --after ./patched_dir
```

**3. Install as a pre-commit hook (to block unsafe commits locally):**
```bash
python -m proofline install-hook --fail-on HIGH
```

**4. Generate an interactive Visual Dashboard:**
```bash
python -m proofline scan --base HEAD~1 --html report.html --serve
```

---

## 🛑 Honest Limits

Transparency is critical. Because Proofline achieves 100% of its functionality using only the standard library, we made calculated architectural trade-offs:

1.  **Dynamic Resolution (`getattr`)**: Because Proofline relies on static AST analysis rather than runtime tracing, deeply dynamic Python calls (like `getattr(obj, func_name)()`) are notoriously difficult to track. Proofline mitigates this by flagging these edges as `UNKNOWN` confidence in the Caller Graph, aggressively downgrading the trust score, but it cannot guarantee resolution of metaprogramming.
2.  **Performance on Massive Monorepos**: Without leveraging C-extensions (like `orjson` for serialization or `libcst` for AST parsing), full AST traversal on repositories with millions of lines of code will inevitably be slower than compiled alternatives. Proofline is optimized for *incremental* diff analysis (only parsing what actually changed), but initial full-tree builds may take a few extra seconds on huge codebases.
3.  **Test Detection Heuristics**: Our test associations are made via module names and static `import` edge scanning, not via runtime code coverage (e.g., `coverage.py`). It strictly assumes standard naming conventions (`test_*.py`).

---

## 📜 License
MIT License
