<div align="center">
  <h1>Proofline 🦖</h1>
  <p><b>AI made code generation cheap. Verification didn't keep up. We fixed it.</b></p>
  <p><i>A Zero-Dependency Static Analysis Guardian for the 2026 Hackathon (Track A).</i></p>
</div>

---

## 📖 The Story

We are living in a new era of software engineering. Today, half of your codebase is written by AI. And while AI is incredibly fast, it has a fatal flaw: **it hallucinates.**

It makes up standard library functions that don't exist. It silently swallows exceptions in critical authentication boundaries. It introduces untested routes. And because human reviewers suffer from fatigue when reading massive AI-generated Pull Requests, these silent, highly-destructive bugs slip right into the `main` branch. 

Worse yet, the tools we typically use to catch these bugs rely on massive, deeply-nested dependency trees. Every install is a trust decision delegated to a stranger, exposing you to supply chain attacks.

We built **Proofline** as the counter-move.

### The Weapon: A Zero-Dependency Verification Gate

Proofline is an enterprise-grade static analysis engine built entirely from scratch using **100% Python standard library**. Absolutely zero third-party packages. No supply chain risk. Just pure, vanilla Python code.

It acts as a ruthless verification gate in your CI/CD pipeline. Instead of just regex-matching your code, Proofline actually understands it. It parses your Python AST (Abstract Syntax Tree) to build a massive **Caller Graph** and **Evidence Graph** to understand the true *blast radius* of an AI's hallucinated change.

---

## 🕵️‍♂️ How It Catches The Hallucinations

When an AI tries to sneak a bug past you, Proofline cross-references the diff against the entire repository to ask the hard questions:

1. **The Silent Signature Break:** Did the AI alter a core API signature that 50 other functions rely on?
2. **The Security Bypass:** Did the AI add a broad `except Exception:` inside an authentication function, silently converting a critical failure into a `None` return?
3. **The Orphaned Code:** Did the AI generate 100 lines of complex logic that has zero active callers? *(Rule 11)*
4. **The Dependency Attack Surface:** Did the AI quietly add a hallucinated or malicious third-party package to your `requirements.txt`? *(Rule 10)*
5. **The Testing Illusion:** Did the AI drastically change the implementation logic, but fail to update the associated test file?

If the calculated risk crosses the defined threshold (e.g., `HIGH`), Proofline exits with a non-zero status, slamming the door shut on the Pull Request.

---

## 🚀 Wielding Proofline

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

**4. Generate the Visual Dashboard:**
```bash
python -m proofline scan --base HEAD~1 --html report.html --serve
```
*(This generates a beautiful, interactive HTML dashboard. We even host a live demo on Vercel [here](https://zerodep-analyzer-qyam.vercel.app/)!)*

---

## 🛑 Honest Limits

Transparency is critical. Because Proofline achieves 100% of its functionality using only the standard library, we made calculated architectural trade-offs:

*   **Dynamic Resolution (`getattr`)**: Because Proofline relies on static AST analysis rather than runtime tracing, deeply dynamic Python calls (like `getattr(obj, func_name)()`) are notoriously difficult to track. Proofline mitigates this by flagging these edges as `UNKNOWN` confidence in the Caller Graph, aggressively downgrading the trust score, but it cannot guarantee resolution of metaprogramming.
*   **Performance on Massive Monorepos**: Without leveraging C-extensions (like `orjson` for serialization or `libcst` for AST parsing), full AST traversal on repositories with millions of lines of code will inevitably be slower than compiled alternatives. Proofline is optimized for *incremental* diff analysis (only parsing what actually changed), but initial full-tree builds may take a few extra seconds on huge codebases.
*   **Test Detection Heuristics**: Our test associations are made via module names and static `import` edge scanning, not via runtime code coverage (e.g., `coverage.py`). It strictly assumes standard naming conventions (`test_*.py`).

---

## 📜 License
MIT License
