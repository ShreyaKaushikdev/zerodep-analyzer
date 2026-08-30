# Proofline v7.0: The Zero-Dependency Package Killer

**The Year is 2026. AI made code generation cheap, but verification didn't keep up.**

## 📖 The Story

It started with a simple realization: AI coding agents are incredibly fast. They can churn out hundreds of lines of code in seconds. But there's a dark side. AI hallucinates. It quietly swallows errors by writing broad `except Exception:` blocks. It alters critical security functions and forgets to update the tests.

The human reviewer is left holding the bag, drowning in PRs they don't fully understand. 

We needed a strict gatekeeper. A bouncer for our `main` branch. But there was a catch: we were entering the **Zero Dependency Hackathon**. We couldn't rely on `pip install`. We couldn't use heavy AST parsing libraries. We couldn't use templating engines or environment variable loaders. We had to build a weapon using only what Python gave us out of the box.

### The Engine
Using nothing but the naked Python standard library (`ast`, `importlib`, `subprocess`), we built **Proofline**. It mathematically traces the "blast radius" of every AI-generated change. 

We taught it to understand the difference between a direct call (PROVEN) and a dynamically dispatched method (UNKNOWN). We taught it to detect when an AI breaks a public signature but leaves the test suite untouched. 

### The Bouncer at the Door
But developers forget to run tools. So we built `proofline install-hook`, a pure Python feature that generates a Git pre-commit hook natively. Now, the moment an AI tries to commit a hallucinated exception handler, Proofline steps in. **Commit Blocked.**

### Closing the Loop
When Proofline catches an unverified AI change, it doesn't just yell at you. We built `scaffold-tests`—a feature that reads the Evidence Graph and automatically writes the `unittest` boilerplate for you, closing the gap as fast as the AI opened it.

And if you need the AI to fix its own mess, we built `pack-context`. Proofline generates a highly optimized LLM prompt containing exactly the right evidence, instructions, and source code, perfectly framing the problem for the agent.

### The Package Killers
To secure the ultimate hackathon score, we relentlessly hunted down the most commonly installed packages and murdered them with standard library code:
1. **`python-dotenv` Killed**: Proofline automatically parses `.env` files using a naive standard library reader to inject `PROOF_PORT` and other config natively.
2. **`strip-ansi` Killed**: Proofline strips terminal color codes using pure regex (`ansi_stripper.py`), allowing you to pipe beautiful CLI logs directly into flat text files using `--log-file`.
3. **`jinja2` Killed**: HTML reports are generated using Python's native `string.Template` engine rather than heavy external templating packages.
4. **`watchdog` Killed**: Proofline features a native file watcher with debouncing using pure `hashlib` and `os.stat`.
5. **The Deps Enforcer**: We even built a self-enforcing gatekeeper that scans our own `requirements.txt` on boot and terminates the program if it finds *any* third-party package! 
6. **`fastapi` / `Flask` / Web Servers Killed**: Proofline features a built-in interactive dashboard served natively by `http.server`.

### The Final Polish (v7.0)
We went even further. To ensure zero external tooling was ever needed, we added:
- **`proofline init`**: An interactive terminal wizard (using pure `input()`) to automatically generate your `.env` and `.prooflineignore` settings.
- **The Audit Packager (`proofline archive`)**: Natively uses `zipfile` to execute an analysis and compress the results into a timestamped `.zip` file for compliance sharing.
- **AST Caching Engine**: Hashing code via `hashlib` and serializing AST objects via `pickle` into `.proofline/cache/` bypassing massive `ast.parse` overhead on unchanged files.
- **Parallel AST Processing**: Natively distributes AST parsing across all CPU cores using `concurrent.futures.ProcessPoolExecutor` for insane performance on large repos!
- **Dashboard Server (`proofline serve`)**: Natively spins up a local web server and pops open your browser using `webbrowser` to interactively view the audit dashboard!

This is Proofline v7.0. Zero dependencies. Total verification.

---

## 🚀 Features

- **The Package Killers**: Natively loads `.env` files, generates HTML templates, and strips ANSI codes—all without downloading a single dependency.
- **Git-Native Analysis (`--staged`)**: Securely analyze code directly from the Git index without modifying your working tree.
- **Automated Test Scaffolding (`scaffold-tests`)**: Automatically generate `unittest` boilerplate for unverified changed symbols.
- **LLM Context Packer (`pack-context`)**: Seamlessly package proofline analysis into markdown context so AI agents can fix their own code.
- **Interactive Triage**: The CLI dynamically analyzes symbol complexity (Cyclomatic Complexity) and prompts interactive fixes.
- **.prooflineignore System**: Natively suppress rules by function or wildcard without an external TOML parser.
- **Zero-Dependency Plugin Architecture**: Drop any `.py` script into `.proofline/rules/` to instantly add custom organizational rules to the engine.

---

## 🛠️ Usage

### 1. Setup Wizard
Bootstrap your repository interactively natively without creating config files by hand:
```bash
proofline init
```

### 2. Installing the Bouncer (Git Hooks)
Secure your repository by blocking unverified AI changes before they are committed:
```bash
proofline install-hook
```

### 3. Git-Native Analysis
Analyze your currently staged Git changes against `HEAD` and dump the clean output to a log file using native ANSI stripping:
```bash
proofline analyze --staged --log-file proof.log
```

### 4. The Dashboard Server
Done auditing? Spin up the zero-dependency local web server and open the interactive dashboard in your browser:
```bash
proofline serve --port 8080
```

### 5. Audit Packaging
Run an analysis and natively generate a compressed zip archive of the reports for your compliance team:
```bash
proofline archive --before demo_repo/baseline --after demo_repo/patch
```

### 6. Packing LLM Context
Tell your AI exactly what it broke:
```bash
proofline pack-context --before demo_repo/baseline --after demo_repo/patch --out llm_context.md
```

### 7. Scaffolding Missing Tests
Automatically generate boilerplate unit tests for changed symbols the AI missed:
```bash
proofline scaffold-tests --before demo_repo/baseline --after demo_repo/patch
```

---

## 🧪 The Ultimate Test

Proofline strictly tests itself. Running the test suite ensures that the engine is operating correctly against adversarial logic gates, ensuring no AI trickery gets past it.

```bash
python run_tests.py
```
*Currently passing 128 out of 128 unit tests and verification gates.*

---

**Built with ❤️ for the Zero Dependency Hackathon.**
